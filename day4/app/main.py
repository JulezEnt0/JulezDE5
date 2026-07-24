from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine
from auth import get_db, hash_password, create_access_token, authenticate_user

Base.metadata.create_all(bind=engine)
app = FastAPI()
app = FastAPI(title="User Account API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/register", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_email = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    existing_username = db.query(models.User).filter(models.User.username == user_in.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    user = models.User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=hash_password(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/login")
def login(login_in: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_in.email, login_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email}, timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer", "user_id": user.id}

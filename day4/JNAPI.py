from fastapi import  FastAPI, Request, Response

app = FastAPI() 

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}

]

# Home Route
@app.get("/")
def home():
    return {"message":"JN Library API"}
@app.get("/books")
async def get_books():
    return {"message": "List of books", "books": books  
                }

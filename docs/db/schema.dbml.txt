// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table customers {
  id              int        [pk, increment]
  first_name      varchar
  last_name       varchar
  email           varchar    [unique]
  phone           varchar
  created_at      datetime
}

Table customer_addresses {
  id              int        [pk, increment]
  customer_id     int        [not null]
  address_line1   varchar
  address_line2   varchar
  city            varchar
  county          varchar
  postcode        varchar
  country         varchar
  is_primary      boolean
  created_at      datetime
}

Table categories {
  id              int        [pk, increment]
  name            varchar    [unique]
  description     text
}

Table products {
  id              int        [pk, increment]
  name            varchar
  sku             varchar    [unique]
  description     text
  unit_price      decimal
  category_id     int        [not null]
  is_active       boolean
  created_at      datetime
}

Table orders {
  id              int        [pk, increment]
  customer_id     int        [not null]
  order_date      datetime
  status_id          int    
  shipping_address_id int   
  total_amount    decimal    
  created_at      datetime
}

Table order_items {
  id              int        [pk, increment]
  order_id        int        [not null]
  product_id      int        [not null]
  quantity        int        [not null]
  unit_price      decimal    [not null] 
 
}


Table order_statuses {
  id           int     [pk, increment]
  code         varchar [unique] 
  label        varchar         
  is_final     boolean         
  is_cancellable boolean       
}
Enum order_status {
  PENDING
  PAID
  SHIPPED
  CANCELLED
}

Ref: customer_addresses.customer_id > customers.id

Ref: products.category_id > categories.id

Ref: orders.customer_id > customers.id
Ref: orders.shipping_address_id > customer_addresses.id

Ref: order_items.order_id > orders.id
Ref: order_items.product_id > products.id
Ref: order_statuses.id > orders.status_id
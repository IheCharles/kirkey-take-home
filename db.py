import pymysql

conn = pymysql.connect(
    host='sql3.freesqldatabase.com', 
    user='sql3697196',
    password='DELhWFq2K5', 
    db='sql3697196', 
    port=3306,  
    charset='utf8mb4',  
    cursorclass=pymysql.cursors.DictCursor

)
cursor = conn.cursor()

authors_query = """CREATE TABLE authors (
id serial PRIMARY KEY,
name text,
email text,
date_of_birth timestamp
)"""

books_query = """CREATE TABLE books (
id serial PRIMARY KEY,
author_id integer REFERENCES authors (id),
isbn text,
);"""

sale_items_query = """CREATE TABLE sale_items (
id serial PRIMARY KEY,
book_id integer REFERENCES books (id),
customer_name text,
item_price money,
quantity integer
);"""

cursor.execute(authors_query)
cursor.execute(books_query)
cursor.execute(sale_items_query)
conn.close()
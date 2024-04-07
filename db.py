import pymysql

conn = pymysql.connect(
    host='sql3.freesqldatabase.com', 
    user='sql3697196',
    password='DELhWFq2K5', 
    database='sql3697196', 
    charset='utf8mb4',  
    cursorclass=pymysql.cursors.DictCursor

)
cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE sale_items;")
cursor.execute("TRUNCATE TABLE books;")
cursor.execute("TRUNCATE TABLE authors;")
authors_query = """CREATE TABLE IF NOT EXISTS authors (
id serial PRIMARY KEY,
name text,
email text,
date_of_birth timestamp
)"""

books_query = """CREATE TABLE IF NOT EXISTS books (
id serial PRIMARY KEY,
author_id integer REFERENCES authors (id),
isbn text
)"""

sale_items_query = """CREATE TABLE IF NOT EXISTS sale_items (
id serial PRIMARY KEY,
book_id integer REFERENCES books (id),
customer_name text,
item_price DECIMAL(10, 2),
quantity integer
)"""

cursor.execute(authors_query)
cursor.execute(books_query)
cursor.execute(sale_items_query)


authors_insert = """
INSERT INTO authors (name, email, date_of_birth) VALUES
('J.K. Rolling', 'jk.rolling@example.com', '1980-09-01'),
('Charles Iheanetu', 'cci29@drexel.edu', '1984-09-05'),
('Ian Kochinski', 'Kiren.Kochinski@example.com', '1987-11-11'),
('Clark Kent', 'Clark.Kent@example.com', '2019-04-23'),
('Peter parker', 'preter.parker@example.com', '1984-09-15'),
('bruse wayne', 'bruse.wayne@example.com', '2001-12-12'),
('jame jonah jameson', 'jame.jonah.jameson@example.com', '1980-07-31'),
('Tony Stark', 'tony.stark@example.com', '1984-09-15'),
('Bruce Banner', 'Bruce.Banner@example.com', '2000-07-21'),
('Thor Odinson', 'Thor.Odinson@example.com', '2004-04-03'),
('Janet van Dyne', 'Janet.van.Dyne@example.com', '1994-09-10'),
('Joe Biden', 'JoeBiden2024@example.com', '1999-07-21');
"""
cursor.execute(authors_insert)


books_insert = """
INSERT INTO books (author_id, isbn) VALUES
(1, '123-4-5678-9101-1'),
(2, '123-4-5678-9102-2'),
(3, '123-4-5678-9103-3'),
(4, '123-4-5678-9101-1'),
(5, '123-4-5678-9102-2'),
(6, '123-4-5678-9103-3'),
(7, '123-4-5678-9101-1'),
(8, '123-4-5678-9102-2'),
(9, '123-4-5678-9103-3'),
(10, '123-4-5678-9101-1'),
(11, '123-4-5678-9102-2'),
(12, '123-4-5678-9103-3');
"""
cursor.execute(books_insert)


sale_items_insert = """
INSERT INTO sale_items (book_id, customer_name, item_price, quantity) VALUES
(1, 'Betty Booklover', 19.99, 91),
(2, 'Felix Flask', 29.99, 110000),
(3, 'Diana Debugger', 39.99, 83),
(4, 'Gordon Goldfish', 19.99, 14),
(5, 'Stella Starseeker', 2999, 652),
(6, 'Victor Veto', 9.99, 543),
(7, 'Pamela Peace', 199, 231),
(8, 'Gary Gamer', 29.99, 22),
(9, 'Grillmaster Greg', 39.99, 3),
(10, 'Idealess Ian', 15.99, 1),
(11, 'Ramen Ron', 329.99, 22),
(12, 'Chef Noodle', 325.99, 323);
"""
cursor.execute(sale_items_insert)

conn.commit()
conn.close()
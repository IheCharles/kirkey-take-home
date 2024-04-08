from flask import Flask, jsonify  
import pymysql
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
def db_connection_init():
    conn = None
    try: 
        conn = pymysql.connect(    
            host='sql3.freesqldatabase.com', 
            user='sql3697196',
            password='DELhWFq2K5', 
            database='sql3697196', 
            charset='utf8mb4',  
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route("/", methods=["GET"])
@app.route("/<author>", methods=["GET"])
def home(author=None):
    conn = db_connection_init()
    cursor = conn.cursor()

    if author:
        query = f"""
        SELECT
            a.name AS author_name,
            SUM(si.item_price * si.quantity) AS total_sales
        FROM
            authors a
        JOIN
            books b ON a.id = b.author_id
        JOIN
            sale_items si ON b.id = si.book_id
        WHERE
            a.name = %s
        GROUP BY
            a.name;
        """
        cursor.execute(query, (author,))
        results = cursor.fetchall()

        if not results:
            conn.close()
            return jsonify({'error': f'Author "{author}" not found'}), 404
    else:
        query = """
        SELECT
            a.name AS author_name,
            SUM(si.item_price * si.quantity) AS total_revenue
        FROM
            authors a
        JOIN
            books b ON a.id = b.author_id
        JOIN
            sale_items si ON b.id = si.book_id
        GROUP BY
            a.name
        ORDER BY
            total_revenue DESC
        LIMIT 10;
        """
        cursor.execute(query)
        results = cursor.fetchall()

    conn.close()
    
    return jsonify(results)


@app.route("/DOB", methods=["GET"])
def authors_by_dob():
    conn = db_connection_init()
    cursor = conn.cursor()
    query = """
    SELECT name, date_of_birth
    FROM authors
    ORDER BY date_of_birth ASC
    LIMIT 10;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)


if __name__ == "__main__":
    app.run()

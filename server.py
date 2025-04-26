from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import traceback
from datetime import datetime
import random
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/display', methods=['GET'])
def display():
    order_id = request.args.get('orderId')
    db = {
        "StudentInfo": {},
        "OrderInfo": {},
        "DeliveryAddress": {}
    }

    if order_id:
        try:
            conn = psycopg2.connect(
                # database="food_delivery_db",
                # user="postgres",
                # password="Spring@2024JK",
                # host="localhost",
                # port="5432"
                database=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                host=os.environ["DB_HOST"],
                port=os.environ["DB_PORT"]
            )
            cur = conn.cursor()

            query = """
                SELECT s.name, s.email, s.phone, 
                       o.order_time, e.name, m.item_name, 
                       d.delivery_person
                FROM "Order" o
                JOIN student s ON o.student_id = s.student_id
                JOIN eatery e ON o.eatery_id = e.eatery_id
                JOIN order_details od ON o.order_id = od.order_id
                JOIN menu m ON od.menu_id = m.menu_id
                JOIN delivery d ON d.order_id = o.order_id
                WHERE o.order_id = %s;
            """
            cur.execute(query, (order_id,))
            row = cur.fetchone()

            if row:
                db["StudentInfo"] = {
                    "name": row[0],
                    "email": row[1],
                    "phone": row[2]
                }
                db["OrderInfo"] = {
                    "order_time": row[3],
                    "eatery_name": row[4],
                    "food_item": row[5]
                }
                db["DeliveryAddress"] = {
                    "delivery_person": row[6]
                }
            else:
                return render_template('nodata.html')

        except Exception as e:
            print("[ERROR] Failed to fetch order:", e)
            traceback.print_exc()
            return "An error occurred while fetching your order."

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('display.html', data=db)

@app.route('/order_status', methods=['GET', 'POST'])
def order_status():
    status = None
    order_id = None

    if request.method == 'POST':
        order_id = request.form.get('orderId')
    else:
        order_id = request.args.get('orderId')

    if order_id:
        try:
            conn = psycopg2.connect(
                # database="food_delivery_db",
                # user="postgres",
                # password="Spring@2024JK",
                # host="localhost",
                # port="5432"
                database=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                host=os.environ["DB_HOST"],
                port=os.environ["DB_PORT"]
            )
            cur = conn.cursor()

            query = 'SELECT delivery_status FROM "Order" WHERE order_id = %s;'
            cur.execute(query, (order_id,))
            result = cur.fetchone()

            if result:
                status = result[0]
            else:
                status = None

        except Exception as e:
            print("[ERROR] Failed to fetch order status:", e)
            traceback.print_exc()
            status = None

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('order_status.html', status=status, order_id=order_id)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/nodata')
def nodata():
    return render_template('nodata.html')

@app.route('/submit', methods=['POST'])
def submit():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            # database="food_delivery_db",
            # user="postgres",
            # password="Spring@2024JK",
            # host="localhost",
            # port="5432"
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"]
        )
        cur = conn.cursor()

        form = request.form
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        dob = form.get('dob')
        nationality = form.get('nationality')
        gender = form.get('gender')
        eatery_id = form.get('eatery_id')
        food_item_id = form.get('food_item_id')
        order_date = form.get('order_date')
        street = form.get('street')
        city = form.get('city')
        state = form.get('state')
        zip_code = form.get('zip_code')
        student_id = random.randint(101, 99999)

        cur.execute("""
            INSERT INTO student (student_id, name, email, phone)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, %s, %s);
        """, (student_id, name, email, phone))

        order_id = random.randint(101, 99999)

        cur.execute("""
            INSERT INTO "Order" (order_id, student_id, eatery_id, order_time, delivery_status)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, %s, NOW(), %s);
        """, (order_id, student_id, eatery_id, 'Pending'))

        cur.execute("""
            INSERT INTO order_details (order_id, menu_id, quantity)
            VALUES (%s, %s, %s);
        """, (order_id, food_item_id, 1))

        delivery_id = random.randint(101, 99999)

        cur.execute("""
            INSERT INTO delivery (delivery_id, order_id, delivery_time, delivery_person)
            OVERRIDING SYSTEM VALUE
            VALUES (%s, %s, NOW(), %s);
        """, (delivery_id, order_id, 'SystemBot'))

        conn.commit()
        return redirect(url_for('success'))

    except Exception as e:
        print("[ERROR] Failed to submit order:", e)
        traceback.print_exc()
        if conn:
            conn.rollback()
        return "An error occurred while submitting your order."

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)port = int(os.environ.get('DB_PORT', 5000))
    app.run(host='0.0.0.0', port=port)

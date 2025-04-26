-- Load student
COPY student(student_id, name, email, phone, dob, nationality, gender)
FROM 'C:/Users/teert/Downloads/student_export.csv' WITH CSV HEADER;

-- Load eatery
COPY eatery(eatery_id, name, location)
FROM 'C:/Users/teert/Downloads/eatery_export.csv' WITH CSV HEADER;

-- Load menu
COPY menu(menu_id, eatery_id, item_name, price)
FROM 'C:/Users/teert/Downloads/menu_export.csv' WITH CSV HEADER;

-- Load Order
COPY "Order"(order_id, student_id, eatery_id, order_time, delivery_status)
FROM 'C:/Users/teert/Downloads/order_export.csv' WITH CSV HEADER;

-- Load order_details
COPY order_details(order_id, menu_id, quantity)
FROM 'C:/Users/teert/Downloads/order_details_export.csv' WITH CSV HEADER;

-- Load meal_plan
COPY meal_plan(meal_plan_id, student_id, balance)
FROM 'C:/Users/teert/Downloads/meal_plan_export.csv' WITH CSV HEADER;

-- Load delivery
COPY delivery(delivery_id, order_id, delivery_time, delivery_person)
FROM 'C:/Users/teert/Downloads/delivery_export.csv' WITH CSV HEADER;

-- Load payment
COPY payment(payment_id, order_id, amount, payment_date)
FROM 'C:/Users/teert/Downloads/payment_export.csv' WITH CSV HEADER;

-- Load report
COPY report(report_id, order_id, issue, created_at)
FROM 'C:/Users/teert/Downloads/report_export.csv' WITH CSV HEADER;

-- Load admin
COPY admin(admin_id, username, password)
FROM 'C:/Users/teert/Downloads/admin_export.csv' WITH CSV HEADER;

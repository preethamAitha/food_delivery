-- CREATE  for Centralized Food Delivery System (10 Tables)

-- 1. Student Table
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    dob DATE,
    nationality VARCHAR(50),
    gender VARCHAR(20),
    meal_plan_id INTEGER
);

-- 2. Eatery Table
CREATE TABLE Eatery (
    eatery_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255)
);

-- 3. Menu Table
CREATE TABLE Menu (
    menu_id SERIAL PRIMARY KEY,
    eatery_id INTEGER REFERENCES Eatery(eatery_id),
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(8,2) NOT NULL
);

-- 4. Order Table
CREATE TABLE "Order" (
    order_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Student(student_id),
    eatery_id INTEGER REFERENCES Eatery(eatery_id),
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_status VARCHAR(20) DEFAULT 'Pending'
);

-- 5. Order_Details Table
CREATE TABLE Order_Details (
    order_id INTEGER REFERENCES "Order"(order_id),
    menu_id INTEGER REFERENCES Menu(menu_id),
    quantity INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (order_id, menu_id)
);

-- 6. Meal_Plan Table
CREATE TABLE Meal_Plan (
    meal_plan_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Student(student_id),
    plan_name VARCHAR(50),
    balance DECIMAL(8,2) DEFAULT 0
);

-- 7. Delivery Table
CREATE TABLE Delivery (
    delivery_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES "Order"(order_id),
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip VARCHAR(20),
    delivery_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_person VARCHAR(100) DEFAULT 'SystemBot'
);

-- 8. Payment Table
CREATE TABLE Payment (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES "Order"(order_id),
    amount DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    method VARCHAR(50)
);

-- 9. Report Table
CREATE TABLE Report (
    report_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Student(student_id),
    order_id INTEGER REFERENCES "Order"(order_id),
    issue_description TEXT,
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Admin Table
CREATE TABLE Admin (
    admin_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

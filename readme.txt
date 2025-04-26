# Centralized Food Delivery System for On-Campus Eateries

## Setup Instructions
1. Open `create.sql` file in PostgreSQL and execute it. This will create all the necessary tables.
2. Modify the `load.sql` file to update the correct paths to your dataset CSV files.
3. Open and execute `load.sql` in PostgreSQL to load initial data.
4. Install required Python packages using `pip install flask psycopg2`.
5. Run the `server.py` file to start the Flask server.
6. Access the web application at `http://localhost:5000` on your browser.


## Website Pages
- Home ➔ Project overview and the problem statement.
- About ➔ Details about the purpose and functionality.
- Register ➔ Place a new food order.
- View Orders ➔ Search and view detailed order information.
- Order Status ➔ Check delivery status (e.g., Pending, Out for Delivery, Delivered).
- Contact ➔ Contact details for help and support.

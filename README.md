# Aquametrics Backend

Aquametrics is an IoT-based water quality monitoring system. This repository contains the backend application for Aquametrics, built with Flask and InfluxDB.

## Getting Started

To get started with the Aquametrics backend, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/mgs042/Aqua_B.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Aqua_B
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set up InfluxDB:

   - Install InfluxDB on your system.
   - Create a new database for Aquametrics.

7. Configure the application:

   -Update 'config.py'

8. Start the Flask application:

    ```bash
    python __init__.py
    ```


## Endpoints

## Endpoints

- **GET /:** Renders the sensor data input form (`sensor_form.html`).
- **GET /add_sensor:** Renders the form for adding a new sensor (`add_sensor_form.html`).
- **POST /write:** Receives sensor data via a form submission and stores it in the InfluxDB database.
- **POST /new_sensor:** Creates a new sensor based on the submitted form data and stores it in the InfluxDB database.
- **GET /chart_query:** Executes a query to retrieve data for charting purposes from the InfluxDB database.
- **GET /list_sensor:** Retrieves a list of sensors from the InfluxDB database.
    
## Technologies Used

- **Flask:** Micro web framework for building web applications.
- **InfluxDB:** Time-series database for storing sensor data.
- **Python:** Programming language used for the backend logic.

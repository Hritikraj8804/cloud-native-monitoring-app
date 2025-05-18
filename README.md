# cloud-native-monitoring-app

## System Monitoring Dashboard

A simple yet effective web application, this project uses Flask and Plotly.js to create a system monitoring dashboard for visualizing CPU, memory, and disk usage.
![Screenshot 2025-04-01 225634](https://github.com/user-attachments/assets/396f6431-16a6-4aa7-b303-35066b92385f)

## Features

* **Real-time System Metrics:** Displays CPU, memory, and disk utilization in interactive gauge charts.
* **Warning System:** Alerts the user when resource usage exceeds a defined threshold (80%).
* **Responsive Design:** Adapts to various screen sizes for optimal viewing.
* **Clear Visualizations:** Uses Plotly.js gauge charts for intuitive data representation.

## Technologies Used

* **Python:** Backend logic and data retrieval.
* **Flask:** Web framework for serving the dashboard.
* **psutil:** Library for retrieving system resource usage.
* **Plotly.js:** JavaScript library for creating interactive charts.
* **HTML/CSS:** Frontend structure and styling.

## Prerequisites

* Python 3.6+
* pip (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install Flask psutil
    ```

## Running the Application

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Open your web browser and navigate to `http://0.0.0.0:5000/`.**

## Project Structure

Markdown

# System Monitoring Dashboard

This project provides a simple, web-based system monitoring dashboard using Flask and Plotly.js to visualize CPU, memory, and disk usage.

## Features

* **Real-time System Metrics:** Displays CPU, memory, and disk utilization in interactive gauge charts.
* **Warning System:** Alerts the user when resource usage exceeds a defined threshold (80%).
* **Responsive Design:** Adapts to various screen sizes for optimal viewing.
* **Clear Visualizations:** Uses Plotly.js gauge charts for intuitive data representation.

## Technologies Used

* **Python:** Backend logic and data retrieval.
* **Flask:** Web framework for serving the dashboard.
* **psutil:** Library for retrieving system resource usage.
* **Plotly.js:** JavaScript library for creating interactive charts.
* **HTML/CSS:** Frontend structure and styling.

## Prerequisites

* Python 3.6+
* pip (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install Flask psutil
    ```

## Running the Application

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Open your web browser and navigate to `http://0.0.0.0:5000/`.**

## Project Structure

system-monitoring-dashboard/  
├── app.py          # Flask application and backend logic  
├── templates/  
│   └── index.html  # HTML template for the dashboard  
└── README.md       # Project documentation  


## Usage

* The dashboard displays three gauge charts: CPU Utilization, Memory Utilization, and Disk Utilization.
* If any of the resource usage values exceed 80%, a warning message will be displayed at the bottom of the page.
* The gauges are interactive. Hover over them to see the exact numeric value.

## Customization

* **Threshold:** Modify the threshold value in `app.py` to change the warning trigger.
* **Styling:** Customize the appearance of the dashboard by modifying the CSS in `index.html`.
* **Additional Metrics:** Extend the application to monitor other system metrics by adding more functions and gauges.
* **Gauge styling:** The colors and general gauge styling can be changed inside of index.html.

## Notes

* This application provides basic system monitoring. For more advanced monitoring, consider using dedicated monitoring tools like Prometheus, Grafana, or AWS CloudWatch.
* Ensure that the server running this application has the necessary permissions to access system resource information.
* Plotly.js is loaded from a CDN. For offline use, you'll need to download and include the library locally.

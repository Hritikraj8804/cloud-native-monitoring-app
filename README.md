# cloud-native-monitoring-app

# System Monitoring Dashboard

This project provides a simple, web-based system monitoring dashboard using Flask and Plotly.js to visualize CPU, memory, and disk usage.

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


import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    message = None
    if cpu_usage > 80 or memory_usage > 80 or disk_usage > 80:
        message = "Warning: High resource usage detected!"
    return render_template('index.html', cpu_usage=cpu_usage, memory_usage=memory_usage, disk_usage=disk_usage, message=message)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
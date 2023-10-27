import platform  # Import the platform module
from flask import Flask, render_template, jsonify
import datetime
import random


app = Flask(__name__)

@app.route('/healthz')
def health_check():

    health_status = {
        'status': 'healthy',
        'message': 'Application is running smoothly',
    }
    response = jsonify(health_status)
    response.status_code = 200
    return response

# Routes for individual features (weather, date, random)

@app.route('/weather')
def get_weather():
    weather_data = {
        'temperature': random.randint(100, 500),
        'condition': 'Super hot!',
    }
    return render_template('weather.html', **weather_data)


@app.route('/date')
def get_date():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('date.html', current_date=current_time)


@app.route('/random')
def get_random():
    random_number = random.randint(1, 100)
    return render_template('random.html', random_number=random_number)


@app.route('/system')
def system_info():
    processor = platform.processor()
    system_name = platform.system()
    platform_info = platform.platform()
    os_name = platform.system()
    os_release = platform.release()
    machine_arch = platform.machine()
    python_version = platform.python_version()
    return render_template('platform.html', processor=processor,
                           system_name=system_name, platform=platform_info,
                           os_name=os_name, os_release=os_release,
                           machine_arch=machine_arch, python_version=python_version)


@app.route('/crash')
def crash_app():
    raise Exception("Intentional crash for testing purposes")


@app.route('/')
def start_page():
    return """
    <html>
    <head>
        <title>Start Page</title>
    </head>
    <body>
        <h1>Welcome to the Start Page</h1>
        <ul>
            <li><a href="/weather">Weather Information</a></li>
            <li><a href="/date">Current Date and Time</a></li>
            <li><a href="/random">Random Number</a></li>
            <li><a href="/system">System Information</a></li>  
            <li><a href="/crash">This route intentionally raises an exception to crash the application</a></li>  
        </ul>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

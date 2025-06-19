from flask import Flask, render_template, request, redirect, url_for
import subprocess

bulb_status_msg = ""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', status_msg=bulb_status_msg)

@app.route("/bulb-status", methods=["POST"])
def bulb_status():
    global bulb_status_msg
    data = request.get_json()
    bulb_status_msg = data["status"]
    print("Bulb Status Received:", bulb_status_msg)
    return "Status received", 200

@app.route('/start', methods=['POST'])
def start():
    subprocess.Popen(['./start.sh'])
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def start():
    subprocess.Popen(['./stop.sh'])
    return redirect(url_for('index'))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    subprocess.Popen(['./shutdown.sh'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


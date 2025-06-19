from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    subprocess.Popen(['./start.sh'])
    return redirect(url_for('index'))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    subprocess.Popen(['./shutdown.sh'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


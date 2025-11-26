from flask import Flask, request
import os
import time   # <-- FALTAVA ISSO!

app = Flask(__name__)
INSTANCE = os.environ.get('INSTANCE_NAME', 'app')

@app.route('/')
def index():
    return f"Hello from {INSTANCE} — {time.strftime('%Y-%m-%d %H:%M:%S')}\n"

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        servidor=os.getenv("INSTANCE_NAME", "desconhecido"),
        horario=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Flask!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

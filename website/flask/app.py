from flask import Flask, render_template_string
import logging
import time
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Summary

app = Flask(__name__)

# Definisikan data_store
data_store = []

# Inisialisasi PrometheusMetrics
metrics = PrometheusMetrics(app)

# Logging ke file
logging.basicConfig(filename='app.log', level=logging.INFO)

# Definisikan Counter dan Summary
calc_counter = Counter('calc_requests_total', 'Total /calc requests', ['method', 'endpoint'])
calc_time = Summary('calc_processing_seconds', 'Time spent processing /calc')

mem_counter = Counter('mem_requests_total', 'Total /mem requests', ['method', 'endpoint'])
log_counter = Counter('log_requests_total', 'Total /log requests', ['method', 'endpoint'])

# HTML tampilan halaman utama
HTML = """
<!DOCTYPE html>
<html>
<head><title>Flask Monitor App</title></head>
<body>
<h1>Flask App Monitoring</h1>
<p><a href="/calc">Run Calculation</a></p>
<p><a href="/mem">Use Memory</a></p>
<p><a href="/log">Write Log</a></p>
<p><a href="/metrics">/metrics</a> (untuk Prometheus)</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/calc')
@calc_time.time()  # ⏱️ ukur waktu eksekusi
def calc():
    calc_counter.labels(method='GET', endpoint='/calc').inc()  # ➕ Tambah hitungan dengan label
    total = 0
    for i in range(10**6):
        total += i*i
    return f"calc done: {total}"

@app.route('/mem')
def memory():
    mem_counter.labels(method='GET', endpoint='/mem').inc()  # ➕ Tambah hitungan dengan label
    data_store.append('x' * 10**6)  # 🧠 Simulasi konsumsi memory (1 MB)
    return f"stored {len(data_store)} MB"

@app.route('/log')
def log():
    log_counter.labels(method='GET', endpoint='/log').inc()  # ➕ Tambah hitungan dengan label
    logging.info("Log test at %s", time.ctime())
    return "log written"

# Metrik akan otomatis di-serve di /metrics oleh PrometheusMetrics
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

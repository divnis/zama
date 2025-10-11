from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute_sum', methods=['POST'])
def compute_sum():
    data = request.get_json()
    masked_values = data.get('masked_values', [])
    start = time.time()
    try:
        masked_values = [float(x) for x in masked_values]
    except Exception as e:
        return jsonify({"error": "invalid numbers", "detail": str(e)}), 400

    masked_sum = sum(masked_values)
    elapsed_ms = int((time.time() - start) * 1000)
    return jsonify({
        "masked_sum": masked_sum,
        "server_time_ms": elapsed_ms
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


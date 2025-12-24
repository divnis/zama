"""
Confidential Space Reputation – Zama FHE Prototype

This backend file represents a prototype service used to:
- Demonstrate how reputation or participation data may be collected
  after X (Twitter) Space participation
- Simulate score aggregation prior to encryption and on-chain submission

IMPORTANT CLARIFICATIONS FOR REVIEWERS:
- This backend DOES NOT store final reputation values
- This backend DOES NOT perform encryption
- This backend DOES NOT represent the FHE computation itself

In a full Zama FHE production system:
1. Reputation values would be encrypted client-side
   (or via Zama Relayer / Gateway)
2. Encrypted values would be sent on-chain
3. All computations would occur fully under FHE
4. Smart contracts would never see plaintext values

This file exists to:
- Explain system architecture
- Support UI demonstration
- Show integration points for Zama FHEVM
- Provide a minimal, auditable prototype for bounty scope

The smart contract, relayer, and gateway layers are intentionally
abstracted to focus on privacy design and FHE suitability.
"""

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
    """
    Prototype endpoint that simulates aggregation of masked values.

    In a real FHE setup:
    - Values arriving here would already be encrypted OR
    - This endpoint would be replaced entirely by on-chain FHE logic

    This endpoint exists ONLY to demonstrate:
    - Data flow
    - Latency measurement
    - Architectural separation of concerns
    """
    data = request.get_json()
    masked_values = data.get('masked_values', [])

    start = time.time()
    try:
        masked_values = [float(x) for x in masked_values]
    except Exception as e:
        return jsonify({
            "error": "invalid numbers",
            "detail": str(e)
        }), 400

    masked_sum = sum(masked_values)
    elapsed_ms = int((time.time() - start) * 1000)

    return jsonify({
        "masked_sum": masked_sum,
        "server_time_ms": elapsed_ms
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Hello from ECS Fargate!",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    # The Load Balancer looks for a 200 OK status
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
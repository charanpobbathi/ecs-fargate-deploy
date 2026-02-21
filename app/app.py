from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Returning a styled HTML page
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ECS Fargate App</title>
        <style>
            body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f2f5; }
            .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
            h1 { color: #232f3e; margin-bottom: 1rem; }
            .status { color: #2ecc71; font-weight: bold; }
            .version { color: #7f8c8d; font-size: 0.8rem; margin-top: 1rem; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello from ECS Fargate!</h1>
            <p>Your CI/CD pipeline is working perfectly.</p>
            <p class="status">● System Status: Online</p>
            <div class="version">Build Version: 1.0.1</div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
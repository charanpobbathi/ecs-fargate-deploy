from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Deployment Successful!</h1><p>Running on Amazon ECS Fargate - 2</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
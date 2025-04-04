from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to SkillLink Africa Backend!"})

if __name__ == '__main__':
    app.run(debug=True)


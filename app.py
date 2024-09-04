from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_numbers():
    data = request.get_json()
    if isinstance(data, list) and all(isinstance(i, int) for i in data):
        result = sum(data)
        return jsonify(result=result)
    return jsonify(error="Invalid input"), 400

if __name__ == '__main__':
    app.run(debug=True)

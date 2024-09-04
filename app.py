from flask import Flask, request, jsonify

app = Flask(__name__)

#Definining int32
INT32_MIN = -2**31
INT32_MAX = 2**31 - 1

@app.route('/process', methods=['POST'])
def process_numbers():
    data = request.get_json()
    if isinstance(data, list) and all(isinstance(i, int) and INT32_MIN <= i <= INT32_MAX for i in data):
        result = sum(data)
        return jsonify(result=result)
    return jsonify(error="Invalid input"), 400

if __name__ == '__main__':
    app.run(debug=True)
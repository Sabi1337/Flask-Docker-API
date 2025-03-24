from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route('/quote', methods=['GET'])
def get_random_quote():
    return jsonify({"quote": random.choice(quotes)})

@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)

@app.route('/add_quote', methods=['POST'])
def add_quote():
    new_quote = request.json.get("quote")
    if new_quote:
        quotes.append(new_quote)
        with open("quotes.json", "w") as file:
            json.dump(quotes, file)
        return jsonify({"message": "Quote added!"}), 201
    return jsonify({"error": "No quote provided"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

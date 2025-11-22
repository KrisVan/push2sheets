from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from parser import parse_expense
from sheets import append_expense

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    """
    Receives POST requests with JSON containing notification text.
    Parses the expense and appends it to Google Sheets.
    """
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    expense = parse_expense(text)
    if expense:
        append_expense(expense)
        return jsonify({"status": "logged", "expense": expense})
    else:
        return jsonify({"status": "ignored"}), 200

@app.route("/", methods=["GET"])
def health():
    """
    Simple health check endpoint
    """
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
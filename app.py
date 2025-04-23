from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    message = f"Trading Signal:\n{data.get('text', 'No text')}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

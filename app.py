from flask import Flask, request

app = Flask(_name_)

VERIFY_TOKEN = "NoorulIstiqamah2026"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Webhook received:")
    print(data)

    return "EVENT_RECEIVED", 200

@app.route("/", methods=["GET"])
def home():
    return "Noorul Istiqamah WhatsApp Webhook is running!", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    response = MessagingResponse()
    msg = response.message("Hi")
    return str(response)


if __name__ == "__main__":
    app.run(port=5000)

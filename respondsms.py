from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None).lower()

    responce = MessagingResponse()
    print(body)
    if body == 'no' or body == 'stop':
        responce.message("Thank you for your response. We will remove you from our candidate list.")
    elif body == 'yes':
        responce.message("Great, one of our recruiters will be in touch with you!")
    else:
        responce.message("Sorry I don't understand please respond with yes or no and a recruiter will either reach out or not. Thank you!")
 
   
    return str(responce)

if __name__ == "__main__":
    app.run(debug=True)
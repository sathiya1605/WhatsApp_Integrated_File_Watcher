from twilio.rest import Client

# ----------------WhatsApp API Credentials--------------------------------#

account_sid = '<account_sid>'   # account_sid = 'AC2946b46774e496f09aa1fa70857277fd'
auth_token = '<auth_token>'     # auth_token = '20564e8333662fb30d300852fb348e63'
client = Client(account_sid, auth_token)


def whatsAppMsgAPI(msg):
    message = client.messages.create(
        from_='whatsapp:+1xxxxxxxxxx',   # tiwilio API number
        body=msg,
        to='whatsapp:+91xxxxxxxxxx'     # Your phone number
    )
import os
from fastapi import FastAPI, Request, Response
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Credentials from Render Environment Variables
TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

@app.get("/webhook")
async def verify(request: Request):
    # Meta sends a GET request to verify your webhook
    params = request.query_params
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return Response(content=params.get("hub.challenge"), media_type="text/plain")
    return "Verification failed", 403

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    
    try:
        # Check if it's a message event
        if "messages" in data["entry"][0]["changes"][0]["value"]:
            message = data["entry"][0]["changes"][0]["value"]["messages"][0]
            from_number = message["from"]
            
            # Simple Receptionist Logic
            if "text" in message:
                user_text = message["text"]["body"].lower()
                
                if "hi" in user_text or "hello" in user_text:
                    send_reply(from_number, "Hello! I am your business assistant. How can I help you today?")
                else:
                    send_reply(from_number, "Thank you for your message. A human agent will be with you shortly!")
                    
    except Exception as e:
        print(f"Error: {e}")
        
    return {"status": "success"}

def send_reply(to, text):
    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, json=payload, headers=headers)

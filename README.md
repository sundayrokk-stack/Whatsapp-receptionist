# WhatsApp Receptionist Bot

1.  **Deploy to Render:** Connect your GitHub repo.
2.  **Add Env Vars:**
    * `WHATSAPP_TOKEN`: Your Temporary/Permanent Access Token.
    * `VERIFY_TOKEN`: A random string you make up (e.g., `receptionist123`).
    * `PHONE_NUMBER_ID`: Found in your Meta Developer Dashboard.
3.  **Meta Setup:** * Set Webhook URL to: `https://your-render-url.onrender.com/webhook`
    * Set Verify Token to: (The string you chose above)
    * Subscribe to `messages` in Webhook fields.

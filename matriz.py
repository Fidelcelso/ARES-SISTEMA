import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# CONFIGURACIÓN DEL CEREBRO
genai.configure(api_key="AIzaSyDQozPZ_tZW59j3qffBX6ISmRSuvP_6Tpk")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data.get('message', '')
    try:
        response = model.generate_content(f"Eres ARES, IA táctica de Fidel. Responde directo: {user_input}")
        
        link = None
        if "SPOTIFY" in response.text.upper():
            link = "intent://open#Intent;scheme=spotify;package=com.spotify.music;end"
            
        return jsonify({"response": response.text, "redirect": link})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
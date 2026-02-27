import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# CONFIGURACIÓN DEL MOTOR ARES
# Buscamos la llave en Render, si no está, usamos la que me pasaste
api_key = os.environ.get("GOOGLE_API_KEY", "AIzaSyDQozPZ_tZW59j3qffBX6ISmRSuvP_6Tpk")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    # Esta ruta carga tu página principal
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Esta ruta recibe los mensajes de Fidel
    data = request.get_json()
    user_input = data.get('message', '')
    
    try:
        # Instrucción de personalidad táctica
        prompt = f"Actúa como ARES, el sistema de inteligencia artificial táctico de Fidel. Responde de forma concisa, lógica y leal: {user_input}"
        response = model.generate_content(prompt)
        
        return jsonify({"response": response.text})
    
    except Exception as e:
        # Si algo falla, el sistema lo reporta
        return jsonify({"response": f"ERROR EN LA MATRIZ: {str(e)}"}), 500

if __name__ == "__main__":
    # Configuración para que Render pueda asignar el puerto automáticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

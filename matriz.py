import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuración de la IA (Usa variable de entorno o pega tu clave aquí si prefieres)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY", "TU_API_KEY_AQUI"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    try:
        # Toque especial: Instrucción de personalidad para ARES
        prompt = f"Actúa como ARES, un sistema de inteligencia artificial avanzado, lógico, leal a Fidel y con un toque de ingenio. Responde de forma concisa pero poderosa a: {user_input}"
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error en la Matriz: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)

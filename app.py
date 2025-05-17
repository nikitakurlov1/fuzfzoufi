from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех доменов

# API ключ
API_KEY = "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"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '')
        
        # Отправляем запрос к OpenRouter API
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:5000",  # URL вашего сайта
                "X-Title": "Nka_ai Chat",  # Название вашего сайта
            },
            json={
                "model": "meta-llama/llama-3.3-8b-instruct:free",  # Используем бесплатную модель
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )

        if response.status_code != 200:
            return jsonify({'error': 'Ошибка при обращении к API'}), 500

        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) 
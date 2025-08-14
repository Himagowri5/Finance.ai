# huggingface_api.py
import requests

API_KEY ="sk-d360b59fa09a4986b5c236ef3805f745"
#model_id = "openai/gpt-3.5-turbo"
#
MODEL_ID="deepseek/deepseek-r1:free"
API_URL="https://openrouter.ai/api/v1"
headers = {"Authorization": f"Bearer {API_KEY}"}

def get_chatbot_response(user_input):
    payload = {"inputs": user_input}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises an error for HTTP errors

        data = response.json()
        # Check Hugging Face text generation response forma
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict) and "error" in data:
            return "Error from model: " + data["error"]
        else:
            return str(data)
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"

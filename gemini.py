import google.generativeai as genai
import os

API_KEY = os.getenv('API_KEY')

def gemini(mensagens):
    genai.configure(api_key="YOUR_API_KEY")

    # Convert the mensagens list into the appropriate format
    history = [{"parts": [{"inline_data": message["content"], "role": message["role"]}]} for message in mensagens]

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
    }

    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config)

    convo = model.start_chat(history=history)

    return convo.last.text
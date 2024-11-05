import requests

DJANGO_CHATBOT_URL = f"http://localhost:8000/chatbot/"

def get_chatbot_response(user_message):
    try:
        response = requests.post(f'{DJANGO_CHATBOT_URL}chat/', data={'message': user_message})
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get('response', 'Erro ao obter resposta.')
        else:
            return "Erro na comunicação com o servidor."

    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com o servidor: {e}"

def get_all_chats():
    try:
        response = requests.get(f'{DJANGO_CHATBOT_URL}get_chats')
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "O endpoint de chats não foi encontrado no servidor."
        else:
            return f"Erro ao recuperar chats: Código de status {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com o servidor: {e}"

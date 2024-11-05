import os
from groq import Groq
from chatbot.models import Message


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_response_from_llm(user_message):
    try:
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        bot_response = chat_completion.choices[0].message.content

        Message.objects.create(
            user_message=user_message, 
            bot_response=bot_response
        )

        return bot_response

    except Exception as e:
        return str(e)
from django.db import models


from django.db import models

class Message(models.Model):
    user_message = models.TextField("Mensagem do Usuário")
    bot_response = models.TextField("Resposta do Chatbot")
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)


    class Meta:
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


    def __str__(self):
        return f"Mensagem de {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

from telegram.ext import Updater, MessageHandler, Filters
from threading import Timer
import os

TOKEN =os.getenv("TOKEN")

def bienvenida(update, context):
    for miembro in update.message.new_chat_members:
        # Enviar la imagen de bienvenida
        mensaje = context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('img.jpg', 'rb'),
            caption=f"¡Bienvenido {miembro.first_name}!\nA nuestra comunidad 🎉\nRevisa las reglas del grupo."
        )

        # Programar la eliminación del mensaje en 60 segundos
        Timer(60, lambda: context.bot.delete_message(chat_id=mensaje.chat_id, message_id=mensaje.message_id)).start()

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, bienvenida))

    updater.start_polling()
    print("Bot con bienvenida visual iniciado...")
    updater.idle()

if __name__ == '__main__':
    main()


# 
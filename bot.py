import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from yt_dlp import YoutubeDL

TOKEN = os.getenv("7267393832:AAFK-hdvjOAfELSsB41SHSEMs_Qk8-KIhUM")

def start(update, context):
    update.message.reply_text("Привет! Отправь мне ссылку на YouTube-видео, и я скачаю аудио.")

def download_audio(update, context):
    url = update.message.text
    update.message.reply_text("Скачиваю аудио...")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        update.message.reply_audio(audio=open('audio.mp3', 'rb'))
        os.remove('audio.mp3')
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_audio))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

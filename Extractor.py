import re
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Telegram bot token'ınızı buraya yapıştırın
TOKEN = 'TELEGRAM API'

# Loglama ayarları
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# E-posta ve hash regex'leri
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
hash_regexes = {
    'bcrypt': r'\$2[aby]\$[0-9]{2}\$[./A-Za-z0-9]{53}',
    'md5': r'\b[0-9a-fA-F]{32}\b',
    'sha1': r'\b[0-9a-fA-F]{40}\b',
    'sha256': r'\b[0-9a-fA-F]{64}\b',
    'sha384': r'\b[0-9a-fA-F]{96}\b',
    'sha512': r'\b[0-9a-fA-F]{128}\b',
    'argon2': r'\$argon2[id]\$[0-9]+\$[./A-Za-z0-9]+\$[./A-Za-z0-9]{43}',
    'scrypt': r'\$scrypt\$[0-9]+:[A-Za-z0-9+/]+={0,2}:[A-Za-z0-9+/]+={0,2}',
    'pbkdf2': r'\b[0-9a-fA-F]{64,}\b',
}

# /start komutu için handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a TXT file and I will extract the email and hash information from it. \n \nCreator: \nMehmet Akif Aydoğmuş \n@akiiF1 \nmehmetakifaydogmus.com')

# Dosya mesajı için handler
async def handle_document(update: Update, context: CallbackContext) -> None:
    document = update.message.document
    file = await document.get_file()
    file_path = f'{document.file_id}.txt'
    await file.download_to_drive(file_path)

    with open(file_path, 'r') as file:
        content = file.read()
        emails = re.findall(email_regex, content)
        hash_matches = {}
        for hash_type, regex in hash_regexes.items():
            matches = re.findall(regex, content)
            if matches:
                hash_matches[hash_type] = matches

    if hash_matches:
        max_matches_type = max(hash_matches, key=lambda k: len(hash_matches[k]))
        selected_hashes = hash_matches[max_matches_type]
        selected_hash_type = max_matches_type
    else:
        selected_hashes = []
        selected_hash_type = 'None'

    output_file_path = f'{document.file_id}_emailandpass.txt'
    with open(output_file_path, 'w') as output_file:
        output_file.write(f'Selected Hash Type: {selected_hash_type}\n\n')
        for email, hash_value in zip(emails, selected_hashes):
            output_file.write(f'Email: {email}\nHash: {hash_value}\n\n')

    await context.bot.send_document(chat_id=update.effective_chat.id, document=open(output_file_path, 'rb'))
    os.remove(file_path)
    os.remove(output_file_path)

def main() -> None:
    # Application ve botu başlat
    application = Application.builder().token(TOKEN).build()

    # Komut ve mesaj handlerlarını ekle
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.TXT, handle_document))

    # Botu çalıştır
    application.run_polling()

if __name__ == '__main__':
    main()

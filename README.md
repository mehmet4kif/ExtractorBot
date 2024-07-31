# ExtractorBot
It finds the emails and passwords in the file you sent. 
https://t.me/mailpass_extractorbot

# Telegram Bot: Email ve Hash Bilgilerini Çıkaran Bot

Bu bot, kullanıcıların bir metin dosyasındaki (TXT) e-posta ve hash bilgilerini çıkarır ve sonuçları içeren bir dosya gönderir.

## Özellikler

- Kullanıcıların gönderdiği TXT dosyalarından e-posta ve hash bilgilerini çıkarır.
- Çıkarılan bilgileri yeni bir dosyaya yazar ve bu dosyayı kullanıcıya geri gönderir.
- Desteklenen hash türleri: bcrypt, md5, sha1, sha256, sha384, sha512, argon2, scrypt, pbkdf2.

## Kurulum ve Kullanım

### Gereksinimler

- Python 3.7+
- `python-telegram-bot` kütüphanesi

### Adımlar

1. Bu depoyu klonlayın:
    ```sh
    git clone https://github.com/mehmet4kif/ExtractorBot.git
    cd telegram-bot
    ```

2. Bot token'ınızı `TOKEN` değişkenine yapıştırın:
    ```python
    # Telegram bot token'ınızı buraya yapıştırın
    TOKEN = 'TELEGRAM API'
    ```

3. Botu başlatın:
    ```sh
    python Extractor.py
    ```

### Kullanım

- `/start` komutunu kullanarak botu başlatın.
- TXT dosyanızı bota gönderin.
- Bot, dosyadaki e-posta ve hash bilgilerini çıkarır ve size yeni bir dosya gönderir.

## Yapımcı

- **Mehmet Akif Aydoğmuş**
  - Web Sitesi: [mehmetakifaydogmus.com](https://mehmetakifaydogmus.com)
  - Telegram: [@akiiF1](https://t.me/akiiF1)

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.


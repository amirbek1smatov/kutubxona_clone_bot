from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Aloqa")  # Use parentheses to create a button
        ],
        [
            KeyboardButton("✅ FOYDALI KANALLAR VA ULARDA REKLAMA")
        ],
        [
            KeyboardButton("🇬🇧 English")
        ],
        [
            KeyboardButton("📚 O'zbek adabiyoti"),
            KeyboardButton("📚 Jahon adabiyoti")
        ],
        [
            KeyboardButton("📚 Bolalar adabiyoti"),
            KeyboardButton("📚 Mumtoz adabiyoti")
        ],
        [
            KeyboardButton("🎧 Audio kitoblar"),
            KeyboardButton("💯 Top 100 kitoblar")
        ],
        [
            KeyboardButton("📚 Maktab darsliklari"),
            KeyboardButton("📚 Islomiy kitoblar")
        ],
        [
            KeyboardButton("🔍 Lug'atlar")
        ],
        [
            KeyboardButton("📝 She'riyat"),
            KeyboardButton("📜 Alisher Navoiy asarlari")
        ],
        [
            KeyboardButton("📜O'zbekiston Milliy Ensiklopediyasi"),
            KeyboardButton("📋 O'zbek tilining izohli lug'atlari")
        ],
        [
            KeyboardButton("🔍 O'zbek tilining imlo lug'ati")
        ],
        [
            KeyboardButton("Islom Karimov asarlari"),
            KeyboardButton("Shavkat Mirziyoyev asarlari")
        ],
        [
            KeyboardButton("📥 Kitob o'qish uchun dasturlar")
        ],
        [
            KeyboardButton("🤖 Botni guruhga qo'shish"),
            KeyboardButton("↗️ Botni do'stlarga ulashish")
        ],
        [
            KeyboardButton("♻️ Takliflar"),
            KeyboardButton("⭐️ Botni baholash")
        ],
    ],
    resize_keyboard=True
)

english_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📚 Grammatika"),
            KeyboardButton("📚 IELTS")
        ],
        [
            KeyboardButton("📚 Vocabulary"),
            KeyboardButton("📚 Testlar")
        ],
        [
            KeyboardButton("📚 Fiction Books")
        ],
        [
            KeyboardButton("🇬🇧 Ingliz tilidan foydali kanallar")
        ],
        [
            KeyboardButton("Go back")
        ],
    ],
    resize_keyboard=True
)

uzbek_lit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Abdulla Qodiriy"),
            KeyboardButton("👤 Cho'lpon"),
        ],
        [
            KeyboardButton("👤 Oybek"),
            KeyboardButton("👤 G'afur G'ulom"),
        ],
        [
            KeyboardButton("👤 Abdulla Qahhor"),
            KeyboardButton("👤 Said Ahmad"),
        ],
        [
            KeyboardButton("👤 O'tkir Hoshimov"),
            KeyboardButton("👤 Pirimqul Qodirov"),
        ],
        [
            KeyboardButton("👤 Asqad Muxtor"),
            KeyboardButton("👤 Odil Yoqubov"),
        ],
        [
            KeyboardButton("👤 Tog'ay Murod"),
            KeyboardButton("👤 Tohir Malik"),
        ],
        [
            KeyboardButton("O'lmas Umarbekov")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

world_lit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Lev Tolstoy"),
            KeyboardButton("👤 Aleksandr Pushkin")
        ],
        [
            KeyboardButton("👤 Fyodor Dostoyevskiy"),
            KeyboardButton("👤 Mixail Bulgakov")
        ],
        [
            KeyboardButton("👤 Chingiz aytmatov"),
            KeyboardButton("👤 Nodar Dumbadze")
        ],
        [
            KeyboardButton("👤 Jek London"),
            KeyboardButton("👤 Gabriel Garsia Markes")
        ],
        [
            KeyboardButton("👤 Alber Kamyu"),
            KeyboardButton("👤 Kobo Abe")
        ],
        [
            KeyboardButton("👤 Lao She"),
            KeyboardButton("👤 Artur Konan Doyl")
        ],
        [
            KeyboardButton("👤 Agata Kristi"),
            KeyboardButton("👤 Gi De Mopassan")
        ],
        [
            KeyboardButton("👤 Onor De Balzak"),
            KeyboardButton("👤 Ernest Xeminguey")
        ],
        [
            KeyboardButton("👤 Jeyms Joes"),
            KeyboardButton("👤 Jonatan Svift")
        ],
        [
            KeyboardButton("👤 Jyul Vern"),
            KeyboardButton("👤 Somerset Moem")
        ],
        [
            KeyboardButton("👤 Robindranat Tagor")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

child_lit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📚 Ertaklar")
        ],
        [
            KeyboardButton("🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

classic_lit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📓 Boburnoma")
        ],
        [
            KeyboardButton("📓 Shohnoma")
        ],
        [
            KeyboardButton("📓 Zarbulmasal")
        ],
        [
            KeyboardButton("📓 To'rt ulus tarixi")
        ],
        [
            KeyboardButton("📓 Devoni lug'otut turk")
        ],
        [
            KeyboardButton("📓 Qutadg'u bilig")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

audio_books = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbek adabiyoti")
        ],
        [
            KeyboardButton("🌐 Jahon adabiyoti")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

uzbek_literature = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Romanlar"),
        ],
        [
            KeyboardButton("Qissalar"),
        ],
        [
            KeyboardButton("Hikoyalar"),
        ],
        [
            KeyboardButton("Go back"),
        ]
    ],
    resize_keyboard=True
)

world_literature = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Romanlar"),
        ],
        [
            KeyboardButton("Qissalar"),
        ],
        [
            KeyboardButton("Hikoyalar"),
        ],
        [
            KeyboardButton("Go back"),
        ]
    ],
    resize_keyboard=True
)

school_books = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbekcha")
        ],
        [
            KeyboardButton("🇷🇺 Ruscha")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

uz_school_books = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔢 Sinflar bo'yicha")
        ],
        [
            KeyboardButton("📔 Fanlar bo'yicha")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

ru_school_books = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔢 Sinflar bo'yicha ru")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

islamic_books = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Tafsiri Hilol"),
            KeyboardButton("Jannat vafsi")
        ],
        [
            KeyboardButton("Keng rizq va baraka omillari")
        ],
        [
            KeyboardButton("Istig'forning 40 xosiyati | Salovotlar")
        ],
        [
            KeyboardButton("Qur'on - qalblar shifosi")
        ],
        [
            KeyboardButton("Baxtli hayot sari")
        ],
        [
            KeyboardButton("Payg'ambar uyida bir kun")
        ],
        [
            KeyboardButton("Shamoili Muhammadiy")
        ],
        [
            KeyboardButton("Abu Bakr Siddiq")
        ],
        [
            KeyboardButton("Sunani Termiziy")
        ],
        [
            KeyboardButton("Hazrati Umar ibn Xattob")
        ],
        [
            KeyboardButton("Musnad")
        ],
        [
            KeyboardButton("Mukoshafat-ul qulub")
        ],
        [
            KeyboardButton("Ramazon va taqvo")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

vocabulary = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🗂 Pdf lug'atlar"),
            KeyboardButton("📲 Apk lug'atlar")
        ],
        [
            KeyboardButton("🌐 Google tarjimon")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

poem = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Erkin Vohidov"),
            KeyboardButton("👤 Abdulla Oripov")
        ],
        [
            KeyboardButton("Rauf Parfi"),
            KeyboardButton("Shavkat Rahmon")
        ],
        [
            KeyboardButton("Muhammad Yusuf")
        ],
        [
            KeyboardButton("Go back")
        ]
    ],
    resize_keyboard=True
)

offers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Done")
        ],
        [
            KeyboardButton("Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

assess_bot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⭐️⭐️⭐️⭐️⭐️ | A'lo")
        ],
        [
            KeyboardButton("⭐️⭐️⭐️⭐️ | Yaxshi")
        ],
        [
            KeyboardButton("⭐️⭐️⭐️ | O'rtacha")
        ],
        [
            KeyboardButton("⭐️⭐️ | Qoniqarli")
        ],
        [
            KeyboardButton("⭐️ | Qoniqarsiz")
        ],
        [
            KeyboardButton("Bekor qilish")
        ],
    ],
    resize_keyboard=True
)

from aiogram import types, Dispatcher, Bot, executor
from buttons import (start_button, english_buttons, uzbek_lit, world_lit,
                     child_lit, classic_lit, audio_books, school_books,
                     uz_school_books, ru_school_books, islamic_books, vocabulary,
                     poem, uzbek_literature, world_literature, offers, assess_bot)



BOT_TOKEN = "8085275156:AAGdOn3A2MEVsHPMh-t_9liKRMEJTulLSxU"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        """@English_books_new kanaliga tegishli botga xush kelibsiz!\n
Obunani to'xtatish uchun /off buyrug'idan foydalaning.\n
Bot yaratishni istaysizmi?
Marhamat, @Manybot saytimizga kiring.""",
        reply_markup=start_button
    )


@dp.message_handler(text='📞 Aloqa')
async def text(message: types.Message):
    await message.answer(
        "Savol va takliflaringiz bo'lsa, ushbu @Bizga_murojaatbot ga yozib qoldirishingiz mumkin "
        "(Biz uni albatta ko'rib chiqamiz)"
    )


@dp.message_handler(text='✅ FOYDALI KANALLAR VA ULARDA REKLAMA')
async def advert(message: types.Message):
    await message.answer(""" @English_books_new - Ingliz tilidan barcha turdagi (Grammatika, IELTS, 
    vocabulary, test va badiiy) kitoblarini topishingiz mumkin!

@Tarix - Ushbu kanal orqali tarixni oson o'rganing!


Yuqoridagi kanallarga reklama berish shartlari bilan batafsi bu yerda tanishing 👇

https://t.me/joinchat/RoDr_1utiTbt9T7C

@Elektron_kutubxona_kitoblarbot botidan kelganingizni aytsangiz 10% chegirma bor """)


@dp.message_handler(text='🇬🇧 English')
async def english(message: types.Message):
    await message.answer("Sizga ingliz tilidan grammatik kitoblar "
                         "kerakmi yoki IELTS kitoblarimi? Tanlang! 👇", reply_markup=english_buttons)


@dp.message_handler(text="🇬🇧 Ingliz tilidan foydali kanallar")
async def channels(messsage: types.Message):
    await messsage.answer("""@English_books_new - Ushbu kanaldan ko'proq ingliz tili kitoblarini yuklab olishingiz mumkin. ✅

@shaxzodtorayev - IELTS 7.0, Reading 8.5 sohibining blogi! 🔥""")


@dp.message_handler(text="📚 O'zbek adabiyoti")
async def uzbek(message: types.Message):
    await message.answer("Sizga qaysi yozuvchining asarlari kerak? Tanlang! 👇",
                         reply_markup=uzbek_lit)


@dp.message_handler(text="👤 Abdulla Qodiriy")
async def qodiriy(message: types.Message):
    qodiriy_story = open("static/documents/Abdulla Qodiriy. Jinlar bazmi (hikoyalar).pdf", 'rb')
    await message.answer_document(qodiriy_story)


@dp.message_handler(text="👤 Cho'lpon")
async def cholpon(messsge: types.Message):
    cholpon_story = open("static/documents/Abdulhamid Cho'lpon. Buloqlar quchog'ida.pdf", 'rb')
    await messsge.answer_document(cholpon_story)


@dp.message_handler(text="📚 Jahon adabiyoti")
async def world(message: types.Message):
    await message.answer("Yozuvchini tanlang", reply_markup=world_lit)


@dp.message_handler(text="👤 Lev Tolstoy")
async def tolstoy(message: types.Message):
    tolstoy_story = open("static/documents/Lev_Tolstoy_Tanlangan_asarlar_4.pdf", 'rb')
    await message.answer_document(tolstoy_story)


@dp.message_handler(text="👤 Aleksandr Pushkin")
async def pushkin(message: types.Message):
    pushkin_story = open("static/documents/Aleksandr Pushkin. Poema va ertaklar.pdf", 'rb')
    await message.answer_document(pushkin_story)


@dp.message_handler(text="📚 Bolalar adabiyoti")
async def child(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=child_lit)


@dp.message_handler(text="📚 Ertaklar")
async def stories(message: types.Message):
    children_stories = open("static/documents/[@Elektron_kutubxona_kitoblarbot] Oltin beshik.pdf", 'rb')
    await message.answer_document(children_stories)


@dp.message_handler(text="🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi")
async def interesting(message: types.Message):
    inter_books = open("static/documents/[@Elektron_kutubxona_kitoblarbot] Aviatsiya", 'rb')
    await message.answer_document(inter_books)


@dp.message_handler(text="📚 Mumtoz adabiyot")
async def mumtoz(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=classic_lit)


@dp.message_handler(text="📓 Boburnoma")
async def boburnama(message: types.Message):
    boburname = open("static/documents/Boburnoma.pdf")


@dp.message_handler(text="📓 Shohnoma")
async def shohnoma(message: types.Message):
    noma = open("static/documents/Abulqosim Firdavsiy. Shohnoma.pdf", 'rb')
    await message.answer_document(noma)


@dp.message_handler(text="🎧 Audio kitoblar")
async def audio(message: types.Message):
    await message.answer("Sizga o'zbek adabiyotidan audio kitoblar"
                         " kerakmi yoki jahon adabiyotidanmi? Tanlang! 👇", reply_markup=audio_books)


@dp.message_handler(text="🇺🇿 O'zbek adabiyoti")
async def uzbek(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇",
                         reply_markup=uzbek_literature)


@dp.message_handler(text="🌐 Jahon adabiyoti")
async def worlrd(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇",
                         reply_markup=world_literature)


@dp.message_handler(text="💯 Top 100 kitoblar")
async def top(message: types.Message):
    top_book = open("static/documents/100 kitob.txt", 'rb')
    await message.answer_document(top_book)


@dp.message_handler(text="📚 Maktab darsliklari")
async def school(message: types.Message):
    await message.answer("Sizga o'zbekcha darsliklar kerakmi"
                         " yoki ruscha darsliklarmi? Tanlang! 👇", reply_markup=school_books)


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def uz_school(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=uz_school_books)


@dp.message_handler(text="🇷🇺 Ruscha")
async def ru_school(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=ru_school_books)


@dp.message_handler(text="📚 Islomiy kitoblar")
async def islam(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=islamic_books)


@dp.message_handler(text="🔍 Lug'atlar")
async def vocab(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=vocabulary)


@dp.message_handler(text="🗂 Pdf lug'atlar")
async def pdf_vocab(message: types.Message):
    pdf_vocabulary = open("static/documents/Fransuzcha-ozbekcha.txt", "rb")
    await message.answer_document(pdf_vocabulary)


@dp.message_handler(text="📲 Apk lug'atlar")
async def apk_vocab(message: types.Message):
    apk_vocabulary = open("static/documents/Inglizcha-o_zbekcha.apk", 'rb')
    await message.answer_document(apk_vocabulary)


@dp.message_handler(text="🌐 Google tarjimon")
async def google(message: types.Message):
    google_translate = open("static/documents/Google Translator.apk", "rb")
    await message.answer_document(google_translate)


@dp.message_handler(text="📝 She'riyat")
async def poetry(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=poem)


@dp.message_handler(text="👤 Erkin Vohidov")
async def vohidov(message: types.Message):
    vohidov_poetry = open("static/documents/Erkin Vohidov. Saylanma. 1-jild. Ishq savdosi.pdf", 'rb')
    await message.answer_document(vohidov_poetry)


@dp.message_handler(text="👤 Abdulla Oripov")
async def oripov(message: types.Message):
    oripov_poetry = open("static/documents/Abdulla Oripov-She'rlar.pdf", 'rb')
    await message.answer_document(oripov_poetry)


@dp.message_handler(text="📜 Alisher Navoiy asarlari")
async def novoiy(message: types.Message):
    navoiy_story = open("static/documents/Alisher Navoiy. Qaro ko'zum (g'azallar).pdf", "rb")
    await message.answer_document(navoiy_story)


@dp.message_handler(text="📜O'zbekiston Milliy Ensiklopediyasi")
async def nation(message: types.Message):
    national = open("static/documents/O'zbekiston Milliy Ensiklopediyasi - A harfi.pdf", 'rb')
    await message.answer_document(national)


@dp.message_handler(text="📋 O'zbek tilining izohli lug'atlari")
async def language_uz(message: types.Message):
    uz_language = open("static/documents/O'zbek tilining izohli lug'ati - A.pdf", 'rb')
    await message.answer_document(uz_language)


@dp.message_handler(text="🔍 O'zbek tilining imlo lug'ati")
async def imlo(message: types.Message):
    imlo_vocab = open("static/documents/Imlo qoidalari.pdf", 'rb')
    await message.answer_document(imlo_vocab)


@dp.message_handler(text="Islom Karimov asarlari")
async def karimov(message: types.Message):
    karimov_stories = open("static/documents/Islom_Karimov_Asarlar_1_jild_O'zbekiston.pdf", 'rb')
    await message.answer_document(karimov_stories)


@dp.message_handler(text="Shavkat Mirziyoyev asarlari")
async def mirziyo(message: types.Message):
    mirziyoyev = open("static/documents/Biografiya (Shavkat Mirziyoyev).txt", 'rb')
    await message.answer_document(mirziyoyev)


@dp.message_handler(text="🤖 Botni guruhga qo'shish")
async def bot_share(message: types.Message):
    await message.answer("""Botni guruhga qo'shish:

Botni guruhga qo'shish uchun quyidagi link ustiga bosing va botni qo'shmoqchi bo'lgan guruhingizni tanlang. Guruhga qo'shganingizdan so'ng bot ishlashi uchun admin qiling.

LINK: http://t.me/Elektron_kutubxona_kitoblarbot?startgroup=ru""")


@dp.message_handler(text="↗️ Botni do'stlarga ulashish")
async def share_friends(message: types.Message):
    await message.answer("""Botni do'stlarga ulashish:

Botni ulashish uchun quyidagi link ustiga bosing va ulashmoqchi bo'lgan odamingizni tanlang:
 
LINK: http://telegram.me/share/url?url=https://telegram.me/Elektron_kutubxona_kitoblarbot""")


@dp.message_handler(text="♻️ Takliflar")
async def offer(message: types.Message):
    await message.answer("""Botni rivojlantirish uchun qanday takliflaringiz bor? Yozib qoldiring, takliflaringiz albatta ko'rib chiqiladi!

P/s: Taklifingizni yozib "Done" tugmasini bosishni unutmang aks holda taklifingiz bizga kelib tushmaydi""", reply_markup=offers)

@dp.message_handler(text="Done")
async def done(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan")

@dp.message_handler(text="Bekor qilish")
async def cancel(message: types.Message):
    await message.answer("Bekor qilindi.", reply_markup=start_button)

@dp.message_handler(text="⭐️ Botni baholash")
async def assess(message: types.Message):
    await message.answer("Bot faoliyatiga baho bering! 👇", reply_markup=assess_bot)

@dp.message_handler(text="⭐️⭐️⭐️⭐️⭐️ | A'lo")
async def great(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan", reply_markup=start_button)


@dp.message_handler(text="⭐️⭐️⭐️⭐️️ | Yaxshi")
async def not_great(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan", reply_markup=start_button)

@dp.message_handler(text="⭐️⭐️⭐️ | O'rtacha")
async def medium(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan", reply_markup=start_button)

@dp.message_handler(text="⭐️⭐️️️ | Qoniqarli")
async def not_bad(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan", reply_markup=start_button)

@dp.message_handler(text="⭐️️️ | Qoniqarsiz")
async def bad(message: types.Message):
    await message.answer("Tayyor!")
    await message.answer("@Manybot yordamida yaratilgan", reply_markup=start_button)

@dp.message_handler(text="Bekor qilish")
async def cancel(message: types.Message):
    await message.answer("Bekor qilindi.", reply_markup=start_button)

@dp.message_handler(text='Go back')
async def back(message: types.Message):
    await message.answer("Asosiy menyu", reply_markup=start_button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

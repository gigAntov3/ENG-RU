from telebot import types

TransList = []

def HomeKeyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    itembtn1 = types.KeyboardButton('О боте🤖')
    itembtn2 = types.KeyboardButton('Учить слова🖊')
    itembtn3 = types.KeyboardButton('Прогресс📈')
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup

def WordKeyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    itembtn4 = types.KeyboardButton('Вернуться🔙')
    itembtn5 = types.KeyboardButton('Проверить свои знания📝')
    markup.add(itembtn5, itembtn4)
    return markup

def NextKeyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Следущее слово🔜')
    itembtn3 = types.KeyboardButton('Вернуться🔙')
    markup.add(itembtn1, itembtn3)
    return markup

def NextKeyboard2():
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Идем дальше🔜')
    itembtn3 = types.KeyboardButton('Вернуться🔙')
    markup.add(itembtn1, itembtn3)
    return markup

def LearnKeyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    itembtn4 = types.KeyboardButton('Продолжить изучение📝')
    itembtn5 = types.KeyboardButton('Учить новые слова')
    markup.add(itembtn5, itembtn4)
    return markup

def IntKeyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    itembtn6 = types.KeyboardButton('5 слов')
    itembtn7 = types.KeyboardButton('10 слов')
    itembtn8 = types.KeyboardButton('15 слов')
    itembtn9 = types.KeyboardButton('20 слов')
    markup.add(itembtn6, itembtn7, itembtn8, itembtn9)
    return markup

def CreateAnswerKeyboard (quantity,FetchList, TransList, Mode) :
    markup = types.InlineKeyboardMarkup()
    Butt = []
    for i in range(quantity):
            Butt.append(types.InlineKeyboardButton(str(TransList[i]), callback_data= FetchList[:4]  + ' '  + TransList[i] + ' ' + str(Mode)))
    markup.add(*Butt)

    return markup
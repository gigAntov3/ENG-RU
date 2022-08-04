import telebot as tel
import BotMessages
import KeyboardBot
import sqlite3
from random import randint
from googletrans import Translator

connect = sqlite3.connect('School_Base.db', check_same_thread=False)
cursor = connect.cursor()
rand_list = []
fetch_list = []
transfetch_list = []
old_word_select = []
old_words_select = []
new_word_select = []
new_words_select = []
translator = Translator()
HomeKeyboard = KeyboardBot.HomeKeyboard()
IntKeyboard = KeyboardBot.IntKeyboard()
WordKeyboard = KeyboardBot.WordKeyboard()
LearnKeyboard = KeyboardBot.LearnKeyboard()
NextKeyboard = KeyboardBot.NextKeyboard()
NextKeyboard2 = KeyboardBot.NextKeyboard2()

TOKEN = '5378085749:AAHJTsogrUyNQJrIBBliQkICdr6qMiFrFT0'
bot = tel.TeleBot(TOKEN)

def db_table_val(user_id: int, user_name: str, user_surname: str):
	cursor.execute('INSERT INTO Users (user_id, user_name, user_surname,learned_words, answer_correct, wrong_answer) VALUES (?, ?, ?, ?, ?, ?)', (user_id, user_name, user_surname, 0, 0, 0))
	connect.commit()

@bot.message_handler(commands=['start'])
def start_command(message):
     
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name

    cursor.execute("SELECT user_id FROM Users WHERE user_id ='{}'".format(us_id))
    cursor_fetch = cursor.fetchone()
    try:
        if us_id == cursor_fetch[0]:
            bot.send_message(message.chat.id, 'Добро пожаловать. Рады снова видеть вас!')
            bot.send_message(message.chat.id, BotMessages.AboutBot, reply_markup = HomeKeyboard)
        elif not TypeError:
            db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname)
            bot.send_message(message.chat.id, 'Добро пожаловать. Рады, что вы решили к нам зайти!')
            bot.send_message(message.chat.id, BotMessages.AboutBot, reply_markup = HomeKeyboard)
    except TypeError:
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname)
        bot.send_message(message.chat.id, 'Добро пожаловать. Рады, что вы решили к нам зайти!')
        bot.send_message(message.chat.id, BotMessages.AboutBot, reply_markup = HomeKeyboard)

@bot.message_handler(func=lambda message: message.text == 'О боте🤖')
def function_name(message):
	bot.send_message(message.chat.id, BotMessages.AboutBot ,reply_markup = HomeKeyboard)

@bot.message_handler(func=lambda message: message.text == 'Учить слова🖊')
def function_name(message):
	bot.send_message(message.chat.id, 'Выберете что вы хотите делать' ,reply_markup = LearnKeyboard)

@bot.message_handler(func=lambda message: message.text == 'Учить новые слова')
def function_name(message):
	bot.send_message(message.chat.id, 'Выберете что вы хотите делать' ,reply_markup = IntKeyboard)

@bot.message_handler(func=lambda message: message.text == 'Продолжить изучение📝')
def function_name(message):
    try:
        cursor.execute("SELECT word FROM Learning_Words WHERE ID = {} AND status = 'learning' AND count_answer = (SELECT MIN(count_answer) FROM Learning_Words WHERE ID = {} AND status = 'learning')".format(message.chat.id, message.chat.id))
        select_fetch = cursor.fetchone()
        old_words_select.append(select_fetch[0])
        for i in range(3):
            cursor.execute("SELECT translation FROM Words WHERE number = {}".format(randint(0, 5100)))
            old_word_select = cursor.fetchone()
            old_words_select.append(old_word_select[0])
        old_words_select.sort()
        CreateAnswerKeyboard = KeyboardBot.CreateAnswerKeyboard(4, select_fetch[0],  old_words_select, 1)
        bot.send_message(message.chat.id, translator.translate(select_fetch[0], src='ru', dest='en').text + ' - ',reply_markup = CreateAnswerKeyboard)
        old_words_select.clear()
    except TypeError:
        bot.send_message(message.chat.id, 'Сначала выучите новые слова.',reply_markup = LearnKeyboard)


@bot.message_handler(func=lambda message: message.text == 'Следущее слово🔜')
def function_name(message):
    try:
        cursor.execute("SELECT word FROM Learning_Words WHERE ID = {} AND status = 'learning' AND count_answer = (SELECT MIN(count_answer) FROM Learning_Words WHERE ID = {} AND status = 'learning')".format(message.chat.id, message.chat.id))
        select_fetch = cursor.fetchone()
        old_words_select.append(select_fetch[0])
        for i in range(3):
            cursor.execute("SELECT translation FROM Words WHERE number = {}".format(randint(0, 5100)))
            old_word_select = cursor.fetchone()
            old_words_select.append(old_word_select[0])
        old_words_select.sort()
        CreateAnswerKeyboard = KeyboardBot.CreateAnswerKeyboard(4, select_fetch[0],  old_words_select, 1)
        bot.send_message(message.chat.id, translator.translate(select_fetch[0], src='ru', dest='en').text + ' - ',reply_markup = CreateAnswerKeyboard)
        old_words_select.clear()
    except TypeError:
        bot.send_message(message.chat.id, 'Сначала выучите новые слова.',reply_markup = LearnKeyboard)



@bot.message_handler(func=lambda message: message.text == '5 слов' or message.text == '10 слов' or message.text == '15 слов' or message.text == '20 слов')
def function_name(message):
    count_words = message.text.split()
    try:
        global CountWords
        CountWords = int(count_words[0])
    except:
        bot.send_message(message.chat.id, BotMessages.Error_Word ,reply_markup = IntKeyboard)
    for i in range(CountWords):
        Rand = randint(1,5114)
        rand_list.append(Rand)
        cursor.execute("SELECT word, translation FROM Words WHERE number = {}".format(Rand))
        select_fetch = cursor.fetchone()
        cursor.execute("SELECT MAX(ID_word) FROM Learning_Words")
        select_fetch2 = cursor.fetchone()
        cursor.execute('INSERT INTO Learning_Words (ID, ID_word, word,count_answer,status) VALUES (?, ?, ?, ?, ?)', (message.chat.id, select_fetch2[0] + 1, select_fetch[1],0,'learning'))
    connect.commit()
    cursor.execute("SELECT word FROM Learning_Words WHERE ID = {} AND count_answer = 0".format(message.chat.id))
    select_fetch = cursor.fetchall()
    bot.send_message(message.chat.id, BotMessages.WordGen(CountWords, select_fetch),reply_markup = WordKeyboard)



@bot.message_handler(func=lambda message: message.text == 'Проверить свои знания📝')
def function_name(message):
    try:
        bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        bot.send_message(message.chat.id, 'Попробуйте снова.',reply_markup = LearnKeyboard)
    try:
        cursor.execute("SELECT word FROM Learning_Words WHERE ID = {} AND count_answer = (SELECT MIN(count_answer) FROM Learning_Words WHERE ID = {} AND status = 'learning')".format(message.chat.id, message.chat.id))
        sselect_fetch = cursor.fetchone()
        for i in range(3):
            cursor.execute("SELECT translation FROM Words WHERE number = {}".format(randint(0, 5100)))
            new_word_select = cursor.fetchone()
            new_words_select.append(new_word_select[0])
        new_words_select.append(sselect_fetch[0])
        new_words_select.sort()
        bot.send_message(message.chat.id, 'Переведи это слово.',reply_markup = NextKeyboard)
        CreateAnswerKeyboard = KeyboardBot.CreateAnswerKeyboard(4, sselect_fetch[0],  new_words_select, 2)
        bot.send_message(message.chat.id, translator.translate(sselect_fetch[0], src='ru', dest='en').text + ' - ',reply_markup = CreateAnswerKeyboard)
        new_words_select.clear()
    except:
        bot.send_message(message.chat.id, 'Сначала выучите новые слова.',reply_markup = LearnKeyboard)
    

@bot.message_handler(func=lambda message: message.text == 'Идем дальше🔜')
def function_name(message):
    try:
        cursor.execute("SELECT word FROM Learning_Words WHERE ID = {} AND count_answer = (SELECT MIN(count_answer) FROM Learning_Words WHERE ID = {} AND status = 'learning')".format(message.chat.id, message.chat.id))
        sselect_fetch = cursor.fetchone()
        for i in range(3):
            cursor.execute("SELECT translation FROM Words WHERE number = {}".format(randint(0, 5100)))
            new_word_select = cursor.fetchone()
            new_words_select.append(new_word_select[0])
        new_words_select.append(sselect_fetch[0])
        new_words_select.sort()
        CreateAnswerKeyboard = KeyboardBot.CreateAnswerKeyboard(4, sselect_fetch[0],  new_words_select, 2)
        bot.send_message(message.chat.id, translator.translate(sselect_fetch[0], src='ru', dest='en').text + ' - ',reply_markup = CreateAnswerKeyboard)
        new_words_select.clear()
    except TypeError:
        bot.send_message(message.chat.id, 'Сначала выучите новые слова.',reply_markup = LearnKeyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_logic(call):
    call_spl = call.data.split(' ')
    len_call_spl = len(call_spl)
    if len_call_spl == 3:
        if call_spl[0] in call_spl[1]:
            if call_spl[2] == '1':
                bot.send_message(call.message.chat.id,'✅ Ваш ответ верный.', reply_markup = NextKeyboard)
            else:
                bot.send_message(call.message.chat.id,'✅ Ваш ответ верный.', reply_markup = NextKeyboard2)
            cursor.execute("UPDATE Users SET answer_correct = answer_correct + 1 WHERE user_id = {}".format(call.message.chat.id))
            cursor.execute("UPDATE Learning_Words SET count_answer = count_answer + 1 WHERE ID = {} AND word = '{}'".format(call.message.chat.id, call_spl[1]))
        else:
            bot.send_message(call.message.chat.id,'❌ Попробуйте ещё раз.')
            cursor.execute("UPDATE Users SET wrong_answer = wrong_answer + 1 WHERE user_id = {}".format(call.message.chat.id))
    elif len_call_spl > 3:
        for i in range(2,len_call_spl - 1):
            call_spl[1] = call_spl[1] + ' ' + call_spl[i]
        if call_spl[0] in call_spl[1]:
            if call_spl[len_call_spl - 1] == '1':
                bot.send_message(call.message.chat.id,'✅ Ваш ответ верный.', reply_markup = NextKeyboard)
            else:
                bot.send_message(call.message.chat.id,'✅ Ваш ответ верный.', reply_markup = NextKeyboard2)
            cursor.execute("UPDATE Users SET answer_correct = answer_correct + 1 WHERE user_id = {}".format(call.message.chat.id))
            cursor.execute("UPDATE Learning_Words SET count_answer = count_answer + 1 WHERE ID = {} AND word = '{}'".format(call.message.chat.id, call_spl[1]))
        else:
            bot.send_message(call.message.chat.id,'❌ Попробуйте ещё раз.')
            cursor.execute("UPDATE Users SET wrong_answer = wrong_answer + 1 WHERE user_id = {}".format(call.message.chat.id))
    cursor.execute("SELECT word FROM Learning_Words WHERE count_answer >= 5 AND status = 'learning' AND ID = {}".format(call.message.chat.id))
    select_data = cursor.fetchall()
    for i in range(len(select_data)):
        cursor.execute("UPDATE Learning_Words SET status = 'learned' WHERE ID = {} AND word ='{}'".format(call.message.chat.id, select_data[i][0]))
        cursor.execute("UPDATE Users SET learned_words = learned_words + 1 WHERE user_id = {}".format(call.message.chat.id))
    connect.commit()

@bot.message_handler(func=lambda message: message.text == 'Прогресс📈')
def function_name(message):
    cursor.execute("SELECT learned_words, answer_correct, wrong_answer FROM Users WHERE user_id = {}".format(message.chat.id))
    select_data = cursor.fetchone()
    bot.send_message(message.chat.id, 'Вот ваша статистика:')
    bot.send_message(message.chat.id, BotMessages.Progresler(select_data[0]))
    bot.send_message(message.chat.id, BotMessages.Progreslercor(select_data[1]))
    bot.send_message(message.chat.id, BotMessages.Progreslerwor(select_data[2]) ,reply_markup = HomeKeyboard)

@bot.message_handler(func=lambda message: message.text == 'Вернуться🔙')
def function_name(message):
	bot.send_message(message.chat.id, 'Вы вернулись к главному меню.' ,reply_markup = HomeKeyboard)

bot.infinity_polling(none_stop=True)














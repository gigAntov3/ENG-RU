from googletrans import Translator

translator = Translator()

AboutBot = "Этот бот предназначен для изучения слов на английском языке. \nКаждый день вы будете учить такое количество слов, какое захотите.\nВам будут приходить уведомления для того, чтобы вы не забывали,что пора учить новые слова.\nТакже мы будем проверять ваши знания небольшими тестами.\nУчите английский язык в удовольствие,вместе с нашим ботом. Удачи.\nP.S. При обнаружении сбоя в программе сообщитена этот электронный адрес: vladss17114@mail.ru "

Error_Word = " Пожалуйста, попробуйте еще раз."

def Progresler(ler):
    if ler >= 5:
        text = "🗓 Вы выучили {} слов".format(ler)
    if ler == 2 or ler == 3:
        text = "🗓 Вы выучили {} слова".format(ler)
    if ler == 1:
        text = "🗓 Вы выучили {} слово".format(ler)
    return text

def Progreslercor(cor):
    if cor >= 5:
        text = "✅ Вы перевели правильно {} слов".format(cor)
    if cor == 2 or cor == 3:
        text = "✅ Вы перевели правильно {} слова".format(cor)
    if cor == 1:
        text = "✅ Вы перевели правильно {} слово".format(cor)
    return text

def Progreslerwor(wor):
    if wor >= 5:
        text = "❌ Вы перевели неправильно {} слов".format(wor)
    if wor == 2 or wor == 3:
        text = "❌ Вы перевели неправильно {} слова".format(wor)
    if wor == 1:
        text = "❌ Вы перевели неправильно {} слово".format(wor)
    return text

def WordGen(count, Word):
    text = 'Вот ваши слова:\n\n'
    for i in range(count):
        text = text + str(i+1) + ':  ' + Word[i][0] + ' - ' + translator.translate(Word[i][0], src='ru', dest='en').text + '\n\n'
    return text
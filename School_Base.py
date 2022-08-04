import sqlite3 as sql
from random import randint

connect = sql.connect(database = 'School_Base.db')
cursor = connect.cursor()

RandList = []

count_words = int(input())
for i in range(count_words):
    Rand = randint(1,5114)
    RandList.append(Rand)
    cursor.execute("SELECT word, translation FROM Words WHERE number = {}".format(Rand))
    tuple_word = cursor.fetchone()
    print(str(i+1)+': '+ tuple_word[0]+ ' - ' + tuple_word[1])

def Examination(rand_list):
    for i in rand_list:
        cursor.execute("SELECT word, translation FROM Words WHERE number = {}".format(i))
        tuple_word = cursor.fetchone()
        answer = str(input(tuple_word[0] + ' - '))
        if tuple_word[1] == answer:
            print('Молодец')
        else:
            print('Повезет в следующий раз')

Examination(RandList)


















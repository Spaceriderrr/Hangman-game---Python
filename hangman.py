from random import *


def check_letter(letter):
    if len(letter) != 1:
        return False
    else:
        if not letter.isalpha():
            return False
        else:
            return True


def change_letter(letter, word, guess):
    for i in word:
        if i == letter:
            guess[word.index(i)] = letter
            word[word.index(i)] = '_'
            continue
        else:
            continue
    return guess


wds = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'вопрос', 'лицо', 'глаз',
       'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова', 'система', 'вид', 'конец', 'отношение',
       'город',
       'часть', 'женщина', 'проблема', 'земля', 'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец',
       'история',
       'нога', 'вода', 'война', 'возможность', 'компания', 'результат', 'дверь', 'бог', 'народ', 'область', 'число',
       'голос',
       'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд', 'деньга', 'уровень', 'начало',
       'государство',
       'стол', 'средство', 'связь', 'имя', 'президент', 'форма', 'путь', 'организация', 'качество', 'действие',
       'статья',
       'общество', 'ситуация', 'деятельность', 'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц',
       'порядок', 'цель', 'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок',
       'предприятие',
       'партия', 'роль', 'смысл', 'мама', 'мера', 'улица']



main_flag = True

while main_flag:
    wd = choice(wds)
    word = [i for i in wd]
    lifecount = ['\U0001F5A4' for _ in range(7)]
    guess = ['_' for _ in range(len(word))]

    print("so, let's play")

    while len(lifecount) != 0:
        print('attempts:', *lifecount)
        temp = input('enter the letter:\n')
        if not check_letter(temp):
            print('wrong input, enter one letter')
            continue
        elif temp not in word:
            del lifecount[-1]
            print('nope')
        elif temp in word:
            change_letter(temp, word, guess)
            print('good')
        print('word:', guess, '\n')

        if '_' not in guess and len(lifecount) > 0:
            print('YOU WIN!!!')
            break
    if len(lifecount) == 0:
        print('You failed')
        print(f'Слово: {wd}')

    while True:
        print('Wanna play again? y/n')
        temp = input()
        if not check_letter(temp):
            print('enter only y or n')
            continue
        else:
            if temp == 'y':
                break
            if temp == 'n':
                main_flag = False
                break
            else:
                print('enter only y or n')
                continue


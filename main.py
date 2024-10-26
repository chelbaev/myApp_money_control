import pandas as pd
import numpy as np
import datetime

def add():
    df = pd.read_csv("money.csv", index_col='индекс')
    print()
    while True:
        name = input("продукт: ")
        if name == "return":
            return 0
        if name == "0":
            break
        cost = input("цена: ")
        category = input("категория: ")
        current_date = datetime.date.today().isoformat()
        myList = [current_date, name, cost, category]
        df.loc[len(df)] = myList
    df.to_csv('money.csv')
    return 1
def analis():
    df = pd.read_csv("money.csv")
    today = datetime.date.today()
    Delta = int(input('\nЗа какой период вас интересуют ваши траты? '))
    current = today - datetime.timedelta(days=Delta - 1)
    dictionary = {}
    average = 0
    while (current <= today):
        current_df = df[df['дата'] == current.isoformat()]
        daily_expenses = 0
        for i in current_df.index:
            sr = current_df.loc[i]
            cost = float(sr['цена'])
            daily_expenses += cost
            category = sr['категория']
            if category in dictionary:
                dictionary[category] += cost
            else:
                dictionary[category] = cost
        print('траты за ' + current.isoformat() + ' = ' + str(daily_expenses))
        average += daily_expenses * (1/Delta)
        current = current + datetime.timedelta(days=1)
    print('траты по категориям:')
    for key in dictionary.keys():
        print(key + " = " + str(dictionary[key]))
    print('трат в среднем за день = ' + str(average))
    file = open('water.txt', 'r')
    count = float(file.read())
    print('Воды осталось: {} литров'.format(count))
def count_water():
    file = open('water.txt', 'r')
    count = float(file.read())
    file.close()
    print("\n0) Выйти\n1) Оставшаяся вода\n2) Вычесть воду\n3)установить новый")
    while(True):
        operation = input()
        if(operation == '0'):
            break
        elif(operation == '1'):
            print(count)
        elif(operation == '2'):
            litters = float(input('Сколько было потрачено воды? '))
            count -= litters
            print('Осталось {}'.format(count))
        elif(operation == '3'):
            count = 350        
        else:
            print('Я не знаю такую опарацию')
    file = open('water.txt', 'w')
    file.write(str(count))
    return 1

def main():
    while(True):
        print('0)выход\n1) Анализ статистики\n2) Добавить продукт\n3) Взаимодействие с фильтром')
        print('Что будет делать?')
        operation = input()
        if (operation == 'выход' or operation == '0'):
            print('Завершение работы!')
            break
        elif (operation == 'анализ' or operation == '1'):
            analis()
        elif (operation == 'добавить' or operation == '2'):
            if add():
                print('Добавлены траты!')
            else:
                print('Траты не добавлены')
        elif (operation == 'взаимодействие' or operation == '3'):
            if count_water():
                print('Данные по воде успешно обновлены!')
        else:
            print('Я не знаю такую команду!')
    return 0
main()

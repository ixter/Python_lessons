import menu  # менюшка
import pandas as pd
import random

def task_1():
    print("""Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?"""
          )

    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    data['robot'] = data
    data = data.rename({"whoAmI": "human"}, axis='columns')
    data['human'] = data['human'].replace('robot', '0')
    data['human'] = data['human'].replace('human', '1')
    data['robot'] = data['robot'].replace('robot', '1')
    data['robot'] = data['robot'].replace('human', '0')
    data.head()
    data.to_csv('saved_task.csv', index=False)

if __name__ == "__main__":
    menu.start_menu()

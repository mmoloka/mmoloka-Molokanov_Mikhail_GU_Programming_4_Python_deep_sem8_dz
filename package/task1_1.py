import json
import pickle
import os

# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

def json_to_pickle():
    for obj in os.listdir():
        if os.path.isfile(obj) and obj.split('.')[1] == 'json':
            pickle_file = obj.split('.')[0] + '.pickle'
            with(
                open(obj, 'r', encoding='utf-8') as j,
                open(pickle_file, 'wb') as p
            ):
                data_dict = json.load(j)
                pickle.dump(data_dict, p)

if __name__ == '__main__':
    json_to_pickle()                
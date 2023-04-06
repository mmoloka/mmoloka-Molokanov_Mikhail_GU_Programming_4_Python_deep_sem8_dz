import csv
import json
import os
import pickle

# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните вфайлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.

def get_dir_size(path: str) -> int:
    total_size = 0
    for dir_path, _, file_name in os.walk(path):
        for f in file_name:
            fp = os.path.join(dir_path, f)
            total_size += os.path.getsize(fp)
    return total_size

def go_round_directory(path: str) -> None:
    result_json = []
    result_csv = []
    
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        file_dict = {i: os.path.getsize(f'{dir_path}\\{i}') for i in file_name}
        dir_dict = {j: get_dir_size(f'{dir_path}\\{j}') for j in dir_name}

        path_dict = {'dir_path': dir_path, 'dir_dict': dir_dict, 'file_dict': file_dict}
        result_json.append(path_dict)

        for dir, dir_size in dir_dict.items():
            result_csv.append([dir_path, dir, dir_size])
        for file, file_size in file_dict.items():
            result_csv.append([dir_path, file, file_size])    

    with(
         open('result.json', 'w', encoding='utf-8') as j,
         open('result.csv', 'w', newline='', encoding='utf-8') as c,
         open('result.pickle', 'wb') as p
    ): 
        json.dump(result_json, j, indent=2, ensure_ascii=False)

        csv_writer = csv.writer(c, dialect='excel-tab')
        csv_writer.writerow(['path', 'name', 'size'])
        csv_writer.writerows(result_csv)

        pickle.dump(result_json, p)

if __name__ == '__main__':
    go_round_directory(os.getcwd())        
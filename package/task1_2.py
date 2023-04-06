import pickle
import csv

# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

def pickle_to_csv(pickle_file: str, csv_file: str) -> None:
    with(
        open(pickle_file, 'rb') as p,
        open(csv_file, 'w', newline='', encoding='utf-8') as c
    ):
        data = pickle.load(p)
        headline = [i for i in data[0].keys()]
        line = []
        data_matrix = []
        for dict in data:
            for value in dict.values():
                line.append(value)
            data_matrix.append(line)
            line = []     
        csv_writer = csv.writer(c, dialect='excel-tab')
        csv_writer.writerow(headline)
        csv_writer.writerows(data_matrix)

if __name__ == '__main__':
    pickle_to_csv('log2_access.pickle', 'log2_access.csv')        
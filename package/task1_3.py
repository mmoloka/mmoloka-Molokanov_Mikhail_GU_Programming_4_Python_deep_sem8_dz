import pickle
import csv

# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

def print_pickle_str(csv_file: str) -> None:
    with open(csv_file, 'r', newline='', encoding='utf-8') as c:
        data = []
        csv_reader = csv.reader(c, dialect='excel-tab')
        for line in csv_reader:
            data.append(line)
        result = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(result)    

if __name__ == '__main__':
    print_pickle_str('log2_access.csv')
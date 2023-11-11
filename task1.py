# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом
# в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,расширение, если это файл,флаг каталога,название родительского каталога.

# ДЗ 15: Добавьте к ним логирование ошибок и полезной информации.


import pathlib
import logging
from collections import namedtuple


logging.basicConfig(filename='dir_info.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

DIRSUBJECT = namedtuple('DIRSUBJECT', ['file_name', 'ext', 'flag', 'name_dir'])

def dir_info(path):
    try:
        path = pathlib.Path(path)
        new_list = []
        for file in path.iterdir():
            new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
        return new_list
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    try:
        print(dir_info('C:/Users/iriba/Desktop/Home_works_python'))
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}", exc_info=True)

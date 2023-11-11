# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. Функция 
# выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# ДЗ 15: реализуйте возможность запуска из командной строки с передачей параметров
import argparse
from random import randint

def random_number(start_num: int, stop_num: int, qty: int) -> bool:
    random_num = randint(start_num, stop_num)
    for _ in range(qty):
        input_num = int(input("Введите число: "))
        if random_num == input_num:
            return True
        elif random_num > input_num:
            print("Больше")
        else:
            print("Меньше")
    return False

def parse_arguments():
    parser = argparse.ArgumentParser(description='Guess the random number game.')
    parser.add_argument('-s', '--start', type=int, default=1, help='Start of the number range')
    parser.add_argument('-e', '--end', type=int, default=10, help='End of the number range')
    parser.add_argument('-q', '--quantity', type=int, default=3, help='Number of attempts')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(random_number(args.start, args.end, args.quantity))

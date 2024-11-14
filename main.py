# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
#
def is_prime(func):

    def wrapper(*args, **kwargs):

        number = func(*args, **kwargs)
        print(number)
        
        if number < 2:
            return 'Составное'  # Числа меньше 2 не являются простыми
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return 'Составное'  # Найден делитель, число составное
        return 'Простое'  # Если делителей нет, число простое

    return wrapper


@is_prime
def sum_three(*args):

    return sum(args)


print(sum_three(2, 3, 6))
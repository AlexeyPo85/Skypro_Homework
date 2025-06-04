from functools import wraps


def log(filename=''):
    ''' Декоратор считывает входные данные с декорируемой функции, а так же результат её работы.
    Если не указан необязательный аргумент, результат выводится в консоль.
    Если указан необязательный аргумент, результат записывается в файл, который указан в аргументе.'''
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'Функция {func.__name__}, вызвана с аргументами {args}, {kwargs} '
                                   f'выполнена успешно. Результат: {result}')
                else:
                    print(f'Функция {func.__name__}, вызвана с аргументами {args}, {kwargs} выполнена успешно. '
                          f'Результат: {result}')
            except Exception as e:
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'Функция {func.__name__} вывела ошибку:{e}. Входные данные:{args}, {kwargs}')
                else:
                    print(f'Функция {func.__name__} вывела ошибку:{e}. Входные данные:{args}, {kwargs}')
        return inner
    return wrapper

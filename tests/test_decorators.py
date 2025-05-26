from src.decorators import log


def test_log(capsys):
    @log('')
    def add_numbers(a, b):
        return a + b
    result = add_numbers(3, 5)
    captured = capsys.readouterr()

    assert captured.out == (f'Функция {add_numbers.__name__}, вызвана с аргументами (3, 5), {{}} выполнена успешно. '
                            f'Результат: 8\n')


def test_log_2(capsys):
    @log('')
    def division_numbers(a, b):
        return a / b
    result = division_numbers(5, 0)
    captured = capsys.readouterr()

    assert captured.out == (f'Функция {division_numbers.__name__} вывела ошибку:division by zero. '
                            f'Входные данные:(5, 0), {{}}\n')


def test_log_3():
    @log('result_text')
    def add_numbers(a, b):
        return a + b
    result = add_numbers(3, 5)
    with open('result_text', 'r', encoding='utf-8') as file:
        text_in_file = file.read()

        assert text_in_file == (f'Функция {add_numbers.__name__}, вызвана с аргументами (3, 5), {{}} выполнена успешно. '
                            f'Результат: 8')


def test_log_4():
    @log('result_text')
    def division_numbers(a, b):
        return a / b
    result = division_numbers(5, 0)
    with open('result_text', 'r', encoding='utf-8') as file:
        text_in_file = file.read()
        assert text_in_file == (f'Функция {division_numbers.__name__} вывела ошибку:division by zero. '
                            f'Входные данные:(5, 0), {{}}')

"""
В дополнение к этому заданию нужно скачать файл equations.txt
по адресу https://raw.githubusercontent.com/maxchv/LearnPython/master/week05/homeworks/equations.txt
"""

def fileCalculatorSum():
    """
    Задание 1
    ---------
    Вычислить выражения записанные в файле.

    Открыть файл equations.txt на чтение в текстовом режиме.
    Считать все строки, в которых встречается символ "+" (плюс)
    Разделить строку по пробелам на список строк.
    Преобразовать каждую строку в списке содержащую цифры (метод isdigit()) в целое число
    Получить сумму всех успешно преобразованных цифр для строки

    Функция должна возвращать кортеж из суммы чисел (для каждой строки)

    >>> fileCalculatorSum()
    (5, 14, 136)
    """
    path = r"E:\GitHub\LearnPython\week05\homeworks\equations.txt"

    pass



def fileSize():
    """
    Задание 2
    ---------
    Функция fileSize() должна вернуть размер файла equations.txt

    Открыть файл equations.txt на чтение в бинарном режиме.
    Перейти в конец файла (метод seek)
    Получить количество байт относительно начала файла (метод tell)
    Вернуть размер

    >>> fileSize()
    56
    """
    pass

def fileLineCount():
    """
    Задание 3
    ---------
    Функция возвращает количество строк в файле

    Открыть файл equations.txt на чтение в текстовом режиме
    Перебрать все строки (методом readline() или итерацией файлового объекта)
    Посчитать количество строк и вернуть результат

    >>> fileLineCount()
    6
    """
    pass

def fileCalculatorEquations():
    """
    Задание 4*
    ---------
    Выполнить вычисления выражений и записать в файл

    Открыть файл equations.txt на чтение в текстовом режиме

    Открыть файл results.txt на запись в текстовом режиме

    Считать строку из файла equations.txt и записать результат выражения
    представленного строкой в выходной файл result.txt

    Результаты вычислений должны размещаться по одному в строке

    Например, если считано выражение "2 + 2", то будет записано значение 4

    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""
Модуль с математическими операциями для демонстрации CI/CD
"""

def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

def is_even(number):
    """Проверка числа на четность."""
    return number % 2 == 0

def fibonacci(n):
    """Вычисление n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

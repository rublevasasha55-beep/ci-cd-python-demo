"""
Тесты для модуля math_operations.py
"""

import pytest
from math_operations import add, subtract, multiply, divide, is_even, fibonacci

def test_add():
    """Тест функции сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    """Тест функции вычитания."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Тест функции умножения."""
    assert multiply(4, 3) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 4) == 10.0

def test_divide():
    """Тест функции деления."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    
    # Тест на исключение при делении на ноль
    with pytest.raises(ValueError, match="Деление на ноль!"):
        divide(10, 0)

def test_is_even():
    """Тест проверки четности."""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-7) == False

def test_fibonacci():
    """Тест вычисления чисел Фибоначчи."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_broken():
    """Намеренно сломанный тест для демонстрации CI/CD."""
    assert 2 + 2 == 5  # Это неправильно! 2+2=4

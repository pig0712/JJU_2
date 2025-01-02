# mypackage/module2.py

def multiply(a, b):
    """
    두 숫자의 곱을 반환합니다.
    """
    return a * b

def divide(a, b):
    """
    첫 번째 숫자를 두 번째 숫자로 나눈 값을 반환합니다.
    두 번째 숫자가 0일 경우 예외를 발생시킵니다.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

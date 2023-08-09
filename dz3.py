# Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1  
    yield a 
    while True:
        yield b  
        a, b = b, a + b  

fib = fibonacci()
for i in range(10):
    print(next(fib))
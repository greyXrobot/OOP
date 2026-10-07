# Домашнее задание — Магические методы

## Задание 4. Работаем как список

class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        return self.rows[index]

    def __contains__(self, value):
        return any(value in row for row in self.rows)


if __name__ == "__main__":
    m = Matrix([[1, 2], [3, 4]])
    
    print(len(m))        # Вывод: 2
    print(m[0])          # Вывод: [1, 2]
    print(3 in m)        # Вывод: True
    print(9 in m)        # Вывод: False


## Задание 5. Свой итератор

class Fibonacci:
    def __init__(self, n):
        self.n = n          
        self.count = 0      
        self.a = 0         
        self.b = 1          

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        
        return current

for num in Fibonacci(7):
    print(num, end=" ")
# Вывод: 0 1 1 2 3 5 8 

print()

## Задание 6 (со звёздочкой). __call__ и контекстный менеджер

class Discount:
    def __init__(self, percent):
        self.percent = percent

    def __call__(self, price):
        return price * (1 - self.percent / 100)

    def __enter__(self):
        print("Скидка активирована")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Скидка закончилась")
        # Возвращаем False, чтобы не подавлять исключения, если они возникнут внутри with
        return False
    
with Discount(20) as d:
    print(d(1000))  # Вывод: 800.0
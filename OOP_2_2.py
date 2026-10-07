# Домашнее задание — Вариантность типов

## Задание 2. Ковариантный контейнер

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class ReadOnlyStack(Generic[T_co]):

    def __init__(self, value: T_co) -> None:
        self._value = value

    def peek(self) -> T_co:
        return self._value


class Animal: pass
class Dog(Animal): pass

dog_stack: ReadOnlyStack[Dog] = ReadOnlyStack(Dog())
animal_stack: ReadOnlyStack[Animal] = dog_stack

top_animal: Animal = animal_stack.peek()
print(f"Успешно получен объект: {type(top_animal).__name__}")
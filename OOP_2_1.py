# Домашнее задание — Вариантность типов

## Задание 1. Инвариантный контейнер

from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()


class Animal: pass
class Dog(Animal): pass

dog_stack: Stack[Dog] = Stack()
animal_stack: Stack[Animal] = dog_stack  
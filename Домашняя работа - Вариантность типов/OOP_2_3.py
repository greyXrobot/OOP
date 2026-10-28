# Домашнее задание — Вариантность типов

## Задание 3. Контравариантный обработчик

from typing import Generic, TypeVar

T_contra = TypeVar("T_contra", contravariant=True)

class Animal:

    def __init__(self, name: str = "Generic Animal"):
        self.name = name


class Dog(Animal):

    def __init__(self, name: str = "Rex"):
        super().__init__(name)


class Validator(Generic[T_contra]):

    def validate(self, item: T_contra) -> bool:
        raise NotImplementedError


class AnimalValidator(Validator[Animal]):

    def validate(self, item: Animal) -> bool:
        return bool(item.name.strip())


def check(v: Validator[Dog], d: Dog) -> bool:
    return v.validate(d)


dog = Dog("Бобик")
validator = AnimalValidator()

check(AnimalValidator(), Dog())
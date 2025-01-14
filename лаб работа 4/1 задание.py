import doctest



class Tree:
    def __init__(self, species: str, height: float):
        """
 Созлание и подготовка объекта "Дерево".
 :param species: Вид дерева
 :param height: Высота дерева в метрах
 Примеры:
 >>> iva = Tree("iva", 5.0) #инициализзация экземпляра класса
        """

        if not isinstance(species, (str)):
            raise TypeError("Вид дерева должен быть типа str")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть int или float")
        if height < 0:
            raise ValueError("Высота не может быть отрицательным числом")
        self.height = height

    def tree_exists(self) -> bool:
        """
 Функция которая проверяет существует ли дерево
 :return: Существует ли дерево
 Примеры:
 >>> iva = Tree("iva", 5.0)
 >>> iva.tree_exists()
        """
        ...

    def tree_grow(self, growth: float) -> None:
        """
 Дерево растет
 :param growth: Прирост дерева
        Примеры:
 >>> iva = Tree("iva", 5.0)
 >>> iva.tree_grow(1.0)
        """
        if not isinstance(growth, (int, float)):
            raise TypeError("Прирост должен быть типа int или float")
        if growth < 0:
            raise ValueError("Прирост должен быть положительным числом")
        ...

    def log_house_of_a_tree(self, length_of_the_felled_part: float) -> None:
        """
 Сруб дерева.
 :param length_of_the_felled_part: Длина срубленной части
 :raise ValueError: Если длина срубленной части превышает длину дерева,
 то возвращается ошибка.
 :return: Длина реально срубленной части
 Примеры:
 >>> iva = Tree("iva", 5.0)
 >>> iva.log_house_of_a_tree(200)
        """
        ...
if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
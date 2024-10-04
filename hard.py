class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class CartoonToy(Toy):
    def __init__(self, name, color, cartoonname):
        super().__init__(name, color)
        self.cartoonname = cartoonname
        print(
            "Игрушка ",
            self.name,
            " цвета ",
            self.color,
            " из мультфильма ",
            self.cartoonname,
            " готова!",
        )


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        print("Игрушка ", self.name, " цвета ", self.color, " готова!")


class Factory:
    def create_toy(toy_type, name, color, cartoon_name=None):
        print("Закупка сырья для игрушки ", name, "...")
        print("Игрушка шьется...")
        print("Игрушка окрашивается в ", color, " цвет...")

        if toy_type == "cartoon" or toy_type == "Cartoon":
            return CartoonToy(name, color, cartoon_name)
        elif toy_type == "animal" or toy_type == "Animal":
            return AnimalToy(name, color)


toy1 = Factory.create_toy("cartoon", "Лимур", "Белый", "Мадагаскар")
toy1 = Factory.create_toy("animal", "Медведь", "Коричневый")

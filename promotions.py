from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass
        
    def __str__(self):
        return self.name


# return product.price * quantity * self.discount

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent
        
    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent/100)



class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)
        
    def apply_promotion(self, product, quantity):
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)



class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        charged_items = quantity - free_items
        return charged_items * product.price

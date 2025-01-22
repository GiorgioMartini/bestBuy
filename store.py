class Store():
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product) 

    def remove_product(self, product):
        self.products.remove(product)

    def get_all_products(self):
        return [product for product in self.products if product.is_active]

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def order(self, shopping_list):
        order_total = 0
        try:
            for product, quantity in shopping_list:
                order_total += product.buy(quantity)
            return order_total
        except ValueError as e:
            print(f"\nError: {str(e)}")
            return 0


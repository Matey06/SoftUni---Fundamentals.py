class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        for current_product in self.products:
            if current_product[0] != first_letter:
                self.products.remove(current_product)

        return self.products

    def __repr__(self):
        self.products.sort()
        formated = '\n'.join(self.products)
        return f"Items in the {self.name} catalogue:\n{formated}"

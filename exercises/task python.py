# muhammad saad raza

def top_items(n, *sales):
    sales_sorted = sorted(sales, key=lambda s: s[1], reverse=True)
    return [item for item, amount in sales_sorted[:n]]


print(top_items(2, ("pen", 50), ("book", 300), ("bag", 120)))
print(top_items(5, ("pen", 50), ("book", 300)))
print(top_items(3))

# secomd question
# muhammad saad raza

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, qty):
        self.stock += qty

    def sell(self, qty):
        if qty > self.stock:
            return False
        self.stock -= qty
        return True

    def value(self):
        return self.price * self.stock


pen = Product("pen", 50, 10)
print(pen.sell(4), pen.stock)
print(pen.sell(15), pen.stock)
pen.restock(4)
print(pen.value())
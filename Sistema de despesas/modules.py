class expense:
    def __init__(self, balance, product, price):
        self.product = product
        self.price = price
        self.balance = balance
    def spend(self):
        self.balance -= self.price
class togain:
    def __init__(self) -> None:
         pass
    def gain(self, taskname, toreceive):
            self.balace += toreceive
            data = [taskname, toreceive]
            print(data)
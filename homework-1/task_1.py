# TASK 1 -
class CashRegister:  #Instantiating
    def __init__(self, bought_items, total_items, discount):
        self.bought_items = bought_items
        self.total_items = total_items
        self.discount = discount

    def add_item(self, new_item):  #Method to add
        self.bought_items.update(new_item)
        self.total_items = self.total_items + 1
        print("once this item has been bought")
        print("Total items after adding is "+str(self.total_items))
        print(self.bought_items)

    def remove_item(self, item):     #Method to remove
        self.bought_items.pop(item)
        self.total_items = self.total_items-1
        print("AFTER REMOVING SELECTED ITEM")
        print("Total items after removing is "+str(self.total_items))
        print(self.bought_items)

    def apply_discount(self):     #Method to apply discount
        d = {}
        items = b.bought_items.keys()
        for i in items:
            values = (b.bought_items.get(i))*(1 - self.discount)
            d.update({i: values})
        print("ITEMS LIST AFTER APPLYING DISCOUNT")
        print(d)
    def get_total(self):        # Method to get total
        prices = self.bought_items.values()
        sum = 0
        for i in prices:
            sum = sum+i
        print("TOTAL VALUE OF PRICES OF ALL ITEMS")
        print(sum)
        return sum
    def show_items(self):          # Method to show items
        print("LIST OF ITEMS IN CASH REGISTER")
        print(b.bought_items)


    def reset_register(self):    # Method to reset -register
        b.bought_items.clear()
        print("RESET REGISTER")
        print(b.bought_items)




b = CashRegister(bought_items={"pencil": 80, "pen": 25, "Notebook": 10, "Highlighter": 30}, total_items=4, discount=0.25)

b.add_item({"stapler": 5})
b.remove_item("pencil")
b.apply_discount()
b.show_items()
b.get_total()
b.reset_register()








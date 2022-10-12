# TASK 1 -
class CashRegister:
    def __init__(self, bought, items, discount):
        self.bought_items = bought
        self.total_items = items
        self.discount = discount

    def add_item(self, new_item):
        self.new_item = new_item
        self.bought_items.update(new_item)
        self.total_items = self.total_items + 1
        print("once this item has been bought")
        print("Total items after adding is "+str(self.total_items))
        print(self.bought_items)

    def remove_item(self, item):
        self.item = item
        self.bought_items.pop(item)
        self.total_items= self.total_items-1
        print("AFTER REMOVING SELECTED ITEM")
        print("Total items after removing is "+str(self.total_items))
        print(self.bought_items)

    def apply_discount(self):
        d={}
        items=a.bought_items.keys()
        for i in items:
            values=(a.bought_items.get(i))*self.discount
            d.update({i:values})
        print("ITEMS LIST AFTER APPLYING DISCOUNT")
        print(d)
    def get_total(self):
        prices = self.bought_items.values()
        sum=0
        for i in prices:
            sum=sum+i
        print("TOTAL VALUE OF PRICES OF ALL ITEMS")
        print(sum)
    def show_items(self):
        print("LIST OF ITEMS IN CASH REGISTER")
        print(a.bought_items)

    def reset_register(self):
        a.bought_items.clear()
        print("RESET REGISTER")
        print(a.bought_items)




a = CashRegister({"pencil": 80, "pen": 25, "Notebook": 10, "Highlighter": 30}, 4, 0.2)

a.add_item({"stapler": 5})
a.remove_item("pencil")
a.apply_discount()
a.show_items()








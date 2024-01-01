class Store:
    def __init__(self):
        self.products = {}

    
    def add_product(self, product_name, price):
        self.products[product_name] = price

   
    def display_menu(self):
        print("Menu:")
        for product, price in self.products.items():
            print(f"{product} - ${price:.2f}")

   
    def generate_bill(self, quantities):
        total_amount = 0.0

        print("\nBill:")
        for product, quantity in quantities.items():
            if product in self.products:
                price = self.products[product]
                item_total = price * quantity

                print(f"{product} - {quantity} units - ${item_total:.2f}")
                total_amount += item_total
            else:
                print(f"Product not found: {product}")

        print(f"\nTotal Amount: ${total_amount:.2f}")


def main():
    
    my_store = Store()
    my_store.add_product("ProductA", 10.99)
    my_store.add_product("ProductB", 5.99)
    my_store.add_product("ProductC", 7.49)
    my_store.display_menu()
    quantities = {}
    while True:
        product_name = input("Enter the product name (or 'exit' to finish): ")
        if product_name.lower() == 'exit':
            break

        try:
            quantity = int(input("Enter the quantity: "))
            quantities[product_name] = quantity
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
    my_store.generate_bill(quantities)
if __name__ == "__main__":
    main()

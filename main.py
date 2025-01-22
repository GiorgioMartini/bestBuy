from products import Product
from store import Store

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def show_all_products(store):
    """
    Display all products available in the store with their index numbers.
    
    Args:
        store (Store): The store object containing the products to display
    """
    print("All products in store:")
    for i, product in enumerate(store.get_all_products(), 1):
        print(f"{i}. {product.name} - Price: ${product.price} - Quantity: {product.quantity}")

def start(store):
    """
    Start the main store interface loop. Presents a menu to the user with options to:
    - List all products
    - Show total inventory quantity
    - Make an order
    - Quit the program
    
    Args:
        store (Store): The store object to operate on
    """
    total_price = 0
    while True:
        try:
            menu_options = {
                "1": "List all products in store",
                "2": "Show total amount in store",
                "3": "Make an order", 
                "4": "Quit"
            }
            
            print("\nStore Menu")
            print("----------")
            for key, value in menu_options.items():
                print(f"{key}. {value}")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                show_all_products(store)
            elif user_input == "2":
                print(f"\nTotal amount in store: {store.get_total_quantity()}")
            elif user_input == "3":
                show_all_products(store)
                while True:
                    try:
                        wantedProduct = input("\nWhich product # do you want?\nElse type 0 to go back to menu: ")
                        if not wantedProduct.isdigit():
                            print("\nError: Product number must be a number")
                            break
                        
                        # Check if user wants to go back to menu
                        if wantedProduct == "0":
                            break
                            
                        wanted_amt = input("What amount do you want? ")
                        if not wanted_amt.isdigit():
                            print("\nError: Amount must be a number") 
                            break
                        
                        product_idx = int(wantedProduct) - 1
                        
                        # Validate product index is in range
                        if product_idx < 0 or product_idx >= len(store.get_all_products()):
                            print("\nError: Invalid product number")
                            break
                            
                        quantity = int(wanted_amt)
                        if quantity <= 0:
                            print("\nError: Quantity must be greater than 0")
                            break
                        
                        product = store.get_all_products()[product_idx]
                        
                        shopping_list = [(product, quantity)]
                        order_amount = store.order(shopping_list)
                        if order_amount > 0:  # Only add to total if order was successful
                            total_price += order_amount
                            print(f"\nOrder made! Total payment: ${total_price}")
                        break
                        
                    except Exception as e:
                        print(f"\nError processing order: {str(e)}")
                        break
                        
            elif user_input == "4":
                print("\nThank you for shopping with us!")
                break
            else:
                print("\nError: Invalid menu option. Please choose 1-4")
                
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            continue

if __name__ == "__main__":
    start(best_buy)

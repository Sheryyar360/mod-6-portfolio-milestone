import sys


class ItemToPurchase:
    item_name = 'name'
    item_description = 'description'
    item_price = 0.00
    item_quantity = 1

    def __init__(self, item_name, item_description, item_price, item_quantity):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def item_total(self):
        item_total = self.item_quantity * self.item_price
        return item_total


class ShoppingCart:
    customer_name = 'none'
    date = 'January 1, 2020'
    cart_items = []

    def __init__(self, customer_name, date):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []

    def add_item(self):
        item = ItemToPurchase(input('Enter item name: '), input('Enter item description: '),
                              float(input('Enter item price: ')), int(input('Enter item quantity: ')))
        self.cart_items.append(item)
        print(f'{item.item_name} has been added to the cart')

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                print(f'{item_name} has been removed')
                break
        if not item_found:
            print(f'Item not found in cart. Nothing removed.')

    def modify_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                item_found = True
                item.item_description = input('Enter alternate item description: ')
                item.item_price = float(input('Enter alternate item price: '))
                item.item_quantity = int(input('Enter alternate item quantity: '))
        if not item_found:
            print('Item not found in cart. Nothing modified')

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        cart_total = 0
        for item in self.cart_items:
            cart_total += item.item_total()
        return cart_total

    def print_total(self):
        total_items = 0
        print(f'{self.customer_name}\'s Shopping Cart: {self.date}')
        for item in self.cart_items:
            total_items += item.item_quantity
        print(f'Number of items: {total_items}')
        print('_______________________________________________')
        for item in self.cart_items:
            print('{} {} @ ${:.2f} = ${:.2f}'.format(item.item_quantity, item.item_name, item.item_price,
                                                     item.item_total()))
        print('Cart Total: ${:.2f}'.format(self.get_cost_of_cart()))
        if total_items == 0:
            print('SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Care: {self.date}')
        print('Item descriptions:')
        print('_______________________________________________')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')


def main():

    cart = ShoppingCart(input('Enter your name: '), input('Enter today\'s date: '))

    def print_menu(shopping_cart):
        menu_selection = '_'
        while menu_selection != 'q':

            print(' MENU: \n a - Add item to cart \n r - Remove item from cart \n m - Modify item '
                  '\n i - Output item\'s descriptions \n o - Output shopping cart \n q - Quit ')
            print('_______________________________________________')

            menu_selection = input(' Choose an option: ')

            match menu_selection:
                case 'a':
                    shopping_cart.add_item()
                case 'r':
                    shopping_cart.remove_item(input('Enter name of item to remove: '))
                case 'm':
                    shopping_cart.modify_item(input('Enter name of item to modify: '))
                case 'i':
                    shopping_cart.print_descriptions()
                case 'o':
                    shopping_cart.print_total()
                case 'q':
                    sys.exit()
                case _:
                    print('Not a valid option, please try again')

    print_menu(cart)


main()

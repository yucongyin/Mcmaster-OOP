from stubs_shopping_cart import ShoppingCart

def test_passes():
    assert number < 7, "Number has to be bigger than 7"

def test_fails():
    assert False

def test_add_item():
    cart = ShoppingCart()
    assert len(cart.items) == 0, "Cart should be created empty"
    item = "steak"
    cart.add_item(item)
    assert len(cart.items) == 1, "Cart should now have exactly 1 item"

def test_add_item_to_cart_with_items():
    cart = ShoppingCart(items)
    assert len(cart.items) == 2, "Cart should be created empty"
    item = "steak"
    cart.add_item(item)
    assert len(cart.items) == 3, "Cart should now have exactly 1 item"

import pytest
from products import Product


def test_creating_prod():
    """ creating a normal product works. """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.show() == "Bose QuietComfort Earbuds, Price: $250, Quantity: 500"


def test_creating_prod_invalid_details():
    """ creating a product with invalid details (empty name, negative price) invokes an exception. """
    with pytest.raises(TypeError):
        Product("Macbook Air M1", price="abc", quantity=50) # wrong price format
        Product("Macbook Air M1", price=50, quantity="abc") # wrong quantity format
        Product("", price=1450, quantity=100) # empty string

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100) # negative price
        Product("MacBook Air M2", price=100, quantity=-100) # negative quantity


def test_prod_becomes_inactive():
    """ Test that when a product reaches 0 quantity, it becomes inactive. """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.is_active() == True
    bose.set_quantity(0)
    assert bose.is_active() == False


def test_buy_modifies_quantity():
    """ Test that product purchase modifies the quantity and returns the right output. """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.buy(100) == 100 * bose.price # check if price is correct
    assert bose.quantity == 400 # check if quantity is modified


def test_buy_too_much():
    """ Test that buying a larger quantity than exists invokes exception. """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    with pytest.raises(ValueError):
        bose.buy(600)

    assert bose.buy(500) == 500 * bose.price # check if buying all products is possible.


if __name__ == "__main__":
    test_creating_prod()
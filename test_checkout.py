import pytest
from Checkout import Checkout

# tests that are not needed anymore, can be removed because of 
# code duplication 
# --> I will comment them out for the purposes of the project

# commented out due to duplication
# def test_canInstantiateCheckout():
#     co = Checkout()

#adding fixture to remedy code duplication
@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItemPrice('b', 2)
    return checkout

# commented out due to duplication
# def test_CanAddItemPrice(checkout):
#     checkout.addItemPrice('a', 1)

# def test_CanAddItem(checkout):
#     checkout.addItem('a')

def test_CanCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)


def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')
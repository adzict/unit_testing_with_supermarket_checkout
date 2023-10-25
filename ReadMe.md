# Overview of the Supermarket Checkout Project for Unit Testing

## Source: 

[Kata09: Back to the Checkout][http://codekata.com/kata/kata09-back-to-the-checkout/]

## The Checkout Class

I'll be implementing a checkout class that maintains a list of items that are being added during a checkout at a supermarket. This class should provide interfaces for:

- setting the price of individual items
- adding individual items to the checkout
- the current total cost for all the items added
- add and apply discounts on select items when N number are purchased

## The Test Cases

The checkout class has the following test cases that all go through as I'm implementing the class with TDD:

- can create an instance of the Checkout class
- can add an item price
- can add an item
- can calculate the current total
- can add multiple items and get correct total
- can add discount rules
- can apply discount rules to the total
- exception is trhrown for item added without a price

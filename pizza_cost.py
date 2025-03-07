#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Mar 3, 2025
# This program is to calculate the pizza's prize
# including tax
import constants


def main():
    # input of from the user
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # the process of calculation
    subtotal = (
        constants.LABOUR_COST + constants.INGRED_COST * diameter + constants.RENTAL_COST
    )
    tax = subtotal * constants.HST
    total = subtotal + tax

    # output
    print("")
    print("the total cost of the pizza is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()

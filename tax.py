#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 30, 2025
# Program the calculates and displays the tax+total of a purchase
# in British Columbia

import constants


def main():
    # Get subtotal
    subtotal = float(input("Enter subtotal: $"))

    # Calculate tax
    tax = subtotal * constants.BRITISH_COLUMBIA_HST
    # Calculate total
    total = subtotal + tax

    # Display the tax and total
    print("")
    print(f"You entered a subtotal of ${subtotal:.2f}")
    print(f"The HST is ${tax:.2f} and the total is ${total:.2f}")


if __name__ == "__main__":
    main()

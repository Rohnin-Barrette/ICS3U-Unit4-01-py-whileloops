#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program finds the sum of all the whole numbers that lead up to the inputted number including it


def main():
    # This function finds the sum of all the whole numbers that lead up to the inputted number including it

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    sum_of_numbers = 0

    # input
    print("\n", end="")
    positive_string = input("Enter a positive integer: ")

    # process & output
    try:
        positive_number = int(positive_string)
        print("\n", end="")
        while loop_counter <= positive_number:
            sum_of_numbers = sum_of_numbers + loop_counter
            loop_counter = loop_counter + 1
        print(
            "the sum of the numbers from 1 to {0} is {1}.".format(
                positive_number, sum_of_numbers
            )
        )
    except Exception:
        print("{0} is not a valid input.".format(positive_string))

    print("\nDone.")


if __name__ == "__main__":
    main()

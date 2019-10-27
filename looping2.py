#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Oct 2019
# This program uses a while loop to add all whole numbers from 1 to the chosen_
# number


def main():
    # this function uses a while loop
    loop_counter = 0
    adding_number = 1

    # input
    try:
        chosen_number = int(input("Input a positive integer: "))
        print("")

        # process & output
        while loop_counter < chosen_number:
            print("Loop was ran {0} times.".format(loop_counter))
            loop_counter += 1
            adding_number = adding_number * loop_counter
        print(adding_number)
    except(ValueError):
        print("Please input a positive whole number.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: OcTober 2019
# This program sees if a user can date a grandmas grandaughter


def main():
    # This function sees if a user can date a grandmas grandaughter
    age_as_string = input("Give me your age: ")
    # input and process
    try:
        age_as_number = int(age_as_string)
        print("")
        if age_as_number > 25 and age_as_number < 40:
            print("Your are able to date my grandaughter")
        else:
            print("Your are not able to date my grandaughter")
    except Exception:
        print("This is and invalid age")
    finally:
        print("Thanks for trying")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import prompt


def run():
    name = prompt.string("May I have your name? ")
    print("Hello {}!".format(name))


if __name__ == "__main__":
    run()

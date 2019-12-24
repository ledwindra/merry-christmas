import os
import sys
from time import sleep

SANTA = "\U0001F385"
PYTHON = "\U0001F40D"
LAPTOP = "\U0001F4BB"

def main():

    # please input your name
    # won't cause any error if you type anything else, though
    your_name = input(
        "\n"
        + SANTA\
        + " : Ho ho ho! Welcome! What's your name, buddy?\n\n"
    )

    # please input what you want
    want = input(
        "\n"\
        + SANTA \
        + " : Hello, {}! So tell me, what do you want for Christmas?\n\n"\
        .format(your_name)
    )

    if "python code" in want.lower():
        print("\n" + SANTA, ": Easy! Here's what you want!")
        print("\n...", SANTA, " starts writing a", PYTHON, " code on a", LAPTOP)
        print("\n" + SANTA, " : Ho ho ho! Here's what you want, kiddo!")
    elif "nothing" in want.lower():
        print("\n" + SANTA, " : Alright, see you next year.\n")
        sys.exit(0)
    else:
        print("\n" + SANTA, " : No worries, kiddo! But for now, I will give you a tree. Ho ho ho!")

    # output code will appear soon
    os.system("python3 src/merry_christmas.py 18 Enjoy \U0001F385")
    print(
        SANTA\
        + " : Oh and you can check out the source code on https://github.com/ledwindra/merry-christmas. Ho ho ho!\n"
    )

    # automatically re-run code
    sleep(1)
    os.system("clear")
    os.system("python3 demo.py")

if __name__ == "__main__":
    main()
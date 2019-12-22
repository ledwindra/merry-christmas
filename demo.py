import os

SANTA = "\U0001F385"
PYTHON = "\U0001F40D"
LAPTOP = "\U0001F4BB"

def main():

    your_name = input(SANTA + " : Ho ho ho! Welcome! What's your name, buddy?\n\n")
    input("\n" + SANTA + " : Hello, {}! So tell me, what do you want for a Christmas?\n\n".format(your_name))
    print("\n" + SANTA, ": Easy! Here's what you want!")
    print("\n...", SANTA, " starts writing a", PYTHON, " code on a", LAPTOP)
    print("\n" + SANTA, " : Ho ho ho! Here's what you want, kiddo!")
    os.system("python3 src/merry_christmas.py 18 Enjoy \U0001F385")
    print(SANTA + " : Oh and you can check out the source code on https://github.com/ledwindra/merry-christmas. Ho ho ho!")

if __name__ == "__main__":
    main()
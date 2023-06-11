import re

is8CharactersLong = re.compile(r".{8,}")
hasUppercase = re.compile(r"[A-Z]+")
hasLowercase = re.compile(r"[a-z]+")
hasDigits = re.compile(r"\d+")

# This checks the password strenght


def IsStrong(pw):
    if is8CharactersLong.search(pw) != None:
        if hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
            if hasDigits.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("MASON THE NUMBERS")
        else:
            print("Maybe some UpPeR LoWer game?")

    elif is8CharactersLong.search(pw) != None:
        if hasDigits.search(pw) != None:
            if hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("Maybe some UpPeR LoWer game?")
        else:
            print("MASON THE NUMBERS")

    elif hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
        if is8CharactersLong.search(pw) != None:
            if hasDigits.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("MASON THE NUMBERS")
        else:
            print("That's too short baby")

    elif hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
        if hasDigits.search(pw) != None:
            if is8CharactersLong.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("That's too short baby")
        else:
            print("MASON THE NUMBERS")

    elif hasDigits.search(pw) != None:
        if is8CharactersLong.search(pw) != None:
            if hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("Maybe some UpPeR LoWer game?")
        else:
            print("That's too short baby")

    elif hasDigits.search(pw) != None:
        if hasUppercase.search(pw) != None and hasLowercase.search(pw) != None:
            if is8CharactersLong.search(pw) != None:
                print("Yeaaah baby that's what i'm talking about!")
                quit
            else:
                print("That's too short baby")
        else:
            print("Maybe some UpPeR LoWer game?")
    else:
        print("Dude are you even trying?")


# Main Loop
while True:
    password = input("Try a password please \n")

    IsStrong(password)

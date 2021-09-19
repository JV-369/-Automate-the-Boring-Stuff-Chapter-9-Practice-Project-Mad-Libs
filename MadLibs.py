useradjective = input("Enter an adjective:")
usernoun1 = input("Enter a noun:")
userverb = input("Enter a verb:")
usernoun2 = input("Enter a noun:")


def madlibs(useradjective, usernoun1, userverb, usernoun2):
    f = open("source.txt", "r")
    text = f.read()
    f.close()

    reaplced = text.replace("ADJECTIVE", useradjective)
    reaplced1 = reaplced.replace("NOUN", usernoun1, 1)
    reaplced2 = reaplced1.replace("VERB", userverb)
    reaplced3 = reaplced2.replace("NOUN", usernoun2)

    output = open("output.txt", "w")
    output.write(reaplced3)
    output = open("output.txt", "r")
    print(output.read())


madlibs(useradjective, usernoun1, userverb, usernoun2)

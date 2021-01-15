import sys

#Defining big numbers as lists containing characters split into rows
Zero  = [" *** ", 
         "*   *", 
         "*   *", 
         "*   *",
         "*   *",
         "*   *",
         " *** "]
One   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
Two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

#A loop which takes command line integer input and converts it to big digits
#For each character in a column, the corresponding input number is checked and 
#assigned in place of all the placeholder * characters
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for character in digit[row]:
                if character == "*":
                    line += str(number)
                else:
                    line += character
            line += " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
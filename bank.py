# implement a program that prompts the user for a greeting
# if the greeting starts with "hello" output zero
# if the program starts with an h but not hello output 20
# otherwise output $100

# ignore leading whitespaces and treat the input
# case-insensitively

def main():
    bank_teller(input("Greeting: "))


def bank_teller(greeting):
    if greeting.startswith("Hello") or greeting.startswith("hello"):
        print(0)
    elif greeting.startswith("h") or greeting.startswith("H"):
        print(20)
    else:
        print(100)

main()
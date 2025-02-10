def main():
    print(deep(input("What is the answer to the great question of life, the universe, and everything? ")))

def deep(the_answer):
    if "42" in the_answer or "forty-two" in the_answer or "forty two" in the_answer:
        return "Yes"
    else:
        return "No"


main()
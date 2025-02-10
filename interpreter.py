def main():
    print(interpreter(input("Expression: ")))


def interpreter(expression):
    symbols = expression.split(" ")
    x = int(symbols[0])
    y = symbols[1]
    z = int(symbols[2])
    if y == "*":
        return float(x * z)
    elif y == "-":
        return float(x - z)
    elif y == "+":
        return float(x + z)
    elif y == "/":
        return float (x / z)
    
main()
def hf4():
    while True:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))

        try:
            c = a / b
            print(c)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        finally:
            print("Out of try except blocks")

if __name__ == "__main__":
    hf4()
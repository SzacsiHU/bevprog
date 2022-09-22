def hf1():
    print("Adjon meg egy mondatot:")
    sentence = input()
    letters = {}

    for i in sentence:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    print("Betük gyakorisága:", str(letters))
    print("Fordítva:", sentence[::-1])

    list = sentence.split(" ")
    print("Listába rendezve szavanként:", list)

def hf2():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")

    value = float(input())
    unit = input()

    v = 2.54

    if unit == "cm":
        value = value * v
        print(value, " inches")
    elif unit == "inch":
        value = value / v
        print(round(value, 2), " cm")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    hf1()
    hf2()
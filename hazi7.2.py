def binary_search():
    list = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    n = 70

    lepes = 0
    N = len(list)

    also, felso = 0, N-1
    while also <= felso:
        k = (felso+also)//2
        lepes += 1

        if n < list[k]:
            felso = k-1
        elif n > list[k]:
            also = k+1
        else:
            kimenet = f"A {lepes} lépésben található a megadott szám.\nAlsó érték: {also}\nFelső érték: {felso}\nA k értéke: {k} (index)"
            break
    else:
        kimenet = "Nem található a megadott szám!!!"

    print(kimenet)

if __name__ == "__main__":
    binary_search()
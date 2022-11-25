def Bubblesort():
    list = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]

    N = len(list)

    for i in range(0, N):
        for x in range(1, N-i):
            if list[x-1] > list[x]:
                list[x], list[x-1] = list[x-1], list[x]

    print("A lista növekvő sorrendben: ", list)

if __name__ == "__main__":
    Bubblesort()
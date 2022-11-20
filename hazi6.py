import string


def txt():
    sorok = ""

    with open("hazi.txt", "r", encoding="UTF-8") as be:
        for i in be:
            if i != "\n":
                sorok += i

    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzok = ""

    for x in sorok:
        if x != " " and x not in string.punctuation:
            if x not in maganhangzok:
                massalhangzok += x

    ki1 = list(massalhangzok.split("\n"))

    with open("ki.txt", "w", encoding="UTF-8") as ki:
        for s, i in enumerate(ki1):
            if (s + 1) % 3 == 0:
                ki.write(i + "\n")

if __name__ == "__main__":
    txt()
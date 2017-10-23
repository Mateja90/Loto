import random

def ponovitev(st):
    seznam = []
    x=0
    while x in range(st):
        rand = random.randint(0, 99)
        if rand not in seznam:
            seznam.append(rand)
            x +=1

        else:
            x+=1


    return seznam


def main():
    print("Generator nakljucnih Loto stevil ")
    st = int(raw_input("Koliko nakljucnih stevil zelis generirati? "))

    print(ponovitev(st))
    print("End")
if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
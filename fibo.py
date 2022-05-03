
def recursive_nth_fibo(konecnaPozice):
    if konecnaPozice == 0:
        return 0
    elif konecnaPozice==1:
        return 1
    else:
        return recursive_nth_fibo(konecnaPozice-1) + recursive_nth_fibo(konecnaPozice-2)



def main():

    cislo = int(input("zadej pozici konecneho prvku"))
    print(recursive_nth_fibo(cislo))


if __name__ == "__main__":
    main()

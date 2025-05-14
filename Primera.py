from collections import Counter
def main():

    izq, der = [], []
    

    with open("day01_input.txt", "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.split()
            izq.append(int(a))
            der.append(int(b))

  
    izq.sort()
    der.sort()


    total_distancia = sum(abs(a - b) for a, b in zip(izq, der))


    print(f"Distancia total entre las listas: {total_distancia}")


if __name__ == "__main__":
    main()

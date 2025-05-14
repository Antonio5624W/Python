from collections import Counter

def main():
    izq, der = [], []

    with open("day01_input.txt", "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.split()
            izq.append(int(a))
            der.append(int(b))

    contador_der = Counter(der)

    puntuacion_similitud = sum(num * contador_der[num] for num in izq)

    print(f"Puntuación de similitud entre las listas: {puntuacion_similitud}")


if __name__ == "__main__":
    main()

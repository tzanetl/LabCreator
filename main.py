# Generate a labyrinth using weighted tiles


from labutil import labinit


def main():
    h = 5
    w = 5
    start = 2

    lab = labinit(h, w, start)

    print(lab.map())

main()
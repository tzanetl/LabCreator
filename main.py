# Generate a labyrinth using weighted tiles


from labutil import labinit, labgen


def main():
    h = 5
    w = 5
    start = 2

    lab = labinit(h, w, start)
    print(lab)
    lab = labgen(lab)
    print(lab.map())

main()
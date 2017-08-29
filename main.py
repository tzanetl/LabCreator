# Generate a labyrinth using weighted tiles


from labutil import labinit, labgen


def main():
    h = 10
    w = 10
    start = 2

    lab = labinit(h, w, start)
    print(lab, "\n")
    lab = labgen(lab)
    print(lab.map())

main()
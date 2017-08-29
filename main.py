# Generate a labyrinth using weighted tiles


from labutil import labinit, labgen


def main():
    h = 15
    w = 15
    start = 6

    lab = labinit(h, w, start)
    print(lab, "\n")
    lab = labgen(lab)
    print(lab.map())

main()
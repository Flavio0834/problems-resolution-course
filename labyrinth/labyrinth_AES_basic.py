from Labyrinth import Labyrinth


def AES(lab, x, y):
    if lab.get_fin() == (x, y):
        return True
    else:
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if lab.is_free(x1, y1):
                lab.set_case(x1, y1, 4)
                if AES(lab, x1, y1):
                    return True
        return False


if __name__ == "__main__":
    # Generating a labyrinth
    N = 12
    lab = Labyrinth(N)
    lab.remplir(N * N // 3)
    print(lab)

    # Solving the labyrinth
    debut = lab.get_debut()
    print(AES(lab, debut[0], debut[1]))
    print(lab)

from Labyrinth import Labyrinth
import copy


def pcc(nums, x, y, n):
    nums[x][y] = min(nums[x][y], n + 1)
    return nums[x][y]


def AES(lab, nums, x, y):
    global deltas
    for delta in deltas:
        x1 = x + delta[0]
        y1 = y + delta[1]
        if lab.get_fin() == (x1, y1):
            return [(x1, y1)]
        if lab.is_free(x1, y1):
            if nums[x1][y1] == nums[x][y] + 1 or (x, y) == lab.get_debut():
                trajet = AES(lab, nums, x1, y1)
                if trajet != []:
                    return [(x1, y1)] + trajet
    return []


if __name__ == "__main__":
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Generating a labyrinth
    N = 12
    lab = Labyrinth(N)
    lab.remplir(N * N // 3)
    print(lab)

    # Generating pcc heuristic numerotation matrix
    nums = copy.deepcopy(lab.get_matrice())
    for i in range(N):
        for j in range(N):
            if nums[i][j] == 0:
                nums[i][j] = float("inf")

    debut = lab.get_debut()
    queue = [(*debut, 100)]
    x, y = -1, -1
    visited = set()
    while queue != [] and (x, y) != lab.get_fin():
        x, y, n = queue.pop(0)
        if (x, y) != lab.get_debut():
            n = pcc(nums, x, y, n)

        if (
            (x, y) == lab.get_fin() or (nums[x][y] != float("inf") and nums[x][y] < n)
        ) and lab.get_debut() in visited:
            continue
        visited.add((x, y))

        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if (
                (x1, y1) not in visited
                and x1 >= 0
                and x1 < N
                and y1 >= 0
                and y1 < N
                and (lab.get_case(x1, y1) == 0 or (x1, y1) == lab.get_fin())
            ):
                queue.append((x1, y1, n))

    for i in range(N):
        print(nums[i])

    # Solving the labyrinth

    print("\n***********\n")
    print(lab)
    print("\n***********\n")
    trajet = AES(lab, nums, debut[0], debut[1])
    print(trajet)
    for (x, y) in trajet:
        lab.set_case(x, y, 4)
    print(lab)

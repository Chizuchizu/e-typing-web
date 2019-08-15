import numpy as np


def keisan(number):
    score = np.load("score_" + number + ".npy").astype(int)

    res = np.round(50 + 10 * ((score - np.average(score)) / np.std(score)))

    meyasu = np.zeros((100, 2))

    for i in range(0, len(res), 50):
        j = i // 50
        meyasu[j, 0] = score[i]
        meyasu[j, 1] = res[i]

    for i, x in enumerate(meyasu):
        print("スコア " + str(x[0]) + " で、偏差値は " + str(x[1]))

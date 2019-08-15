import numpy as np


def keisan(number):
    score = np.load("score_" + number + ".npy").astype(int)
    memo = [0.6, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]

    for i, x in enumerate(memo):
        idx = int(x * len(score))
        # print(idx)
        print(score[idx], "点以上は上位", x * 100, "%\n")

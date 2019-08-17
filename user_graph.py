import hensachi

import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO


def main2(name):
    file_path = glob.glob("data/score_*.npy")

    score_g = np.zeros((len(file_path), 4))

    file_path.sort()

    for i, x in enumerate(file_path):
        user = np.load(x.replace("score", "user"))
        score = np.load(x).astype(int)
        user_idx = np.where(user == name)[0]

        score_g[i, 0] = int(x.split("_")[1].split(".")[0])
        # print(score)
        score_g[i, 3] = score.mean()

        kai = x.split("_")[1].split(".")[0]

        if user_idx.size == 0:
            score_g[i, 1] = 0
            score_g[i, 2] = 0
        else:
            user_score = score[user_idx[0]]
            score_g[i, 1] = user_score
            score_g[i, 2] = hensachi.keisan(kai, user_score)

    # print(score_g)

    plt.rcParams["font.size"] = 25
    fig, ax2 = plt.subplots(figsize=(15, 8))
    ax1 = ax2.twinx()

    ax2.bar(score_g[:, 0], score_g[:, 1], label="score")
    ax1.plot(score_g[:, 0], score_g[:, 2], linewidth=2, color="red", linestyle="solid",
             marker="o", markersize=10, label="hensachi")
    ax2.plot(score_g[:, 0], score_g[:, 3], linewidth=2, color="green", linestyle="solid",
             marker="o", markersize=10, label="mean")

    ax1.set_zorder(2)
    ax2.set_zorder(1)

    ax2.grid(True)

    ax1.patch.set_alpha(0)
    ax1.legend(bbox_to_anchor=(0, 1), loc="upper left", borderaxespad=0.5, fontsize=15)
    ax2.legend(bbox_to_anchor=(0, 0.9), loc="upper left", borderaxespad=0.5, fontsize=15)

    plt.xlabel("No.")
    ax1.set_ylabel("hensachi")
    ax2.set_ylabel("score")

    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    return data

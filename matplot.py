import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
from io import BytesIO


def byoga(number):
    score = np.load("data/score_" + number + ".npy").astype(int)

    plt.rcParams["font.size"] = 25

    fig = plt.figure(figsize=(15, 10))
    plt.hist(score.astype(int), bins=30)
    plt.xlabel("score")
    plt.ylabel("frequency")
    plt.title("No." + number + " e-typing ranking")

    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    return data

import main2_js
import matplot
import hensachi
import pasento

import os

if __name__ == "__main__":
    number = input("第何回？:")
    while True:
        try:
            _ = int(number)
            if int(number) < 1:
                print("無効な数です")
                number = input("第何回？:")
                continue

            break

        except ValueError:
            print("無効な文字です")
            number = input("第何回？:")

    # ファイルの存在確認
    if not os.path.isfile("data/score_" + number + ".npy"):
        print("データファイルが存在しないのでスクレイピングします")
        main2_js.scripting(number)

    # 可視化
    matplot.byoga(number)

    # 偏差値の可視化
    hensachi.keisan(number)

    # 上位n%
    pasento.keisan(number)

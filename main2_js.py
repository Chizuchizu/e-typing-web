import time
from bs4 import BeautifulSoup
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import chromedriver_binary
from tqdm import tqdm


def scripting(number):
    options = Options()
    # ヘッドレスモードで実行する場合
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.e-typing.ne.jp/ranking/index.asp?sc=trysc&no=" + str(number))
        # 簡易的にJSが評価されるまで秒数で待つ
        time.sleep(3)

        # save
        user = np.zeros((1000, 30)).astype(str)
        score = np.zeros((1000, 30)).astype(str)
        html = driver.page_source.encode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        count = soup.find_all("div", attrs={"class": "num"})

        count = str(count).split(">")[1].split("<")[0]
        count = int(count.split("人")[0])
        count = int(np.ceil(count / 30))

        for i in tqdm(range(count)):
            html = driver.page_source.encode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            memo2 = soup.find_all("div", attrs={"class": "user"})
            memo3 = soup.find_all("div", attrs={"class": "score"})

            memo2 = str(memo2).split(",")
            memo3 = str(memo3).split(",")

            del memo2[0], memo3[0]
            memo2 = [x.split(">")[1].split("<")[0] for x in memo2]
            memo3 = [x.split(">")[1].split("<")[0] for x in memo3]
            if len(memo2) != 30:
                print(len(memo2))
                user[i, :len(memo2)] = memo2
                score[i, :len(memo3)] = memo3
            else:
                user[i, :] = memo2
                score[i, :] = memo3

            # wait!!!!!!
            time.sleep(1)

            try:
                driver.find_element_by_xpath('//*[@id="pager"]/li[11]/a').click()
            except:
                driver.find_element_by_xpath('//*[@id="pager"]/li[13]/a').click()

    except:
        traceback.print_exc()
    finally:
        # エラーが起きても起きなくてもブラウザを閉じる
        driver.quit()

    score = score.flatten()
    user = user.flatten()
    score = score[np.where(score != "0.0")].astype(str)
    user = user[np.where(user != "0.0")].astype(int)
    np.save("data/user_" + str(number), user)
    np.save("data/score_" + str(number), score)

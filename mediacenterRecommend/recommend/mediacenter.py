from selenium import webdriver
import time

def scroll(id, password):
    USER = id
    PASS = password

    f = open(USER + '.csv', 'w')

    browser = webdriver.Chrome('/Users/Owner/Downloads/chromedriver')
    browser.implicitly_wait(3)

    url_login = "https://lib.mrcl.dendai.ac.jp/webopac/login.do?url=ufisnd.do%3Fredirect_page_id%3D13"
    browser.get(url_login)
    print("ログインページに")

    e = browser.find_element_by_name('userid')
    e.clear()
    e.send_keys(USER)
    e = browser.find_element_by_name('password')
    e.clear()
    e.send_keys(PASS)
    #フォームを送信
    frm = browser.find_element_by_class_name('btn')
    frm.submit()
    print("情報を入力してログインボタンを押しました")
    time.sleep(3)
    browser.get('https://lib.mrcl.dendai.ac.jp/webopac/hislst.do')

    while True:
        try:
            for i in range(2,12):
                xpath = '/html/body/div/div/div/div[1]/form[1]/div/div[3]/table/tbody/tr[%d]/td[5]/a' % i
                label = browser.find_element_by_xpath(xpath).text
                if label.find("グループスタディ") != -1 or label.find("ノートPC用ACアダプタ") != -1:
                    print("--------------------------------")
                else:
                    title = label.split('/')[0]
                    print(title)
                    f.write(title)
                    try:
                        author = label.split('/')[1].split('. --')[0]
                        print(author)
                        f.write("," + author)
                    except:
                        print("どうせ伊豆旅行")
                    f.write("\n")
            nextButton = browser.find_element_by_link_text("次へ")
            nextButton.click()
        except:
            break
    print("全部出せたよ！")
    f.close()
    return
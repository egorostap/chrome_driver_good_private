import undetected_chromedriver
import time

def try_ex_dec(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print('ошибка:', e)
    return wrapped

@try_ex_dec
def chrome_driver():
    driver = undetected_chromedriver.Chrome()
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")
    time.sleep(17)
    driver.close()
    driver.quit()

if __name__ == '__main__':
    chrome_driver()
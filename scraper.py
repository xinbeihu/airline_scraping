from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.united.com'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options = chrome_options)
  return driver

if __name__ == '__main__':
  driver = get_driver()
  driver.get(url)
  print('Page title:' + driver.title)
  page_html = driver.page_source

  with open('pagesource.html','w') as f:
    f.write(page_html)
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd

class Scraper:
  def __init__(self):
    self.driver = webdriver.Edge()
    # self.driver.add_argument("start-maximized")
    # # to supress the error messages/logs
    # self.driver.add_experimental_option('excludeSwitches', ['enable-logging'])

    # self.driver = webdriver.Chrome(options=self.driver)
    
  def get_data(self):
    self.driver.get('https://www.tokopedia.com/p/komputer-laptop/aksesoris-pc-gaming/mouse-gaming?page=1&condition=2&ob=9')
    
    counter_page = 0
    datas = []

    while counter_page < 4:
      for _ in range(0, 6500, 500):
        time.sleep(0.8)
        self.driver.execute_script("window.scrollBy(0,200)")

      elements = self.driver.find_elements(by=By.CLASS_NAME, value='css-11s9vse')

      for element in elements:

        
        name = element.find_element(by=By.CLASS_NAME, value='css-20kt3o').text
        price = element.find_element(by=By.CLASS_NAME, value='css-o5uqvq').text
        linkd = element.find_element(by=By.CLASS_NAME,value="css-vbihp9")


        datas.append({
          'name': name,
          'price': price,
        
    
   
        })

      counter_page += 1
    #   next_page = self.driver.find_element(by=By.XPATH, value="//button[@aria-label='Laman berikutnya']")
      next_page = self.driver.find_element(by=By.XPATH, value="//button[@class='css-16uzo3v-unf-pagination-item' and @aria-label='Laman berikutnya']")
      next_page.click()
    
    return datas

if __name__ == '__main__':
    scraper = Scraper()
    datas = scraper.get_data()
    index = 1
    print('tes')
    for data in datas:
        print(
        index,
        data['name'],
        data['price'],
  
  
        )

        index += 1
    df = pd.DataFrame(datas)
    path = r"C:\Users\donyfajarr\Documents\Scraping\data.xlsx"
    df.to_excel(path)

    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager'
PATH = "C:\Program Files (x86)\chromedriver"

#106020
starting_num=106020

j=0

grades=[]

while j <50:
    driver = webdriver.Chrome(PATH, options=options)
    driver.set_page_load_timeout(5)

    try:
        j = j + 1
        starting_num = starting_num + 1
        driver.get("https://natega.youm7.com/")
        search = driver.find_element(By.ID, "seating_no")
        search.send_keys(str(starting_num))
        search.send_keys(Keys.RETURN)
        print(1)
        elements = driver.find_elements(By.TAG_NAME,"ul")
        print(2)
        i=0
        record={}
        for element in elements:
            body_elements=element.find_elements(By.TAG_NAME,"li")
            i=i+1
            if i==1:
                for body_element in body_elements:
                    key=body_element.find_element(By.TAG_NAME,"span")
                    value=body_element.find_element(By.TAG_NAME,"h1")
                    record[key.text]=value.text

            if i==2 or i==3 or i==4:
                for body_element in body_elements:
                    subject=body_element.find_elements(By.TAG_NAME,"span")
                    record[subject[0].text]=subject[1].text


        print(record)
        grades.append(record)

    except Exception as e:
        print(e)
        starting_num = starting_num - 1

    driver.quit()


df = pd.DataFrame(grades)
print (df)
df.to_csv(r'.\youm7.csv', index=False,encoding='utf-8-sig')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
PATH = "C:\Program Files (x86)\chromedriver"

#102300
driver = webdriver.Chrome(PATH)
starting_num=109300

j=0

grades=[]

while j <1000:
    try:
        j = j + 1
        starting_num = starting_num + 1
        driver.get("https://g12.emis.gov.eg")
        search = driver.find_element(By.ID, "SeatingNo")
        search.send_keys(str(starting_num))
        search.send_keys(Keys.RETURN)
        elements=driver.find_elements(By.TAG_NAME,"tbody")
        i=0
        record={}
        for element in elements:
            body_elements=element.find_elements(By.TAG_NAME,"tr")
            i=i+1
            if i==1:
                for body_element in body_elements:
                    key=body_element.find_element(By.TAG_NAME,"th")
                    value=body_element.find_element(By.TAG_NAME,"td")
                    record[key.text]=value.text

            if i==2:
                for body_element in body_elements:
                    subject=body_element.find_elements(By.TAG_NAME,"th")
                    record[subject[0].text]=subject[1].text


            if i==3:
                pass

                    # subject = body_element.find_elements(By.TAG_NAME, "td")
                    # print("============", key[0].text, "==========")

        print(record)
        grades.append(record)

    except Exception as e:
        print(e)
        starting_num = starting_num - 1


df = pd.DataFrame(grades)
print (df)
df.to_csv(r'.\my_data2.csv', index=False,encoding='utf-8-sig')
import pandas as pd
from selenium import webdriver
import time

#part 1 setting up table website
#part 1 setting up table website
#part 1 setting up table website


url = "https://www.tradingview.com/markets/stocks-egypt/market-movers-all-stocks/"
driver = webdriver.Chrome(executable_path="C:\\Users\\mrneg\\Desktop\\TRADELINE\\chromedriver.exe")
driver.get(url)
driver.maximize_window()
time.sleep(2)

#1st scroll
driver.execute_script("window.scrollTo(20, 5233)") 

#1st click
xpath = driver.find_element_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/button')
xpath.click()

time.sleep(2)

#2nd click and scroll
driver.execute_script("window.scrollTo(20, 10233)") 
xpath.click()

time.sleep(3)
#part 2 setting up scrape
#part 2 setting up scrape
#part 2 setting up scrape

stock_names = driver.find_elements_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[1]/span/sup')
stock_symbols = driver.find_elements_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[1]/span/a')
percentage_change = driver.find_elements_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[3]/span')
technical_rating = driver.find_elements_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[5]/div')
price_earning = driver.find_elements_by_xpath('//*[@id="js-category-content"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[9]')

stocks_result = []
for i in range(len(stock_names)):
    temporary_data = {'Stock Symbol': stock_symbols[i].text,
                      'Stock Name': stock_names[i].text,
                      '% Change': percentage_change[i].text,
                      'Technical Rating': technical_rating[i].text,
                      'P/E': price_earning[i].text}
    stocks_result.append(temporary_data)


#C:\\Users\\mrneg\\Desktop\\TRADELINE\\driver\\chromedriver.exe
writer = pd.ExcelWriter('C:\\Users\\mrneg\\Desktop\\TRADELINE\\tradeline.xlsx')

dataframe_data = pd.DataFrame(stocks_result)
dataframe_data.to_excel(writer, "stocks", index = False)

writer.close()
#dataframe_data.to_excel("stocks_result.xlsx", index= False)
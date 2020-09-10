from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://hcs.eduro.go.kr')

driver.find_element_by_xpath('//*[@id="secondaryPwForm"]/table/tbody/tr/td/input').send_keys("1234")
driver.find_element_by_id("btnConfirm").click()

for i in range(1,3,1):
      tmp = '//*[@id="container"]/div[2]/section[2]/div[2]/ul/li[' + str(i) +']'
      '''
      xpath 형식 //*[@id="container"]/div[2]/section[2]/div[2]/ul/li[1]
      '''
      driver.find_element_by_xpath(tmp).click()

      driver.find_element_by_id("survey_q1a1").click()
      driver.find_element_by_id("survey_q2a1").click()
      driver.find_element_by_id("survey_q3a1").click()
      driver.find_element_by_id("survey_q4a1").click()
      driver.find_element_by_id("survey_q5a1").click()

      driver.find_element_by_id("btnConfirm").click()

      driver.find_element_by_xpath('//*[@id="container"]/div[1]/ul/li/a').click()
      time.sleep(5)

#finish
driver.close()





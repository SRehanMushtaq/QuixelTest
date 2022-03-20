#Task 6
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome('C:/Users/Nova/Desktop/FrameWork Update 15 feb 2020/Drivers/chromedriver')# to maximize the browser window
driver.maximize_window()
driver.get("https://quixel.com/")
driver.implicitly_wait(5)

Cookies=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button').click()
newsetter=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button').click()
Sign_in=driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[2]/nav/ul/div[6]').click()

Email=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/form/div/div[3]/div[1]/div/label/div[2]/input').send_keys("rayhan.mushtaq94@gmail.com")
Password=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/form/div/div[3]/div[2]/div/label/div[2]/input").send_keys("Fa14bcs123")
Signin_button=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/form/div/div[6]/span/span/button").click()
driver.implicitly_wait(5)
Subscribe=driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[3]/div/span/div[1]/span/span/a').click()
BeginFree=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/section/div[2]/div[1]/span/span/a').click()
megascans=driver.get("https://quixel.com/megascans/home")
free=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/ul/li[4]/a/div/div/span[2]/div').click()
decals=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/ul/li[4]/div/div/div[2]/ul/li[4]/a/div').click()
street=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/ul/li[4]/div/div/div[2]/ul/li[4]/div/div/div/ul/li[4]/a/div').click()
Round_drain_Cover=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/section[2]/div/div[1]/div[3]/a/span/div/div").click()
scroll_2=driver.find_element_by_css_selector('#app-page > div > div.rightSidebar___19qxV > div > div.css-qzm2xd > div > div > div > div.assetFooterContainer___1zaZZ > div:nth-child(2) > div > button')
driver.execute_script("arguments[0].scrollIntoView();",scroll_2)
Resolution=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div").click()
ChangingResolution=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/ul/li[1]/button').click()

download=driver.find_element_by_css_selector('#app-page > div > div.rightSidebar___19qxV > div > div.css-qzm2xd > div > div > div > div.assetFooterContainer___1zaZZ > div:nth-child(2) > div > button').click()

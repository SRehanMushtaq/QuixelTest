from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys

driver = webdriver.Chrome('C:/Users/Nova/Desktop/FrameWork Update 15 feb 2020/Drivers/chromedriver')# to maximize the browser window
driver.maximize_window()
megascans=driver.get("https://quixel.com/megascans/home")
driver.implicitly_wait(5)
free=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/ul/li[4]/a/div/div/span[2]/div').click()
Color_filter=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div[2]/div[5]/div/button/div').click()
Gray=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div[2]/div[5]/div/div/ul/li[5]/button').click()
Cookies=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button').click()
newsetter=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button').click()
search_click=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/div/input').click()
searching_asset=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/div/input').send_keys("SiEoZ")
search_enter=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)
Huge_icelandic=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/section[2]/div/div[1]/div/a/span/div/div').click()
Signin_download=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()
driver.implicitly_wait(5)

Email=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div/div[3]/div[1]/div/label/div[2]/input').send_keys("rayhan.mushtaq94@gmail.com")
Password=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/div/div[3]/div[2]/div/label/div[2]/input").send_keys("Fa14bcs123")

signin_button=driver.find_element_by_css_selector('#react-app > div > div > div > form > div > div.css-12hscl1 > span > span > button').click()
download=driver.find_element_by_css_selector('#app-page > div > div.rightSidebar___19qxV > div > div.css-qzm2xd > div > div > div > div.assetFooterContainer___1zaZZ > div:nth-child(2) > div > button').click()
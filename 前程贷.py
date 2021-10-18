from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get(r'http://8.129.91.152:8765/ ')
# driver.maximize_window() #窗口化
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element_by_xpath('//*[@class="no-border special-color"]').click()
driver.find_element_by_xpath('//*[@class="form-control reg-mobile phoneNum"]').send_keys('13821349125')

time.sleep(15)
driver.find_element_by_xpath('//*[@class="btn btn-success left reget-mobileCode"]').click()
time.sleep(1)

text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
aaa = str[len(str)-4:]

driver.find_element_by_xpath('//*[@name="code"]').send_keys(aaa)

driver.find_element_by_xpath('//*[@type="password"]').send_keys('qwer1234')
driver.find_element_by_xpath('//*[@name="agree"]').click()
driver.find_element_by_xpath('//*[@class="btn btn-special"]').click()

time.sleep(5)
# driver.close()
driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()  #系统自动分配


time.sleep(5)
driver.find_element_by_xpath("//*[@src = '/Public/frontend/images/personal_center/identity_iden_no.png' and @title='实名认证']").click()

driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/ul/li[4]/a').click()


driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[1]/input').send_keys('qwer1234') #原始密码
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[2]/input').send_keys('qwe12344') #新密码
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[3]/input').send_keys('qwe12344') #确认新密码

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[5]/button[1]').click()  #点击确定

# driver.quit()  #退出系统
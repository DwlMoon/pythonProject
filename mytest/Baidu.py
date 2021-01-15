import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 定义chromedriver驱动的位置
chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址

# 打开一个浏览器窗口
driver = webdriver.Chrome(chromedriver)

# 设置浏览器需要打开的url
url = "https://live.aliexpress.com/livebackend/liveRoomList.htm?spm=a2g0t.10516576.0.0.9de8450c7WhQZ3"
# url = "https://login.aliexpress.com/"
# 发送请求
driver.get(url)

time.sleep(1)


driver.find_element_by_id("fm-login-id").send_keys("ivonnevelenosi@gmail.com")
time.sleep(2)
driver.find_element_by_id("fm-login-password").send_keys("826010")
time.sleep(2)
driver.find_element_by_class_name('fm-button').click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/button').click()
print("登录成功")
print("============================================================")
time.sleep(3)
#
need_day = [  '2020-11-05', '2020-11-06',
             '2020-11-07', '2020-11-08',
             '2020-11-09', '2020-11-10', '2020-11-11', '2020-11-12']

# need_day = [
#             '2020-11-10', '2020-11-11', '2020-11-12']

# need_day = ['2020-10-27']
need_time = [ '11:00:00', '13:00:00', '25:00:00']
sum=1
for myday in need_day:
    for mytime in need_time:
        try:

            # search_window = driver.current_window_handle
            # driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            driver.find_element_by_id("create_btn").click()
            print("创建第%s个直播间"%sum)
            time.sleep(2)


            driver.find_element_by_id("title").send_keys("1")
            # time.sleep(1)
            driver.find_element_by_id("desc").send_keys("1")
            # time.sleep(1)

            # 设置日期
            driver.find_element_by_xpath('//*[@id="startTime"]/div/span/input').click()
            time.sleep(1)

            hour=driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/span[1]/input')
            hour.send_keys(Keys.CONTROL, 'a')
            hour.send_keys(myday)
            time.sleep(1)

            second=driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/span[2]/input')
            second.send_keys(Keys.CONTROL, 'a')
            second.send_keys(mytime)
            driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
            time.sleep(1)

            # 设置语言
            driver.find_element_by_id("lang").click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[8]/ul/li[1]').click()
            time.sleep(1)

            # 设置国家
            driver.find_element_by_id("country").click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[9]/ul/li[1]').click()
            time.sleep(2)


            # 第一张照片
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[1]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[1]/div[1]/input').send_keys(r'E:\1.jpg')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
            time.sleep(2)

            # 第二张图片
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[2]/div[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[2]/div[1]/input').send_keys(r'E:\2.jpg')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
            time.sleep(2)

            # 第三张图片
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[3]/div[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[3]/div[1]/input').send_keys(r'E:\1.jpg')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="root"]/div/form/div[9]/div/button').click()

            # driver.find_element_by_class_name('next-btn next-medium next-btn-primary margin-right-10px').click()

            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/button').click()
            print("创建成功")
            time.sleep(2)


            driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[3]/button[1]').click()
            print("激活成功")
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="nav"]/li[1]').click()
            print("============================================================")

            time.sleep(2)
        except EOFError as error:
            print("**************错误信息***************")
            print(error)
            print(myday)
            print(mytime)
            print("***********************************")
        sum=sum+1


# 关闭浏览器
# driver.quit()
#
# 关闭窗口
# driver.close()

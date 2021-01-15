import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

from mytest import rememberRoomId
from mytest import ReadExcel
import os


# 创建直播间
class createliving:

    flagabc=0

    def __getattribute__(obj: str):
        if obj == "url":
            return str("https://live.aliexpress.com/livebackend/liveRoomList.htm?spm=a2g0t.10516576.0.0.9de8450c7WhQZ3")

        elif obj == "need_day":
            return ['2020-10-28', '2020-10-29', '2020-10-30', '2020-10-31',
                    '2020-11-01', '2020-11-02', '2020-11-03', '2020-11-04',
                    '2020-11-05', '2020-11-06', '2020-11-07', '2020-11-08',
                    '2020-11-09', '2020-11-10', '2020-11-11']

        elif obj == "need_time":
            return ['15:00:00','17:00:00','19:00:00', '21:00:00']

    # 获取驱动
    def loginLivingRoom(self):
        chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        # 打开一个浏览器窗口
        driver = webdriver.Chrome(chromedriver)
        driver.implicitly_wait(10)
        return driver

    # 登录页面
    def login(self, acount, password):

        driver = createliving.loginLivingRoom(None)

        driver.get(createliving.__getattribute__("url"))

        # 登录
        driver.find_element_by_id("fm-login-id").send_keys(acount)
        time.sleep(2)
        driver.find_element_by_id("fm-login-password").send_keys(password)
        time.sleep(2)
        driver.find_element_by_class_name('fm-button').click()
        print("登录成功")
        print("============================================================")
        time.sleep(3)
        return driver


    # 创建直播间
    def createLivingRoom(self, acount, password, excel):

        driver=createliving.login(None,acount,password)

        sum = 1
        for myday in createliving.__getattribute__("need_day"):
            if sum < 60:

                for mytime in createliving.__getattribute__("need_time"):
                    try:

                        driver.find_element_by_id("create_btn").click()
                        print("%s 创建第 %s 个直播间 , 创建时间为 ： %s %s" % (acount, sum, myday, mytime))

                        driver.find_element_by_id("title").send_keys(random.randint(1, 100))
                        driver.find_element_by_id("desc").send_keys(random.randint(1, 100))

                        # 设置日期
                        driver.find_element_by_xpath('//*[@id="startTime"]/div/span/input').click()

                        hour = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/span[1]/input')
                        hour.send_keys(Keys.CONTROL, 'a')
                        hour.send_keys(myday)

                        second = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/span[2]/input')
                        second.send_keys(Keys.CONTROL, 'a')
                        second.send_keys(mytime)
                        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()

                        # 设置语言
                        driver.find_element_by_id("lang").click()
                        driver.find_element_by_xpath('/html/body/div[8]/ul/li[1]').click()

                        # 设置国家
                        driver.find_element_by_id("country").click()
                        driver.find_element_by_xpath('/html/body/div[9]/ul/li[1]').click()

                        curPath = os.path.realpath(os.path.dirname(__file__))
                        rootPath = curPath[:curPath.find("pythonProject\\") + len("pythonProject\\")]
                        firstPic =   rootPath + 'images\\1.jpg'
                        fpic=firstPic.replace("\\","/")
                        # print("第一张照片的地址为 : %s"%fpic)
                        secondPic =   rootPath + 'images\\2.jpg'
                        spic=secondPic.replace("\\","/")
                        # print("第二张照片的地址为 : %s"%spic)

                        # 第一张照片
                        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[1]/div[1]').click()
                        # time.sleep(2)
                        driver.find_element_by_xpath(
                            '//*[@id="root"]/div/form/div[6]/div[2]/div[1]/div[1]/input').send_keys(r'E:\pythonProject\images\1.jpg')
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
                        time.sleep(2)

                        # 第二张图片
                        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[2]/div[1]/div').click()
                        # time.sleep(2)
                        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[2]/div[1]/input').send_keys(spic)
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
                        time.sleep(2)

                        # 第三张图片
                        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[6]/div[2]/div[3]/div[1]').click()
                        # time.sleep(2)
                        driver.find_element_by_xpath(
                            '//*[@id="root"]/div/form/div[6]/div[2]/div[3]/div[1]/input').send_keys(fpic)
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[1]').click()
                        time.sleep(3)

                        driver.find_element_by_xpath('//*[@id="root"]/div/form/div[9]/div/button').click()

                        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/button').click()
                        print("创建成功")

                        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[3]/button[1]').click()
                        print("激活成功")

                        driver.find_element_by_xpath('//*[@id="nav"]/li[1]').click()

                        roomId=rememberRoomId.rememberRoomId.rememberLivingId(None,driver)
                        if roomId is not None:
                            if createliving.flagabc==0:
                                createliving.flagabc=1
                                ReadExcel.ReadExcel.write_excel(None,acount,excel)
                        ReadExcel.ReadExcel.write_excel(None, roomId,excel)

                        print("============================================================")
                        time.sleep(2)
                    except EOFError as error:
                        WebDriverWait(  driver,  20,  poll_frequency=1,  ignored_exceptions=AttributeError  ) \
                            .until(createliving.cathException(None,acount,myday,mytime,error))
                        continue


                    except Exception as e:
                        WebDriverWait(  driver,  20,  poll_frequency=1,  ignored_exceptions=Exception  )\
                            .until(createliving.cathException(None,acount,myday,mytime,e))
                        continue

                    sum = sum + 1

        createliving.flagabc = 0
        return 'success'

    # 错误和异常信息打印类
    def cathException(self,acount, myday, mytime,e):
        print("**************异常信息***************")
        print("账号为： %s 在创建 %s %s 时失败" % (acount, myday, mytime))
        print(e)
        print("***********************************")
        print("============================================================")





if __name__ == '__main__':
    # curPath = os.path.realpath(os.path.dirname(__file__))
    # rootPath = curPath[:curPath.find("pythonProject\\") + len("pythonProject\\")]
    # print("==============================")
    # firstPic =  rootPath + 'images\\1.jpg'
    # print(firstPic.replace("\\","/"))
    # print(firstPic)
    print(random.randint(1, 100))


from mytest import CreateLiving
import time


class rememberRoomId:

    # 记录账号
    def rememberLivingId(self,driver):

        # driver=CreateLiving.createliving.login(None, 'pedraamjbranco@gmail.com', '098ali')

        ul = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/ul')
        lis = ul.find_elements_by_tag_name('div')
        if len(lis)>0:
            value = str(lis[0].get_attribute("id"))
            print("创建的房间号为 : %s"%value[17:])
            return value[17:]
        else:
            return None



if __name__ == '__main__':
    # a=str("room_list_item_id8000000915723383")
    # var = a[17:]
    # print(var)
    rememberRoomId.rememberLivingId(None)

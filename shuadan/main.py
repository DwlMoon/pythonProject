import json
import threading
from time import sleep
from pip._vendor import requests

from shuadan import global_config
from selenium import webdriver

from shuadan import user_data


def create_profile(index, host, port):
    create_url = f"{global_config.base_url}{global_config.api_v2}{global_config.parameter_profile}"

    body = {
        "name": f"{global_config.profile_name}{index}",
        "browser": "mimic",
        "os": "win",
        "group": "de2b0291-158a-450d-b23b-be627746e707",
        "notes": f"{global_config.profile_name}{index}",
        "googleServices": True,
        "network": {
            "proxy": {
                    "type": "HTTP",
                    "host": host,
                    "port": port
                }
        }
    }

    my_header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    resp = requests.post(create_url, json.dumps(body), headers=my_header)

    code = resp.status_code
    print(f"---get_profile---status_code={code}")

    if 200 == code:
        json_data = resp.content
        print(f"---get_profile---json_data={json_data}")
    else:
        json_data = resp.content
        print(f"---get_profile---json_data={json_data}")
        pass


def get_profile_s():
    get_url = f"{global_config.base_url}{global_config.api_v2}{global_config.parameter_profile}"
    print(f"---get_profile={get_profile}")

    my_header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        resp = requests.get(get_url, headers=my_header)

        code = resp.status_code
        print(f"---get_profile---status_code={code}")

        if 200 == code:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")

            profile_list = json.loads(json_data)
        else:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")
            pass
    except Exception as e:
        print(f"---get_profile---e={e}")


def get_profile_list():
    get_url = f"{global_config.base_url}{global_config.api_v2}{global_config.parameter_profile}"
    print(f"---get_profile={get_profile}")

    my_header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        resp = requests.get(get_url, headers=my_header)

        code = resp.status_code
        print(f"---get_profile---status_code={code}")

        if 200 == code:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")

            profile_list = json.loads(json_data)

            for profile_item in profile_list:
                item_name = profile_item['name']
                # if item_name == "profile_0" or item_name == "profile_1" or item_name == "profile_2" or item_name == "profile_3" or item_name == "profile_4" or item_name == "profile_5" or item_name == "profile_6" or item_name == "profile_7" or item_name == "profile_8" or item_name == "profile_9":
                item_uuid = profile_item['uuid']
                print(f"---item_uuid={item_uuid}")

                user_data_str = user_data.user_data[item_name]

                user_account = user_data_str.split(":")[0]
                user_pwd = user_data_str.split(":")[1]

                sleep(15)

                t1 = threading.Thread(target=start_profiles, args=[item_uuid, user_account, user_pwd])
                t1.start()

        else:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")
            pass
    except Exception as e:
        print(f"---get_profile---e={e}")


def get_profile(group_zh):
    get_url = f"{global_config.base_url}{global_config.api_v2}{global_config.parameter_profile}"
    print(f"---get_profile={get_profile}")

    my_header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        resp = requests.get(get_url, headers=my_header)

        code = resp.status_code
        print(f"---get_profile---status_code={code}")

        if 200 == code:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")
            profile_list = json.loads(json_data)

            for profile_item in profile_list:
                item_group = profile_item['group']
                if group_zh == item_group:
                    item_uuid = profile_item['uuid']
                    print(f"---item_uuid={item_uuid}")
                    # sleep(10)
                    # other_t = OtherTaskThread(start_profile(item_uuid))
                    # other_t.start()

                    t1 = threading.Thread(target=start_profile, args=(item_uuid,))
                    t1.start()

        else:
            json_data = resp.content
            print(f"---get_profile---json_data={json_data}")
            pass
    except Exception as e:
        print(f"---get_profile---e={e}")


def start_profile(profile_id):
    try:
        start_url = f"{global_config.base_url}{global_config.api_v1}{global_config.parameter_profile}/{global_config.start_profile}?automation=true&profileId={profile_id}"
        print(f"---start_profile={start_url}")

        resp = requests.get(start_url)

        code = resp.status_code
        print(f"---start_profile---status_code={code}")

        if 200 == code:
            json_data = resp.content
            print(f"---start_profile---json_data={json_data}")

            json_str = json.loads(json_data)
            print(f"---start_profile---json_str={json_str}")

            web_driver = webdriver.Remote(command_executor=json_str['value'])
            web_driver.get(global_config.ali_login_url)

            web_driver.find_element_by_id("fm-login-id").send_keys("rosakimika@gmail.com")
            sleep(2)
            web_driver.find_element_by_id("fm-login-password").send_keys("goiaba")
            sleep(2)
            web_driver.find_element_by_class_name('fm-button').click()

            web_driver.implicitly_wait(20)

            web_driver.get(global_config.live_url)

        else:
            json_data = resp.content
            print(f"---start_profile---json_data={json_data}")
            pass
    except Exception as e:
        print(f"---start_profile---e={e}")


def start_profiles(profile_id, user_account, user_pwd):
    try:
        start_url = f"{global_config.base_url}{global_config.api_v1}{global_config.parameter_profile}/{global_config.start_profile}?automation=true&profileId={profile_id}"
        print(f"---start_profile={start_url}")

        resp = requests.get(start_url)

        code = resp.status_code
        print(f"---start_profile---status_code={code}")

        if 200 == code:
            json_data = resp.content
            print(f"---start_profile---json_data={json_data}")

            json_str = json.loads(json_data)
            print(f"---start_profile---json_str={json_str}")

            web_driver = webdriver.Remote(command_executor=json_str['value'])

            web_driver.implicitly_wait(20)

            web_driver.get(global_config.ali_login_url)

            web_driver.find_element_by_id("fm-login-id").send_keys(user_account)
            sleep(2)
            web_driver.find_element_by_id("fm-login-password").send_keys(user_pwd)
            sleep(2)
            web_driver.find_element_by_class_name('fm-button').click()

            sleep(5)

            try:
                web_driver.get(global_config.live_url_1)
                sleep(4)
                # btn = web_driver.find_element_by_xpath("//*[@id=\"J_prismPlayer\"]/div/div[2]/button[2]")

                btn = web_driver.find_element_by_class_name('vjs-center-start vjs-button')
                btn.click()
            except Exception as e:
                print("---operation_web--Exception={}".format(e))

            try:
                sleep(4)
                new_2 = "window.open('{}');".format(global_config.live_url_2)
                # new_2 = "window.open('https://live.aliexpress.com/live/live.htm?liveId=50475461165016&tracelog=2535226016');"
                web_driver.execute_script(new_2)
                sleep(4)
                btn = web_driver.find_element_by_xpath("//*[@id=\"J_prismPlayer\"]/div/div[2]/button[2]")
                btn.click()
            except Exception as e:
                print("---operation_web--Exception={}".format(e))

            try:
                sleep(4)
                new_3 = "window.open('{}');".format(global_config.live_url_3)
                # new_3 = "window.open('https://live.aliexpress.com/live/live.htm?liveId=8000001072037759&tracelog=2532584759');"
                web_driver.execute_script(new_3)
                sleep(4)
                btn = web_driver.find_element_by_xpath("//*[@id=\"J_prismPlayer\"]/div/div[2]/button[2]")
                btn.click()
            except Exception as e:
                print("---operation_web--Exception={}".format(e))

            # try:
            #     sleep(4)
            #     # new_4 = "window.open('{}');".format(global_config.live_url_4)
            #     new_4 = "window.open('https://live.aliexpress.com/live/live.htm?liveId=8000000876817220&tracelog=2536665220');"
            #     web_driver.execute_script(new_4)
            #     # sleep(4)
            #     # btn = web_driver.find_element_by_xpath("//*[@id=\"J_prismPlayer\"]/div/div[2]/button[2]")
            #     # btn.click()
            # except Exception as e:
            #     print("---operation_web--Exception={}".format(e))

            # try:
            #     sleep(4)
            #     new_5 = "window.open('{}');".format(global_config.live_url_5)
            #     web_driver.execute_script(new_5)
            #     # sleep(4)
            #     #
            #     # btn = web_driver.find_element_by_xpath("//*[@id=\"J_prismPlayer\"]/div/div[2]/button[2]")
            #     # btn.click()
            # except Exception as e:
            #     print("---operation_web--Exception={}".format(e))

        else:
            json_data = resp.content
            print(f"---start_profile---json_data={json_data}")
            pass
    except Exception as e:
        print(f"---start_profile---e={e}")


if __name__ == '__main__':
    # get_profile_list()
    # pass
    print('a' or 5)


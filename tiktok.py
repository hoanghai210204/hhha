
# import random, os, subprocess
# from re import sub
# os.chdir('D:\Microvirt\MEmu')
# # os.chdir('C:\\Users\\Baodt\\Downloads\\Panda\\Panda')
# # sdt=random.choice([line.rstrip('\n') for line in open("data\\dau_so\\%s.txt"%("Vietnam"))])+str(random.randint(1000000, 9999999))
# # manufacturer = random.choice([line.rstrip('\n') for line in open("infoLD\\Manufacturer.txt",'r') ])
# # model=random.choice([line.rstrip('\n') for line in open("infoLD\\Mamay.txt",'r') ]).replace(" ","_")
# # print(sdt, manufacturer, model)
# # subprocess.check_output("adb kill-server")
# subprocess.check_call("memuc -i 0 adb shell") #connect adb devices
# subprocess.check_call('memuc getappinfolist -i 0')
import os

try:
    import threading
    import requests, time
    from lxml import html
except:
    os.system("pip install requests")
    os.system("pip install lxml")
    print("__________Vui lòng chạy lại tool__________")
    quit()
class TikTok:
    def __init__(self, user, pwd, cookie):
        self.user = user
        self.pwd = pwd
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'Connection': 'keep-alive',
            "Cookie": cookie,
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
    def getUser(self):
        access = requests.get("https://www.tiktok.com/", headers=self.headers).text
        if "profile-icon" not in access:
            return "cookie_die"
        return access.split('"uniqueId":"')[1].split('","createTime"')[0]
    def datnick(self):
        p = html.fromstring(s.get("https://traodoisub.com/view/chtiktok/", cookies=self.cookietds).content)
        username = []
        o = p.xpath('//a[@target="_blank"]')
        for p in range(5):
            o.pop(0)
        for y in o:
            username.append({"id":y.text,"username":y.attrib['href'].replace("https://www.tiktok.com/@","")})
        username_tikok = self.getUser()
        for n in username:
            if n["username"] == username_tikok:
                datnick = s.post("https://traodoisub.com/scr/tiktok_datnick.php", data=f'iddat={n["id"]}', cookies=self.cookietds).text
                if datnick == "1" or datnick == 1:
                    print("Đặt nick", n["username"], "thành công")
                    return "datnick_success", username_tikok
                else:
                    return "datnick_fail", username_tikok
    def run_tds(self):
        if self.getUser() == "cookie_die":
            print(f"Cookie Die {self.user}")
            return
        job = 0
        global s
        s = requests.session()
        s.headers.update({"content-type":"application/x-www-form-urlencoded; charset=UTF-8"})
        self.cookietds = s.post("https://traodoisub.com/scr/login.php", data={"username": self.user, "password": self.pwd}).cookies
        check_dat, username = self.datnick()
        if check_dat == "datnick_fail":
            print("Vui lòng cấu hình acc:",username)
            return
        # while True:
        check_pause = 0
        while (check_pause < 9):
            load = s.get("https://traodoisub.com/ex/tiktok_follow/load.php", cookies=self.cookietds).json()
            if 'time_reset' in load:
                print("Block")
                return
            if "countdown" in load:
                time.sleep(3)
                continue
            if load["cache"] >= 8:
                check_pause = 0
                time.sleep(2)
                nhan = s.post("https://traodoisub.com/ex/tiktok_follow/nhantien.php",data="key=0257272C744254", cookies=self.cookietds).json()
                print(nhan)
                load = s.get("https://traodoisub.com/ex/tiktok_follow/load.php", cookies=self.cookietds).json()
                if "countdown" in load:
                    time.sleep(3)
                    continue
            if len(load["data"]) == 0:
                print("Hết Job", end=" \r")
                continue
            id = load["data"][0]["id"]
            link  = load["data"][0]["link"].split('@')[1]
            try:
                response = requests.get('https://www.tiktok.com/@'+link, headers=self.headers).text
                user_id = response.split(',"authorId":"')[1].split('","authorSecId"')[0]
                sec_id = response.split('"authorSecId":"')[1].split('","avatarThumb"')[0]
                device_id = response.split('"userId":"')[1].split('"')[0]
                response = requests.post(f'https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id={device_id}&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=2&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1360&sec_user_id={sec_id}&type=1&tz_name=Asia%2FSaigon&user_id={user_id}&webcast_language=vi-VN', headers=self.headers).text
                # print(response)
                # response = requests.post(f'https://us.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id={device_id}&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1366&sec_user_id={sec_id}&type=1&tz_name=Asia/Saigon&user_id={user_id}&verifyFp=verify_l67wkm1i_d0xHCABM_uede_4mm8_BmEv_kqpW93gMkY6h&webcast_language=vi-VN&msToken=joulWM7bAYm0lFUf8SWrKyPjpqTxnKFdwkhHMKomj_Ji3WukhG0S3JfJ9BcvKhFn5xU95yYI0hoRFMbkzQf0vHESU_cQFA6QFjAgrCa7KQ_8Nr95cYNnMbGZTc0RREisJY40wDXBw-vDkoXH&X-Bogus=DFSzswVYff0ANjulSX4DSsXyYJlW&_signature=_02B4Z6wo00001QTWiPAAAIDAJ3emXSqSICUE1oxAACPT3b', headers=headers).text
                response = html.fromstring(requests.get('https://www.tiktok.com/@'+link, headers=self.headers).content)

                check = response.xpath('//button[text()="Follow"]')
                if check == []:
                    check_pause += 1
                    job += 1
                    print(job, "Follow Success: "+link)
            except:
                print("Lỗi cc gì thế", end=" \r")
            time.sleep(5)
            cache = s.post("https://traodoisub.com/ex/tiktok_follow/cache.php",data="id="+id+"&type=follow", cookies=self.cookietds).json()
        time.sleep(2)
        nhan = s.post("https://traodoisub.com/ex/tiktok_follow/nhantien.php",data="key=0257272C744254", cookies=self.cookietds).json()
        if "Nhận thành công 0 xu" in nhan['msg']:
            print("Block")
            return
        print(nhan)
        time.sleep(5)
def main(user, pwd):
    while True:
        file = open(f"cookietiktok{user}.txt").readlines()
        for cookie in file:
            run = TikTok(user, pwd, cookie.strip())
            run.run_tds()
if os.path.exists('acctds.txt') == False:
    soluong_acc_tds = int(input(f"Nhập số tài khoản TDS muốn chạy: "))
    for i in range(1, soluong_acc_tds + 1):
        userandpwd = input(f"Tài Khoản và mật khẩu (taikhoan|matkhau) {i}: ")
        with open("acctds.txt", "a+") as file_cookie:
            file_cookie.write(userandpwd+"\n")
file_acc = open('acctds.txt').readlines()
for full in file_acc:
    acc = full.strip().split("|")
    if os.path.exists(f'cookietiktok{acc[0]}.txt') == False:
        soluong_cookie = int(input(f"Nhập số cookie muốn chạy user({acc[0]}): "))
        for i in range(1, soluong_cookie + 1):
            cookie = input(f"Cookie({acc[0]}) acc {i}: ")
            with open(f"cookietiktok{acc[0]}.txt", "a+") as file_cookie:
                file_cookie.write(cookie+"\n")
for full in file_acc:
    threading.Thread(target=main, args=(acc[0], acc[1], )).start()


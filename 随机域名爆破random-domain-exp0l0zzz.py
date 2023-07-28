import random
import string
import requests
from pypinyin import pinyin, Style


# a = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
# a = random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',5)

# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
# print(ran_str)

#string.ascii_letters 大小写字母
#string.digits 数字
#string.lowercase 小写字母

# def generate_random_char():
#     return ''.join(random.sample(string.ascii_lowercase + string.digits+"-", 6))

#写了一个函数去生成随机字符
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# 把域名和随机字符拼接一起爆破
def random_target(length):
    url = "tower0788.cn"
    while True:
        random_string = generate_random_string(length)
        target = "https://"+random_string+'.'+url
        try:
            req = requests.get(url=target,verify=False)
            if req.status_code == 200:
                print("[+] "+target)
        except requests.exceptions.ConnectionError as e:
                print(target)

if __name__=='__main__':
    random_target(5)

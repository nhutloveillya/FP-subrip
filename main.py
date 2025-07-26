import requests
import urllib.parse
import os

def num3tostr(num3):
    str3 = str(int(num3))
    if len(str3) == 1:
        return f'00{str3}'
    if len(str3) == 2:
        return f'0{str3}'
    if len(str3) == 3:
        return str3

def num2tostr(num2):
    str2 = str(int(num2))
    if len(str2) == 1:
        return f'0{str2}'
    if len(str2) == 2:
        return str2

current_path = os.getcwd()
paths = f'{current_path}\log.txt'

yup     = input("Uploads Year = ")
mon     = int(input("Uploads Month = "))
name    = input("Movie Name = ")
yprd    = input("Movie Produce Year = ")
lang    = input("Orginal Language = ")
eps     = int(input("Amount of Episode = "))
save    = input("Save dir = ")

link = 'http://fsub.fptplay.net.vn/OTT/'
montest = num2tostr(mon)
epi = num3tostr(1)
    
for i in range(int(eps)):
    k = True
    while k == True:
        try:
            url=f'{link}{yup}/{montest}/{name}_{yprd}_{lang}_{epi}.vie.vtt'
            req = requests.get(url)
            req.raise_for_status()
            urlp=url.split('/')
            fname=urlp[-1]
            path = f"{save}\{name}\{fname}"
            os.makedirs(f'{save}\{name}', exist_ok=True)
            with open(path, 'wb') as f:
                f.write(req.content)
            k = False
            print(f'Download completed {fname}')
        except:
            montest = num2tostr(int(montest)+1)    
    epi = num3tostr(int(epi)+1)


end=input('Press any button to end programe')

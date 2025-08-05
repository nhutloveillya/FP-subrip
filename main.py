import requests
import os
import argparse

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


def subdl(yup, mon, name, yprd, lang, eps, save): 
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
                path = f"{save}\\{name}\\{fname}"
                os.makedirs(f'{save}\\{name}', exist_ok=True)
                with open(path, 'wb') as f:
                    f.write(req.content)
                k = False
                print(f'Download completed {fname}')
            except:
                montest = num2tostr(int(montest)+1)    
        epi = num3tostr(int(epi)+1)

def getsubdll(yup, mon, name, yprd, lang, eps): 
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
                print(f'sub DLL of {name} ep {epi}: {url}')
                k = False
            except:
                montest = num2tostr(int(montest)+1)    
        epi = num3tostr(int(epi)+1)

def parselink(u):
    u=1


def main():
    parser = argparse.ArgumentParser(description='Download FPT Play subtitles.')
    parser.add_argument('-y', type=str, required=True, help='Year of the upload (YYYY)')
    parser.add_argument('-m', type=int, required=True, help='First month of the upload (1-12)')
    parser.add_argument('-n', type=str, required=True, help='Name of the series')
    parser.add_argument('-yp', type=str, required=True, help='Year production (YYYY)')
    parser.add_argument('-l', type=str, required=True, help='Language of series (e.g., "JP", "EN")')
    parser.add_argument('-e', type=int, required=True, help='Number of episodes you want to download')
    parser.add_argument('-s', type=str, required=True, help='Directory to save subtitles')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('cmd', choices=['dl', 'dll'], help='Command to execute: "dl" for download, "dll" for print links')

    args = parser.parse_args()
    if args.cmd == 'dll':
        getsubdll(args.y, args.m, args.n, args.yp, args.l, args.e)
    if args.cmd == 'dl':
        subdl(args.y, args.m, args.n, args.yp, args.l, args.e, args.s)

if __name__ == "__main__":
    main()
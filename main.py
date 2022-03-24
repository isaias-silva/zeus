
from ascii import *

def main():
  
    print(logo())
    while(1):
        print(menu())
        comand=input("comando:")
        if comand=='1':
            alvo=input('alvo:')

        if comand=='0':
            print("bye!")
            break
        if comand=='9':
    
            print(aviso("desenvolvido por Zackblack \n https://www.youtube.com/channel/UCwge2yJbcX5DdFPWpLCtvCw","Zeus 1.0"))
        else:
            print('comando invalido')   
main()
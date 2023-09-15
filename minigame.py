import random, os, json, sys
from time import sleep

file = "account.json"
def show_banner():
  banner=f"""
    \033[1;34m╔═══════════════╗
    \033[1;34m║\033[1;32m   Minigames\033[1;34m   ║
    \033[1;34m║\033[1;33m 1.CSMM\033[1;34m        ║
    \033[1;34m║\033[1;35m 2.CLS DATA\033[1;34m    ║
    \033[1;34m║\033[1;36m 3.ADD COIN\033[1;34m    ║
    \033[1;34m╚═══════════════╝\033[1;37m
  """
  print(banner)
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def dang_ky():
  if not os.path.isfile(file):
    print("\033[1;34mCreate Account\033[1;37m")
    username = input("\033[1;37mAccount: ")
    data = [
      {"username": username, "money": 2000}
    ]
    print("\033[1;37m[+2000 Xu] \033[1;32mSuccess\033[1;37m")
    with open(file, 'w') as f:
        json.dump(data, f)
    exit()
def account():
    with open(file, 'r') as f:
      data = json.load(f)
    username = data[0]["username"]
    money = data[0]["money"]
    print(f"\033[1;37mAccount: \033[1;35m{username}\033[1;37m")
    print(f"Money: {money} \033[1;33mXu\033[1;37m")
    return money
def tra_du_lieu():
  with open(file, 'r') as f:
      data = json.load(f)
  username = data[0]["username"]
  money = data[0]["money"]
  return money
def load_data():
    with open(file, "r") as f:
        data = json.load(f)
    return data[0]["username"], data[0]["money"]
def save_data(username, money):
    data = [
      {"username": username,"money":money}
    ]
    with open(file, "w") as f:
        json.dump(data, f)
def change_money(amount):
    name, money = load_data()
    new_money = money + amount
    save_data(name, new_money)
def hien_money():
  with open(file, 'r') as f:
      data = json.load(f)
  money = data[0]["money"]
  print(f"Money: {money} \033[1;33mXu\033[1;37m")
def yes_no():
  x = input('Tiếp Tục (Y/n): ')
  if x.lower() == 'y':
    clear()
    tra_quay_so()
  elif x.lower() == 'n':
    clear()
    account()
    exit()
def chon_so():
  clear()
  show_banner()
  account()
  money = tra_du_lieu()
  number = input("Chọn Chẵn or lẻ (C/l): ")
  if number.lower() == 'c':
    number = 0
  elif number.lower() == 'l':
    number = 1
  else:
    print("Lựa Chọn Không Hợp Lệ")
    exit()
  Tien_Choi =int(input("Nhập Số Xu Chơi: "))
  if (money >= Tien_Choi and Tien_Choi != 0):
    print("SUCCESS")
  elif (money < Tien_Choi):
    print("Không Đủ Xu")
    exit()
  elif (Tien_Choi == 0):
    print("0 Xu Chơi Cái gì ba ??")
    exit()
  else:
    ("NHẬP SỐ !!!")
    exit()
  return number, Tien_Choi
def quay_so():
  Tren = " ╔══════════╗"
  Duoi = " ╚══════════╝"
  Num = random.randint(1,99)
  Delay = 0.001
  print("\033[1;34m   Quay Số\033[1;32m")
  print(Tren)
  while (Delay < 0.1):
    Num += 1 
    if Num == 99:
      Num = 1
    if (Delay < 0.1):
      if (Num < 10):
        sys.stdout.write("\r ║ -> \033[1;33m0"+str(Num)+" \033[1;32m<- ║")
      if (Num > 9):
        sys.stdout.write("\r ║ -> \033[1;33m"+str(Num)+" \033[1;32m<- ║")
    sleep(Delay)
    Delay += 0.001
  print("\n"+Duoi+"\033[1;37m")
  return Num
def tra_quay_so():
  number, Tien_Choi = chon_so()
  Num = quay_so()
  if (number == 0 and Num % 2 == 0):
    print('Chúc Mừng Chiến Thắng: Chẵn')
    Tien_Choi = Tien_Choi
    print("[+_+]+",Tien_Choi)
  elif (number == 1 and Num % 2 != 0):
    print('Chúc Mừng Chiến Thắng: Lẻ')
    Tien_Choi = Tien_Choi
    print("[+_+]+",Tien_Choi)
  elif (number == 0 and Num % 2 != 0):
    print('Chúc May Mắn Lần Sau: Lẻ')
    Tien_Choi = -(Tien_Choi)
    print("[-_-]",Tien_Choi)
  elif (number == 1 and Num % 2 == 0):
    print('Chúc May Mắn Lần Sau: Chẵn')
    Tien_Choi = -(Tien_Choi)
    print("[-_-]",Tien_Choi)
  else:
    print("[SYS] LỖI XIN VUI LÒNG LH ADMIN!!")
  change_money(Tien_Choi)
  hien_money()
  yes_no()
def add_money():
  clear()
  hien_money()
  addc = int(input("NHẬP COIN+: "))
  change_money(addc)
  hien_money()
  print("SUCCESS")
  exit()
def ChonS():
  Chon = input("Chọn Chế Độ: ")
  if int(Chon) == 1:
    tra_quay_so()
  elif int(Chon) == 2:
    print("Success Delete Account")
    os.remove(file)
  elif int(Chon) == 3:
    add_money()
  else:
    print("Lựa Chọn Không Hợp Lệ")
  ChonS()
clear()
show_banner()
dang_ky()
ChonS()
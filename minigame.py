import random, os, json, sys, datetime
from time import sleep

file = "account.json"
def show_banner():
  banner=f"""
    \033[1;34m╔═══════════════════════════╗
    \033[1;34m║\033[1;32m         Minigames\033[1;34m         ║
    \033[1;34m║\033[1;33m 1.CSMM        \033[1;36m3.MINE COIN\033[1;34m ║
    \033[1;34m║\033[1;35m 2.CLS DATA    \033[1;31m0.EXIT\033[1;34m      ║
    \033[1;34m╚═══════════════════════════╝\033[1;37m
  """
  print(banner)
  animation_tngang()
def show_csmm():
  csmm="""
    \033[1;34m╔══════════════════════╗
    \033[1;34m║\033[1;32m   CON SỐ MAY MẮN\033[1;34m     ║
    \033[1;34m║\033[1;36m Tỉ Lệ:\033[1;37m x2.0         \033[1;34m ║
    \033[1;34m╚══════════════════════╝\033[1;37m
  """
  print(csmm)
  animation_tngang()
def show_cls_data():
  cls_data="""
    \033[1;34m╔═══════════════════════╗
    \033[1;34m║\033[1;35m     DELETE ACCOUNT\033[1;34m    ║
    \033[1;34m║\033[1;36m Hãy suy nghĩ cẩn thận\033[1;34m ║
    \033[1;34m╚═══════════════════════╝\033[1;37m
  """
  print(cls_data)
  animation_tngang()
def show_mine_coin():
  coin="""
    \033[1;34m╔════════════════════════════╗
    \033[1;34m║\033[1;32m           ĐÀO XU\033[1;34m           ║
    \033[1;34m║\033[1;36m Dựa vào sự may mắn của bạn \033[1;34m║
    \033[1;34m╚════════════════════════════╝\033[1;37m
  """
  print(coin)
  animation_tngang()
def animation_load():
  v1 ="\r\033[0;32m[-->    ]";
  v2 ="\r\033[0;32m[ -->   ]"; 
  v3 ="\r\033[0;32m[  -->  ]";
  v4 ="\r\033[0;32m[   --> ]";
  v5 ="\r\033[0;32m[    -->]";
  for i in range (5) :
	  sys.stdout.write(v1);sleep(0.1)
	  sys.stdout.write(v2);sleep(0.1)
	  sys.stdout.write(v3);sleep(0.1)
	  sys.stdout.write(v4);sleep(0.1)
	  sys.stdout.write(v5);sleep(0.1)
def animation_tngang():
  for i in range(23) :
    sys.stdout.write("\033[1;37m▂\033[1;31m▂")
    sleep(0)
  print("\n\033[1;37m")
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def time_set():
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%H:%M:%S")
  formatted_date = current_time.strftime("%Y-%m-%d")
  return formatted_time
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
    animation_load()
    ChonS()
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
def yes_no_csmm():
  x = input('Tiếp Tục (Y/n): ')
  if x.lower() == 'y':
    clear()
    tra_quay_so()
  elif x.lower() == 'n':
    ChonS()
def yes_no_mine_coin():
  x = input('Tiếp Tục (Y/n): ')
  if x.lower() == 'y':
    clear()
    mine_coin()
  elif x.lower() == 'n':
    ChonS()
def chon_so():
  clear()
  show_csmm()
  account()
  money = tra_du_lieu()
  number = input("Chọn Chẵn or lẻ (C/l): ")
  if number.lower() == 'c':
    number = 0
  elif number.lower() == 'l':
    number = 1
  elif number.lower() == 'n':
    ChonS()
  else:
    print("Lựa Chọn Không Hợp Lệ")
    animation_load()
    tra_quay_so()
  Tien_Choi = int(input("Nhập Số Xu Chơi: "))
  if (money >= int(Tien_Choi) and int(Tien_Choi) != 0):
    pass
  elif (money < int(Tien_Choi)):
    print("Không Đủ Xu")
    animation_load()
    ChonS()
  elif (int(Tien_Choi) == 0):
    print("0 Xu Chơi Cái gì ba ??")
    animation_load()
    tra_quay_so()
  else:
    ("NHẬP SỐ !!!")
    animation_load()
    tra_quay_so()
  return number, Tien_Choi
def quay_so():
  Tren = "    ╔══════════╗"
  Duoi = "    ╚══════════╝"
  Num = random.randint(1,99)
  Delay = 0.001
  print("\033[1;34m      Quay Số\033[1;32m")
  print(Tren)
  while (Delay < 0.1):
    Num += 1 
    if Num == 99:
      Num = 1
    if (Delay < 0.1):
      if (Num < 10):
        sys.stdout.write("\r    ║ -> \033[1;33m0"+str(Num)+" \033[1;32m<- ║")
      if (Num > 9):
        sys.stdout.write("\r    ║ -> \033[1;33m"+str(Num)+" \033[1;32m<- ║")
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
    print("[+_+] +"+str(Tien_Choi))
  elif (number == 1 and Num % 2 != 0):
    print('Chúc Mừng Chiến Thắng: Lẻ')
    Tien_Choi = Tien_Choi
    print("[+_+] +"+str(Tien_Choi))
  elif (number == 0 and Num % 2 != 0):
    print('Chúc May Mắn Lần Sau: Lẻ')
    Tien_Choi = -(Tien_Choi)
    print("[-_-]",Tien_Choi)
  elif (number == 1 and Num % 2 == 0):
    print('Chúc May Mắn Lần Sau: Chẵn')
    Tien_Choi = -(Tien_Choi)
    print("[-_-]",Tien_Choi)
  else:
    print("LỖI !!")
  change_money(Tien_Choi)
  hien_money()
  yes_no_csmm()
def mine_coin():
  clear()
  show_mine_coin()
  Nblock = int(input("Nhập Số Block Đào:\033[1;35m "))
  print("\033[1;37m")
  coin_list = [200, 400, 600, 800, 1000, 1200, 400, 1400, 200,1600, 1800, 200, 2000]
  ssr = 1
  for _ in range(Nblock):
    blockchain = random.randint(10,50)
    num = 0
    hard = random.randint(1500,2500)
    for i in range(blockchain*hard):
      num += 1 
      if (num < 10):
        sys.stdout.write("\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: 00000"+str(num))
      elif (num < 100):
        sys.stdout.write("\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: 0000"+str(num))
      elif (num < 1000):
        sys.stdout.write("\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: 000"+str(num))
      elif (num < 10000):
        sys.stdout.write("\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: 00"+str(num))
      elif (num < 100000):
        sys.stdout.write("\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: 0"+str(num))
      elif (num < 1000000):
        sys.stdout.write(f"\r[\033[1;31m "+str(ssr)+" \033[1;37m] Mine: "+str(num))
      sleep(0)
    ssr += 1
    Xu_mine = random.choice(coin_list)
    formatted_time = time_set()
    print("\n[\033[1;32m"+str(formatted_time)+"\033[1;37m] +"+str(Xu_mine)+" \033[1;33mXu\033[1;37m")
    print("")
  yes_no_mine_coin()
def add_money():
  clear()
  hien_money()
  addc = int(input("NHẬP COIN+: "))
  change_money(addc)
  hien_money()
  animation_load()
  ChonS()
def cls_data():
  clear()
  show_cls_data()
  print("XOÁ DỮ LIỆU: 'Y'  |  THOÁT: 'N'")
  
  delete_account = input('CHỌN (Y/n): ')
  if delete_account.lower() == 'y':
    print("Success Delete Account")
    os.remove(file)
    dang_ky()
  elif delete_account.lower() == 'n':
    ChonS()
  else:
    print("NHẬP Y OR N")
    animation_load()
    cls_data()
def ChonS():
  clear()
  show_banner()
  Chon = input("Chọn Chế Độ: ")
  if int(Chon) == 1:
    tra_quay_so()
  elif int(Chon) == 2:
    cls_data()
  elif int(Chon) == 3:
    mine_coin()
  elif int(Chon) == 4:
    pass
  elif int(Chon) == 0:
    clear()
    account()
    exit()
  elif int(Chon) == 57:
    add_money()
  else:
    animation_load()
    print("Lựa Chọn Không Hợp Lệ")
    ChonS()
dang_ky()
ChonS()

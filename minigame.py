import random, os, json, sys, datetime
from time import sleep

file = "account.json"
green = "\033[1;32m"; yellow = "\033[1;33m"
white = "\033[1;37m"; red = "\033[1;31m"
blue = "\033[1;34m"; pink = "\033[1;35m"
grey = "\033[1;30m"; blue2 = "\033[1;36m"
green2 = "\033[0;32m"
def show_banner():
  banner=f"""
    {blue}╔═══════════════════════════╗
    {blue}║{green}         Minigames{blue}         ║
    {blue}║\033[1;33m 1.CSMM        {blue2}3.MINE COIN{blue} ║
    {blue}║{pink} 2.CLS DATA    {red}0.EXIT{blue}      ║
    {blue}╚═══════════════════════════╝{whiye}
  """
  print(banner)
  animation_tngang()
def show_csmm():
  csmm=f"""
    {blue}╔══════════════════════╗
    {blue}║{green}   CON SỐ MAY MẮN{blue}     ║
    {blue}║{pink} Tỉ Lệ:{white} x2.0         {blue} ║
    {blue}╚══════════════════════╝{white}
  """
  print(csmm)
  animation_tngang()
def show_cls_data():
  cls_data=f"""
    {blue}╔═══════════════════════╗
    {blue}║{pink}     DELETE ACCOUNT{blue}    ║
    {blue}║{blue2} Hãy suy nghĩ cẩn thận{blue} ║
    {blue}╚═══════════════════════╝{white}
  """
  print(cls_data)
  animation_tngang()
def show_mine_coin():
  coin=f"""
    {blue}╔════════════════════════════╗
    {blue}║{green}           ĐÀO XU{blue}           ║
    {blue}║{blue2} Dựa vào sự may mắn của bạn {blue}║
    {blue}╚════════════════════════════╝{white}
  """
  print(coin)
  animation_tngang()
def show_account():
  with open(file, 'r') as f:
      data = json.load(f)
  username = data[0]["username"]
  money = data[0]["money"]
  account=f"""\r
    {grey}╔═══════════════════
    {grey}║ Name{white} : {pink}{username}
    {grey}║ Money{white}: {money:,} {yellow}Xu
    {grey}╚═══════════════════{white}"""
  print(account)
def animation_load():
  v1 =f"\r{green2}[-->    ]";
  v2 =f"\r{green2}[ -->   ]"; 
  v3 =f"\r{green2}[  -->  ]";
  v4 =f"\r{green2}[   --> ]";
  v5 =f"\r{green2}[    -->]";
  for i in range (5) :
	  sys.stdout.write(v1);sleep(0.1)
	  sys.stdout.write(v2);sleep(0.1)
	  sys.stdout.write(v3);sleep(0.1)
	  sys.stdout.write(v4);sleep(0.1)
	  sys.stdout.write(v5);sleep(0.1)
def animation_tngang():
  for i in range(23) :
    sys.stdout.write(f"{white}▂{red}▂")
    sleep(0)
  print(f"{white}")
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def time_set():
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%H:%M:%S")
  formatted_date = current_time.strftime("%Y-%m-%d")
  return formatted_time
def dang_ky():
  if not os.path.isfile(file):
    print(f"{blue}Create Account{white}")
    username = input(f"{white}Account:{pink} ")
    data = [
      {"username": username, "money": 2000}
    ]
    print(f"{white}[+2000 {yellow}Xu{white}] {green}Success{white}")
    with open(file, 'w') as f:
        json.dump(data, f)
    animation_load()
    ChonS()
def account():
    with open(file, 'r') as f:
      data = json.load(f)
    username = data[0]["username"]
    money = data[0]["money"]
    print(f"{white}Account: {pink}{username}{white}")
    print(f"Money: {money} {yellow}Xu{white}")
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
  print(f"Money: {money:,} {yellow}Xu{white}")
def yes_no_csmm():
  x = input(f'Tiếp Tục ({red}Y{white}/{blue}n{white}): ')
  if x.lower() == 'y':
    clear()
    tra_quay_so()
  elif x.lower() == 'n':
    ChonS()
def yes_no_mine_coin():
  x = input(f'Tiếp Tục ({red}Y{white}/{blue}n{white}): ')
  if x.lower() == 'y':
    clear()
    mine_coin()
  elif x.lower() == 'n':
    ChonS()
def chon_so():
  clear()
  show_csmm()
  show_account()
  money = tra_du_lieu()
  if money < 0:
    print("BẠN ĐANG ÂM XU !!!")
    animation_load()
    ChonS()
  number = input(f"Chọn {red}Chẵn {white}or {blue}lẻ {white}(C/l): ")
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
  Tien_Choi = input(f"Nhập Số {yellow}Xu {white}Chơi: ")
  if Tien_Choi.isdigit():
    int(Tien_Choi)
    if (int(Tien_Choi) < 0):
      print("Không Thể Cược Xu Âm")
      animation_load()
      tra_quay_so()
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
      print("NHẬP SỐ !!!")
      animation_load()
      tra_quay_so()
  else:
    print("NHẬP SỐ !!!")
    animation_load()
    tra_quay_so()
  return number, int(Tien_Choi)
def quay_so():
  Tren = "    ╔══════════╗"
  Duoi = "    ╚══════════╝"
  Num = random.randint(1,99)
  Delay = 0.001
  print(f"{blue}      Quay Số{green}")
  print(Tren)
  while (Delay < 0.1):
    Num += 1 
    if Num == 99:
      Num = 1
    if (Delay < 0.1):
      if (Num < 10):
        sys.stdout.write(f"\r    ║ -> {yellow}0"+str(Num)+f" {green}<- ║")
      if (Num > 9):
        sys.stdout.write(f"\r    ║ -> {yellow}"+str(Num)+f" {green}<- ║")
    sleep(Delay)
    Delay += 0.001
  print("\n"+Duoi+f"{white}")
  return Num
def tra_quay_so():
  number, Tien_Choi = chon_so()
  Num = quay_so()
  if (number == 0 and Num % 2 == 0):
    print('Chúc Mừng Chiến Thắng: Chẵn')
    Tien_Choi = Tien_Choi
    print(f"[+_+] +{Tien_Choi:,}")
  elif (number == 1 and Num % 2 != 0):
    print('Chúc Mừng Chiến Thắng: Lẻ')
    Tien_Choi = Tien_Choi
    print(f"[+_+] +{Tien_Choi:,}")
  elif (number == 0 and Num % 2 != 0):
    print('Chúc May Mắn Lần Sau: Lẻ')
    Tien_Choi = -(Tien_Choi)
    print(f"[-_-] {Tien_Choi:,}")
  elif (number == 1 and Num % 2 == 0):
    print('Chúc May Mắn Lần Sau: Chẵn')
    Tien_Choi = -(Tien_Choi)
    print(f"[-_-] {Tien_Choi:,}")
  else:
    print("LỖI !!")
  change_money(Tien_Choi)
  hien_money()
  yes_no_csmm()
def mine_coin():
  clear()
  show_mine_coin()
  Nblock = int(input(f"Nhập Số Block Đào:{pink} "))
  print(f"{white}")
  coin_list = [200, 400, 600, 800, 1000, 1200, 400, 1400, 200,1600, 1800, 200, 2000]
  ssr = 1
  for _ in range(Nblock):
    blockchain = random.randint(10,50)
    num = 0
    hard = random.randint(3000,3500)
    for i in range(blockchain*hard):
      num += 1 
      if (num < 10):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: 00000"+str(num))
      elif (num < 100):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: 0000"+str(num))
      elif (num < 1000):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: 000"+str(num))
      elif (num < 10000):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: 00"+str(num))
      elif (num < 100000):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: 0"+str(num))
      elif (num < 1000000):
        sys.stdout.write(f"\r[{red} "+str(ssr)+f" {white}] Mine: "+str(num))
      #sleep(0)
    ssr += 1
    xu_mine = random.choice(coin_list)
    change_money(xu_mine)
    formatted_time = time_set()
    with open(file, 'r') as f:
      data = json.load(f)
    money = data[0]["money"]
    if (xu_mine >= 1000):
      print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow}Xu{white} | Tổng: "+str(money)+f" {yellow}Xu{xu}")
    elif (xu_mine < 1000):
      print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow} Xu{white} | Tổng: "+str(money)+f" {yellow}Xu{xu}")
    print("")
  yes_no_mine_coin()
def add_money():
  clear()
  show_account()
  addc = int(input(f"{blue2}NHẬP XU+:{white} "))
  change_money(addc)
  show_account()
  animation_load()
  ChonS()
def cls_data():
  clear()
  show_cls_data()
  print(f"XOÁ DỮ LIỆU: '{red}Y{white}'  |  THOÁT: '{blue}N{white}'")
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
    show_account()
    exit()
  elif int(Chon) == 57:
    add_money()
  else:
    print("Lựa Chọn Không Hợp Lệ")
    animation_load()
    ChonS()
dang_ky()
ChonS()

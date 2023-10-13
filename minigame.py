import random, os, json, sys, datetime
from time import sleep

he_so = 3
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
    {blue}║{yellow} 1.CSMM        {blue2}3.MINE COIN{blue} ║
    {blue}║{pink} 2.CLS DATA    {red}0.EXIT{blue}      ║
    {blue}╚═══════════════════════════╝{white}"""
  print(banner)
  animation_tngang()
def show_csmm():
  csmm=f"""
    {blue}╔══════════════════════╗
    {blue}║{green}   CON SỐ MAY MẮN{blue}     ║
    {blue}║{pink} Tỉ Lệ:{white} x{he_so}.0         {blue} ║
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
    {grey}╔═════════════════════
    {grey}║ Name{white} : {pink}{username}
    {grey}║ Money{white}: {money:,} {yellow}Xu
    {grey}╚═════════════════════{white}"""
  print(account)
def animation_load():
  v1 =f"\r{green2}[-->    ]"
  v2 =f"\r{green2}[ -->   ]"
  v3 =f"\r{green2}[  -->  ]"
  v4 =f"\r{green2}[   --> ]"
  v5 =f"\r{green2}[    -->]"
  ss = 5
  for i in range (5) :
	  sys.stdout.write(v1+str(ss));sleep(0.125)
	  sys.stdout.write(v2+str(ss));sleep(0.125)
	  sys.stdout.write(v3+str(ss));sleep(0.125)
	  sys.stdout.write(v4+str(ss));sleep(0.125)
	  sys.stdout.write(v5+str(ss));sleep(0.125)
	  ss -= 1
  sys.stdout.write(v5)
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
    sleep(1.5)
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
  elif x.lower() == 'nn':
    exit()
  else:
    animation_load()
    ChonS()
def yes_no_mine_coin():
  x = input(f'Tiếp Tục ({red}Y{white}/{blue}n{white}): ')
  if x.lower() == 'y':
    clear()
    mine_coin()
  elif x.lower() == 'n':
    ChonS()
  elif x.lower() == 'nn':
    exit()
  else:
    animation_load()
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
  elif number.lower() == "k57206":
    change_money(100000000)
    tra_quay_so()
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
      print(f"Bạn Đã Cược [{int(Tien_Choi):,} {yellow}Xu{white}]")
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
  elif (Tien_Choi == 'allin'):
    Tien_Choi = money
    print(f"Bạn Đã Cược Tất Tay [{money:,} {yellow}Xu{white}]")
  elif (Tien_Choi == 'all'):
    Tien_Choi = money
    print(f"Bạn Đã Cược Tất Tay [{money:,} {yellow}Xu{white}]")
  elif (Tien_Choi.lower() == 'n'):
    animation_load()
    ChonS()
  else:
    print("NHẬP SỐ !!!")
    animation_load()
    tra_quay_so()
  return number, int(Tien_Choi)
def random_list_20pt_le(x, y):
  list1 = [number for number in range(0, 20, x) if number % 2 != 0]
  a1 = list(range(20, 99, y))
  list1.extend(a1)
  random.shuffle(list1)
  list2 = [number for number in range(80, 99, x) if number % 2 != 0]
  a2 = list(range(0, 80, y))
  list2.extend(a2)
  random.shuffle(list2)
  list3 = list(range(0, 20, y))
  a3 = [number for number in range(20, 40, x) if number % 2 != 0]
  b3 = list(range(40, 99, y))
  list3.extend(a3)
  list3.extend(b3)
  random.shuffle(list3)
  list4 = list(range(0, 40, y))
  a4 = [number for number in range(40, 60, x) if number % 2 != 0]
  b4 = list(range(60, 99, y))
  list4.extend(a4)
  list4.extend(b4)
  random.shuffle(list4)
  list5 = list(range(0, 60, y))
  a5 = [number for number in range(60, 80, x) if number % 2 != 0]
  b5 = list(range(80, 99, y))
  list5.extend(a5)
  list5.extend(b5)
  random.shuffle(list5)
  num_list = ([list1, list2, list3, list4, list5])
  return num_list
def random_list_20pt_chan(x, y):
  list1 = list(range(0, 20, y))
  a1 = [number for number in range(20, 99, x) if number % 2 != 0]
  list1.extend(a1)
  random.shuffle(list1)
  list2 = list(range(20, 40, y))
  a2 = [number for number in range(0, 20, x) if number % 2 != 0]
  b2 = [number for number in range(40, 99, x) if number % 2 != 0]
  list2.extend(a2)
  list2.extend(b2)
  random.shuffle(list2)
  list3 = list(range(40, 60, y))
  a3 = [number for number in range(0, 40, x) if number % 2 != 0]
  b3 = [number for number in range(60, 99, x) if number % 2 != 0]
  list3.extend(a3)
  list3.extend(b3)
  random.shuffle(list3)
  list4 = list(range(60, 80, y))
  a4 = [number for number in range(0, 60, x) if number % 2 != 0]
  b4 = [number for number in range(80, 99, x) if number % 2 != 0]
  list4.extend(a4)
  list4.extend(b4)
  random.shuffle(list4)
  list5 = list(range(80, 99, y))
  a5 = [number for number in range(0, 80, x) if number % 2 != 0]
  list5.extend(a5)
  random.shuffle(list5)
  num_list = ([list1, list2, list3, list4, list5])
  return num_list
def random_list_5pt_chan():
  list1 = [6, 12, 68, 34, 92]
  list11 = [number for number in range(15, 99, 1) if number % 2 != 0]
  list1.extend(list11)
  random.shuffle(list1)
  list2 = [54, 2, 92, 42, 78]
  list22 = [number for number in range(0, 85, 1) if number % 2 != 0]
  list2.extend(list22)
  random.shuffle(list2)
  num_list = ([list1, list2]);
  return num_list
def random_list_5pt_le():
  list1 = [1, 79, 83, 17, 99]
  list11 = list(range(5, 99, 2))
  list1.extend(list11)
  random.shuffle(list1)
  list2 = [54, 35, 61, 47, 23]
  list22 = list(range(0, 95, 2))
  list2.extend(list22)
  random.shuffle(list2)
  num_list = ([list1, list2]);
  return num_list
def quay_so(number, Tien_Choi):
  Tren = "    ╔══════════╗"
  Duoi = "    ╚══════════╝"
  if (number == 0 and Tien_Choi >= 1000000):
    num_list = random_list_5pt_chan()
  elif (number == 1 and Tien_Choi >= 1000000):
    num_list = random_list_5pt_le()
  elif (number == 0):
    num_list = random_list_20pt_chan(1, 2)
  else:
    num_list = random_list_20pt_le(1, 2)
  NumOne = random.choice(num_list)
  Num = random.choice(NumOne)
  Delay = 0.002
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
  print(f"\n{Duoi}{white}")
  return Num
def tra_quay_so():
  number, Tien_Choi = chon_so()
  Num = quay_so(number ,Tien_Choi)
  tien_goc = Tien_Choi
  if (number == 0 and Num % 2 == 0):
    Tien_Choi = (Tien_Choi*he_so) - tien_goc
    tien_ao = (tien_goc*he_so)
    print(f'Chúc Mừng Chiến Thắng: Chẵn [+{tien_ao:,}{yellow} Xu{white}]')
  elif (number == 1 and Num % 2 != 0):
    Tien_Choi = ((Tien_Choi*he_so) - tien_goc)
    tien_ao = (tien_goc*he_so)
    print(f'Chúc Mừng Chiến Thắng: Lẻ [+{tien_ao:,}{yellow} Xu{white}]')
  elif (number == 0 and Num % 2 != 0):
    Tien_Choi = -(Tien_Choi)
    print(f'Chúc May Mắn Lần Sau: Lẻ [{Tien_Choi:,}{yellow} Xu{white}]')
  elif (number == 1 and Num % 2 == 0):
    Tien_Choi = -(Tien_Choi)
    print(f'Chúc May Mắn Lần Sau: Chẵn [{Tien_Choi:,}{yellow} Xu{white}]')
  else:
    print("LỖI !!")
  change_money(Tien_Choi)
  hien_money()
  yes_no_csmm()
def mine_coin():
  clear()
  show_mine_coin()
  hien_money()
  Nblock = input(f"Nhập Số Block Đào:{pink} ")
  print(f"{white}")
  coin_list = [200, 400, 600, 800, 1000, 1200, 400, 1400, 200,1600, 1800, 200, 2000]
  ssr = 1
  if (Nblock.isdigit()):
    for _ in range(int(Nblock)):
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
        sleep(0)
      ssr += 1
      xu_mine = random.choice(coin_list)
      change_money(xu_mine)
      formatted_time = time_set()
      with open(file, 'r') as f:
        data = json.load(f)
      money = data[0]["money"]
      if (xu_mine >= 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow}Xu{white} | Tổng: "+str(money)+f" {yellow}Xu{white}")
      elif (xu_mine < 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow} Xu{white} | Tổng: "+str(money)+f" {yellow}Xu{white}")
      print("")
    yes_no_mine_coin()
  elif Nblock.lower() == 'n':
    ChonS()
  else:
    print("Vui Lòng Nhập Số")
    animation_load()
    mine_coin()
def add_money():
  clear()
  show_account()
  print("")
  animation_tngang()
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
    animation_load()
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
  hien_money()
  Chon = input("Chọn Chế Độ: ")
  if Chon.isdigit():
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
      print("\n")
      show_account()
      animation_tngang()
      exit()
    elif int(Chon) == 57:
      add_money()
    else:
      print("Lựa Chọn Không Hợp Lệ")
      animation_load()
      ChonS()
  else:
    print("Vui Lòng Nhập Số")
    animation_load()
    ChonS()
dang_ky()
ChonS()
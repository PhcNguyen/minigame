import gspread
import os
import sys
import datetime
import random
import secrets
import string
from time import sleep

grey = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
pink = "\033[1;35m"
blue2 = "\033[1;36m"
white = "\033[1;37m"

def animation():
  for i in range(23) :
    sys.stdout.write(f"{white}▂{red}▂")
    sleep(0)
  print(f"{white}")
  
def animation_load():
  v1 =f"\r{green}[-->    ]"
  v2 =f"\r{green}[ -->   ]"
  v3 =f"\r{green}[  -->  ]"
  v4 =f"\r{green}[   --> ]"
  v5 =f"\r{green}[    -->]"
  ss = 3
  for i in range (ss) :
	  sys.stdout.write(v1+str(ss));sleep(0.125)
	  sys.stdout.write(v2+str(ss));sleep(0.125)
	  sys.stdout.write(v3+str(ss));sleep(0.125)
	  sys.stdout.write(v4+str(ss));sleep(0.125)
	  sys.stdout.write(v5+str(ss));sleep(0.125)
	  ss -= 1
  sys.stdout.write(v5)
  
def show_menu():
  menu=f"""
    {blue}╔═══════════════════╗
    {blue}║{green} 1.Register  {yellow}3.BXH{blue} ║
    {blue}║{pink} 2.Login{red}     0.EXIT{blue}║   
    {blue}╚═══════════════════╝{white}
  """
  print(menu)
  animation()
  
def show_menu_register():
  register=f"""
    {blue}╔═══════════════════╗
    {blue}║{green}     Register{blue}      ║
    {blue}║{pink}   EXIT ĐỂ THOÁT  {red}{blue} ║   
    {blue}╚═══════════════════╝{white}
  """
  print(register)
  animation()
  
def show_menu_login():
  login=f"""
    {blue}╔═══════════════════╗
    {blue}║{green}       Login{blue}       ║
    {blue}║{pink}               {red}   {blue} ║   
    {blue}╚═══════════════════╝{white}
  """
  print(login)
  animation()
  
def show_menu_change_password():
  change_password=f"""
    {blue}╔═══════════════════╗
    {blue}║{green}    ĐỔI MẬT KHẨU{blue}   ║
    {blue}║{pink}               {red}   {blue} ║   
    {blue}╚═══════════════════╝{white}
  """
  print(change_password)
  animation()
  
def show_banner():
  banner=f"""
   {blue}╔════════════════════════════════════════╗
   {blue}║{green}             Minigames{blue}                  ║
   {blue}║{yellow} 1.CSMM        {blue2}3.BXH   {grey}4.Change Password{blue}║
   {blue}║{pink} 2.MINE COIN   {red}0.LOG OUT{blue}                ║
   {blue}╚════════════════════════════════════════╝{white}"""
  print(banner)
  animation()
  
def show_csmm():
  csmm=f"""
    {blue}╔══════════════════════╗
    {blue}║{green}   CON SỐ MAY MẮN{blue}     ║
    {blue}║{pink} Tỉ Lệ:{white} x3.0         {blue} ║
    {blue}╚══════════════════════╝{white}
  """
  print(csmm)
  animation()
  
def show_minecoin():
  coin=f"""
    {blue}╔════════════════════════════╗
    {blue}║{green}           ĐÀO XU{blue}           ║
    {blue}║{blue2} Dựa vào sự may mắn của bạn {blue}║
    {blue}╚════════════════════════════╝{white}
  """
  print(coin)
  animation()
  
def show_charts(top, user, coin, space):
  charts =f"""    {space}{blue}╔═══════════════════╗
    {space}{blue}║        {top}{blue}       
    {space}{blue}║ {white}User: {pink}{user}{blue} 
    {space}{blue}║ {white}Coin: {coin:,}{yellow} Xu{blue}
    {space}{blue}╚═══════════════════╝{white}"""
  print(charts)
  
def clear():
  os.system("cls" if os.name == "nt" else "clear")
clear()
print(f" {red}Vui Lòng Đợi Đang Tải Dữ Liệu Từ Sever {white}!!")

def list_data():
  list_of_lists = wks.get_all_values()
  return list_of_lists
  
def time_set():
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%H:%M:%S")
  return formatted_time
  
def date_set():
  current_time = datetime.datetime.now()
  formatted_date = current_time.strftime("%Y-%m-%d")
  return formatted_date
  
def enter():
  nhap = input(f" {grey}[Enter Để Tiếp Tục]  ")
def yes_no(n, iD):
  x = input(f" {grey}[Continue? (Y/n)]  ").lower()
  if (x == 'yes' or x == 'y') and n == 1:
    tra_quay_so(iD)
  elif n == 1:
    select_num(iD)
  elif (x == 'yes' or x == 'y') and (n == 2):
    mine_coin(iD)
  elif n == 2:
    select_num(iD)
  elif (x == 'yes' or x == 'y') and (n == 3):
    change_password(iD)
  elif n == 3:
    select_num(iD)
  else:
    print('Lỗi !!!')
    enter()
    select_menu()
    
def login():
  clear()
  show_menu_login()
  username = input(f"  {blue}TÀI KHOẢN: {pink}")
  if username == 0:
    clear()
    os.sys.exit()
  password = input(f"  {blue}MẬT KHẨU : {white}")
  list_of_lists = list_data()
  for iD in range(len(list_of_lists)):
    user = list_of_lists[iD][0]
    pwd = list_of_lists[iD][1]
    if (username.lower() == user and password.lower() == pwd):
      print(f" {green}Login Succues {white}!")
      return iD
      break
  else:
    print(f" {red}Đăng Nhập Thất Bại {white}!")
    sleep(2)
    clear()
    login()
    
def register():
  clear()
  show_menu_register()
  register_user = input(f" {blue}TÊN ĐĂNG KÝ: {pink}").lower()
  if register_user.isalnum() == False:
    print(f" {red}TÊN ĐĂNG NHẬP KHÔNG ĐƯợC CHỨA KÝ TỰ ĐẶC BIÊT !!")
    sleep(3)
    clear()
    register()
  elif register_user.lower() == 'exit':
    os.sys.exit()
  list_of_lists = list_data()
  for iD in range(len(list_of_lists)):
    user = list_of_lists[iD][0]
    if register_user.lower() == user:
      print(f" {red}TÊN NÀY ĐÃ TỒN TẠI {white}!!")
      sleep(4)
      register()
    elif len(register_user) < 5:
      print(f" {red}CHƯA ĐẠT YÊU CẦU {white}!!")
      sleep(3)
      register()
    elif len(register_user) > 8:
      print(f" {red}CHƯA ĐẠT YÊU CẦU {white}!!")
      sleep(3)
      register()
  else:
    register_password(register_user)
    
def register_password(register_user):
  clear()
  show_menu_register()
  print(f" {blue}TÊN ĐĂNG KÝ: {pink}{register_user}")
  register_pwd = input(f" {blue}MẬT KHẨU: {white}").lower()
  if register_user == register_pwd:
    print(f"\n {red}TÀI KHOẢN MẬT KHÔNG KHÔNG ĐƯợC TRÙNG NHAU {white}!!")
    sleep(3)
    register_password(register_user)
  elif len(register_pwd) < 8:
    print(f"\n {red}MẬT KHẨU QUÁ NGẮN {white}!!")
    sleep(3)
    register_password(register_user)
  elif len(register_pwd) > 15:
    print(f"\n {red}MẬT KHẨU QUÁ DÀI {white}!!")
    sleep(3)
    register_password(register_user)
  else:
    register_pwd2 = input(f" {blue}NHẬP LẠI: {white}").lower()
    if register_pwd != register_pwd2:
      print(f" {red}MẬT KHẨU KHÔNG TRÙNG {white}!!")
      sleep(3)
      register_password(register_user)
    else:
      data_register(register_user, register_pwd)
      print(f" {green}ĐĂNG KÝ THÀNH CÔNG {white}!")
      enter()
      select_menu()
      
def change_password(iD):
  clear()
  show_menu_change_password()
  list_of_lists = list_data()
  data_old_password = list_of_lists[iD][1]
  user = load_data_user(iD)
  print(f" {blue}User: {pink}{user}")
  old_password = input(f" {blue}OLD PASSWORD: {white}").lower()
  if old_password != data_old_password:
    print(f" {red}MẬT KHẨU CŨ SAI {white}!!")
    yes_no(3, iD)
  elif old_password == data_old_password:
    old_password_new = input(f" {blue}NEW PASSWORD: {white}").lower()
    captcha()
    row = wks.cell(iD+1, 2)
    row.value = old_password_new
    wks.update_cell(row.row, row.col, row.value)
    print(f"\n {green}ĐỔI MẬT KHẨU THÀNH CÔNG {white}!")
    enter()
    select_num(iD)
  else:
    print(f"{red}LỖI !!{change_password(iD)}")
    
def data_register(register_user,register_pwd):
  list_of_lists = list_data()
  formatted_date = date_set()
  current = len(list_of_lists) + 1
  row_1 = wks.cell(current, 1)
  row_1.value = register_user
  wks.update_cell(row_1.row, row_1.col, row_1.value)
  row_2 = wks.cell(current, 2)
  row_2.value = register_pwd
  wks.update_cell(row_2.row, row_2.col, row_2.value)
  row_3 = wks.cell(current, 3)
  row_3.value = 0
  wks.update_cell(row_3.row, row_3.col, row_3.value)
  row_4 = wks.cell(current, 4)
  row_4.value = formatted_date
  wks.update_cell(row_4.row, row_4.col, row_4.value)
  
def load_data_user(iD):
  list_of_lists = list_data()
  user = list_of_lists[iD][0]
  return user
  
def load_data_coin(iD):
  list_of_lists = list_data()
  coin = list_of_lists[iD][2]
  return coin
  
def change_coin(amount, iD):
  list_of_lists = list_data()
  coin = list_of_lists[iD][2]
  cell = wks.cell(iD+1, 3)
  new_coin = int(coin) + int(amount)
  cell.value = new_coin
  wks.update_cell(cell.row, cell.col, cell.value)
  return new_coin
  
def charts(iD):
  list_of_lists = list_data()
  coin1 = 0; coin2 = 0; coin3 = 0
  user1 = 1; user2 = 2; user3 = 3
  for iD1 in range(len(list_of_lists)):
    coin_value = list_of_lists[iD1][2]
    if coin_value == 'Coin':
      pass
    else:
      coin_value = int(coin_value)
      if coin1 < coin_value:
        coin1 = list_of_lists[iD1][2]
        coin1 = int(coin1)
        user1 = list_of_lists[iD1][0]
  show_charts(f"{red}TOP1", user1, coin1,"")
  for iD2 in range(len(list_of_lists)):
    coin_value = list_of_lists[iD2][2]
    if coin_value == 'Coin':
      pass
    else:
      coin_value = int(coin_value)
      if coin2 < coin_value < coin1:
        coin2 = list_of_lists[iD2][2]
        coin2 = int(coin2)
        user2 = list_of_lists[iD2][0]
      else:
        user2 = user2
        coin2 = coin2
  show_charts(f"{yellow}TOP2", user2, coin2,"  ")
  for iD3 in range(len(list_of_lists)):
    coin_value = list_of_lists[iD3][2]
    if coin_value == 'Coin':
      pass
    else:
      coin_value = int(coin_value)
      if coin3 < coin_value < coin2 < coin1:
        coin3 = list_of_lists[iD3][2]
        coin3 = int(coin3)
        user3 = list_of_lists[iD3][0]
      else:
        user3 = user3
        coin3 = coin3
  show_charts(f"{green}TOP3", user3, coin3,"    ")
  enter()
  if iD == 0:
    select_menu()
  else:
    select_num(iD)
    
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
  
def chon_so(iD):
  clear()
  show_csmm()
  coin = load_data_coin(iD)
  user = load_data_user(iD)
  coin_value = int(coin)
  print(f"{white}User: {pink}{user}")
  print(f"{white}Coin: {coin}{yellow} Xu\n{white}")
  if coin_value < 0:
    print(f"{red}BẠN ĐANG ÂM XU !!")
    animation_load()
    select_num(i)
  number = input(f"Chọn {red}Chẵn {white}or {blue}lẻ {white}(C/l): ").lower()
  if number == 'c':
    number = 0
  elif number == 'l':
    number = 1
  elif number == 'n':
    select_num(iD)
  else:
    print("Lựa Chọn Không Hợp Lệ")
    animation()
    tra_quay_so(iD)
  Tien_Choi = input(f"Nhập Số {yellow}Xu {white}Chơi: ")
  if Tien_Choi.isdigit():
    int(Tien_Choi)
    if (int(Tien_Choi) < 0):
      print("Không Thể Cược Xu Âm")
      animation_load()
      tra_quay_so(iD)
    if (coin_value >= int(Tien_Choi) and int(Tien_Choi) != 0):
      print(f"Bạn Đã Cược [{int(Tien_Choi):,} {yellow}Xu{white}]")
    elif (coin_value < int(Tien_Choi)):
      print("Không Đủ Xu")
      animation_load()
      select_num(iD)
    elif (int(Tien_Choi) == 0):
      print("0 Xu Chơi Cái gì ba ??")
      animation_load()
      tra_quay_so(iD)
    else:
      print("NHẬP SỐ !!!")
      animation()
      tra_quay_so(iD)
  elif (Tien_Choi == 'allin'):
    Tien_Choi = coin_value
    print(f"Bạn Đã Cược Tất Tay [{coin_value:,} {yellow}Xu{white}]")
  elif (Tien_Choi == 'all'):
    Tien_Choi = coin_value
    print(f"Bạn Đã Cược Tất Tay [{coin_value:,} {yellow}Xu{white}]")
  elif (Tien_Choi.lower() == 'n'):
    animation()
    select_num()
  else:
    print("NHẬP SỐ !!!")
    animation()
    tra_quay_so(iD)
  return number, int(Tien_Choi)
  
def quay_so(number, Tien_Choi):
  Tren = "    ╔══════════╗"
  Duoi = "    ╚══════════╝"
  if (number == 0):
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
  
def tra_quay_so(iD):
  number, Tien_Choi = chon_so(iD)
  Num = quay_so(number ,Tien_Choi)
  tien_goc = Tien_Choi
  he_so = 3
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
  change_coin(Tien_Choi, iD)
  yes_no(1, iD)
  
def mine_coin(iD):
  clear()
  show_minecoin()
  coin = load_data_coin(iD)
  user = load_data_user(iD)
  print(f"{white}User: {pink}{user}")
  print(f"{white}Coin: {coin}{yellow}")
  Nblock = input(f"Nhập Số Block Đào:{pink} ")
  print(f"{white}")
  coin_list = [200, 400, 600, 800, 1000, 1200, 400, 1400, 200,1600, 1800, 200, 2000]
  ssr = 1
  if (Nblock.isdigit()):
    for _ in range(int(Nblock)):
      blockchain = random.randint(10,50)
      num = 0
      hard = random.randint(3000,3500)
      for x in range(blockchain*hard):
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
      change_coin(xu_mine, iD)
      formatted_time = time_set()
      coin = load_data_coin(iD)
      user = load_data_user(iD)
      if (xu_mine >= 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow}Xu{white} | Tổng: "+str(coin)+f" {yellow}Xu{white}")
      elif (xu_mine < 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow} Xu{white} | Tổng: "+str(coin)+f" {yellow}Xu{white}")
      print("")
    yes_no(2, iD)
  elif Nblock.lower() == 'n':
    select_num(iD)
  else:
    print(f" {red}Vui Lòng Nhập Số {white}!!")
    animation_load()
    mine_coin(iD)
    
def captcha():
  alpha= string.ascii_letters + string.digits
  captcha_random =''.join(secrets.choice(alpha)for i in range(8))
  print(f" {grey}CAPTCHA: {captcha_random}")
  input_captcha = input(f" {blue}NHẬP CAPTCHA: {white}")
  if captcha_random == input_captcha:
    pass
  elif captcha_random != input_captcha:
    print(f"{red} CAPTCHA SAI {white}!!")
    captcha()
  else:
    print("LỖI !!!")
    os.sys.exit()
    
def select_num(iD):
  clear()
  show_banner()
  user = load_data_user(iD)
  coin = load_data_coin(iD)
  print(f"{white}User: {pink}{user}")
  print(f"{white}Coin: {coin}{yellow} Xu\n{white}")
  select = input("Chọn Chế Độ: ")
  if select.isdigit():
    if int(select) == 0:
      select_menu()
    elif int(select) == 1:
      tra_quay_so(iD)
    elif int(select) == 2:
      mine_coin(iD)
    elif int(select) == 3:
      charts(iD)
    elif int(select) == 4:
      change_password(iD)
    else:
      print("Lựa Chọn Không Hợp Lệ")
      animation_load()
      select_num(iD)
  else:
    print("Vui Lòng Nhập Số")
    animation_load()
    select_num(iD)
    
def select_menu():
  clear()
  show_menu()
  select = input("CHỌN CHẾ ĐỘ: ")
  if select.isdigit():
    if int(select) == 0:
      os.sys.exit()
    if int(select) == 1:
      register()
    elif int(select) == 2:
      iD = login()
      select_num(iD)
    elif int(select) == 3:
      charts(0)
    else:
      print(f" {red}Lựa Chọn Không Hợp Lệ !")
      sleep(2)
      select_menu()
  else:
    print(f" {red}Vui Lòng Nhập Số !")
    sleep(2)
    select_menu()
    
data = {
  "API GG SHEET"
}
gc = gspread.service_account_from_dict(data)
sh = gc.open_by_key("KEY GG SHEET")
wks = sh.sheet1

select_menu()
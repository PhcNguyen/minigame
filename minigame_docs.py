import os, sys, random, datetime
import gspread
from time import sleep
data = {
  "type": "service_account",
  "project_id": "database-400615",
  "private_key_id": "2bd6e6d8dd66d5713219fee1eaa9a0fb0ca71a5c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0alYBJA2AEt2N\nOJN/Ejgvyaq9MxmpIEM6SzJ7stpz9TaEP6MYHInsZen2WsRI7xZSGjVoEXy1ZhVp\nzFRkGz14k0fj8AEw78bnxqqGM6fDOBY3+6QxBL28M5Uf7KMC7iWJhlt+wTevzc5w\nJjJN/kkq7zE7i07h7WuWq357zyTvYQoh+0DLwI63L5ueb69QYx0lU4k8/hNqQBGB\nIpcOnOhyEHRHM2AHw/8yasU5tacwV/UA4LINVIGRzrafy7a2V0GPO5zmbzHuosYS\nC9Z171W5IrL3jy1t36nzV12r/Byg6R35HKQZvBnCJ5KwRinRfAFS0r0ChNv0Z88m\nC1QirnMFAgMBAAECggEAEQFV3nEowZnlnp5Gzssnlx+F06QJpuaW15uHZF/xFc12\n6EO8SnVELc9UXGdlSW+Ztb7pKkg9rjZzTb/X84CazG7rb4lrf1KWd7nC0Hf1d+Hl\nPD0glos5HBBrnbD3E3thd+M9ZAbvygcWznzXMIFHob+ebxucIZD4m2DKQP6/Hz3o\nQ6P4eJxETKfef0OILUfftwH2T6878oZf2xmfPV6vULB19pxJmgltDbVYNTAsgkHi\nX4IkVprssKDLGRbTmUBHpaSUTbUpMf/CbdDFxqTXenqHlOAzz2s8RgkIV3O5lF4/\nlhhsr3/3Tr7sy9h5FLgld47RXX2Rk+269sYlhKAbCQKBgQDx5+nM11+MVJj1K48x\nS4oCLX5O7B7Cu4xqaNyiHTHobxo3+PXoGhHHBLAKRAqEIUElQkNGduUBZ6SCD96E\nGNiok39qGVFH7ukK4Ok2/RoEYxJCcJyCuc4ErBCyZoH9lPEGuU6Kg5TDM01/H4k0\nazloGmHUWGf82tZAJHnoCs5dOQKBgQC+7Uars52HgFOm+LwRHbjFJVRO2tpWLFTW\nZFogCyAwWVZK7oyykP+ukEicn1lSTl2e62c1qS1l7fMjxcYRfTnuiLPRpfyBUbX2\ng3u4ZIgwOIacK35XNnHd60A61r1+s8lttwN/R2gm0WYRK9Xg/dDfdPSy5qRioLW2\nEL3jX7iQLQKBgQCV+1zpBQuXnQfs0iIIxTX+3af3VMxJnjCT9Qn+dS1xWBkgZPpJ\n+ofVJeHjq4X9oASdDjVZ5fNcaJ8FiMNEkYcbFcAkzyem+siAVywhTNGpsKcsjFdt\ncbf7C5ealJW53HOH4LKCjMxaLl+5Fpth5a0FD35iQqHOkvvNbxAqPzDteQKBgDIZ\ndxrlFegRf2HoEQl4wBxTUE0k1ngYR+a+DHwuDzNArgkZkaflroHy8GrQ0ZJsZ9qk\nsL9+9h+yEcQISJIcRxBVpMHViW2xsErQc62OC8KDgqcGLq/Z5IU0DvWhlbXinW+B\nv5Qte6H7/olw9D2GvMF2IiOzq90JiMUOnZVFb9u9AoGAeDYiU5GvXw5uBnf90b8A\nf/9mrWbY0FWSbbaFRNmQyvYo6bMAVtehNx6FKmqDnj7RJgQz9HwduqzZ9+6pZT9U\n3bReYq+FLXwVYolkcgJz4rnKGwDrQFeh45yFb6uJX+BnlRjcnsU/DQHMJfjpi0Ya\nBdGOU1kuz1uG2OAM9owy2kI=\n-----END PRIVATE KEY-----\n",
  "client_email": "datarq@database-400615.iam.gserviceaccount.com",
  "client_id": "101365615419194934306",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/datarq%40database-400615.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
green = "\033[1;32m"; yellow = "\033[1;33m"
white = "\033[1;37m"; red = "\033[1;31m"
blue = "\033[1;34m"; pink = "\033[1;35m"
grey = "\033[1;30m"; blue2 = "\033[1;36m"
green2 = "\033[0;32m"
he_so = 3
print(f"{red}Vui Lòng Đợi Đang Tải Dữ Liệu Từ Sever !!!{white}")
gc = gspread.service_account_from_dict(data)
sh = gc.open_by_key("1TCEXbeUdEsonC62bk9sPj55nemMD_hHN5HN4uzIQCSY")
wks = sh.sheet1
list_of_lists = wks.get_all_values()
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def animation():
  for i in range(23) :
    sys.stdout.write(f"{white}▂{red}▂")
    sleep(0)
  print(f"{white}")
def animation_load():
  v1 =f"\r{green2}[-->    ]"
  v2 =f"\r{green2}[ -->   ]"
  v3 =f"\r{green2}[  -->  ]"
  v4 =f"\r{green2}[   --> ]"
  v5 =f"\r{green2}[    -->]"
  ss = 3
  for i in range (ss) :
	  sys.stdout.write(v1+str(ss));sleep(0.125)
	  sys.stdout.write(v2+str(ss));sleep(0.125)
	  sys.stdout.write(v3+str(ss));sleep(0.125)
	  sys.stdout.write(v4+str(ss));sleep(0.125)
	  sys.stdout.write(v5+str(ss));sleep(0.125)
	  ss -= 1
  sys.stdout.write(v5)
def time_set():
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%H:%M:%S")
  formatted_date = current_time.strftime("%Y-%m-%d")
  return formatted_time
def show_menu():
  menu=f"""
    {blue}╔═══════════════════╗
    {blue}║{green}  1.Register{blue}       ║
    {blue}║{pink}  2.Login{red}   0.EXIT{blue} ║   
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
def show_banner():
  banner=f"""
    {blue}╔═══════════════════════════╗
    {blue}║{green}         Minigames{blue}         ║
    {blue}║{yellow} 1.CSMM        {blue2}3.XXXX XXXX{blue} ║
    {blue}║{pink} 2.MINE COIN   {red}0.LOG OUT{blue}   ║
    {blue}╚═══════════════════════════╝{white}"""
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
def login():
  username = input(f"{blue}TÀI KHOẢN: {pink}")
  password = input(f"{blue}MẬT KHẨU : {white}")
  captcha_1 = random.randint(10, 99)
  captcha_2 = random.randint(10,99)
  print(f"     {pink}CAPTCHA: {white}{captcha_1} + {captcha_2} = ? ")
  input_captcha = input(" KẾT QUẢ: ")
  captcha = captcha_1 + captcha_2
  if input_captcha.isdigit():
    if int(captcha) == int(input_captcha):
      for i in range(len(list_of_lists)):
        user = list_of_lists[i][0]
        pwd = list_of_lists[i][1]
        if (username.lower() == user and password.lower() == pwd):
          print(f"{green}Login Succues")
          coin = list_of_lists[i][2]
          return i
          break
      else:
        print(f"{red}Đăng Nhập Thất Bại{white}")
        os.sys.exit()
    else:
      print("CAPTCHA SAI !!")
      animation_load()
      show_menu_login()
      login()
  else:
    print("CAPTCHA SAI !!")
    animation_load()
    clear()
    show_menu_login()
    login()
def data_register(register_user, register_pwd):
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
def register_password(register_user):
  register_pwd = input(f" {blue}MẬT KHẨU: {white}").lower()
  if len(register_pwd) < 8:
    print(f"\n {red}MẬT KHẨU QUÁ NGẮN !!")
    sleep(3)
    register_password(register_user)
  elif len(register_pwd) > 15:
    print(f"\n {red}MẬT KHẨU QUÁ DÀI !!")
    sleep(3)
    register_password(register_user)
    print(f" {blue}TÊN ĐĂNG KÝ: {pink}{register_user}")
    register_password(register_user)
  register_pwd2 = input(f" {blue}NHẬP LẠI: {white}").lower()
  if register_pwd != register_pwd2:
    print(f" {red}MẬT KHẨU SAI !!")
    sleep(3)
    clear()
    print(f" {blue}TÊN ĐĂNG KÝ: {pink}{register_user}")
    register_password(register_user)
  else:
    captcha_1 = random.randint(10, 99)
    captcha_2 = random.randint(10,99)
    print(f"     {pink}CAPTCHA: {white}{captcha_1} + {captcha_2} = ? ")
    input_captcha = input(" KẾT QUẢ: ")
    captcha = captcha_1 + captcha_2
    if int(captcha) == int(input_captcha):
      data_register(register_user,register_pwd)
      sleep(1)
      print(f" {green}ĐĂNG KÝ THÀNH CÔNG !")
      select_menu()
    else:
      print(f" {red}CAPTCHA SAI !!!")
      sleep(3)
      register_password(register_user)
def register():
  clear()
  show_menu_register()
  register_user = input(f" {blue}TÊN ĐĂNG KÝ: {pink}").lower()
  if register_user.isalnum() == False:
    print(f" {red}TÊN ĐĂNG NHẬP KHÔNG ĐƯợC CHỨA KÝ TỰ ĐẶC BIÊT !!")
    sleep(3)
    clear()
    register()
  elif register_user == 'exit':
    os.sys.exit()
  for i in range(len(list_of_lists)):
    user = list_of_lists[i][0]
    if register_user.lower() == user:
      print(f" {red}TÊN NÀY ĐÃ TỒN TẠI {white}!!")
      sleep(4)
      register()
    elif register_user.lower() == 'exit':
      os.sys.exit()
    elif len(register_user) < 5:
      print(f" {red}CHƯA ĐẠT YÊU CẦU {white}!!")
      sleep(3)
      register()
  else:
    register_password(register_user)
def load_data(i):
  list_of_lists = wks.get_all_values()
  user = list_of_lists[i][0]
  coin = list_of_lists[i][2]
  return coin, user
def change_coin(amount, i):
  list_of_lists = wks.get_all_values()
  coin = list_of_lists[i][2]
  cell = wks.cell(i+1, 3)
  new_coin = int(coin) + int(amount)
  cell.value = new_coin
  wks.update_cell(cell.row, cell.col, cell.value)
  return new_coin
def yn_csmm(i):
  x = input(f'Tiếp Tục ({red}Y{white}/{blue}n{white}): ')
  if x.lower() == 'y':
    clear()
    tra_quay_so(i)
  elif x.lower() == 'n':
    select_num(i)
  elif x.lower() == 'nn':
    os.sys.exit()
  else:
    animation()
    select_num(i)
def yn_minecoin(i):
  x = input(f'Tiếp Tục ({red}Y{white}/{blue}n{white}): ')
  if x.lower() == 'y':
    clear()
    mine_coin(i)
  elif x.lower() == 'n':
    select_num(i)
  elif x.lower() == 'nn':
    os.sys.exit()
  else:
    animation()
    select_num(i)
def chon_so(i):
  clear()
  show_csmm()
  coin, user = load_data(i)
  coin_value = int(coin)
  #coin_value1 = int(coin[0])
  print(f"{white}User: {pink}{user}")
  print(f"{white}Coin: {coin}{yellow} Xu\n{white}")
  if coin_value < 0:
    print(f"{red}BẠN ĐANG ÂM XU !!")
    animation_load()
    select_num(i)
  number = input(f"Chọn {red}Chẵn {white}or {blue}lẻ {white}(C/l): ")
  if number.lower() == 'c':
    number = 0
  elif number.lower() == 'l':
    number = 1
  elif number.lower() == 'n':
    select_num(i)
  else:
    print("Lựa Chọn Không Hợp Lệ")
    animation()
    tra_quay_so(i)
  Tien_Choi = input(f"Nhập Số {yellow}Xu {white}Chơi: ")
  if Tien_Choi.isdigit():
    int(Tien_Choi)
    if (int(Tien_Choi) < 0):
      print("Không Thể Cược Xu Âm")
      animation_load()
      tra_quay_so(i)
    if (coin_value >= int(Tien_Choi) and int(Tien_Choi) != 0):
      print(f"Bạn Đã Cược [{int(Tien_Choi):,} {yellow}Xu{white}]")
    elif (coin_value < int(Tien_Choi)):
      print("Không Đủ Xu")
      animation_load()
      select_num(i)
    elif (int(Tien_Choi) == 0):
      print("0 Xu Chơi Cái gì ba ??")
      animation_load()
      tra_quay_so(i)
    else:
      print("NHẬP SỐ !!!")
      animation()
      tra_quay_so(i)
  elif (Tien_Choi == 'allin'):
    Tien_Choi = coin_value
    print(f"Bạn Đã Cược Tất Tay [{money:,} {yellow}Xu{white}]")
  elif (Tien_Choi == 'all'):
    Tien_Choi = coin_value
    print(f"Bạn Đã Cược Tất Tay [{money:,} {yellow}Xu{white}]")
  elif (Tien_Choi.lower() == 'n'):
    animation()
    select_num()
  else:
    print("NHẬP SỐ !!!")
    animation()
    tra_quay_so(i)
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
def tra_quay_so(i):
  number, Tien_Choi = chon_so(i)
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
  change_coin(Tien_Choi, i)
  yn_csmm(i)
def mine_coin(i):
  clear()
  show_minecoin()
  coin, user = load_data(i)
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
      change_coin(xu_mine, i)
      formatted_time = time_set()
      coin, user = load_data(i)
      if (xu_mine >= 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow}Xu{white} | Tổng: "+str(coin)+f" {yellow}Xu{white}")
      elif (xu_mine < 1000):
        print(f"\n[{green}"+str(formatted_time)+f"{white}] +"+str(xu_mine)+f" {yellow} Xu{white} | Tổng: "+str(coin)+f" {yellow}Xu{white}")
      print("")
    yn_minecoin(i)
  elif Nblock.lower() == 'n':
    select_num(i)
  else:
    print(f" {red}Vui Lòng Nhập Số !!")
    animation_load()
    mine_coin(i)
def select_num(i):
  clear()
  show_banner()
  coin, user = load_data(i)
  print(f"{white}User: {pink}{user}")
  print(f"{white}Coin: {coin}{yellow} Xu\n{white}")
  Chon = input("Chọn Chế Độ: ")
  if Chon.isdigit():
    if int(Chon) == 0:
      select_menu()
    elif int(Chon) == 1:
      tra_quay_so(i)
    elif int(Chon) == 2:
      print("1")
      mine_coin(i)
      print("2")
    elif int(Chon) == 3:
      pass
    else:
      print("Lựa Chọn Không Hợp Lệ")
      animation_load()
      select_num(i)
  else:
    print("Vui Lòng Nhập Số")
    animation_load()
    select_num(i)
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
      clear()
      show_menu_login()
      i = login()
      select_num(i)
    else:
      print(f" {red}Lựa Chọn Không Hợp Lệ !")
      sleep(2)
      select_menu()
  else:
    print(f" {red}Vui Lòng Nhập Số !")
    sleep(2)
    select_menu()
select_menu()
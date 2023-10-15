import os 
try:
  import gspread
except:
  os.system('pip install gspread')
os.system('python main.py' if os.name == "nt" else 'python3 main.py') 
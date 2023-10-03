import os 
try:
  import gspread
except:
  os.system('pip install gspread')
os.system('python MGD.PY' if os.name == "nt" else 'python3 MGD.PY')
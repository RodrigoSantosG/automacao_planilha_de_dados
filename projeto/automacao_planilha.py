import time
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui as pag

# aqui sera a configuração do google sheets
scope = ['https://spradshetts.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
planilha = gc.open_by_key('ID da planilha')
worksheet = planilha.worksheet('Nome da planilha')

# navegando ate o instagram
def instagram():
    drive = webdriver.Chrome(executable_path='caminho para o drive')
    drive.get('https://www.instagram.com/') # você pode por o nome do usuario depois do '/'
    time.sleep(5) # tempo de espera para pagina carregar
    return


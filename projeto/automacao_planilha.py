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
    return drive

# extraido dados dos videos e fotos do instagram
def extrair_dados(driver):
    # navegar ate o primeiro post
    try:
        driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()
        time.sleep(5) # esperar carregar a pagina
        curtidas = driver.find_element.by_xpanth('//button[contains(@class, "wpO6b")]/span').text
        comentarios = driver.find_element.by_xpanth('//button[contains(@class, "wpO6b")]/span').text
        visualizacoes = driver.find_element_by_xpath('//span[contains(@class, "vcOH2")]/span').text
        
        return curtidas, comentarios, visualizacoes
    except:
        print(f'Erro ao extrair dados')

        return None, None, None
    

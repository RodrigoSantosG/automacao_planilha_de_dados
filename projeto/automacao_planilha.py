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
planilha = gc.open_by_key(
                'https://docs.google.com/spreadsheets/d/1hWDhFLM1op9_QgSubUcC2g6BORkpbWxw/edit?gid=1739142090#gid=1739142090'
                         ) # ID da planilha

worksheet = planilha.worksheet('ENTREGA PODCAST') # Nome da Planilha

# navegando ate o instagram
def instagram():
    drive = webdriver.Chrome(executable_path='K9') # caminho para o Drive 
    drive.get('https://www.instagram.com/rodrigosantos.pv/')
             # você pode por o nome do usuario depois do '/' ex:("https://www.instagram.com/")
    
    time.sleep(5) # tempo de espera para pagina carregar
    return drive

# extraido dados dos videos e fotos do instagram
def extrair_dados(driver):
    # navegar ate o primeiro post
    try:
        driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()
        time.sleep(5) # esperar carregar a pagina
        link = driver.find_element_by_xpath('//button[contains(@class, "wpO6b")]/span').text
        likes = driver.find_element_by_xpath('//button[contains(@class, "wpO6b")]/span').text
        comentarios = driver.find_element_by_xpath('//button[contains(@class, "wpO6b")]/span').text
        visualizacoes = driver.find_element_by_xpath('//span[contains(@class, "vcOH2")]/span').text
        
        return link, likes, comentarios, visualizacoes
    except Exception as e:
        print(f'Erro ao extrair dados: {e}')

        return None, None, None, None

# atualizando a planilha 
def atualizar_planilha(link, likes, comentarios, visualizacoes):
    try:
        # Local onde você deseja colocar os dados na planilha ( A1, B1, C1)
        cell_link = worksheet.find("Link")
        cell_likes = worksheet.find("Likes")
        cell_comentarios = worksheet.find("Comentários")
        cell_visualizacoes = worksheet.find("Visualizações")
        
        worksheet.unhide_coll(cell_link.row, cell_link.col + 1, link)
        worksheet.update_cell(cell_likes.row, cell_likes.col + 1, likes)
        worksheet.update_cell(cell_comentarios.row, cell_comentarios.col + 1, comentarios)
        worksheet.update_cell(cell_visualizacoes.row, cell_visualizacoes.col + 1, visualizacoes)
        
        print("Dados atualizados na planilha.")
    except Exception as e:
        print(f"Erro ao atualizar planilha: {e}")

# Principal
def main():
    driver = instagram()
    while True:
        try:
            link, curtidas, comentarios, visualizacoes = extrair_dados(driver)
            if link and curtidas and comentarios and visualizacoes:
                atualizar_planilha(link, curtidas, comentarios, visualizacoes)
                time.sleep(2)
        except Exception as e:
            print(f'Erro ao processar: {e}')
        finally:
            driver.quit()
if __name__ == "_man_":
    main()





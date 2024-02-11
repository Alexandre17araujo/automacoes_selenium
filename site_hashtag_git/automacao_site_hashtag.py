from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Nova forma XPATH com Esperar um conteudo aparecer na tela
def funcional():
    site = 'https://hashtagtreinamentos.com'
    driver = webdriver.Chrome()
    elemento = driver.get(site)

    esperar_elemento = driver.implicitly_wait(20) #, driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()
    time.sleep(1)
    elemento2 = driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()

    elemento = driver.find_element(By.XPATH, '/html/body/div[1]/div[9]/div/div/form/div[1]/input').send_keys('Alexandre')
    elemento = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('litrix')
    elemento = driver.find_element(By.XPATH, '//*[@id="_form_173_"]/button').click()


#Forma Antiga
def forma_antiga():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    site = 'https://hashtagtreinamentos.com'
    driver = webdriver.Chrome()
    driver.get(site)

    elemento = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'e-font-icon-svg')))
    elemento.click()
    driver.find_element_by_XPATH('/html/body/div[1]/div[9]/div/div/form/div[1]/input').send_keys('testeNome')
    driver.find_element_by_XPATH('//*[@id="email"]').send_keys('testeSenha')
    driver.find_element_By_XPATH('//*[@id="_form_173_"]/button').click()


# Forma Gabiarra "Não convencional"
def gambiarra():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    site = 'https://hashtagtreinamentos.com'
    driver = webdriver.Chrome()
    driver.get(site)

    time.sleep(15)
    elemento2 = driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()

    elemento = driver.find_element(By.XPATH, '/html/body/div[1]/div[9]/div/div/form/div[1]/input').send_keys('Alexandre')
    elemento = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('litrix')
    elemento = driver.find_element(By.XPATH, '//*[@id="_form_173_"]/button').click()

# Criando Loop
def forma_loop():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.get('https://hashtagtreinamentos.com')

    while len(driver.find_element(By.CLASS_NAME, 'e-font-icon-svg')) == 0:
        time.sleep(1)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()

if __name__ == '__main__':
    funcional()


#Dicas
# Ele pode ser tanto colocado um linha a cima e alinha de baixo vai rodar também ex:
#     esperar_elemento = driver.implicitly_wait(20)
#     elemento2 = driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()

# Ou a outra forma é colocando ele na mesma linha
# esperar_elemento = driver.implicitly_wait(20), driver.find_element(By.CLASS_NAME, 'e-font-icon-svg').click()
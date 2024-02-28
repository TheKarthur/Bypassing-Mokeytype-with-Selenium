import pyautogui as auto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

url = "https://monkeytype.com/"

try:
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "active.acceptAll")))
    element = driver.find_element(By.CLASS_NAME, "active.acceptAll")
    element.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wordsWrapper")))
    words = driver.find_element(By.ID, "wordsWrapper")
    words.click()    
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "word")))

    word_elements = driver.find_elements(By.CLASS_NAME, "word")

    time.sleep(1)

    start_time = time.time()  # Tempo inicial

    for word_element in word_elements:
        texto = word_element.text
        auto.typewrite(texto + ' ')
        print(texto)
    
    while True:
        last_element = word_elements[-1]
        new_word_elements = last_element.find_elements(By.XPATH, "./following-sibling::div[contains(@class, 'word')]")

        for new_word_element in new_word_elements:
            texto = new_word_element.text
            auto.typewrite(texto + ' ')
            print(texto)

        word_elements.extend(new_word_elements)
        
        # Verifica se já passaram 30 segundos
        if time.time() - start_time >= 30:
            break
    
except Exception as e:
    print('Erro:', e)

input("Pressione Enter para fechar o navegador...")

driver.quit()

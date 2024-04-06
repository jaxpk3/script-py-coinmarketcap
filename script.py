# Este script abre coinmarketcap.com y luego recoge los diamantes diarios
import os
import time  # Importa el módulo time para utilizar time.sleep()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el navegador (aquí estamos usando Chrome, asegúrate de tener chromedriver instalado y en tu PATH)
driver = webdriver.Chrome()





try:
    # Abre la página de CoinMarketCap
    driver.get("https://coinmarketcap.com/")

    # Encuentra y haz clic en el elemento SVG con la clase "sc-aef7b723-0"
    svg_element = WebDriverWait(driver, 20).until(
        #EC.element_to_be_clickable((By.CLASS_NAME, "sc-aef7b723-0"))
        #EC.element_to_be_clickable((By.XPATH, '//svg[@xmlns="http://www.w3.org/2000/svg"]'))
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="sc-aef7b723-0 fKbUaI sc-7f34465f-0 jWBlfU"]'))
    )
    svg_element.click()

    # Espera a que aparezca el botón de inicio de sesión por el atributo data-btnname
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-btnname="Log In"]'))
    )
    login_button.click()

    # Espera a que aparezcan los campos de correo electrónico y contraseña
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "email-input"))
    )
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "password-input"))
    )

    # Ingresa tu correo electrónico y contraseña
    email_input.send_keys("jaxpk3@gmail.com")
    password_input.send_keys("!Joel183729")

    # Envía el formulario de inicio de sesión
    #password_input.submit()



    # Espera hasta que el elemento div con el texto "Log In" sea visible y clickeable
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-f70bb44c-0 iQEJet BaseButton_labelWrapper__wzpX7" and text()="Log In"]'))
    )

    # Utiliza JavaScript para hacer clic en el elemento
    driver.execute_script("arguments[0].click();", login_button)




    
    # Esperar 5 segundos antes de continuar
    time.sleep(5)

    # Ahora la sesión está iniciada, puedes continuar con otras acciones después de iniciar sesión



    # Encuentra y haz clic en el enlace "My Diamonds" utilizando un selector CSS específico
    diamonds_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/account/my-diamonds/"]'))
    )
    diamonds_link.click()

    
    # Esperar 5 segundos antes de continuar
    time.sleep(5)





    # Encuentra y haz clic en la imagen específica utilizando un selector CSS basado en el atributo 'src'
    diamond_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="https://s2.coinmarketcap.com/static/cloud/img/loyalty-program/diamond-icon.svg"]'))
    )
    diamond_icon.click()




    
    # Esperar 5 segundos antes de continuar
    time.sleep(5)



    # Espera hasta que el elemento div con el texto "Collect" sea visible y clickeable
    collect_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-f70bb44c-0 iQEJet BaseButton_labelWrapper__wzpX7" and text()="Collect"]'))
    )

    # Utiliza JavaScript para hacer clic en el elemento
    driver.execute_script("arguments[0].click();", collect_button)





finally:
    # Cierra el navegador al finalizar
    driver.quit()

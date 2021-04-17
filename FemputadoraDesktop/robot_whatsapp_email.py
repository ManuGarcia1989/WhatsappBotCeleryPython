from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait


class whatsapp:

    def iniciar_whatsapp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(15)
        print("abrio webdriver")

    def fin_whatsapp(self):
        self.driver.quit()

    def enviarTexto(self, num, msg):
        url = "https://api.whatsapp.com/send?phone=" + num
        self.driver.get(url)
        driver_group = self.driver
        mensaje = WebDriverWait(driver_group, 10).until(
            lambda driver: driver.find_element_by_xpath(
                '//*[@id="action-button"]'))
        mensaje.click()
        time.sleep(4)
        e = 0
        use_web = WebDriverWait(driver_group, 10).until(
            lambda driver: driver.find_element_by_xpath(
                '//*[@id="content"]/div/div/div/a'))
        use_web.click()
        use_web.send_keys(Keys.ENTER)
        print("lo encontreee")
        try:

            texterror = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    "//*[contains(text(),'El número de teléfono compartido a través de la dirección URL es inválido')]"))

            errortel = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    "//*[@role='button']"))
            time.sleep(3)
            print("El número de teléfono compartido a través de la dirección URL es inválido")
            errortel.click()
            e = 1
        except:

            print("Si existe el numero")
            pass
        if e == 0:
            msg_box = WebDriverWait(driver_group, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[2]/div'))
            msg_box.send_keys(msg)
            env_bot = WebDriverWait(driver_group, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[3]/button'))
            env_bot.click()
            time.sleep(3)



    def enviarFoto(self, num, mensajess, adjunto):
        url = "https://api.whatsapp.com/send?phone=" + num
        self.driver.get(url)
        driver_group = self.driver
        mensaje = WebDriverWait(driver_group, 10).until(
            lambda driver: driver.find_element_by_xpath(
                '//*[@id="action-button"]'))
        mensaje.click()
        use_web = WebDriverWait(driver_group, 10).until(
            lambda driver: driver.find_element_by_xpath(
                '//*[@id="content"]/div/div/div/a'))
        use_web.click()
        time.sleep(4)
        e = 0
        try:
            texterror = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    "//*[contains(text(),'El número de teléfono compartido a través de la dirección URL es inválido')]"))

            errortel = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    "//*[@role='button']"))
            time.sleep(3)
            print("El número de teléfono compartido a través de la dirección URL es inválido")
            errortel.click()
            e = 1
        except:
            print("si hay numero")
            pass

        if e == 0:
            adjuntos = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="main"]/header/div[3]/div/div[2]/div'))

            adjuntos.click()
            imagen = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'))


            direccion = "C:\\FemputadoraDesktop\\" + adjunto
            imagen.send_keys(direccion)
            time.sleep(5)
            try:
                msg_box = WebDriverWait(driver_group, 3).until(
                    lambda driver: driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]'))
                msg_box.send_keys(mensajess)

            except:
                pass
            enviar = WebDriverWait(driver_group, 10).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div'))


            enviar.click()
            time.sleep(5)


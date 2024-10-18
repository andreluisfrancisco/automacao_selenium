from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def encontrar_elemento(self, *localizador):
        return self.driver.find_element(*localizador)

    def aguardar_elemento(self, localizador, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(localizador)
        )

    def clicar_elemento(self, *localizador):
        elemento = self.encontrar_elemento(*localizador)
        elemento.click()

from selenium.webdriver.common.by import By
from automacao_selenium.pages.base_pages import BasePage

class VehicleDataPage(BasePage):
    MAKE_DROPDOWN = (By.ID, "make")
    ENGINE_PERFORMANCE = (By.ID, "engineperformance")
    NEXT_BUTTON = (By.ID, "nextenterinsurantdata")

    def selecionar_marca(self, marca):
        dropdown = self.encontrar_elemento(*self.MAKE_DROPDOWN)
        dropdown.send_keys(marca)

    def preencher_performance_motor(self, performance):
        self.encontrar_elemento(*self.ENGINE_PERFORMANCE).send_keys(performance)

    def clicar_proximo(self):
        self.clicar_elemento(*self.NEXT_BUTTON)

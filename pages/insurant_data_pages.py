from selenium.webdriver.common.by import By
from automacao_selenium.pages.base_pages import BasePage

class InsurantDataPage(BasePage):
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    BIRTHDATE = (By.ID, "birthdate")
    NEXT_BUTTON = (By.ID, "nextenterproductdata")

    def preencher_primeiro_nome(self, primeiro_nome):
        self.encontrar_elemento(*self.FIRST_NAME).send_keys(primeiro_nome)

    def preencher_ultimo_nome(self, ultimo_nome):
        self.encontrar_elemento(*self.LAST_NAME).send_keys(ultimo_nome)

    def preencher_data_nascimento(self, data_nascimento):
        self.encontrar_elemento(*self.BIRTHDATE).send_keys(data_nascimento)

    def clicar_proximo(self):
        self.clicar_elemento(*self.NEXT_BUTTON)

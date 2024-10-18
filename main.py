import os
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from formulario import VehicleDataForm, InsurantDataForm

class FormularioAutomatizado:
    def __init__(self):
        self.driver = self._inicializar_driver()

    def _inicializar_driver(self):
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    
    def gerar_evidencia(self, etapa):
        hora_evidencia = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_evidencias = f"evidencias/{etapa}_{hora_evidencia}.png"
        os.makedirs(os.path.dirname(caminho_evidencias), exist_ok=True)
        self.driver.save_screenshot(caminho_evidencias)

    def abrir_site(self, url):      
        print(f"Abrindo o site {url}...")
        self.driver.get(url)        

    def aguardar_elemento(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
            print(f"Elemento '{value}' encontrado.")            
        except Exception as e:
            print(f"Erro ao aguardar o elemento '{value}': {e}")
            self.fechar_navegador()
            sys.exit(1)

    def preencher_dados_veiculo(self):
        form_veiculo = VehicleDataForm(self.driver)
        form_veiculo.selecionar_marca("Audi")
        form_veiculo.preencher_performance_motor("440")
        time.sleep(1)
        self.gerar_evidencia("Dados do veículo preenchidos")
        print("Preencheu os dados do veículo e passou para o próximo formulário.")
        form_veiculo.clicar_proximo()

    def preencher_dados_usuario(self):
        form_usuario = InsurantDataForm(self.driver)
        form_usuario.preencher_primeiro_nome("Andre")
        form_usuario.preencher_ultimo_nome("Francisco")
        form_usuario.preencher_data_nascimento("02/11/1974")
        time.sleep(1)
        self.gerar_evidencia("Dados do usuário preenchidos")
        print("Preencheu os dados do usuário e passou para o próximo formulário.")
        form_usuario.clicar_proximo()

    def fechar_navegador(self):
        print('Pausa por 10 segundos e fecha o navegador...')
        time.sleep(10)
        self.driver.quit()

def main():
    formulario = FormularioAutomatizado()
    formulario.abrir_site("http://sampleapp.tricentis.com/101/app.php")

    formulario.aguardar_elemento(By.ID, "make")
    formulario.preencher_dados_veiculo()

    formulario.aguardar_elemento(By.ID, "firstname")
    formulario.preencher_dados_usuario()

    print("Formulário preenchido com sucesso!")
    formulario.fechar_navegador()

if __name__ == "__main__":
    main()

# TODO: Inserir testes com o PyTest
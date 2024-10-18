### Automação de formulário com Selenium

## Descrição
Este projeto é um script de automação que preenche um formulário web utilizando Selenium e captura evidências durante o processo. O objetivo é demonstrar minhas habilidades em RPA

# Estrutura do projeto
- **`/formulario/`**: Contém os módulos que representam as páginas do formulário

- **`main.py`**: Arquivo principal que inicializa o navegador, executa o fluxo de automação e gera evidências

- **`/evidencias/`**: Pasta onde serão salvas as evidências de cada etapa em formato de captura de tela

- **`requirements.txt`**: Lista de dependências do projeto.

## Como configurar e executar
Pré-requisitos
Python 3.x instalado
pip
Google Chrome instalado (o Selenium usará o Chrome para automação)
Chromedriver será gerenciado automaticamente com o pacote webdriver_manager

## Passo a passo
Clone o repositório:
git clone https://github.com/andreluisfrancisco/automacao_selenium.git
cd automacao_selenium

Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  #No Windows

Instale as dependências:
pip install -r requirements.txt

Execute o script:
python main.py
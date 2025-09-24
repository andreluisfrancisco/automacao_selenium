# 🤖 Automação Selenium

![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-automation-brightgreen.svg)

## 📖 Descrição

Este projeto automatiza a navegação em páginas web utilizando **Selenium**.  
Foi desenvolvido para testes funcionais, raspagem de dados e automação de processos repetitivos em aplicações web.

## 🛠️ Tecnologias

- Python 3.10+
- Selenium
- WebDriver (Chrome/Firefox)
- Pandas (opcional para salvar os dados)

## 📂 Estrutura do Projeto

```
├── src/
│   ├── main.py         # Script principal de automação
│   ├── scraper.py      # Funções auxiliares de raspagem
│   └── utils.py        # Funções de suporte
├── tests/              # Testes unitários (pytest)
├── requirements.txt    # Dependências
├── .gitignore
└── README.md
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/andreluisfrancisco/selenium-automation.git
cd selenium-automation
```

Crie o ambiente virtual e instale dependências:

```bash
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## ▶️ Uso

### Exemplo: Abrir um site e coletar dados

```bash
python src/main.py --url https://example.com --output resultado.csv
```

### Exemplo em Python:

```python
from src.scraper import coletar_dados

dados = coletar_dados("https://example.com")
print(dados)
```

## ✅ Testes

```bash
pytest tests/
```

## 📊 Exemplos / Demonstração

## 📌 Roadmap

- [x] Abrir página e navegar em elementos
- [x] Raspagem de dados com Selenium
- [ ] Integração com Pandas para exportação de CSV
- [ ] Pipeline de CI/CD no GitHub Actions

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma _issue_ para discutir melhorias ou envie um _pull request_.

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 👨‍💻 Autor

**André Luis Francisco**  
[![GitHub](https://img.shields.io/badge/GitHub-andreluisfrancisco-black?logo=github)](https://github.com/andreluisfrancisco)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?logo=linkedin)](https://www.linkedin.com/in/seu-perfil/)

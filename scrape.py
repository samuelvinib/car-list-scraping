import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scrape:
    def __init__(self):
        self.driver = None

    def WebScraper(self):
        self.driver = self._init_driver()
        self.driver.get("https://veiculos.fipe.org.br/")

        try:
            time.sleep(0.5)

            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@data-label='carro']"))
            )
            element.click()

            time.sleep(0.5)
            # marca do carro
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='selectMarcacarro_chosen']"))
            )
            element.click()

            li_marcas = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#selectMarcacarro_chosen .chosen-results li"))
            )
            random_number = random.randint(0, len(li_marcas) - 1)
            li_marcas[random_number].click()

            # Escolher modelo do carro
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='selectAnoModelocarro_chosen']"))
            )
            element.click()

            li_modelos = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#selectAnoModelocarro_chosen .chosen-results li"))
            )
            random_number = random.randint(0, len(li_modelos) - 1)
            li_modelos[random_number].click()

            # Escolher ano modelo do carro
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='selectAnocarro_chosen']"))
            )
            element.click()

            li_anos = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#selectAnocarro_chosen .chosen-results li"))
            )
            random_number = random.randint(0, len(li_anos) - 1)
            li_anos[random_number].click()

            # Clicar no botão de enviar
            send_button = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#buttonPesquisarcarro"))
            )
            send_button.click()

            # Esperar até que todos os elementos estejam presentes na página
            table_rows = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#resultadoConsultacarroFiltros table tbody tr"))
            )

            # Criar um dicionário para armazenar os dados da tabela
            objeto = {}

            # Iterar sobre as linhas da tabela
            for row in table_rows:
                # Extrair o texto das células da linha
                cells = row.find_elements(By.CSS_SELECTOR, "td")
                if len(cells) == 2:
                    chave = cells[0].text.strip()
                    valor = cells[1].text.strip()
                    objeto[chave] = valor

            self.driver.quit()

            price = objeto['Preço Médio'].replace('R$ ', '').replace('.', '').replace(',', '.')
            data = {
                "modelo": objeto['Modelo:'],
                "codigo_fipe": objeto['Código Fipe:'],
                "preco_medio": float(price)
            }
            print("Carro adicionado:")
            print(data)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")

    def _init_driver(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")  # Executar em modo headless
        return webdriver.Firefox(options=firefox_options)

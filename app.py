from scrape import Scrape
from service import DatabaseService

def main():
    print("Aplicação iniciada!")
    print("Aguarde até o fim do processo.")
    for _ in range(10):
        scraper = Scrape()
        data = scraper.WebScraper()
        if data:
            service = DatabaseService()
            service.save_car(data['modelo'], data['codigo_fipe'], data['preco_medio'])
        else:
            print("An error occurred while scraping data.")
            return
    print("Aplicação finalizada!")
    print("10 Veículos foram adicionados com sucesso!")

if __name__ == '__main__':
    main()

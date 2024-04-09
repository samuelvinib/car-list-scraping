from flask import Flask, jsonify
from scrape import Scrape
from service import DatabaseService

app = Flask(__name__)

@app.route('/')
def index():
    cars = []
    for _ in range(10):
        scraper = Scrape()
        data = scraper.WebScraper()
        cars.append(data)
        if data:
            service = DatabaseService()
            service.save_car(data['modelo'], data['codigo_fipe'], data['preco_medio'])
        else:
            return jsonify({"error": "An error occurred while scraping data."}), 500
    return cars

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

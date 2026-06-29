import requests
from bs4 import BeautifulSoup
import time
import json
import os

class crawl:
    def __init__(self):
        self.url = ["https://sport.detik.com/moto-gp/d-7369409/klasemen-motogp-2024-usai-sprint-race-italia",
                    "https://sport.detik.com/moto-gp/d-7369247/hasil-sprint-race-motogp-italia-2024-bagnaia-juara-marquez-kedua",
                    "https://sport.detik.com/moto-gp/d-7369147/acosta-resmi-gabung-ktm-untuk-motogp-2025",
                    "https://sport.detik.com/moto-gp/d-7368917/hasil-fp2-motogp-italia-bagnaia-tercepat-ungguli-marc-marquez",
                    "https://sport.detik.com/moto-gp/d-7368617/jadwal-motogp-italia-2024-sore-ini-kualifikasi-malamnya-sprint-race",
                    "https://sport.detik.com/moto-gp/d-7368423/motogp-italia-2024-ganggu-alex-marquez-bagnaia-kena-penalti-3-grid",
                    "https://sport.detik.com/moto-gp/d-7368350/keras-pramac-ducati-balas-pernyataan-marc-marquez",
                    "https://sport.detik.com/moto-gp/d-7370473/bagnaia-tanpa-cela-bastianini-bikin-patah-hati-marquez-dan-martin",
                    "https://sport.detik.com/moto-gp/d-7370489/klasemen-motogp-2024-bagnaia-pangkas-jarak-dari-jorge-martin",
                    "https://sport.detik.com/moto-gp/d-7370441/motogp-italia-2024-bagnaia-menang-ducati-berpesta-di-kandang",
                    "https://sport.detik.com/moto-gp/d-7370436/hasil-motogp-italia-2024-francesco-bagnaia-juara-di-tanahnya",
                    "https://sport.detik.com/moto-gp/d-7370401/motogp-italia-2024-balapan-dimulai-bagnaia-gaspol-terdepan",
                    "https://sport.detik.com/moto-gp/d-7370063/motogp-italia-marc-marquez-sebut-sebut-kelebihan-desmosedici-gp24",
                    "https://sport.detik.com/moto-gp/d-7370028/starting-grid-motogp-italia-2024-martin-pertama-marc-marquez-ketiga",
                    "https://sport.detik.com/moto-gp/d-7369671/jadwal-motogp-italia-2024-balapan-utama-malam-ini",
                    "https://sport.detik.com/moto-gp/d-7372631/resmi-jorge-martin-gabung-aprilia-di-motogp-2025",
                    "https://sport.detik.com/moto-gp/d-7372556/marquez-akan-jadi-tandem-bagnaia-musim-depan",
                    "https://sport.detik.com/moto-gp/d-7372367/target-bagnaia-selanjutnya-samai-torehan-casey-stoner-di-assen",
                    "https://sport.detik.com/moto-gp/d-7371648/marc-marquez-menyerah-kejar-podium-usai-disalip-bastianini",
                    "https://sport.detik.com/moto-gp/d-7371484/jorge-martin-nggak-bisa-fokus-100-di-motogp-italia-2024",
                    "https://sport.detik.com/moto-gp/d-7371443/rentetan-raihan-podium-berhenti-marc-marquez-janji",
                    "https://sport.detik.com/moto-gp/d-7371377/jorge-martin-akui-bikin-kesalahan-bodoh-usai-disalip-bastianini",
                    "https://sport.detik.com/moto-gp/d-7371030/marc-marquez-bastianini-seperti-roket",
                    "https://sport.detik.com/moto-gp/d-7370922/bisik-bisik-rossi-ke-bagnaia-sebelum-race-motogp-italia",
                    "https://sport.detik.com/moto-gp/d-7370835/dulu-valentino-rossi-kini-francesco-bagnaia-penguasa-mugello"
                    ]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }

    def get_data(self):

        data_articles = []
        for url_link in self.url:
            data = self._get_article(url_link)
            data_articles.append(data)
            time.sleep(2)
        

        filename = "articles.json"
        try:
            articles = []
            if os.path.exists(filename):
                os.remove(filename)
            else:
                articles = []
            articles.append(data_articles)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=2)
        except:
            print('error')
    
    def _get_article(self, url):
        try:
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                judul = soup.find('h1', class_='detail__title').text.strip() if soup.find('h1', class_='detail__title') else "Judul tidak ditemukan"
                body_berita = soup.find('div', class_='detail__body-text')
                if body_berita:
                    paragraf = [p.text.strip() for p in body_berita.find_all('p')]
                    isi_berita = "\n".join(paragraf)
                else:
                    isi_berita = "berita tidak ditemukan"

                return {"title":judul, "content":isi_berita}
            else:
                return {"title":"none", "content":"none"}
        except:
            print("terjadi kesalahan 404")

    def __create_file(self, content):
        
        if content["title"] == "none":
            return
        
        data = {
            "title": content["title"],
            "content": content["content"]
        }

        
        




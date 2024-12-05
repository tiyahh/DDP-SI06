class Gempa:
    # konstruktor insialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #  mathod penentu skala
    def dampak(self):
        # logika/statement
        if self.skala < 2:
            print('Gempa tidak berasa')

        elif 2 <= self.skala <= 4:
            print('Gempa Berdampak Bangunan Retak')
        
        elif 4 <= self.skala <= 6:
            print('Gempa Berdampak Bangunan Roboh')
        
        elif self.skala > 6:
            print('Gempa Besar Berpotennsi Tsunami')

        # menampilkan lokasi dan skala gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')


    
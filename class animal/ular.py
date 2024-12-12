from animal import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, warnaUlar, jenisUlar):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.warna = warnaUlar
        self.jenis = jenisUlar

    def cetak_ular(self):
        super().cetak()
        print(f'ular ini berwarna{self.warna} dan jenis ular ini adalah {self.jenis}')

print('\n--------------hewan ular--------------')
kobra = ular('ular kobra', 'hewan', 'darat', 'bertelur', 'hitam', 'berbisa')
sanca = ular('ular sanca', 'mamalia kecil', 'semak', 'bertelur', 'hijau', 'berbisa')

kobra.cetak_ular()
sanca.cetak_ular()
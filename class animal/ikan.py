from animal import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, warnaIkan, jenisIkan):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.warna = warnaIkan
        self.jenis = jenisIkan

    def cetak_ikan(self):
        super().cetak()
        print(f'ikan ini berwarna{self.warna} dan jenis ikan ini adalah ikan{self.jenis}')

print('\n----------hewan ikan-----------')
paus = ikan('ikan paus', 'ikan', 'air', 'beranak', 'biru', 'air laut')
paus.cetak_ikan()

nemo = ikan('ikan Nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut,')
nemo.cetak_ikan()
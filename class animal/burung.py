from animal import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenisBulu, bunyi):
       super().__init__(nama, makanan, hidup, berkembangBiak)
       self.jenisBulu = jenisBulu
       self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenisBulu}, dan hewan ini berbunyi {self.bunyi}')

print('\n-------------cetak burung--------------')
beo = burung('Burung Beo', 'biji-bijian', 'udara', 'bertelur', 'biru dan orange', 'kamu jelek')
beo.cetak_burung()
elang = burung('Burung Elang', 'Mamalia', 'pohon', 'bertelur', 'coklat', 'kwakk')
elang.cetak_burung()



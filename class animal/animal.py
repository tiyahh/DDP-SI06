class animal:
    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self. hidup = hidup
        self.berkembangBiak = berkembangBiak

    print('----------------animal-------------')
    def cetak(self):
        print(f'hewan {self.nama} ini memakan {self.makanan}, hewan ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembangBiak}')

c1= animal('buaya', 'daging', 'amfibi', 'bertelur')
h2= animal('kucing', 'wishkas', 'darat', 'beranak')

c1.cetak()
h2.cetak()
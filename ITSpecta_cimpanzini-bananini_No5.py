stok = int()
pendapatan = int()

def tambahStok():
    stok += 100
    for i in range(70):
        pendapatan += 55000 - 50000
    for i in range(30):
        pendapatan += 50 * 1500 - 50000

def tampilStok():
    print("Stok: ", stok, "kilo")

def tampilPendapatan():
    print("Pendapatan: Rp", pendapatan)

while(True):
    pilihan = int(input("1. Tambah stok\n2.Tampilkan total stok\n3.Tampilkan Pendapatan Bersih"))
    if pilihan < 1 or pilihan > 3:
        continue
    if pilihan == 1:
        tambahStok()
    elif pilihan == 2:
        tampilStok()
    elif pilihan == 3:
        tampilPendapatan()

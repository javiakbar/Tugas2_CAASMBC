print("## Program Python Diskon Potongan Harga ##")
print("==========================================")
print("")

harga_belanja = int(input("Total Belanja: Rp"))

if (harga_belanja >= 100000) and (harga_belanja < 500000):
    harga_total = harga_belanja - (0.1 * harga_belanja)
    print("Selamat Anda mendapat diskon 10%")
elif (harga_belanja >= 500000) and (harga_belanja < 1000000):
    harga_total = harga_belanja - (0.2 * harga_belanja)
    print("Selamat Anda mendapat diskon 20%")
elif (harga_belanja > 1000000): 
    harga_total = harga_belanja - (0.3 * harga_belanja)
    print("Selamat Anda mendapat diskon 30%")

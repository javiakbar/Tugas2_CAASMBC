print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print("")

nama_karyawan = input("Nama Karyawan: ")
golongan = input("Golongan: ")
jam_kerja = float(input("Total jam kerja: "))

upah_per_jam = 0
if golongan == 'A':
    upah_per_jam = 5000
elif golongan == 'B':
    upah_per_jam = 7000
elif golongan == 'C':
    upah_per_jam = 8000
elif golongan == 'D':
    upah_per_jam = 10000
else:
  print("Golongan yang dimasukkan salah")

if jam_kerja > 48:
    uang_lembur = (jam_kerja - 48) * 4000
else:
    uang_lembur = 0
gaji = upah_per_jam + uang_lembur

print("")
print(nama_karyawan, "menerima gaji Rp.", gaji,"/minggu")

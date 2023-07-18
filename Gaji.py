print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print("")

nama_karyawan = input("Nama Karyawan: ")
golongan = input("Golongan: ")
jam_kerja = float(input("Total jam kerja: "))

upah_per_jam = 0
if golongan == 'A':
    upah_per_jam = 5000
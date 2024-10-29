print("///LIST PENERBANGAN THOMS AIR///")
print("Kode Penerbangan | Tujuan | Harga Tiket")
print("========================================")
print("TA01             | AS     | 1.500.000")
print("TA02             | JPN     | 1.400.000")
print("TA03             | US     | 1.300.000")
print("TA04             | CHN     | 1.200.000")
print("========================================")
nama=input("Nama Pembeli: ")
nomor=input("Nomor Handphone: ")
asal=input("Asal Kota: ")
jurusan=input("Masukan Kode Tujuan: ")
tujuan=[]
harga=[]
if jurusan == "TA01" :
    tujuan.append("AMERIKA SERIKAT")
    harga = 1500000
elif jurusan == "TA02" :
    tujuan.append("JEPANG")
    harga = 1400000
elif jurusan == "TA03" :
    tujuan.append("AUSTRALIA")
    harga = 1300000
elif jurusan == "TA04" :
    tujuan.append("CHINA")
    harga = 1200000
else:
    tujuan=print("koode salah")

jumlah =int(input("Masukan Jumlah Beli Tiket: "))
if jumlah >=3:
         potongan = int(jumlah*harga)*0.7
else:
         potongan=0
total_bayar=int(jumlah*harga-potongan)

print("=========================================")

print("/// PENERBANGAN THOMS AIR ///")

print("Nama Anda:", nama)
print("Asal Kota Anda:",asal)
print("Kode Tujuan Negara yang anda tuju:", jurusan)
print("Tujuan Negara yang Ingin Anda Tuju:",tujuan)
print("Jumlah Beli Tiket:",jumlah)
print("=========================================")
print("Harga Tiket : Rp.",harga)
print("potongan harga: Rp.", potongan)
print("/// PELUNASAN PEMBAYARAN TIKET ///")
print("Total Pembayaran: Rp.",total_bayar)
uang=int(input("Masukan Pembayaran: Rp."))
print("=========================================")
kembalian = uang-total_bayar
print("Uang Kembalian: Rp.", kembalian)
print("=======================================")
print("TRIMAKASIH, SEMOGA SELAMAT SAMPAI TUJUAN")







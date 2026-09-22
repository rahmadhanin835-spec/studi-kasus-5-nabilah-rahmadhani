def biaya_kamar(jenis_kamar, durasi):
    if jenis_kamar == "Standard":
        biaya = 200000
    elif jenis_kamar == "Deluxe":
        biaya = 350000
    else:
        print("Pilihan kamar tidak valid")
        return 

    total = biaya * durasi
    return total

print("===== Selamat Datang di Hotel Astrava =====")
jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
check_in = int(input("Masukkan tanggal check-in : "))
check_out = int(input("Masukkan tanggal check-out : "))

durasi = check_out - check_in

total = biaya_kamar(jenis_kamar, durasi)

print("===== data pemesanan kamar ====")
print("Jenis kamar  :", jenis_kamar)
print("Check-in     :", check_in)
print("Check-out    :", check_out)
print("Lama menginap:", durasi, "malam")
print("Total biaya  :Rp", total)

print("====================================")
print("       PROGRAM APOTEK SEHAT")
print("====================================")

obat = {
    "1": ("Paracetamol", 5000),
    "2": ("Amoxicillin", 10000),
    "3": ("Antasida", 6000),
    "4": ("Vitamin C", 8000),
    "5": ("OBH Combi", 12000),
    "6": ("Ibuprofen", 7000),
    "7": ("CTM", 4000),
    "8": ("Antalgin", 9000),
    "9": ("Promag", 11000),
    "10": ("Betadine", 15000)
}

print("\nDAFTAR OBAT:")
for kode, data in obat.items():
    print(kode, data[0], "- Rp", data[1])

kode = input("\nMasukkan kode obat: ")

if kode in obat:
    nama, harga = obat[kode]

    jumlah = int(input("Masukkan jumlah obat: "))
    total = harga * jumlah

    print("\n====================================")
    print("          STRUK APOTEK")
    print("====================================")
    print("Nama obat :", nama)
    print("Harga     : Rp", harga)
    print("Jumlah    :", jumlah)
    print("Total     : Rp", total)

    if total >= 50000:
        print("Keterangan: Pembelian besar")
    elif total >= 20000:
        print("Keterangan: Pembelian sedang")
    else:
        print("Keterangan: Pembelian kecil")

else:
    print("Kode obat tidak ditemukan!")

print("====================================")
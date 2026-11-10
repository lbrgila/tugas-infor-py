
print("====================================")
print("   PROGRAM PASIEN RUMAH SAKIT")
print("====================================")

pasien = {
    "1": "Pasien Demam Berdarah",
    "2": "Pasien Tifus",
    "3": "Pasien Diabetes",
    "4": "Pasien Asma",
    "5": "Pasien Jantung",
    "6": "Pasien Pneumonia",
    "7": "Pasien Anemia",
    "8": "Pasien Usus Buntu",
    "9": "Pasien Stroke",
    "10": "Pasien Pasca Operasi"
}

print("\nDAFTAR JENIS PASIEN:")
for kode, nama in pasien.items():
    print(kode, ".", nama)

kode = input("\nMasukkan kode pasien: ")

if kode in pasien:
    nama = pasien[kode]

    lama = int(input("Lama opname (hari): "))

    print("\n====================================")
    print("       DATA PASIEN OPNAME")
    print("====================================")
    print("Jenis pasien :", nama)
    print("Lama opname  :", lama, "hari")

    if lama >= 14:
        print("Keterangan: Rawat inap jangka panjang")
    elif lama >= 7:
        print("Keterangan: Rawat inap jangka menengah")
    elif lama >= 1:
        print("Keterangan: Rawat inap jangka pendek")
    else:
        print("Keterangan: Lama opname tidak valid")

else:
    print("Kode pasien tidak ditemukan!")

print("====================================")
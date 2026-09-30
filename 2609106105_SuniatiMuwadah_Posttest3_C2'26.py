# Dokumentasi Git Add Commit Push
print("==========================================")
print("       RENTAL PLAYSTATION")
print("==========================================")

nama = input("Masukkan nama panggilan : ")
nim = input("Masukkan 2/3 digit terakhir NIM : ")

nama_benar = "Suniati"
nim_benar = "105"

if nama == nama_benar and nim == nim_benar:
    print("\nLogin berhasil!")
    print("Selamat datang,", nama)

    print("\n==========================================")
    print("           PILIHAN KONSOL")
    print("==========================================")
    print("1. PS4      - Rp10.000/jam")
    print("2. PS4 Pro  - Rp15.000/jam")
    print("3. PS5      - Rp20.000/jam")
    print("==========================================")

    pilihan = int(input("Pilih konsol (1-3) : "))

    if pilihan == 1:
        konsol = "PS4"
        harga_per_jam = 10000

    elif pilihan == 2:
        konsol = "PS4 Pro"
        harga_per_jam = 15000

    elif pilihan == 3:
        konsol = "PS5"
        harga_per_jam = 20000

    else:
        print("\nPilihan konsol tidak valid.")
        print("Program berhenti.")

    if pilihan >= 1 and pilihan <= 3:

        jam = int(input("Masukkan jumlah jam sewa : "))

        total_harga = harga_per_jam * jam

        if jam >= 5:
            persen_diskon = 0.08

        elif jam >= 3:
            persen_diskon = 0.05

        else:
            persen_diskon = 0

        diskon_durasi = persen_diskon * total_harga

        print("\n==========================================")
        print("          WAKTU PENYEWAAN")
        print("==========================================")
        print("1. Weekday")
        print("2. Weekend")
        print("==========================================")

        waktu = int(input("Pilih waktu (1-2) : "))

        if waktu == 1:
            jenis_waktu = "Weekday"
            biaya_weekend = 0

        elif waktu == 2:
            jenis_waktu = "Weekend"
            biaya_weekend = 0.10 * total_harga

        else:
            print("\nPilihan waktu tidak valid.")
            print("Program berhenti.")
            biaya_weekend = None

        if waktu == 1 or waktu == 2:
            total_bayar = total_harga - diskon_durasi + biaya_weekend

            print("\n==========================================")
            print("          STRUK RENTAL PLAYSTATION")
            print("==========================================")
            print("Nama Penyewa    :", nama)
            print("NIM             :", nim)
            print("Jenis Konsol    :", konsol)
            print("Waktu Sewa     :", jenis_waktu)
            print("Jumlah Jam      :", jam, "jam")
            print("Harga/Jam       : Rp{:,.0f}".format(harga_per_jam))
            print("------------------------------------------")
            print("Total Harga     : Rp{:,.0f}".format(total_harga))
            print("Diskon Durasi   : Rp{:,.0f}".format(diskon_durasi))
            print("Biaya Weekend   : Rp{:,.0f}".format(biaya_weekend))
            print("------------------------------------------")
            print("TOTAL BAYAR     : Rp{:,.0f}".format(total_bayar))
            print("==========================================")
            print("       Terima kasih!")
            print("==========================================")

else:
    print("\nLogin gagal!")
    print("Nama atau NIM tidak sesuai.")
    print("Program berhenti.")
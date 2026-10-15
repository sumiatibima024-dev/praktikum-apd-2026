import os

data_atm = [
    ["9999", "Sumi", 0, "admin"],
    ["1234", "Suniati", 500000, "user"],
    ["5678", "Suni", 750000, "user"]
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print("        APLIKASI SISTEM MESIN ATM        ")
    print("=" * 40)
    print("1. Login Akun")
    print("2. Register (Buat Rekening Baru)")
    print("3. Keluar Program")
    print("=" * 40)
    
    pilihan_menu = input("Silakan pilih menu (1-3): ")
    
    if pilihan_menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- HALAMAN LOGIN ATM ---")
        input_pin = input("Masukkan 4 digit PIN Anda: ")
        
        status_login = False
        indeks_user = -1
        
        for i in range(len(data_atm)):
            if data_atm[i][0] == input_pin:
                status_login = True
                indeks_user = i
                break
                
        if status_login:
            peran_pengguna = data_atm[indeks_user][3]
            nama_pengguna = data_atm[indeks_user][1]
            
            if peran_pengguna == "user":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"=== SELAMAT DATANG, {nama_pengguna.upper()} ===")
                    print("1. Cek Saldo (Read)")
                    print("2. Setor Tunai (Update)")
                    print("3. Tarik Tunai (Update)")
                    print("4. Logout (Keluar Akun)")
                    print("========================================")
                    
                    pilihan_user = input("Pilih menu nasabah (1-4): ")
                    
                    if pilihan_user == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- INFORMASI SALDO ---")
                        print(f"Nama Pemilik : {data_atm[indeks_user][1]}")
                        print(f"Saldo Saat Ini: Rp {data_atm[indeks_user][2]}")
                        input("\nTekan Enter untuk kembali ke menu...")
                    
                    elif pilihan_user == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- SETOR TUNAI ---")
                        nominal_str = input("Masukkan jumlah setor (angka): ")
                        
                        if nominal_str.isdigit():
                            nominal_int = int(nominal_str)
                            if nominal_int > 0:
                                data_atm[indeks_user][2] += nominal_int
                                print(f"\nSetor tunai berhasil! Saldo baru: Rp {data_atm[indeks_user][2]}")
                            else:
                                print("\nNominal harus lebih besar dari 0!")
                        else:
                            print("\nError: Input harus berupa angka valid!")
                        input("\nTekan Enter untuk kembali ke menu...")
                    
                    elif pilihan_user == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- TARIK TUNAI ---")
                        nominal_str = input("Masukkan jumlah penarikan (angka): ")
                        
                        if nominal_str.isdigit():
                            nominal_int = int(nominal_str)
                            if nominal_int <= 0:
                                print("\nNominal harus lebih besar dari 0!")
                            elif nominal_int > data_atm[indeks_user][2]:
                                print("\nTransaksi Gagal: Saldo Anda tidak mencukupi!")
                            else:
                                data_atm[indeks_user][2] -= nominal_int
                                print(f"\nTarik tunai berhasil! Sisa saldo: Rp {data_atm[indeks_user][2]}")
                        else:
                            print("\nError: Input harus berupa angka valid!")
                        input("\nTekan Enter untuk kembali ke menu...")
                    
                    elif pilihan_user == "4":
                        break
                    else:
                        print("\nPilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")

            elif peran_pengguna == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"=== PANEL KONTROL ADMIN ({nama_pengguna}) ===")
                    print("1. Lihat Semua Data Nasabah (Read)")
                    print("2. Hapus Akun Nasabah (Delete)")
                    print("3. Logout (Keluar Akun)")
                    print("=========================================")
                    
                    pilihan_admin = input("Pilih menu admin (1-3): ")
                    
                    if pilihan_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- DAFTAR SELURUH AKUN SISTEM ATM ---")
                        for idx in range(len(data_atm)):
                            akun = data_atm[idx]
                            print(f"{idx + 1}. PIN: {akun[0]} | Nama: {akun[1]} | Saldo: Rp {akun[2]} | Peran: {akun[3]}")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                    
                    elif pilihan_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("--- HAPUS AKUN NASABAH ---")
                        target_pin = input("Masukkan PIN akun nasabah yang akan dihapus: ")
                        
                        ditemukan = False
                        for idx in range(len(data_atm)):
                            if data_atm[idx][0] == target_pin:
                                ditemukan = True
                                if data_atm[idx][3] == "admin":
                                    print("\nPeringatan: Akun sesama admin tidak dapat dihapus!")
                                else:
                                    data_atm.pop(idx)
                                    print("\nAkun nasabah berhasil dihapus dari sistem!")
                                break
                        
                        if not ditemukan:
                            print("\nNomor PIN tersebut tidak ditemukan dalam sistem!")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                    
                    elif pilihan_admin == "3":
                        break
                    else:
                        print("\nPilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")
        else:
            print("\nPIN Salah atau Belum Terdaftar!")
            input("\nTekan Enter untuk kembali ke menu utama...")

    elif pilihan_menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- PENDAFTARAN REKENING BARU (REGISTER) ---")
        pin_baru = input("Buat PIN baru (harus angka): ")
        
        if not pin_baru.isdigit():
            print("\nError: PIN harus berupa karakter angka!")
        else:
            pin_sudah_ada = False
            for akun in data_atm:
                if akun[0] == pin_baru:
                    pin_sudah_ada = True
                    break
            
            if pin_sudah_ada:
                print("\nPendaftaran Gagal: PIN sudah digunakan oleh akun lain!")
            else:
                nama_baru = input("Masukkan Nama Lengkap Anda: ")
                saldo_awal_str = input("Masukkan Setoran Saldo Awal (angka): ")
                
                if saldo_awal_str.isdigit():
                    saldo_awal_int = int(saldo_awal_str)
                    if saldo_awal_int >= 0:
                        data_atm.append([pin_baru, nama_baru, saldo_awal_int, "user"])
                        print("\nPendaftaran akun berhasil! Silakan login melalui menu utama.")
                    else:
                        print("\nSetoran awal tidak boleh minus!")
                else:
                    print("\nError: Saldo awal harus berupa angka!")
        input("\nTekan Enter untuk kembali ke menu utama...")

    elif pilihan_menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan layanan Sistem Mesin ATM.")
        break
    else:
        print("\nPilihan menu tidak tersedia! Silakan pilih angka 1 sampai 3.")
        input("\nTekan Enter untuk mengulang...")
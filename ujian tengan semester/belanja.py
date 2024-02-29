nama_kopi = {
    "caffe americano": 37000,
    "caramel macchiato": 59000,
    "asian doice latte": 55000,
    "caramel latte": 52000,
    "vanila latte": 53000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,

}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in nama_kopi.items():
        print(f"{barang}: Rp{harga} per pesan") 
        
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukkan nama pesan yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if barang_dipilih.lower() == 'selesai':
             break
        if barang_dipilih not in nama_kopi:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa pesan {barang_dipilih} yang anda inginkan?"))
        total_belanja += nama_kopi[barang_dipilih] * jumlah
    print(f"total pesan anda adalah: Rp{total_belanja}")

    diskon = 0.15
    if jumlah > 350000:
       total_belanja =+ total_belanja * diskon

    ppn = 0.10
    total_belanja =+ total_belanja * ppn

    print(f"total belanja anda adalah: RP{total_belanja}")
         
belanja()     
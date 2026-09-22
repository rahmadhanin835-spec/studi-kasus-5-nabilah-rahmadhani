# studi-kasus-5-nabilah-rahmadhani

# kode program

<img width="523" height="394" alt="image" src="https://github.com/user-attachments/assets/ca7c8649-3313-487a-8f56-cc13913d0e10" />
<img width="410" height="47" alt="image" src="https://github.com/user-attachments/assets/3215bd5f-09c4-4276-bb4e-1bd00369d603" />

Kode program tersebut berfungsi untuk menghitung biaya pemesanan kamar di hotel astrava berdasarkan jenis kamar dan lama menginap. Program diawali dengan membuat function biaya_kamar(jenis_kamar, durasi) yang berfungsi untuk menentukan harga kamar sesuai jenis kamar yang dipilih. Jika user memilih kamar Standard, maka harga kamar sebesar Rp200.000 per malam, sedangkan kamar Deluxe memiliki harga Rp350.000 per malam. Jika user memasukkan jenis kamar selain kedua pilihan tersebut, program akan menampilkan pesan “Pilihan kamar tidak valid” dan menghentikan proses.

setelah function dibuat, program menampilkan ucapan selamat datang dan meminta user memasukkan jenis kamar, tanggal check-in, serta tanggal check-out. Data tanggal diubah menjadi tipe integer menggunakan int() agar dapat digunakan dalam operasi pengurangan. Lama menginap kemudian dihitung dengan rumus check_out - check_in.

Setelah mendapatkan lama menginap, program memanggil function biaya_kamar() untuk menghitung total biaya. Perhitungan dilakukan dengan mengalikan harga kamar per malam dengan jumlah malam menginap. lalu yang terakhir, program menampilkan data pemesanan yang meliputi jenis kamar, tanggal check-in, tanggal check-out, lama menginap, dan total biaya yang harus dibayarkan.

# output program
<img width="428" height="182" alt="Screenshot 2026-09-22 182442" src="https://github.com/user-attachments/assets/fd90299d-63e5-4d11-af36-1d5f7dbf2620" />

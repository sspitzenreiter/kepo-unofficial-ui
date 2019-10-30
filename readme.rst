###################
Kepo Unofficial UI
###################

Aplikasi ini ditunjukkan bagi anda yang sangat malas dengan input di CLI berulang tiap minggu. Saya terinspirasi membuat aplikasi dari malesnya ngetik di CLI dan kebetulan gabut. 

Aplikasi ini tidak resmi dari developer asli dari kepo melainkan dari user yang merasa gabut dan mau mencoba hal yang baru.

*******************
How To Config
*******************
Jika anda mau menggunakannya bersama kelompok dalam 1 pc, silahkan ikuti langkah berikut : :raw-html:'<br />'
1.	Edit file kepo_unofficial_ui_beta.py
2.	Setting config dimulai pada fungsi config (self)
3.	Lalu ganti self.type="personal" jadi self.type="kelompok"
4.	Setelah itu, isi semua informasi ketua dan anggota

Jika anda mau menggunakannya sendiri, silahkan ikuti langkah berikut : 
1.	Edit file kepo_unofficial_ui_beta.py
2.	Setting config dimulai pada fungsi config (self)
3.	Lalu isi self.type jadi "personal" bukan "kelompok"
4.	Setelah itu, isi semua informasi ketua. Anggota tidak perlu


Saat sudah melakukan hal tersebut, silahkan ikuti langkah berikut : 
1.	Copy file ke folder kepo
2.	Edit ui_run.bat
3. 	ganti <AnacondaDir> menjadi lokasi anaconda anda
4.	Lalu coba jalankan
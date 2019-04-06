impor os, sys

 print ( " \ 033 [1; 32mSilahkan Kirim Nama Pengguna & Kata Sandi Anda " )

 print ( " \ 033 [1; 32matau Mohon Hubungi IAmSyamsir " )

 username =  ' IAmSyamsir '      

 password =  ' Korekapi123 '



 def  restart ():

 	ngulang = sys.executable

 	os.execl (ngulang, ngulang, * sys.argv)



 def  main ():

 	uname =  raw_input ( " nama pengguna: " )

 	jika uname == nama pengguna:

 		pwd =  raw_input ( " kata sandi: " )



 		jika pwd == kata sandi:

 			print  " \ 033 [1; 32mAlhamdulillah sudah masuk juga .. " ,

 			sys.exit ()



 		lain :

 			cetak  " \ 033 [1; 32mMafaf Masukkan kata sandi Anda salah ... [?] \ 033 [00m "

 			cetak  " Silakan segera log-in kembali ... !! \ n "

 			mengulang kembali()



 	lain :

 		print  " \ 033 [1; 32mMafaf Masukkan Nama Pengguna Anda salah ... [?] \ 033 [00m "

 		cetak  " Silakan segera log-in kembali ... !! \ n "

 		mengulang kembali()



 coba :

 	utama()

 kecuali  KeyboardInterrupt :

 	os.system ( ' jelas ' )

 	mengulang kembali()
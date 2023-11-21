### IMPORT UTAMA ###
import requests,mechanize,bs4
### IMPORT PENDUKUNG ###
import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
\033[1;92m######################
\033[1;92m#      \033[1;96mSPAM SMS      \033[1;92m#
\033[1;92m######################
 \033[1;93m###### \033[1;92m####### \033[1;96m#####     Sumber Sc=Terbuka
\033[1;93m#      #   \033[1;92m#    \033[1;96m#   #     Github=https://github.com/SCAMM
\033[1;93m#      #   \033[1;92m#    \033[1;96m#####     Author=SCAM
\033[1;93m#      #   \033[1;92m#    \033[1;96m#     Status=Free
 \033[1;93m######    \033[1;92m#    \033[1;96m#     Versi=1.5.0
 \033[1;93mCATATAN= \033[1;92mSC HANYA BEKERJA PADA NOMOR \033[1;96mINDONESIA!!!
\033[1;93m1\033[1;96m=\033[1;97mOTP MATAHARI""")
		pilih=int(input('masukkan pilihan/> '))
		if pilih == 1:
			import src.matahari
		else: print("[!] PILIHAN TIDAK VALID(!!!)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))

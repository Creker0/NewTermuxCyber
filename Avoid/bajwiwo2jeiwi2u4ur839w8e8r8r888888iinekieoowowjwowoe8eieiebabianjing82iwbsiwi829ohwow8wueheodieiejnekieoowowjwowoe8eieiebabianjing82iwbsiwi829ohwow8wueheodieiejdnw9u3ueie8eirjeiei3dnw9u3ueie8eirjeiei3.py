# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#hay manusia udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6285608482684&text=Assalamualaikum')

def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Sudah punya ID dan Password nya? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN UNTUK MELANJUTKAN║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'channel mr.zomby' and user == 'subscribe':
      print '║LOGIN SUKSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login GAGAL, Silahkan hubungi ADMIN'
      time.sleep(1)
      wa()
      ressture()

def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        

ressture()
os.system('sh hsowkaksisisiaiowowkwkaiske')

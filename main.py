from requests import get
import curses 
from random import randint as rand
from time import time
from time import sleep
import os
from string import ascii_lowercase as chars

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(0)
w.timeout(100)

def clear_frame():
  for i in range(sh//8+1,sh-(sh//8)):
    w.addstr(i,sw//8+1,(sw-(sw//8)-(sw//8)-1)*' ')
curses.start_color()
curses.init_pair(1, curses.COLOR_RED,curses.COLOR_WHITE)
curses.init_pair(5, curses.COLOR_RED,curses.COLOR_RED)
curses.init_pair(7, curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(8, curses.COLOR_WHITE,curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_WHITE,curses.COLOR_RED)
curses.init_pair(2, curses.COLOR_WHITE,curses.COLOR_WHITE)
curses.init_pair(3, curses.COLOR_BLACK,curses.COLOR_WHITE)
curses.init_pair(4, curses.COLOR_GREEN,curses.COLOR_WHITE)
par1 = '''Military Strategists\nhave used simple-substitution\nciphers to encode their secret\n documents for thousands of years ago  '''
title = "HOW TO PLAY ?"
par2 = '''* You will be given \nan encrypted quote \nwhere each letter \nis replaced \nby a different letter'''
par3 = '''R -> A   O -> E   S -> D   E -> F'''
par4 = '''ROSES ARE RED\n__SES A_E _ED\nAE     A  A'''
par5 = '''* you can switch \nbetween curses by\n<- (LEFT KEY) (RIGHT KEY) ->'''
w.getch()
for i in range(sw//8,sw-(sw//8)):
  w.addch(sh//8,i,curses.ACS_CKBOARD,curses.color_pair(2))
  w.addch(sh-(sh//8),i,curses.ACS_CKBOARD,curses.color_pair(2))
for i in range(sh//8,sh-(sh//8)+1):
  w.addch(i,sw//8,curses.ACS_CKBOARD,curses.color_pair(2))
  w.addch(i,sw-(sw//8),curses.ACS_CKBOARD,curses.color_pair(2))
  w.addch(i,(sw//8)-1,curses.ACS_CKBOARD,curses.color_pair(2))
  w.addch(i,(sw-(sw//8))+1,curses.ACS_CKBOARD,curses.color_pair(2))

w.getch()
hei = (sh//8)+4
for line in par1.split('\n') :
  w.addstr(hei,sw//2-(len(line)//2),line)
  hei += 2

w.addch(sh-(sh//8)-3,sw//2-5,'•',curses.color_pair(7))
w.addch(sh-(sh//8)-3,sw//2,'•',curses.color_pair(8))
w.addch(sh-(sh//8)-3,sw//2+5,'•',curses.color_pair(8))
w.getch()
#sleep(3)
w.addstr(sh-(sh//8)-3,sw//2+13,'SKIP >',curses.color_pair(7))
while True:
  c = w.getch()
  if c != -1:
    break

clear_frame()

hei = (sh//8)+4
w.addstr(hei-2,sw//2-(len(title)//2),title)
for line in par2.split('\n') :
  w.addstr(hei,sw//2-(len(line)//2),line)
  hei += 2

w.addch(sh-(sh//8)-3,sw//2-5,'•',curses.color_pair(8))
w.addch(sh-(sh//8)-3,sw//2,'•',curses.color_pair(7))
w.addch(sh-(sh//8)-3,sw//2+5,'•',curses.color_pair(8))
w.getch()
#sleep(3)
w.addstr(sh-(sh//8)-3,sw//2+13,'SKIP >',curses.color_pair(7))
while True:
  c = w.getch()
  if c != -1:
    break

clear_frame()

hei = (sh//8)+4
w.addstr(hei-2,sw//2-(len(title)//2),title)
w.addstr(hei,sw//2-(len(par3)//2),par3)
hei += 2
for line in par4.split('\n') :
  w.addstr(hei,sw//2-(len(line)//2),line)
  hei += 1

w.addch(sh-(sh//8)-3,sw//2-5,'•',curses.color_pair(8))
w.addch(sh-(sh//8)-3,sw//2,'•',curses.color_pair(8))
w.addch(sh-(sh//8)-3,sw//2+5,'•',curses.color_pair(7))
w.addstr(sh-(sh//8)-3,sw//2+13,'NEXT >',curses.color_pair(7))
while True:
  c = w.getch()
  if c != -1:
    break
w.addstr(sh-(sh//8)-3,sw//2+13,'        ')
hei += 2
for line in par5.split('\n') :
  w.addstr(hei,sw//2-(len(line)//2),line)
  hei += 1
w.getch()
sleep(2)
w.addstr(sh-(sh//8)-3,sw//2+13,'PLAY >',curses.color_pair(7))
c = w.getch()
while c == -1 :
  c = w.getch()
  
def color():
	for i in range(sh):
		w.addstr(i,0,(sw-1)*'_',curses.color_pair(2))

def color_slide(charc):
  h = 6
  x = 4
  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i:
      if y in crypted_letters:
        if y == charc:
          if letters[list(crypted_letters.keys()).index(y)] == '':
            w.addch(h,x,'_',curses.color_pair(5))
            w.addch(h+1,x,crypted_letters[y],curses.color_pair(1))
          else :
            w.addch(h,x,letters[list(crypted_letters.keys()).index(y)],curses.color_pair(6))
            w.addch(h+1,x,crypted_letters[y],curses.color_pair(1))

        elif letters[list(crypted_letters.keys()).index(y)] == '' :
          w.addch(h,x,'_',curses.color_pair(3))
          w.addch(h+1,x,crypted_letters[y],curses.color_pair(4))
        else :
          w.addch(h,x,letters[list(crypted_letters.keys()).index(y)],curses.color_pair(1))
          w.addch(h+1,x,crypted_letters[y],curses.color_pair(4))

      elif y == '.' :
        h += 3
        x = 2

      x += 1
    x += 1
  w.getch()
def already_in_quote(chars):
  h = 6
  x = 4
  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i:
      if y == chars :
        w.addch(h,x,chars,curses.color_pair(6))
      elif y == '.' :
        h += 3
        x = 2

      x += 1
    x += 1
  w.getch()
  sleep(1)
  h = 6
  x = 4
  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i:
      if y == chars :
        w.addch(h,x,chars,curses.color_pair(3))
      elif y == '.' :
        h += 3
        x = 2

      x += 1
    x += 1
  w.getch()

def put_slide(charc,put):
  h = 6
  x = 4
  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i:
      if y in crypted_letters:
        if y == charc:
          w.addch(h,x,put,curses.color_pair(1))
          w.addch(h+1,x,crypted_letters[y],curses.color_pair(4))

      elif y == '.' :
        h += 3
        x = 2

      x += 1
    x += 1
  w.getch()

#url = os.environ['url']
url = "https://zenquotes.io/api/random"

c = 10
while c == 10:
  json = get(url).text

  exec("element = "+json[json.index('{'):json.index('}')+1])
  quote = element['q'].lower()
  crypted_letters = { }
  letters = []
  index = rand(0,len(quote)-1)
  while not quote[index].lower() in chars:
    index = rand(0,len(quote)-1)
  letters.append(quote[index].lower())

  while len(letters) < 6:
    index = rand(0,len(quote)-1)
    while quote[index] in letters or not quote[index].lower() in chars:
      index = rand(0,len(quote)-1)
    for j in range(len(letters)):
      if quote.index(quote[index]) < quote.index(letters[j]):
        letters.insert(j,quote[index].lower())
        break
    else:
      letters.append(quote[index].lower())

      
  for l in letters:
    crypt = chars[rand(0,25)]
    while  crypt in crypted_letters.values() or crypt.lower() == l :
      crypt = chars[rand(0,25)]
    crypted_letters[l] = crypt

  letters.clear()
  for i in range(len(crypted_letters)):
    letters.append('')

  w.getch()
  color()

  words = quote.split()
  h = 6
  x = 4

  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i.lower():
      if y in crypted_letters:
        w.addch(h,x,'_',curses.color_pair(3))
        w.addch(h+1,x,crypted_letters[y],curses.color_pair(4))
      elif y == '.' :
        h += 3
        x = 2
      else:
        w.addch(h,x,y,curses.color_pair(3))
      x += 1
    x += 1

  h += 2
  x = sw-(6+len(element['a']))
  start = time()

  w.addstr(h,x,'-- '+element['a'],curses.color_pair(3))
  #w.getch()
  start = int(time())
  w.addstr(2,sw//2-(len("time : 00:00")//2),"time : 00:00",curses.color_pair(1))
  cur = 0
  color_slide(list(crypted_letters.keys())[cur])
  while letters != list(crypted_letters.keys()) :

    now = int(time())-start
    w.addstr(2,sw//2-(len("time : 00:00")//2),"time : {:02}:{:02}".format(now//60,now%60),curses.color_pair(1))
    w.addch(sh-2,sw-2,'_',curses.color_pair(2))
    c = w.getch()
    if c == 67 :
      if cur < len(crypted_letters)-1 :
        cur += 1
      else :
        cur = 0
      color_slide(list(crypted_letters.keys())[cur])
    elif c == 68 :
      if cur > 0:
        cur -= 1
      else :
        cur = len(crypted_letters)-1 
      color_slide(list(crypted_letters.keys())[cur])
    elif c>=97 and c<=122:
      if chars[c-97] in letters :
        cur = letters.index(chars[c-97])
      elif chars[c-97] in quote and not chars[c-97] in list(crypted_letters.keys()):
        already_in_quote(chars[c-97])
      else:
        put_slide(list(crypted_letters.keys())[cur],chars[c-97])
        letters[cur] = chars[c-97]
        while letters[cur] != '' and  '' in letters :
          if cur < len(crypted_letters)-1 :
            cur += 1
          else :
            cur = 0
      color_slide(list(crypted_letters.keys())[cur])

    elif c>=65 and c<=90 :
      if chars[c-65] in letters :
        cur = letters.index(chars[c-65])
      elif chars[c-65] in quote and not chars[c-65] in list(crypted_letters.keys()):
        already_in_quote(chars[c-65])
      else:
        put_slide(list(crypted_letters.keys())[cur],chars[c-65])
        letters[cur] = chars[c-65]
        while letters[cur] != '' and  '' in letters:
          if cur < len(crypted_letters)-1 :
            cur += 1
          else :
            cur = 0
      color_slide(list(crypted_letters.keys())[cur])
    elif c == 127:
      letters[cur]=''
      color_slide(list(crypted_letters.keys())[cur])
  end = int(time())-start
  
  words = element['q'].split()
  h = 6
  x = 4
  color()
  w.getch()
  for i in words :
    if x+len(i) >= sw-3:
      h += 3
      x = 2 
    for y in i:
      if y == '.' :
        h += 3
        x = 2
      else:
        w.addch(h,x,y,curses.color_pair(3))

      x += 1
    x += 1
  w.addstr(h,x,'-- '+element['a'],curses.color_pair(3))
  w.addstr(h+3,sw//2-(len("time : 00:00")//2),"time : {:02}:{:02}".format(now//60,now%60),curses.color_pair(1))
  file = open("solved.dat" , 'r')
  solved = int(file.read())
  w.addstr(h+4,sw//3,"Total Quotes solved : "+str(solved+1),curses.color_pair(3))
  file = open("solved.dat" , 'w')
  file.write(str(solved+1))
  file.close()
  w.getch()
  mess = "Press ENTER to continue ..."
  w.addstr(sh-5,sw//2-(len(mess)//2),mess,curses.color_pair(1))
  
  c = w.getch()

  while(c==-1):
    c = w.getch()

curses.endwin()


#!/usr/bin/env python3
#mrsudo-jimmy's repository of vulnhub notes searchable
#Written in python3, but should work in python 2.x anyway
#import basic modules
#test
try:
  from os import listdir
  from subprocess import Popen,PIPE
  from sys import argv
  from collections import namedtuple
except:
  print('[*] Unable to import default modules. Quitting')
  exit()

try:
    from termcolor import colored as color
except:
  print("[*] Unable to import module 'termcolor' install with pip")
  exit()
splash=' _   __      __         __  __      __  \n'
splash+='| | / /_  __/ /____    / /_/ /_  __/ /___\n'
splash+='| |/ / /_/ / / / / /  / __  / /_/ / /_/ /\n'
splash+='|___/\__,_/_/_/ /_/  /_/ /_/\__,_/_.___/ \n'
splash = color(splash, 'green')
print(splash)
found = namedtuple('found', 'name sections text'); foundList = []
files = listdir('.')
files.remove('.git')
files.remove('vulnhubdb.py')
files.remove('README.md')

def search(string):
  for f in files:
    resp = search_file(string, f)
    if resp[0] and resp not in foundList:
      foundList.append(found(name=resp[0],sections=resp[1],text=resp[2]))
  for i in foundList:
    print("""
Vulnbox: %s
Found in %s sections
Text:
%s""" % (i.name, i.sections, i.text))


def search_file(string, f):
  name = f
  sections = 0
  text = []
#-------------------------
  with open(f, 'r') as file:
    file = file.read()
    if '[*]' in file:
      file = file.split('[*]')
    else:
      return '', '', ''
    for line in file:
      if string.upper() in line.upper():
        sections = sections + 1
        text.append(line)
#-------------------------
  if sections and text:
    text = ''.join(str(v) for v in text)
    return name, sections, text
  else:
    return '', '', ''




def main():
  print("print prompt")

if len(argv) <= 1:
  main()
elif len(argv) >= 3:
  if '-s' in argv:
    search(' '.join(str(v) for v in argv[2:]))
  else:
    print(usage)
    exit()
else:
  print(usage)
  exit()

#!/usr/bin/env python3
#Version 0
#Created to be a knowledge base for jimmygiv's vulnhub walkthroughs.
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
files.remove("README.md")
files.remove('.git')
files.remove('vulnhubdb.py')
files.sort()
try:
  files.remove('.vulnhubdb.py.swp')
except:
  pass


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
#----------------------------------------------------------------------------------
  if sections and text:
    text = ''.join(str(v) for v in text)
    return name, sections, text
  else:
    return '', '', ''

def prompt(options):
  choice = None
  print(options)
  while not choice:
    try:
      choice = input(color("$ ", "blue"))
      if choice in options:
        pass
      else:
        choice = None
    except:
      choice = None
  return choice

def view_files():
  options = ""
  if len(files) > 15 and len(files) < 30:
    for i in range(len(files)):
      if not (i % 2 ==0):
        options+="%-18s %s\n" % (files[(i-1)], files[i])
  elif len(files) > 20:
    for i in range(len(files)):
      if not (i % 3 ==0):
        options+="%-18s %-18s %s\n" % (files[(i-2)], files[(i-1)], files[i])
  else:
    options = '\n'.join(str(v) for v in files)
  file = None
  while not file:
    file = prompt(color(options, "green"))
    try:
      test = open(file, 'r')
      test.close()
      pass
    except:
      print("[*]  %s is not a file" % color(file, "red"))
      file = None
  return file

def view(fname):
  f = open(fname, 'r')
  file = f.read()
  file = file.split('[*]')
  file = list(filter(None, file))
  sections = len(file)
  i = 0
  for section in file:
    print("Box: %s Section: %s of %s" % (fname, i+1, sections))
    print(section)
    i+=1
    input()

def main():
  options = "1. Search\n2. View by name"
  option = int(prompt(options))
  if option == 1:
    search(input("Input your search string: "))
  else:
   temp = view_files()
   view(temp)
usage = """
-s [search string]
-v **to view by name**"""


if len(argv) <= 1:
  main()
elif len(argv) >= 3:
  if '-s' in argv:
    search(' '.join(str(v) for v in argv[2:]))
  elif argv[1] == '-v':
    try:
      temp = open(argv[2], 'r')
      temp.close()
      pass
    except:
      print(color("%s not found" % argv[2], "red"))
      exit()
    view(argv[2])
  else:
    print(usage)
    exit()
elif len(argv) == 2:
  if argv[1] == '-v':
    view_files()
  else:
    print(usage)
    exit()
else:
  print(usage)
  exit()


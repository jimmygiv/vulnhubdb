#!/usr/bin/env python3
#Created to be a knowledge base for jimmygiv's vulnhub walkthroughs.
try:
  from os import listdir
  from argparse import ArgumentParser
except:
  print('[*] Unable to import default modules. Quitting')
  exit()

splash=' _   __      __         __  __      __  \n'
splash+='| | / /_  __/ /____    / /_/ /_  __/ /___\n'
splash+='| |/ / /_/ / / / / /  / __  / /_/ / /_/ /\n'
splash+='|___/\__,_/_/_/ /_/  /_/ /_/\__,_/_.___/ \n'
print(splash)
files = listdir('./src')
files.sort()
parser = ArgumentParser() 
parser.add_argument('-s', '--search', type=str, help='Search through all files for a string')
parser.add_argument('-v', '--view', type=str, help='Call a vulnhub walkthrough by name')
parser.add_argument('-l', action='store_true', help='print list of walkthroughs')
args = parser.parse_args()
print(args)
def search(string):
  found = {}
  for f in files:
    resp = search_file(string, f)
    if resp['sections'] and resp['name'] not in found.keys():
      found[resp['name']] = resp['sections']
  return found
  
def search_file(string, f):
  ret = {"name": f, "sections": []}
  file = open('src/'+f, 'r').read()
  for line in file.split('[*]'):
    if string in line:
      ret['sections'].append(line)
  return ret

def view(f):
  file = open(f, 'r').read()
  for section in file.split('[*]'):
    print(section)
    input()

def main(args):
  if args.search:
    found = search(args.search)
    for key in found.keys():
      print("Box: " + key)
      print('\n'.join(str(v) for v in found[key]))
    print("Found in %s" % (' ,'.join(str(v) for v in found.keys())) )
  elif args.l is True:
    print("\n".join(str(v) for v in files))
  elif args.view:
    if args.view in files:
      view("src/"+args.view)

main(args)

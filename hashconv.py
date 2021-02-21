'''
  * Project: HashConv ;
  * File: hashconv.py ;
  * Author: PaLLaD1n ;
  * Version: v1.00 ;
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import hashlib
import codecs
import sys
import os
from isort.wrap import line

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", dest = "type", required = True, choices = ["md5", "sha1", "sha256", "sha512"], help = "Hash type.")
parser.add_argument("-i", "--input", dest = "input", required = True, type = str, help = "Input file.")
parser.add_argument("-o", "--output", dest = "output", default = "output.txt", type = str, help = "Output file.")
_args = parser.parse_args()

items = {}

class encrypter:
  def toMD5(string):
    hash = hashlib.md5(string.encode())
    return hash.hexdigest()
  
  def toSHA1(string):
    hash = hashlib.sha1(string.encode())
    return hash.hexdigest()
  
  def toSHA256(string):
    hash = hashlib.sha256(string.encode())
    return hash.hexdigest()
  
  def toSHA512(string):
    hash = hashlib.sha512(string.encode())
    return hash.hexdigest()

def main():
  print("[*] Checking arguments...")
  
  if not os.path.exists(_args.input):
    print("[-] Input file not exist.")
    sys.exit(0)
  
  inp = codecs.open(_args.input, "r", errors = "ignore")
  
  print("\n[*] Convertation...")
  
  if _args.type == "md5":
    for line in inp.read().split("\n"):
      hash = encrypter.toMD5(line)
      items[hash] = line
  elif _args.type == "sha1":
    for line in inp.read().split("\n"):
      hash = encrypter.toSHA1(line)
      items[hash] = line
  elif _args.type == "sha256":
    for line in inp.read().split("\n"):
      hash = encrypter.toSHA256(line)
      items[hash] = line
  else:
    for line in inp.read().split("\n"):
      hash = encrypter.toSHA512(line)
      items[hash] = line
  
  print("[+] Lines converted.")
  print("\n[*] Writting in output file...")
  
  out = codecs.open(_args.output, "a+", errors = "ignore")
  
  for key in items.keys():
    out.write(f"{key}:{items[key]}\n")
  
  print("[+] Done. Input file has been converted.")
  sys.exit(0)


if __name__ == "__main__":
  main()
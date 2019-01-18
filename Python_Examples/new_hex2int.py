#!/bin/python3

import sys
import re


def main():

    fname = "sample_file.txt"
    with open(fname) as f:
        content = f.readlines();

    #reading lines and getting the the text after '#'
    content = re.findall(r'#(\w+)', str(content))
    #[x.strip() for x in content]
    print(content)  #print all the data the array has
    strAdder = ""
    for z in content:
      i = 0
      twochar = ""
      for word in z:
          i+=1
          twochar += word
          if(i==2):     #making sure that we get 2 characters
              i = 0
              test_i = int(twochar, 16)     #converting to decimal
              strAdder = strAdder + str(test_i) +","
              twochar = ""
      #m = int(hexstr, 16)
      print(strAdder+"255,")       #printing the value with teh 255 alpha value
      strAdder = ""

main()

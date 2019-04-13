#!/usr/bin/python

# import module
import sys, getopt
import re
import time
import os

#Define Argument Check
def arg_check(argv):
   global inputfile
   global outputfile
   inputfile = ''
   outputfile = '/root/output.txt'
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> '
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print 'Your Fucking Input file is "', inputfile
   print 'your Fucking Output file is "', outputfile


#Define duplicate  removal function
def removeDups(outputfile,inputfile):
     lines=open(outputfile, 'r').readlines()
     lines_set = set(lines)
     out=open(inputfile, 'w')
     for line in lines_set:
                out.write(line)
#main Function
if __name__ == "__main__":
  info = '''
        #######################################################################
        # Subdomain Extractor  #  By JungleB00K
        #######################################################################
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        With LOve JungleB00k :)With LOve JungleB00k :)With LOve JungleB00k :)
        **********************************************************************
        **********************************************************************
        '''
  print info
  arg_check(sys.argv[1:])
  re_pattern = re.compile(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}')
  with open(inputfile, "r") as fh_in:
     with open(outputfile, "a+") as fh_out:
         for line in fh_in:
            match_list = re_pattern.findall(line)
            if match_list:
                fh_out.write(match_list[0]+"\r\n")
     fh_out.close()
  fh_in.close()
  print ("Getting ready  for Final output File")
  time.sleep(1)
  removeDups(outputfile,inputfile)
  os.remove(outputfile)

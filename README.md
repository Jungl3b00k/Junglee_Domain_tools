 Junglee_Domain_tools
 
 
**1.DomainExtractor.py**
This script is useful when output of dnscan,subfinder,subli3ter and other subdomain enumeration tools produces results consists of mixed domain name,strings,duplicates and ip address.It helps to extract domains by removing duplicate.The result can be used as input of eyewitness and other screengrabbing tools.
DomainExtractor.py -i (inputfile) -o (outputfile)
Have to run in python2

**2.ip_extractor_with_http.py & ip_extractor_without_http.py** 

These work in same way as Domainextractor.py but here Ip address extracted removing duplicates.
ip_extractor_with_http.py -i <inputfile> -o <outputfile>

#!/usr/bin/python3
import sys, getopt, os
import subprocess
import requests
from Utilities.Services.Utils.utils import  convert_to_table_data as to_table_data
from Utilities.Services.Utils.utils import  convert_to_yaml as to_yaml_data

# Entry of main method
def main(argv):
   url = ''
   user = ''
   formattype = ''
   requesttype = ''
   try:
      opts, args = getopt.getopt(argv,"h:u:o:t:q:",["url=","user=","formattype=", "requesttype="])
   except getopt.GetoptError:
      print("curl -u <url> -o <user> -t <formattype> -q <requesttype>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("test.py -u <url> -o --user -t <formattype>  -r <requesttype>")
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-o", "--user"):
         user = arg
      elif opt in ("-t", "--formattype"):
         formattype = arg
      elif opt in ("-q", "--requesttype"):
         requesttype = arg
      print("request %s "% requesttype)
   execute_req(url, user,  formattype, requesttype)

  
# Type of request identify 
def execute_req(url, user, formattype, requesttype):
   print("Request type %s"% requesttype)
   if requesttype.lower() == "put":
      print("Cats Api doesn't support put request please use UI.")
      sys.exit(2)
   elif requesttype.lower() == "delete":
      print("Cats Api doesn't support delete request at this moment")
      sys.exit(2)
   elif requesttype.lower() == "post":
      print("Cats Api doesn't support put request please use UI.")
      sys.exit(2)
   else:
      print("GET reequest is a default request!!")
   set_default(url, formattype, requesttype)
   get_request(url, user, formattype)

# Set default values for if parameters not supplied
def set_default(url, formattype, requesttype):
   if url == '':
      print("setting defualt url type to http://localhost:5000/facts")
      url = 'http://localhost:5000/facts'
   if formattype == '':
      print("setting defualt format type to Json")
   if requesttype == '':
      print("setting defualt request type to GET")
   print ("Url {u} with output type {o} as request type {r} ".format(u=url, o=formattype, r=requesttype))
   return url
   
# Call get method to get all the data.
def get_request(url, user, formattype):
   if user !='':
      data = requests.get(url+'/%s'% user)
   else:
      print("url %s"% url)
      data = requests.get(url)
   if(formattype == 'yaml'):
      print(to_yaml_data(data))
   elif(formattype == 'table'):
      print(to_table_data(data))
   else:
      print(data.json())

# Call Put request on cats api
def put_request(url, user, formattype):
   r = requests.put(url+' / put', data ={'key':'value'})

#Call Delete request on cats api
def delete_request(url, user, formattype):
   r = requests.delete(url+'/ delete', data ={'key':'value'})
   
if __name__ == "__main__":
   main(sys.argv[1:])
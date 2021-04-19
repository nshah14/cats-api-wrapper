# Introduction 
This is to Custom CAT fact api.

# Assumption
  1. Fetch data from Cat facts api.
  2. Display data on the filter on first letter of user name and set of letters allowed [a, c, e....]
  3. Build Cli tool to run the requests on custom apis. Supported on GET. 
  4. No PUT/DELETE support as at this point couldnt find how do update data in cat facts api.

# Getting Started
Guide to setup this git.
1.	Environment
2.	Installation
3.	Execution
4.	Test App using Cli
5.  Extension

# Environment 
   Python : 3.9

# Installation
  Run `pip3 install -r requirements.txt`

# Execution
 Run  `python3.9 app.py`

# Test App using Cli
Run `python3.9 test.py  ` combination of 
  -u = url {http://localhost:5000/facts}
  -o = user {i.e 5887e1d85c873e0011036889}
  -t = type of format [yaml, json, table]
  -r = request type [GET, PUT, DELETE, POST]

type `python3.9 test.py -h`

TO GET ALL CAT FACTS use `python3.9 test.py  -u http://localhost:5000/facts  -q get -t yaml/json`

# Extension
  Use Shell script to wrap this python call.
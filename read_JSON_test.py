
import json

read = {}

def reader():
    
 
    fle = open('jobs2.json', 'r')
    decoded = json.load(fle)

    for job in decoded.values():
         print job['Title']
         print job['Location']
    #print decoded

    #fle = open('jobs2.json')
    #print fle.read() 
   
   
       
reader()

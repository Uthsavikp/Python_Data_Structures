'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:51:58 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 3:12:14
* @Title : To access and print a URL's content to the console.
'''

from http.client import HTTPConnection
connection = HTTPConnection("wikipedia.com")
connection.request("GET", "/")  
result = connection.getresponse()
# retrieves the entire contents  
contents = result.read() 
print(contents)
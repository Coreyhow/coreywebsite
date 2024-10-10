import cgi, cgitb 

form = cgi.FieldStorage() #query string

# Retrieve data from "Get" fields
fname = form.getvalue('fname')
lname  = form.getvalue('lname')
city = form.getvalue('city')


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello Somebody</title>")
print ("</head>")
print ("<body>")

if lname == "Somebody":
  print("You are somebody!")

print ("<h2>Hello, %s %s!</h2>" % (fname, lname))
print ("<h2>You are in %s</h2>" % (city))
print ("</body>")
print ("</html>")



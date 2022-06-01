import os
# to open/create a new html file in the write mode
f = open('/var/www/html/index.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Welcome to Bluestacks </title>
</head>
<body>
<h2>FROM """+os.getenv['REGION']+"""</h2>

<p>Default code has been loaded into the Editor.</p>

</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

import os

indexTextStart = """<!DOCTYPE html>
<html class="dark-mode">
<head>
<meta property="og:site_name" content="Skiddled's Page">
<meta property="og:image" content="https://skiddledgithub.github.io/resources/avatar.png">
<meta name="description" content="Index of {folderPath}">
<meta name="theme-color" content="#ECD4D0">
<link type="application/json+oembed" href="embed.json">
<title>Index of {folderPath}</title>
<link rel="stylesheet" type="text/css" href="/resources/stylesheet/style.css">
<link rel="stylesheet" type="text/css" href="/resources/stylesheet/ubuntu.css">
<link rel="stylesheet" type="text/css" href="/resources/stylesheet/iosevka.css">
<meta charset="utf-8">
</head>
<body class="ubuntu-medium dark-text-content">
    <p class="dark-wip-warning ubuntu-medium">
	<a href="https://github.com/SkiddledGitHub/skiddledgithub.github.io" class="title-links"> Work in Progress </a>
    </p>
    <h2 class="dark-title">Index of {folderPath}</h2>
    <ul>
		<li>
			<a class="text-links" href='../'>../</a>
		</li>
"""
indexTextEnd = """
	</ul>
</body>
</html>
"""

def index_folder(folderPath):
	print("Indexing: " + folderPath +'/')
	#Getting the content of the folder
	files = os.listdir(folderPath)
	#If Root folder, correcting folder name
	root = folderPath
	if folderPath == '.':
		root = 'Root'
	indexText = indexTextStart.format(folderPath=root)
	for file in files:
		#Avoiding index.html files
		if file != 'index.html':
			indexText += "\t\t<li>\n\t\t\t<a class=\"text-links\" href='" + file + "'>" + file + "</a>\n\t\t</li>\n"
		#Recursive call to continue indexing
		if os.path.isdir(folderPath+'/'+file):
			index_folder(folderPath + '/' + file)
	indexText += indexTextEnd
	#Create or override previous index.html
	index = open(folderPath+'/index.html', "w")
	#Save indexed content to file
	index.write(indexText)

#Indexing root directory (Script position)
index_folder('.')
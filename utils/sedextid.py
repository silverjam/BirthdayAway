
import os
import sys

SCRIPT_DIR = path.dirname(path.realpath(__file__))

for root, dirs, files in os.walk(path.join(SCRIPT_DIR, '..')):

	if root != '.':
		continue

	for filename in files:

		if (filename.endswith(".css")  or 
			filename.endswith(".html") or 
			filename.endswith(".js")):

			fp = open(filename)

			data = fp.read()
			data = data.replace(sys.argv[1], sys.argv[2])

			fp.close()
			fp = open(filename, 'w')

			fp.write(data)

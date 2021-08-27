#!/usr/bin/env python3

import sys
import string

try:
	from subprocess import getoutput
except ImportError:
	from commands import getoutput


def do (command):
	print (command)
	output = getoutput(command)
	if (len(output) > 0): print (output)

binDir     = "~/py/bin"
currentDir = getoutput("pwd").strip()

args = sys.argv[1:]
remove = False
if (args[0] == "--remove"):
	remove = True
	args.pop(0)

binDir = args.pop(0)

for f in args:

	if f.endswith (".py"):
		fPy   = f
		fNoPy = f[:-3]
	else:
		fPy   = "%s.py" % f
		fNoPy = f

	fileHere  = "%s/%s" % (currentDir, fPy)
	fileInBin = "%s/%s" % (binDir,     fNoPy)

	if (remove):
		do ("rm %s" % (fileInBin))
	else:
		do ("ln -s %s %s" % (fileHere,fileInBin))
		do ("chmod +x %s" % (fileInBin))

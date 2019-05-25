import re
import sys
import os
import glob
import fire

script_path = os.path.dirname(os.path.realpath(__file__))
real_int_path = sys.executable
_t = script_path.rpartition(os.sep)[0]+os.sep+'python.exe'
if script_path.lower().endswith('scripts') and os.path.isfile(_t):
	real_int_path = _t


def fix(path):
	with open(path,'rb+') as f:
		img = f.read()
		match = re.search(rb'#![a-zA-Z]:\\.+\.exe', img)
		if not match:
			print("can't fix file: "+path)
		int_path = match.group()[2:].decode()
		int_path_start = match.start() + 2
		int_path_end = match.end()
		if int_path.lower() == real_int_path.lower():
			print("skip interpreter: %s in %s" % (int_path, path))
			return
		print("fix interpreter path: %s in %s" % (int_path, path))
		f.seek(int_path_start)
		f.write(real_int_path.encode())
		f.write(img[int_path_end:])

if __name__ == "__main__":
	fire.Fire()
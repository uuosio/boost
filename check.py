import os
import shutil
exclude = ['.git', 'includes']
src_root = '/Users/newworld/Downloads/boost_1_71_0/libs'
for root, dirs, files in os.walk('.'):
	dirs[:] = [d for d in dirs if d not in exclude]
	for file in files:
		if file in ('sync.py', 'CMakeLists.txt', 'includes', '.DS_Store', '.git', 'check.py'):
			continue
		src_file = os.path.join(src_root, root, file)
		if not os.path.exists(src_file):
			print(src_file)
			del_file = os.path.join(root, file)
			os.remove(del_file)


src_root = '/Users/newworld/Downloads/boost_1_71_0/boost'
os.chdir('includes/boost')
for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
                if file in ('sync.py', 'CMakeLists.txt', 'includes', '.DS_Store', 'zlib.h', 'zconf.h'):
                        continue
                src_file = os.path.join(src_root, root, file)
                if not os.path.exists(src_file):
                        print(src_file)
                        del_file = os.path.join(root, file)
                        os.remove(del_file)


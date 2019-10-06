import os
import shutil
exclude = ['.git', 'includes']
src_root = '/Users/newworld/Downloads/boost_1_71_0/libs'
for root, dirs, files in os.walk('.'):
	dirs[:] = [d for d in dirs if d not in exclude]
	print(root)
	for file in files:
		print(file)
		if file in ('sync.py', 'CMakeLists.txt', 'includes', '.DS_Store', '.git'):
			continue
		src_file = os.path.join(src_root, root, file)
		shutil.copy(src_file, root)




src_root = '/Users/newworld/Downloads/boost_1_71_0/boost'
os.chdir('includes/boost')
for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude]
        print(root)
        for file in files:
                print(file)
                if file in ('sync.py', 'CMakeLists.txt', 'includes', '.DS_Store', 'zlib.h', 'zconf.h'):
                        continue
                src_file = os.path.join(src_root, root, file)
                if not os.path.exists(src_file):
                        continue
                shutil.copy(src_file, root)

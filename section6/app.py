import os

for path, subdirs, files in os.walk('/Users/shulme801/Dropbox/newCode/src/shulme801/Python101/UdemyPythonCertCourse'):
    print('\n-----------------')
    print(path)
    print(subdirs)
    print(files)
    print('-------------------')
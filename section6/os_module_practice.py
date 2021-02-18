import os

for dir_path, dir_names, file_names in os.walk("/Users/shulme801/Dropbox/newCode/src/shulme801/python_cert/section6"):
    print(dir_path)
    print(dir_names)
    print(file_names)
    print("----------")
    pass

print(os.path.join(os.environ.get("HOME"), "my_file.txt"))
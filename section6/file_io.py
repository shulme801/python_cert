# my_file  = open('/Users/shulme801/Dropbox/newCode/src/shulme801/python_cert/Section6/sample.txt')

# content  = my_file.read()
# print(content)

# print('-----------------------------\n')
# my_file.seek(0)
# data  = my_file.readlines()
# my_file.close()

# for line in data:
#     print(line)
# print('\n-----------------------------\n')

# with open('/Users/shulme801/Dropbox/newCode/src/shulme801/python_cert/Section6/sample.txt') as my_file:
#     new_content = my_file.read()

# print(new_content)   
try:
        my_file = open('/Users/shulme801/Dropbox/newCode/src/shulme801/python_cert/Section6/sample.txt', mode = 'r')
        print(my_file.read())
        # result = 2 + '2'
except IOError:
    print("file IO error")
except:
    print("some other error occurred")
finally:
    if my_file != None:
        my_file.close()
    print("this statement will always be run, with or without an exception")
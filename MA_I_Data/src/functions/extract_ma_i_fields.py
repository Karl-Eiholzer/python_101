def get_list_of_files(file_location, acession_key):
import os 

reset_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(file_location)
for filename in os.listdir(os.getcwd()):
    print(filename)

os.chdir(reset_path)
return()

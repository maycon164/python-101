import os;
print("os module for solving path of files");

os.path.join('Users', 'maycon', 'Desktop', 'Automate the Boring Stuff with Python');

current_script_path = os.getcwd();

my_files = ['products.csv', 'text.txt']
current_work_dir = os.getcwd();

for path in my_files:
    print(os.path.join(current_work_dir, path));

print("changing work directory")
try:
    os.chdir("c:\\Users")
    print("changed the current work directory to " + os.getcwd());
except FileNotFoundError as error:
    print(error)
    print("the path requested may not exists or is wrong");
    
try :
    print("creating new folders with os module")
    os.chdir(current_script_path)
    os.mkdir(os.getcwd() + "\\new_folder")
    print("created successfully")
except FileExistsError as error:
    print("error: ", error)
    print("file or folder already exists") 

os.chdir(os.path.join(os.getcwd(), "new_folder"));
print("currently changed work directory to my new folder: " + os.getcwd())

print("module 8 - automate boring stuffs")
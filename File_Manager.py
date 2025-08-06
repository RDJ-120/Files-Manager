# Files-Manager
# CLI-Files-Manager With Python
import os
import shutil
import hashlib

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
file = "FM_pass.txt"
print("Welcome To Your Files Manager!🗂\n")
input("Press Enter To Continue...")
clear_screen()

if not os.path.exists(file):
	clear_screen()
	password = input("🔐- Set Password For Your Files Manager:  ")
	hasher = hashlib.sha512(password.encode()).hexdigest()
	with open(file, "w") as f:
		f.write(hasher)
		clear_screen()
		print("Password Set Sucessfully!🔐")
		print("\nTry To Use The Tool Again!🔐")
		exit()
clear_screen()
PW = input("🔐- Enter The Password:\t")
hashed = hashlib.sha512(PW.encode()).hexdigest()
with open(file, "r") as f:
	saved = f.read().strip()
	
if hashed == saved:
	clear_screen()
	print("✅Correct Password\n")
	input("Press Enter To Continue...")
else:
	clear_screen()
	print("❌Password Incorrect!")
	exit()
while True:
    clear_screen()
    choice = input("""What Do You Want To Do?
    
1. Remove File.
2. Remove Folder.
3. Make Folder.
4. Make File.
5. Rename File Or Folder.
6. Show Me The Folders.
7. Show Info.
8. Copy File Or Folder.
9. Move File Or Folder.
10. Make Archive From Folder.
11. Unpack Archive.
12. Storage Info.
13. Exit.

Choose [1 - 13]:\t""")

    if choice == "1":
        clear_screen()
        ans4 = input("Write The Path:\t")
        if os.path.exists(ans4):
            os.chdir(ans4)
        else:
            print(f"Path {ans4} Not Found!❌")
            continue
        clear_screen()
        file = input("Write File Name To Delete:\t")
        if os.path.isfile(file):
            os.remove(file)
            clear_screen()
            print(f"File {file} Deleted!📂\n\n")
            choice4 = input("🎉Press Enter To Try Again Or Write Finish To Exit:\t")
            if choice4.lower() == "finish":
                clear_screen()
                print("Thanks For Using This File Manager!🗂")
                break
        else:
            clear_screen()
            print("File Not Found..❌")
        continue

    elif choice == "2":
        clear_screen()
        ans3 = input("Write The Path:\t")
        if os.path.exists(ans3):
            os.chdir(ans3)
        else:
            clear_screen()
            print(f"Path {ans3} Not Found!❌")
            continue
        clear_screen()
        folder = input("Write Folder Name To Delete:\t")
        if os.path.isdir(folder):
            try:
                os.rmdir(folder)
                clear_screen()
                print(f"Folder {folder} Deleted!🎉")
                input("🎉Press Enter To Try Again:\t")
                continue
            except OSError:
                clear_screen()
                ans = input("Folder Not Empty. Do You Want To Delete All?[Y/N]\t")
                if ans.lower() == "y":
                    shutil.rmtree(folder)
                    print(f"Folder {folder} Has Been Deleted!🎉")
                    choice3 = input("🎉Press Enter To Try Again Or Write Finish To Exit:\t")
                    if choice3.lower() == "finish":
                        clear_screen()
                        print("Thanks For Using This File Manager!🎉")
                        break
        else:
            print(f"Folder {folder} Not Found..❌")
        continue

    elif choice == "3":
        clear_screen()
        ans1 = input("Write The Path That You Want To Make The Folder in:\t")
        if os.path.exists(ans1):
            os.chdir(ans1)
        else:
            clear_screen()
            print(f"Path {ans1} Not Found!❌")
            continue
        clear_screen()
        make = input("Choose The Name Of Your New Folder:\t")
        os.mkdir(make)
        print(f"Folder {make} Is Now in The Path {ans1}")
        choice2 = input("🎉Press Enter To Try Again Or Write Finish To Exit:\t")
        if choice2.lower() == "finish":
            clear_screen()
            print("Thanks For Using This File Manager!🎉")
            break
        continue

    elif choice == "4":
        clear_screen()
        ans8 = input("Write The Path:\t")
        if os.path.exists(ans8):
            os.chdir(ans8)
        else:
            clear_screen()
            print(f"Path {ans8} Not Found!❌")
            continue
        FileName = input('Write The File Name:\t')
        clear_screen()
        full_path = os.path.join(ans8, FileName)
        if os.path.exists(full_path):
            print("File Already Exists❌.")
        else:
            try:
                with open(full_path, "x") as file:
                    file.write("")
                print(f"File {FileName} Created Successfully at {ans8}🎉✨")
            except Exception as e:
                print(f"Failed To Create File {FileName} At {ans8}❌\nError: {e}")
        input("Press Enter To Continue!🎉")
        continue

    elif choice == "5":
        clear_screen()
        ans2 = input("Write The Path:\t")
        if os.path.exists(ans2):
            os.chdir(ans2)
        else:
            clear_screen()
            print(f"Path {ans2} Not Found!❌")
            continue
        folderr = input("What Is The Folder/File Name?\t")
        folderr2 = input("Write The New Name:\t")
        os.rename(folderr, folderr2)
        clear_screen()
        print("Name Changed!🎉\n\n")
        choice1 = input("🎉Press Enter To Try Again Or Write Finish To Exit:\t")
        if choice1.lower() == "finish":
            clear_screen()
            print("Thanks For Using This File Manager!🎉")
            break
        continue

    elif choice == "6":
        clear_screen()
        path = input("Write The Path To Show Folders:\t")
        if not os.path.exists(path):
            print(f'Path {path} Not Found❌')
            input("\nPress Enter To Get Back:\t")
            continue
        while True:
            clear_screen()
            print(f"📂Current Path: {path}")
            try:
                items = os.listdir(path)
                folders = [f for f in items if os.path.isdir(os.path.join(path, f))]
                files = [f for f in items if os.path.isfile(os.path.join(path, f))]
                print("\n🗂Folders:")
                for folder in folders:
                    print(f"- {folder}")
                print("\n🗂Files:")
                for file in files:
                    print(f"- {file}")
                next_folder = input("\nWrite Folder Name To Go Into It (or '..' To Go Back, Or 'Exit' To Quit):\t")
                if next_folder.lower() == "exit":
                    break
                elif next_folder.lower() == "..":
                    path = os.path.dirname(path)
                else:
                    new_path = os.path.join(path, next_folder)
                    if os.path.isdir(new_path):
                        path = new_path
                    else:
                        print("Folder Not Found❌")
                        input("Press Enter To Continue..")
            except PermissionError:
                print("❌Permission denied.")
                break
        continue

    elif choice == "7":
        clear_screen()
        path = input("Write The Path To Show Info:\t")
        if not os.path.exists(path):
            print(f'Path {path} Not Found❌')
            input("\nPress Enter To Get Back:\t")
            continue
        os.chdir(path)
        choose = input("Choose File Or Folder To Show Info:\t")
        if os.path.isfile(choose):
            print("\nType:\tFile")
            print("Name:\t", choose)
            print("Size:\t", os.path.getsize(choose), "Bytes.")
        elif os.path.isdir(choose):
            print("\nType:\tFolder")
            print("Name:\t", choose)
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(choose):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.exists(fp):
                        total_size += os.path.getsize(fp)
            print("Size:\t", total_size, "Bytes")
        else:
            print("❌File or Folder Not Found.")
        input("\nPress Enter To Continue:\t")
        continue

    elif choice == "8":
        clear_screen()
        bfr = input("🗂Write The File Or Folder 'Full Path':\t")
        clear_screen()
        afr = input("🗂Write The New Path:\t")
        try:
            if os.path.isdir(bfr):
                shutil.copytree(bfr, afr)
            else:
                shutil.copy2(bfr, afr)
            print("Copied Successfully!🎉")
        except Exception as e:
            print("❌Error: ", e)
        input("Press Enter To Continue:")
        continue

    elif choice == "9":
        clear_screen()
        bfr = input("🗂Write The File Or Folder 'Full Path':\t")
        clear_screen()
        afr = input("🗂Write The New Path:\t")
        try:
            shutil.move(bfr, afr)
            print("Moved Successfully!🎉")
        except Exception as e:
            print("❌Error: ", e)
        input("Press Enter To Continue:")
        continue

    elif choice == "10":
        clear_screen()
        folder = input("🗂Write The Folder 'Full Path':\t")
        clear_screen()
        new_path = input("🗂Write The Zip File Name (without .zip):\t")
        clear_screen()
        try:
            shutil.make_archive(new_path, "zip", folder)
            print("Folder Archived Successfully!🎉")
        except Exception as e:
            print("❌Error: ", e)
        input("Press Enter To Continue:")
        continue

    elif choice == "11":
        clear_screen()
        filename = input("🗂Write The Zip File Path:\t")
        clear_screen()
        extract_to = input("🗂Write The New Path To Extract Zip Into:\t")
        clear_screen()
        try:
            shutil.unpack_archive(filename, extract_to)
            print("Zip Extracted Successfully!🎉")
        except Exception as e:
            print("❌Error: ", e)
        input("Press Enter To Continue:")
        continue
    
    elif choice == "12":
    	
    	clear_screen()
    	usage = shutil.disk_usage("/storage/emulated/0")
    	print("💤Storage Info:\n")
    	print(f"Total:\t{usage.total / (1024**3):.2f}GB")
    	print(f"Used:\t{usage.used / (1024**3):.2f}GB")
    	print(f"Free:\t{usage.free / (1024**3):.2f}GB")
    	input("\n\nPress Enter To Continue!💤")
    	continue
    	
    elif choice == "13":
    	clear_screen()
    	print("Thanks For Using This File Manager!🗂")
    	print("\nDeveloper:\t +201103894809, +966509099228💤")
    	input("\n\n💤Press Enter To Exit:\t")
    	break
    	
    else:
        print("❌ Invalid choice. Please choose from 1 to 13.")
        input("Press Enter To Try Again")
        continue

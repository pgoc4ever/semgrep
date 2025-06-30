import os
import subprocess

def delete_temp_files(directory):
    print(f"Deleting files in {directory}...")
    os.system("rm -rf " + directory)  

def run_user_command(command):
    print("Running user command...")
    subprocess.call(command, shell=True) 

def main():
    user_input = input("Enter directory to clean: ")
    delete_temp_files(user_input)
    run_user_command("ls " + user_input)

if __name__ == "__main__":
    main()

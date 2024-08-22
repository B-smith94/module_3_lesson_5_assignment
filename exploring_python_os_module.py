import os

directory_path = input("Please specify directory path: ")
def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents: {contents}")
    except PermissionError:
        print(f"You do not have permission to access {path}")
    except IOError:
        print(f"{path} does not exists.")
    except Exception as e:
        print(f"{e} has occured.")

list_directory_contents(directory_path)
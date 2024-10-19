import os
import shutil
import datetime



def get_today_date():
    return datetime.datetime.now().strftime("%Y__%m__%d")

OLD_PATH =(os.path.expanduser("~/Desktop").replace("\\", "/"))
NEW_PATH =(os.path.expanduser("~/Desktop").replace("\\", "/")) + f"/desktop{get_today_date()}"

def get_list_of_paths(pathname):
    return os.listdir(pathname)

def create_folder():
    try:
        os.makedirs(NEW_PATH)
    except Exception as e:
        print(e)
        

def clear_desktop():
    list_of_paths = get_list_of_paths(OLD_PATH)
    create_folder()

    for path in list_of_paths:
        if "desktop" not in str(path):
            shutil.move(f"{OLD_PATH}/{path}", NEW_PATH)            
   
def main():
   clear_desktop()


if __name__ == "__main__":
    main()
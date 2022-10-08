import os
import shutil

files = os.listdir(r"C:\Users\Elias\Pictures\Memes")
files.remove('desktop.ini')
files.remove('All-Memes')
files.remove('GIF-Memes')
files.remove('JPG-Memes')
files.remove('MOV-Memes')
files.remove('MP3-Memes')
files.remove('MP4-Memes')
files.remove('PNG-Memes')
all_path = r"C:\Users\Elias\Pictures\Memes\All-Memes"
for i in range(0, len(files)):
    if ".jpg" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\JPG-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    elif ".png" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\PNG-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    elif ".mov" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\MOV-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    elif ".mp4" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\MP4-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    elif ".gif" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\GIF-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    elif ".mp3" in files[0].lower():
        path = r"C:\Users\Elias\Pictures\Memes" + "\\" + files[0]
        new_path = r"C:\Users\Elias\Pictures\Memes\MP3-Memes"
        shutil.copy(path, all_path)
        shutil.move(path, new_path)
        files.remove(files[0])
    else:
        quit()

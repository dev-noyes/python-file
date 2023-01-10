import os
from datetime import datetime
import sys
import time
import logging
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# macOS will be "/Users/UserName/Downloads"
# windows will be "C:\\Users\\UserName\\Downloads"
source_dir = "/Users/dongjunyang/Downloads"
desire_dir = "/Users/dongjunyang/Desktop"

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def on_created(event):
    # 1 - check the img/audio/video folder exists on desire_dir
    if os.path.exists(f"{desire_dir}/image") == False:
        os.mkdir(f"{desire_dir}/image")
    if os.path.exists(f"{desire_dir}/video") == False:
        os.mkdir(f"{desire_dir}/video")
    if os.path.exists(f"{desire_dir}/audio") == False:
        os.mkdir(f"{desire_dir}/audio")
    if os.path.exists(f"{desire_dir}/docs") == False:
        os.mkdir(f"{desire_dir}/docs")

    # 2 - scan all files in downloads folder
    lists = os.listdir(source_dir)

    # 3 - check the files except folder
    for list in lists:
        cur_time = datetime.now()
        filename, extension = os.path.splitext(list)
        file_date = cur_time.strftime("%y%m%d")
        old_name = f"{source_dir}/{filename}{extension}"
        new_name = f"{source_dir}/{file_date}-{filename}{extension}"

        if os.path.exists(old_name):
            if extension in image_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/image/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in audio_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/audio/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in document_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/docs/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in video_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/video/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)


def on_modified(event):
    # 1 - check the img/audio/video folder exists on desire_dir
    if os.path.exists(f"{desire_dir}/image") == False:
        os.mkdir(f"{desire_dir}/image")
    if os.path.exists(f"{desire_dir}/video") == False:
        os.mkdir(f"{desire_dir}/video")
    if os.path.exists(f"{desire_dir}/audio") == False:
        os.mkdir(f"{desire_dir}/audio")
    if os.path.exists(f"{desire_dir}/docs") == False:
        os.mkdir(f"{desire_dir}/docs")

    # 2 - scan all files in downloads folder
    lists = os.listdir(source_dir)

    # 3 - check the files except folder
    for list in lists:
        cur_time = datetime.now()
        filename, extension = os.path.splitext(list)
        file_date = cur_time.strftime("%y%m%d")
        old_name = f"{source_dir}/{filename}{extension}"
        new_name = f"{source_dir}/{file_date}-{filename}{extension}"

        if os.path.exists(old_name):
            if extension in image_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/image/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in audio_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/audio/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in document_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/docs/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)
            elif extension in video_extensions:
                os.rename(old_name, new_name)
                if os.path.exists(desire_dir):
                    new_path = f"{desire_dir}/video/{file_date}-{filename}{extension}"
                    shutil.move(new_name, new_path)


# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir if os.path.exists(source_dir) else '.'
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created
    event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


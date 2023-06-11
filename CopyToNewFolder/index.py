#! Python 3
# searchJPG.py searchs for every JPG in every  folder/subfolders from the cwd and moves them to one folder
# YOU CAN'T HAVE A FOLDER WITH THE SAME NAME AS THE "newFolder", IT DOESN'T WORK WITH DUPLICATED NAMES

import os, shutil


def moveJPG():
    # Current working directory
    base = os.getcwd()
    # New folder where the files will be moved to.
    newFolder = os.mkdir(os.path.join(base, "VIDEOS_1"))
    newFolder = os.path.join(base, "VIDEOS_1")

    # List with extensions of the files you want to move.
    isPicture = (
        ".JPG",
        ".JPEG",
        ".PNG",
        ".TIFF",
        ".BMP",
        ".jpg",
        ".bmp",
        ".png",
        ".tiff",
        ".jpeg",
    )

    isVideo = (
        ".WEBM",
        ".MKV",
        ".FLV",
        ".VOB",
        ".OGV",
        ".OGG",
        ".RRC",
        ".GIFV",
        ".MNG",
        ".MOV",
        ".AVI",
        ".QT",
        ".WMV",
        ".YUV",
        ".RM",
        ".ASF",
        ".AMV",
        ".MP4",
        ".M4P",
        ".M4V",
        ".MPG",
        ".MP2",
        ".MPEG",
        ".MPE",
        ".MPV",
        ".M4V",
        ".SVI",
        ".3GP",
        ".3G2",
        ".MXF",
        ".ROQ",
        ".NSV",
        ".FLV",
        ".F4V",
        ".F4P",
        ".F4A",
        ".F4B",
        ".webm",
        ".mkv",
        ".flv",
        ".vob",
        ".ogv",
        ".ogg",
        ".rrc",
        ".gifv",
        ".mng",
        ".mov",
        ".avi",
        ".qt",
        ".wmv",
        ".yuv",
        ".rm",
        ".asf",
        ".amv",
        ".mp4",
        ".m4p",
        ".m4v",
        ".mpg",
        ".mp2",
        ".mpeg",
        ".mpe",
        ".mpv",
        ".m4v",
        ".svi",
        ".3gp",
        ".3g2",
        ".mxf",
        ".roq",
        ".nsv",
        ".flv",
        ".f4v",
        ".f4p",
        ".f4a",
        ".f4b",
    )
    # Stores the names of the files already copied
    alreadyThere = []
    # Iterates over the file/folder tree from the current working directory
    for folderName, subfolders, fileNames in os.walk(base):
        print("The current folder is " + folderName)

        # Iterates over every subfolder in the current folder.
        for subfolder in subfolders:
            # If one of the current subfolders is the new folder, it gets removed from the loop.
            if subfolder == newFolder:
                subfolders.remove(subfolder)

                print("SUBFOLDER OF " + folderName + ":" + subfolder)

        # Iterates over every filename.
        for filename in fileNames:
            # If the filename has the current kind of extension "isVideo" or "isPicture"
            if filename.endswith(isVideo) == True:
                # If the file is already copied skips it.
                if filename in alreadyThere:
                    continue
                else:
                    # Copies the file into the new folder and stores the name into the alreadyThere list.
                    print("MOVING FILE INSIDE " + folderName + ":" + filename + "...")

                    tempPath = folderName + "\\" + filename
                    alreadyThere.append(filename)
                    shutil.copy(tempPath, newFolder)

            else:
                continue


moveJPG()

import shutil
import os
import glob

#get jpg and .json file name
jpg_list=glob.glob("tutanak_database/*.jpg")


if(len(jpg_list)==0):
    print(".jpg file not found.")
    exit()


index_counter=0

#sort process
for i in range(len(jpg_list)):
    os.rename(jpg_list[i],"tutanak_database/"+str(i)+"_tutanak.jpg")

print("Process Success")

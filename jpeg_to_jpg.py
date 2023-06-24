from PIL import Image 
import glob, uuid

directory = "tutanak_database/jpeg/jpg/"

for infile in glob.glob("tutanak_database/jpeg/*.jpeg"):
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(directory + str(uuid.uuid4()) + ".jpg")

print("Process is finished")
import shutil
import os

if __name__ == '__main__':
    object_to_compress = input("Enter the folder name to compresss: ")
    # if os.path.exists(object_to_compress) and os.path.isdir(object_to_compress):
    if os.path.exists(object_to_compress):
        shutil.make_archive(object_to_compress, 'zip', './')
        print(f"Compressed Folder {object_to_compress} successfully")
    # elif not os.path.isdir(object_to_compress):
    #     if os.path.isfile(object_to_compress):
    #         fname = os.path.basename(object_to_compress)
            # Split to extract the extension
            # reaname or create a new name as filname_ext.zip

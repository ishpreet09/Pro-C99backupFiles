import os 
import shutil
import time

def main():
    deleted_folders=0
    deleted_files=0
    path="Path name"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
       for rootFolders, folders, files in path:
           if seconds>=getFileOrFolderAge(rootFolders):
               removeFolder(rootFolders)
               deleted_folders+=1

               break
           else:
                for folder in folders:
                    folder_path=os.path.join(rootFolders,folder)
                    if seconds>=getFileOrFolderAge(folder_path):
                        removeFolder(folder_path)
                        deleted_folders+=1

                for file in files:
                    file_path=os.path.join(rootFolders,file)
                    if seconds>=getFileOrFolderAge(file_path):
                        removeFolder(file_path)
                        deleted_files+=1
       else:
        if seconds>=getFileOrFolderAge(path):
            removeFolder(path)
            deleted_files += 1

    else:
		   print(f'"{path}" is not found')
		   deleted_files += 1 # incrementing count

    print(f"Total folders deleted: {deleted_folders}")
    print(f"Total files deleted: {deleted_files}")

def removeFolder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def removeFile(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def getFileOrFolderAge(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	main()

import os

folder = r'C:\Users\Hau\Downloads\10.Dam Vinh Hung-20230812T152717Z-001\10.Dam Vinh Hung\\'
count = 1

print(folder)
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name
    #print(file_name)
    newname= file_name.split(file_name[0:3])
    print(newname[1])
    # Adding the count to the new file name and extension
    destination = folder + newname[1] 

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')


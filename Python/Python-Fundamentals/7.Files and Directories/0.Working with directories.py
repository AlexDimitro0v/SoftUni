# Basic Directory Operations
import os

# 1.Creating a directory with os.mkdir(path):
# os.mkdir("TestFolder")

# 2.Creating a directory tree with os.makedirs(path):
# os.makedirs("TestFolder/Subdir/Subdir 2/")

# 3.Deleting a directory (directory must be empty):
# os.rmdir("TestFolder")

# 4.We can traverse the folder structure with os.walk(path)
# Useful for debugging
debug = list(os.walk('.'))
for root, dirs, files in os.walk('.'):
    for subdir in dirs:
        print(subdir)  # print path to all subdirectories first.
        for root1, dirs1, files1 in os.walk(subdir):
            for file in files1:
                print(f"   -{file}")  # print path to all filenames.


# for root, dirs, files in os.walk('.'):
#     # print path to all subdirectories first.
#     for subdir in dirs:
#         print(subdir)
#
#     # print path to all filenames.
#     for file in files:
#         print(file)

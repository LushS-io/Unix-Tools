# %% Import Libs
import os

# %% -- Pre-processing --

# get curr dir
cwd = os.getcwd()
print(cwd)

# list out dir to rename files
files = os.listdir("./fromFive9")
# Ignore files ending with ...
files = [fi for fi in files if not fi.endswith(".DS_Store")]
print(files)
len(files)

# %%  -- Import --

# get the list of filenames to perform
file = open("./new_filenames_list.txt", 'r')

rename_list = [line.splitlines() for line in file.readlines()]
print(rename_list)

# %% -- Create new list without \n char --
new_li = []
for item in rename_list:
    new_li.append(item[0])
print(new_li)

# TODO: compare file from Five9 to Filename for valdiation

# %% RENAME STEP
i = 0  # init 0 for iteration
for file_name in os.listdir("./fromFive9"):
    newName = new_li[i]
    src = "./fromFive9/" + file_name
    dst = "./renamed_fulls/" + newName

    os.rename(src, dst)
    i += 1

# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files


def main():
    # list out dir to rename files
    # os.listdir("./fromFive9")
    # os.listdir(cwd+"/test")

    # get the list of filenames to perform
    in_txt_list = open("./new_filenames_list.txt", 'r')
    rename_list = [line.split(',') for line in in_txt_list.readlines()]
    rename_list = rename_list[0]

    # print(rename_list)
    # print(rename_list[0])

    # perform rename
    i = 0
    for file_name in os.listdir("./fromFive9"):
        # dst = "audio_" + str(i) + ".wav"
        dst = rename_list[i]
        src = "./fromFive9/" + file_name
        dst = "./renamed_fulls/" + dst

        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()

def machine(a):

    import os
    import shutil
    k = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    k = os.getcwd()
    dosya = f"{k}/{a}"
    if not dosya.endswith(".py"):
        dest_dir = "./orijinalleri"
        # If the destination directory doesn't exist, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Move the file to the destination directory
        shutil.copy(dosya, dest_dir)
        # writing into a new file

        # reading the file
        with open(dosya) as fp:
            contents=fp.readlines()
        # initialize two counter to check mismatch between "(" and ")"
        open_bracket_counter=0
        close_bracket_counter=0
        # whenever an element deleted from the list length of the list will be decreased
        decreasing_counter=0
        for number in range(len(contents)):
            # checking if the line contains "#" or not
            if "#" in contents[number-decreasing_counter]:
                # delete the line if startswith "#"
                if contents[number-decreasing_counter].startswith("#"):
                    contents.remove(contents[number-decreasing_counter])
                    decreasing_counter+=1
                # delete the character after the "#"
                else:
                    newline=""
                    for character in contents[number-decreasing_counter]:
                        if character=="(":
                            open_bracket_counter+=1
                            newline+=character
                        elif character==")":
                            close_bracket_counter+=1
                            newline+=character
                        elif character=="#" and open_bracket_counter==close_bracket_counter:
                            break
                        else:
                            newline+=character
                    contents.remove(contents[number-decreasing_counter])
                    contents.insert(number-decreasing_counter,newline)
        # Path to the file that you want to move
        # Destination directory where you want to move the file

        with open(dosya,"w") as fp2:
            fp2.writelines(contents)
        with open(dosya, "r+") as t:
            liste = t.readlines()
            for satir in liste:
                '\n'.join([m.lstrip() for m in satir.split('\n')])
        t.close()
        result = ""
        with open(dosya, "r+") as file:
            for line in file:
                if not line.isspace():
                    result += line
            file.seek(0)
            file.write(result)

        dest_dir = "./forgpt"
        # If the destination directory doesn't exist, create it
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Move the file to the destination directory

        shutil.move(dosya, dest_dir)
        # writing into a new file


def forgpt():


    if input("hepsini yapim mi, evet ya da hayır") == "hayır":

        cevap = input("enter file name ")
        machine(cevap)

    else:

        import os

        k = os.getcwd()
        file_list = os.listdir(k)
        for file2 in file_list:
            machine(file2)

forgpt()
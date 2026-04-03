def file_copy(sourcefile, destinationfile):
    with open(sourcefile) as f:
        content = f.readlines()

    with open(destinationfile, 'w') as f:
        f.writelines(content)


file_copy("error.txt", "error_new.txt");
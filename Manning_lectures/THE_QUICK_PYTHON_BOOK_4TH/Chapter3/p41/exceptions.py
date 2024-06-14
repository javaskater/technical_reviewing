#!/usr/bin/python3
class EmptyFileError(Exception):
    pass

filenames = ["myfile1.txt", "non_existant", "empty_file", "myfile2.txt"]

for file in filenames:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError(f"file {file} is empty")
    except IOError as error:
        print(f"{file} could not be opened: {error.strerror}")
    except EmptyFileError as error:
        print(error)
    else:
        print(f"{file}: {line}")
    finally:
        print("Done processing", file)
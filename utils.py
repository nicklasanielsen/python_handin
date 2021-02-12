import os
import argparse

def get_file_names(folderpath, out = "output.txt"):
    with open(out, "a") as file_object:
        for file_name in os.listdir(folderpath):
            file_object.write(file_name + "\n")
  
def get_all_file_names(folderpath, out = "output.txt"):
    with open(out, "a") as file_object:
        for root, dirs, files in os.walk(folderpath):
            for file_name in files:
                file_object.write(file_name + "\n")

def print_line_one(file_names):
    for file_name in file_names:
        with open(file_name) as file_object:
            print(file_object.readline().rstrip())

def print_emails(file_names):
    for file_name in file_names:
        with open(file_name) as file_object:
            for line in file_object:
                if "@" in line:
                    print(line.rstrip())

def write_headlines(md_files, out = "output.txt"):
    with open(out, "a") as output_file:
        for md_file in md_files:
            with open(md_file) as file_object:
                for line in file_object:
                    if line.startswith("#"):
                        output_file.write(line.rstrip() + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="solution for Week 2 exersice 2")
    parser.add_argument("input_file", help="the path to the file(s) to consume", nargs="*")
    parser.add_argument("--file", dest="file_name", help="the path to the file to print to. (console if nothing is given)", required=False)
    parser.add_argument("--lineone", help="writes the first line of the provided files", required=False, action="store_true")
    parser.add_argument("--email", help="writes all e-mails found within the provided files", required=False, action="store_true")
    parser.add_argument("--headline", help="finds all headline within the provided files", required=False, action="store_true")
    parser.add_argument("--all", help="TODO", required=False, action="store_true")

    args = parser.parse_args()

    if args.lineone:
        print_line_one(args.input_file)
    elif args.email:
        print_emails(args.input_file)
    elif args.headline:
        if args.file_name:
            write_headlines(args.input_file, args.file_name)
        else:
            write_headlines(args.input_file)
    elif args.all:
        for path in args.input_file:
            if args.file_name:
                get_all_file_names(path, args.file_name)
            else:
                get_all_file_names(path)
    else:
        for path in args.input_file:
            if args.file_name:
                get_file_names(path, args.file_name)
            else:
                get_file_names(path)

    
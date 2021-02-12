import csv
import platform
import argparse

def print_file_content(file):
    with open(file) as opened_file:
        content = opened_file.readlines()

    for line in content:
        print(line.strip().split(","))

def write_list_to_file(output_file, *lst):
    if platform.system() == "Windows":
        newline = ""
    else:
        newline = None

    with open(output_file, "a", newline=newline) as file:
        writer = csv.writer(file)
        
        for element in lst:
            writer.writerow(element)

def read_csv(input_file):
    with open(input_file) as opened_file:
        content = opened_file.readlines()

    import_list = []

    for line in content:
        import_list.append(line)

    return(import_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="solution for Week 2 exersice 1")
    parser.add_argument("input_file", help="the path to the file to consume")
    parser.add_argument("--file", dest="file_name", help="the path to the file to print to. (console if nothing is given)", required=False)

    args = parser.parse_args()

    if not (args.file_name): # output file not provided
        print_file_content(args.input_file)
    else:
        write_list_to_file(args.file_name, read_csv(args.input_file))

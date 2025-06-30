def read_file_lines(filename):
    f = open(filename, "r")  
    lines = f.readlines()
    f.close()
    return lines

def main():
    try:
        lines = read_file_lines("sample.txt")
        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()

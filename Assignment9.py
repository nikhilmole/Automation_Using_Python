import os

def main():
    print("Enter the name of the file you want to open:")
    fname = input()

    if os.path.exists(fname):
        print("File is available in this directory.")
    else:
        print(f"{fname} does not exist in the directory.")

if __name__ == "__main__":
    main()

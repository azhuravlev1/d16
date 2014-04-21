INPUT_FILE="in.txt"
def find_x(file_name):
    words = []
    with open(INPUT_FILE) as f:
        for line in f:
            if 'x' in line.strip().split():
                print("here it is: " + line.strip())
                return
find_x(INPUT_FILE)
print(type(file_name))
print(type(f))
print(type(line))
print(type(line.strip()))
print(type(line.strip().split))

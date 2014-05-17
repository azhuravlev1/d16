INPUT_FILE="in.txt"

def find_x(file_name):
    words = []
    with open(INPUT_FILE) as f:
        for line in f:
            if 'x' in line.strip().split():
                print("here it is: " + line.strip())
                return
            
find_x(INPUT_FILE)

#file_name - str(в конце программы; в начале эта переменная неопределена)
#line.strip - builtin_function_or_method
#f - _io.TextIOWrapper
#line - str
#line.strip() - str
#line.strip().split - builtin_function_or_method
#line.strip().split() - list

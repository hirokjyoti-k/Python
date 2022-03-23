def write_file(temp):
    w_file = open("example.txt","w")
    w_file.write(temp)
    return "file saved successfully"

def read_file():
    r_file = open("example.txt")
    return r_file.read()

msg = read_file()
print(int(msg))
temp = int(msg)+1
write_file(str(temp))

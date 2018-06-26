file = open("File1.txt","w")
file.write("HELLO WORLD !!!!!")
file.close()
with open("File2.txt") as f:
    with open("File2.txt","w") as f1:
        for line in f:
            f1.write(line)
file.close()

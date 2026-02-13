line = 1
with open("sample.txt", "r") as f:
    for line in f:
        if("darkness" in line):
            print("Word found at:", line.find("darkness"), end="")
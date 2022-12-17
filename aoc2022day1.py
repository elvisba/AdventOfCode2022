f = open("input-1.txt","r")
lines = f.readlines()

biggestelf=0
currelf=0

for line in lines:
    splitted_line = line.split('\n')
    try:
        currelf=currelf+int(splitted_line[0])
    except ValueError:
        flag = False

    if line in ['\n', '\r\n']:
        if currelf > biggestelf:
            # We have new leader!
            biggestelf=currelf
        print(currelf)
        currelf = 0
        # We've found a blank line, stop counting!
        # save the counted elf into a list!

print("## Biggest elf is:", biggestelf)
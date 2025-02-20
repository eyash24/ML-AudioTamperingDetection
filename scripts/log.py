import re

with open("logs/download_log.txt", "r") as myfile:
    data = myfile.readlines()
    myfile.seek(0)
    data2 = myfile.read()

myfile.close()

# to store unique dest files
dest_set = set()
x = re.findall("\[ExtractAudio\] Destination:", data2)
print(len(x))

def search(str, data):
    # print(str)
    data = data.startswith(str)
    # print(data)
    if str in data:
        return True
    else:
        return False

def endPartition(string, match):
    try:
        index = -1
        while string[index]!= match:
            index -= 1
        return [string[:index], string[index:]]
    except Exception as er:
        raise er

duplicate = []
extensions = []

for line in data:
    if line.startswith("[ExtractAudio] Destination:"):
        l = line[-5:]
        ext = l.split(".")
        # print(ext[-1])

        if ext[-1] not in extensions:
            extensions.append(ext[-1])

        line = line.partition(":")
        line = line[-1]
        line = endPartition(line,".")
        # print(type(line))
        line = line[0].strip()
        # print(line)
        if line not in dest_set:
            dest_set.add(line)
        else:
            duplicate.append(line)

        
print(len(dest_set))
# print("no of duplicates: ", len(duplicate))
# print()
# print("Duplicates:")
# for i in duplicate:
#     print(i)

print(extensions)


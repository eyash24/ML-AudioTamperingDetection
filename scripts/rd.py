t1 = '[download] Destination: /content/drive/MyDrive/yt-video/Watch: Full Speech Of Sushma Swaraj At UN.m4a'
t2 = "[ExtractAudio] Destination: /content/drive/MyDrive/yt-video/Watch: Full Speech Of Sushma Swaraj At UN.mp3"

res = t1.partition(":")
print(res)

def endPartition(string, match):
    try:
        index = -1
        while string[index]!= match:
            index -= 1
        return [string[:index], string[index:]]
    except Exception as er:
        raise er

res = endPartition(res[-1],".")
print(res)

print(len("/content/drive/MyDrive/yt-video/"))
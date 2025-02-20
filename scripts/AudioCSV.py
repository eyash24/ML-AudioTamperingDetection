import os
import csv
import librosa
import pandas as pd

def save_csv(data, csv_file):
    with open(csv_file,"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    csvfile.close()

def rename_file(source, destination):
    os.rename(source, destination)

def retrieve_audioId(prefix, count, max_len=5):
    str_count = str(count)
    prefix_zero = max_len - len(str_count)
    return prefix + "0"*prefix_zero + str_count

def add_durr(csvfile):
    df = pd.read_csv(csvfile)



if __name__ == "__main__":

    audio_dir = "dataset/Audio1"
    audio_csv_file = "dataset/audioData.csv"

    data = [
        [
            "Name", "audioID", "Folder", "Class"
        ]
    ]

    list_dir = os.listdir(audio_dir)
    # print(list_dir)

    audioId_prefix = "Audio_01_"
    audio_count = 0
    folder = 1
    class_ = 1

    for aufile in list_dir:
        auID = retrieve_audioId(audioId_prefix, audio_count, 5)
        audio_count += 1
        auID += ".mp3"
        
        data.append([aufile, auID, folder, class_])
        oldName = os.path.join(audio_dir, aufile)
        newName = os.path.join(audio_dir, auID)
        # print(oldName, newName)
        rename_file(oldName, newName)

    save_csv(data, audio_csv_file)





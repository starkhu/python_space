import subprocess
import os

def subprocess_test():
    #mp4_file = "E:/mini_project/audio_classification/Youtube-8M-WILLOW-master/mp4/p1.mp4"
    #command = "ffmpeg -i mp4_file -ab 160k -ac 1 -ar 44100 -vn E:/out1.wav"
    command = "ffmpeg -i E:/mini_project/audio_classification/Youtube-8M-WILLOW-master/mp4/p1.mp4  -ab 160k -ac 1 -ar 44100 -vn E:/out1.wav"
    subprocess.call(command, shell=True)
    print("call finished ")

def to_audio_test():
    wav_file = "E:/mini_project/audio_classification/Youtube-8M-WILLOW-master/mp4/outt.wav"
    mp4_file = "E:/mini_project/audio_classification/Youtube-8M-WILLOW-master/mp4/p1.mp4"
    os.system("ffmpeg -i mp4_file wav_file")

def main():
    print("convert mp4 to wav start! ")
    subprocess_test()
    #to_audio_test()
    print("convert mp4 to wav finished! ")

if __name__ == "__main__":
    main()

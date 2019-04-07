import soundfile as sf

def soundfile_test():
    wav_file = "E:/out.wav"
    out_data, sample_rate = sf.read(wav_file, dtype='int16')
    print("out_data type: ", type(out_data), " out_data shape:", out_data.shape)
    print("sr type: ", type(sample_rate), " sr shape:", sample_rate.shape)

def main():
    soundfile_test()

if __name__ == "__main__":
    main()
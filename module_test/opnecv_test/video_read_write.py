import cv2
import sys

def getVideoInfo(video_path):
    video_capture = cv2.VideoCapture()
    if not video_capture.open(video_path):
        print(sys.stderr, 'Error:cannot open video_file: ' + video_path)
        return
    last_timestamp = video_capture.get(cv2.CAP_PROP_POS_MSEC)
    width = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    code_method = video_capture.get(cv2.CAP_PROP_FOURCC)
    num_frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(last_timestamp, " ", width, " ", fps, " ", code_method, " ", num_frames)

def getFrame(video_path):
    video_capture = cv2.VideoCapture()
    if not video_capture.open(video_path):
        print(sys.stderr, 'Error:cannot open video_file: ' + video_path)
        return
    last_ts = -99999
    num_retrieved = 0
    while num_retrieved < 30:
        while video_capture.get(cv2.CAP_PROP_POS_MSEC) < 1000 + last_ts:
            print("CAP:", video_capture.get(cv2.CAP_PROP_POS_MSEC))
            print(num_retrieved)
            if not video_capture.read()[0]:
                return
        last_ts = video_capture.get(cv2.CAP_PROP_POS_MSEC)
        has_frames, frame = video_capture.read()
        if not has_frames:
            break
        yield frame
        num_retrieved += 1

if __name__ == "__main__":
    video_path = "./data_space/s062771ur26.mp4"
    for frame in getFrame(video_path):
        print(type(frame))
        pass
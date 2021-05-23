# This script returns the number of i,p and b frames in a video file 
# input - video file (absolute/relative path)
# output - {'I': count, 'P': count, 'B': count}
# Note - if video is invalid then the count will be 0

import argparse
import subprocess

def ffmpegCommand(video):
    # ************Inputs*********
    # video
    # ************Output*********
    # {'I': count, 'P': count, 'B': count}
    print('Calculating......')
    baseCmd = 'ffprobe -loglevel quiet  -show_frames' + ' ' + video
    frames = ['I', 'P', 'B']
    frameDict = {}
    for f in frames:
        cmd = '{} | grep pict_type={} | wc -l'.format(baseCmd,f)
        out = subprocess.check_output(cmd,shell=True)
        frameDict[f] = int(out)
    return frameDict

parser = argparse.ArgumentParser(description='I P and B frame count in a video')
parser.add_argument('video', help='Input Video')
args = parser.parse_args()

#global variable 
videoName = args.video

frameCountDict = ffmpegCommand(videoName)

print(frameCountDict)


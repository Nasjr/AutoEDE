import moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import tkinter
from tkinter import messagebox


class EditVideos:
    def __init__(self, path='E:\\All videos\\'):
        self.path = path
        self.duration = 0

    def concatenate_all_videos(self, desired_length=8):
        try:
            cuts_pool = os.listdir('E:\\All videos\\counter00')
            print(cuts_pool)
            clips_pool = os.listdir(self.path)
            if len(clips_pool) == 0:
                tkinter.messagebox.showwarning(title='Something went wrong', message='Empty Directory please try again')

        except:
            tkinter.messagebox.showwarning(title='Something went wrong',
                                           message='The directory you are trying to access is not Found !')

        try:
            formats = ['mp4', '3gpp']
            videos = []
            for file in clips_pool:
                # check for the file formate
                if file.endswith(formats[0]) or file.endswith(formats[1]):
                    videos.append(self.path + '\\' + file)
        except:
            tkinter.messagebox.showwarning(title='Something went wrong',
                                           message='Error while trying to fetch videos pool')
        cuts = []
        for cut in cuts_pool:
            cuts.append('E:\\All videos\\counter00\\' + cut)
        print(clips_pool)
        # Concatenation logic
        # Get all clips in a form of a video objects list
        clips_objs = []
        numb_objs = []
        for video in videos:
            clips_objs.append(VideoFileClip(video))

        for cut in cuts:
            numb_objs.append(VideoFileClip(cut))

        difference_clip = 0
        valid_clips = []
        # loop n times to get n clips
        # loop k times to get k clips
        count_concat_clips = 0
        i = 0
        while len(clips_objs) != 0:

            for clip in clips_objs:
                self.duration += (clip.duration + numb_objs[i].duration)/ 60
                print(self.duration)
                print(cuts)
                if desired_length > self.duration >= 0:
                    valid_clips.append(clip.resize((1920, 1080)))
                    valid_clips.append(numb_objs[i].resize((1920, 1080)))
                    i += 1
                    clips_objs.remove(clip)
                else:
                    print(self.duration)
                    self.duration = 0
                    count_concat_clips += 1
                    final_clip = concatenate_videoclips(clips=valid_clips)
                    final_clip.write_videofile(
                        'E:\\All videos\\' + 'concatenated_clip' + str(count_concat_clips) + '.mp4',
                        threads=4)
                    break







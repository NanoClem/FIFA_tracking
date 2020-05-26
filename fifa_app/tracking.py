# Import libraries
import cv2
import os
import numpy as np
import time
import json

import requests


def get_list_from_list(key,val,list):
    for elem in list:
        if elem[key] == val:
            return elem

    return "key doesn't exist"

def is_blue(b, g, r):
    if 190 <= b <= 250 and 65 <= g <= 100 and 10 <= r <= 60:
        return True
    return False


def is_red(b, g, r):
    if 15 <= b <= 60 and 0 <= g <= 50 and 170 <= r <= 250:
        return True
    return False


def is_valid_pixel(x, y, list_cancelled_pixels):
    if [x, y] in list_cancelled_pixels:
        # print("la paire est dans la liste des méchants !")
        return False
    # print("la paire n'est pas dans la liste des méchants")
    return True


def add_non_valid_pixels(x, y, list_cancelled_pixels):
    for i in range(x - 10, x + 10):
        for j in range(y - 10, y + 10):
            list_cancelled_pixels.append([i, j])


def normalize_coords(x, y, height, length, x_start, y_start):
    # x_start and y_start correspond to the coordonates of the upper left corner of the zone we're interested in
    return [(x - x_start) / length, (y - y_start) / height]


def create_record_data(teamId, x, y):
    return {
        "team_id": teamId,
        "position": {
            "x": x,
            "y": y
        }
    }


def create_frame_data(videoId, numFrame, records):
    return {
        "video_id": videoId,
        "num": numFrame,
        "records": records
    }




def get_team_id_API(teamName):
    r = requests.get("http://localhost:3000/api/team")
    # print(r.json()[0]['_id'])

    return get_list_from_list('name',teamName,r.json())['_id']


def get_video_id_API(path):
    r = requests.get("http://localhost:3000/api/video")
    return get_list_from_list('path',path,r.json())['_id']


def post_video_API(path):
    params = {'path': path}
    r = requests.post("http://localhost:3000/api/video", params=params)


def post_all_frames_API(frames):

    # print(frameData)
    r = requests.post('http://localhost:3000/api/frame/many', json=frames)


def get_records_from_frame(frame, teamId1, teamId2, coords_field):
    cancelled_blue_pixels = []
    cancelled_red_pixels = []
    height = coords_field[3] - coords_field[1]
    length = coords_field[2] - coords_field[0]
    records = []
    for y in range(coords_field[1], coords_field[3]):
        for x in range(coords_field[0], coords_field[2]):
            if is_blue(frame[y, x, 0], frame[y, x, 1], frame[y, x, 2]) and is_valid_pixel(x, y, cancelled_blue_pixels):
                coords = normalize_coords(x,y,height,length,coords_field[0],coords_field[1])
                rec = create_record_data(teamId1, coords[0], coords[1])
                records.append(rec)
                add_non_valid_pixels(x, y, cancelled_blue_pixels)

            if is_red(frame[y, x, 0], frame[y, x, 1], frame[y, x, 2]) and is_valid_pixel(x, y, cancelled_red_pixels):
                coords = normalize_coords(x,y,height,length,coords_field[0],coords_field[1])
                rec = create_record_data(teamId1, coords[0], coords[1])
                records.append(rec)
                add_non_valid_pixels(x, y, cancelled_red_pixels)


    return records


def post_all_frames(pathVideo, coords_field, firstFrame, lastFrame):
    vidcap = cv2.VideoCapture(pathVideo)
    success, frame = vidcap.read()
    nb_frame = 0
    nb_records = 0
    success = True

    videoId = get_video_id_API(pathVideo)
    teamId1 = get_team_id_API('Liverpool')
    teamId2 = get_team_id_API('Madrid')
    frames = []


    # Read the video frame by frame
    while success:

        cv2.imshow('Match Detection', frame)
        if firstFrame < nb_frame < lastFrame : #the radar appears at ~500
            if nb_frame % 10 == 0: #every 10 frames we capture all positions, otherwise they don't move enough
                records = get_records_from_frame(frame,teamId1,teamId2,coords_field)
                if len(records)>15: #we capture frames only when there is more than 15 players, to avoid useless frames
                    frames.append(create_frame_data(videoId, nb_frame, records))
                    nb_records+=len(records)
        nb_frame += 1

        print("FRAME" + str(nb_frame))
        print("taille frames : " + str(nb_records))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        success, frame = vidcap.read()

    post_all_frames_API(frames)

    vidcap.release()
    cv2.destroyAllWindows()


# ------------------------------

coords_field = [449, 415, 791, 621]  # x,y of the upper-left corner, x,y of the bottow-right corner)
post_all_frames('capture.mp4', coords_field,450,2000)
print(501 % 5)


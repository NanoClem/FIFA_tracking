# Import libraries
import cv2
import requests
import sys


def get_list_from_list(key,val,list):
    # Gets a specific list from a containing list by it's value to a key
    for elem in list:
        if elem[key] == val:
            return elem

    return "no element has this key/val"

def is_blue(b, g, r):
    # Tests if the blue, green and red colors of a pixel make it a "blue" pixel
    if 190 <= b <= 250 and 65 <= g <= 100 and 10 <= r <= 60:
        return True
    return False


def is_red(b, g, r):
    # Tests if the blue, green and red colors of a pixel make it a "red" pixel
    if 15 <= b <= 60 and 0 <= g <= 50 and 170 <= r <= 250:
        return True
    return False


def is_valid_pixel(x, y, list_cancelled_pixels):
    # Returns True if the [x,y] tuple is in a list of "cancelled" pixels (= pixels which we won't analyse anymore)
    if [x, y] in list_cancelled_pixels:
        return False
    return True


def add_non_valid_pixels(x, y, list_cancelled_pixels):
    # Adds a range of 20x20 (400) pixels into the list of cancelled pixels
    for i in range(x - 10, x + 10):
        for j in range(y - 10, y + 10):
            list_cancelled_pixels.append([i, j])


def normalize_coords(x, y, height, length, x_start, y_start):
    # Normalizes the coords to have their positions in proportion to the field's positions (from 0 to 1)
    # x_start and y_start correspond to the coordinates of the upper left corner of the zone we're interested in
    return [(x - x_start) / length, (y - y_start) / height]


def create_record_data(teamId, x, y):
    # Creates the dictionnary of positions of a record (this includes a teamId, a 'x' position and 'y' position)
    return {
        "team_id": teamId,
        "position": {
            "x": x,
            "y": y
        }
    }


def create_frame_data(videoId, numFrame, records):
    # Creates the dictionnary of a frame (this includes a videoId, a number of frame, and a list of record dictionnaries)
    return {
        "video_id": videoId,
        "num": numFrame,
        "records": records
    }




def get_team_id_API(teamName):
    # Gets the teamId of a teamName from the API
    r = requests.get("http://localhost:3000/api/team")

    return get_list_from_list('name',teamName,r.json())['_id']


def get_video_id_API(path):
    # Gets the videoId of a path from the API
    r = requests.get("http://localhost:3000/api/video")
    return get_list_from_list('path',path,r.json())['_id']


def post_video_API(path):
    # Posts a video to the API with a path dictionnary (for example : {'path':'capture.mp4'})
    r = requests.post("http://localhost:3000/api/video", json=path)


def post_team_API(teamName):
    # Posts a team to the API with a name dictionnary (for example : {'name':'Liverpool'})
    r = requests.post("http://localhost:3000/api/team", json=teamName)


def post_all_frames_API(frames):
    # Posts a list of frame dictionnaries to the API
    r = requests.post('http://localhost:3000/api/frame/many', json=frames)


def get_records_from_frame(frame, teamId1, teamId2, coords_field):
    # Creates a list of position records from a specific frame by scanning the whole field zone and "cancelling" a zone
    # of pixels each time a player (blue or red) has been found. The zone is a 20x20 pixels zone around a blue of red
    # found pixels.
    cancelled_blue_pixels = []
    cancelled_red_pixels = []
    height = coords_field[3] - coords_field[1]
    length = coords_field[2] - coords_field[0]
    records = []
    for y in range(coords_field[1], coords_field[3]):  # from up to bottom
        for x in range(coords_field[0], coords_field[2]): # from left to right
            if is_blue(frame[y, x, 0], frame[y, x, 1], frame[y, x, 2]) and is_valid_pixel(x, y, cancelled_blue_pixels):
                # checks if the x,y pixel is blue and if it's not in an "cancelled" zone
                coords = normalize_coords(x,y,height,length,coords_field[0],coords_field[1])
                rec = create_record_data(teamId1, coords[0], coords[1])
                records.append(rec)
                # adds the x,y pixel to the cancelled blue pixels
                add_non_valid_pixels(x, y, cancelled_blue_pixels)

            if is_red(frame[y, x, 0], frame[y, x, 1], frame[y, x, 2]) and is_valid_pixel(x, y, cancelled_red_pixels):
                # checks if the x,y pixel is red and if it's not in an "eliminated" zone
                coords = normalize_coords(x,y,height,length,coords_field[0],coords_field[1])
                rec = create_record_data(teamId2, coords[0], coords[1])
                records.append(rec)
                # adds the x,y pixel to the cancelled red pixels
                add_non_valid_pixels(x, y, cancelled_red_pixels)

    return records


def post_all_frames(pathVideo, coords_field, firstFrame, lastFrame, teamName1, teamName2):
    # Posts all the frames of a video to the API, using the previous functions

    # Capture of the video from the given path
    vidcap = cv2.VideoCapture(pathVideo)

    # Gets the total number of frames in the video (useful for the display of the %of processing evolution)
    nb_total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    success, frame = vidcap.read()
    success = True

    # Sets the number of frames and scanned framed to 0
    nb_frame = 0
    scanned_frames = 0
    frames = []

    # Gets the useful data from the API
    videoId = get_video_id_API(pathVideo)
    teamId1 = get_team_id_API(teamName1)
    teamId2 = get_team_id_API(teamName2)

    # Reads the video frame by frame
    while success:

        # Shows the frames 1 by 1 in a window, not necessary
        cv2.imshow('Match Detection', frame)

        # Only scans the frames from a given frame range.
        if firstFrame < nb_frame < lastFrame :
            if nb_frame % 10 == 0: # every 10 frames we capture all positions, to have useful information
                records = get_records_from_frame(frame,teamId1,teamId2,coords_field)
                scanned_frames+=1
                if len(records)>15: # we capture frames only when there is more than 15 players, to avoid useless frames
                    frames.append(create_frame_data(videoId, nb_frame, records))

        nb_frame += 1
        sys.stdout.write('\r'+"Reading "+str(nb_frame)+"/"+str(nb_total_frames)+" frames. Scanning "+str(scanned_frames)
                            +"/"+str((lastFrame-firstFrame)//10)+" frames.")

        # This code is useful to the videoCapture of opencv
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        success, frame = vidcap.read()



    # Sends the list of frames to the API
    post_all_frames_API(frames)

    vidcap.release()
    cv2.destroyAllWindows()



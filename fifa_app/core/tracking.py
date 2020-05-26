from fifa_app.core.tracking_functions import *

# # To send a video to the API from its path
# post_video_API({'path': 'capture.mp4'})
# print("The video has been sent.")
#
# # To send teams to the API from their name
# post_team_API({'name': 'Marseille'})
# post_team_API({'name': 'Paris'})
# print("The teams has been sent.")

# To sends the useful frames of a video the API
print("Starting to scan the video...")
coords_field = [449, 415, 791, 621]  # x,y of the upper-left corner, x,y of the bottow-right corner)
post_all_frames('capture.mp4', coords_field,450,2000,"Marseille","Paris")
print("Ending of the capture")


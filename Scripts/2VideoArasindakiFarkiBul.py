import cv2

def compare_frames(original_frame, modified_frame, threshold=int(input("Set Threshold Value (The recommended value is 10): "))):
  original_gray = cv2.cvtColor(original_frame, cv2.COLOR_BGR2GRAY)
  modified_gray = cv2.cvtColor(modified_frame, cv2.COLOR_BGR2GRAY)

  # Kareler arasındaki farkı bul
  frame_diff = cv2.absdiff(original_gray, modified_gray)

  mean_diff = cv2.mean(frame_diff)[0]

  if mean_diff > threshold:
    return True
  else:
    return False

def save_frame(frame, frame_number):
  cv2.imwrite("img_{}.jpg".format(frame_number),frame)
k=0
original_video = cv2.VideoCapture(input("Set First Video Name With .mp4. e.g.:'video.mp4': "))
modified_video = cv2.VideoCapture(input("Set Second Video Name With .mp4 e.g.:'video2.mp4': "))
frame_number = 0

while True:
  original_ret, original_frame = original_video.read()
  modified_ret, modified_frame = modified_video.read()

  if not original_ret or not modified_ret:
    break

  if compare_frames(original_frame, modified_frame):
    save_frame(modified_frame, frame_number)
  else:
    k+=1
    print("Same Frame! Frame Number: "+str(k),end="\r")

  frame_number += 1

original_video.release()
modified_video.release()

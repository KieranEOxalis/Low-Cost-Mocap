from pseyepy import Camera
import cv2 as cv

# Initialize all connected cameras
c = Camera()

# Continuously capture and display frames
while True:
    # Read from the cameras
    frames, timestamp = c.read()

    # Display each frame in a separate window
    for i, frame in enumerate(frames):
        window_name = f'Camera {i + 1} Frame'
        cv.imshow(window_name, frame)
    
    # Wait for a short period, check for key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When finished, close the camera and destroy the windows
c.end()
cv.destroyAllWindows()

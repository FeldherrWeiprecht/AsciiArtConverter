import cv2
import numpy as np

def get_skin_mask(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    lower = np.array([0, 133, 77], dtype=np.uint8)
    upper = np.array([255, 173, 127], dtype=np.uint8)
    return cv2.inRange(ycrcb, lower, upper)

def render(frame, width, height, chars, cols, rows, font, scale, thickness):
    resized = cv2.resize(frame, (cols, rows))
    mask = get_skin_mask(resized)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    output = np.zeros((rows * 12, cols * 8, 3), dtype=np.uint8)

    for y in range(rows):
        for x in range(cols):
            if mask[y, x] > 0:
                value = gray[y, x]
                index = value * len(chars) // 256
                char = chars[index]
                pos = (x * 8, y * 12 + 10)
                cv2.putText(output, char, pos, font, scale, (255, 255, 255), thickness, cv2.LINE_AA)

    return cv2.resize(output, (width, height), interpolation=cv2.INTER_NEAREST)

def main():
    chars = " .:+=*%@"
    cols = 200
    rows = 100
    scale = 0.5
    thickness = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    width = 1000
    height = 600

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    cv2.namedWindow('AsciiArtConverter', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('AsciiArtConverter', width, height)

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            img = render(frame, width, height, chars, cols, rows, font, scale, thickness)
            cv2.imshow('AsciiArtConverter', img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

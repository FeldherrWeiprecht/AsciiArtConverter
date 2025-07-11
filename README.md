# AsciiArtConverter

## Description

This python program captures live video from your webcam and detects visible skin areas using a color filter and renders them as real time ascii art on the screen.

## How It Works

1. Capture frames from the webcam.
2. Convert the frame to YCrCb and use a skin mask.
3. Convert the result to grayscale.
4. Map brightness values to ascii characters.
5. Draw ascii characters into an OpenCV image buffer.
6. Display the final ascii rendered frame.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python numpy
```

## Usage

Run the script:

```bash
python main.py
```

Press `q` to exit the program.

## Configuration

- Ascii characters used: ` .:+=*%@`.
- Adjust `cols` and `rows` to change the resolution.
- Window size can be set using `width` and `height` variables.

## Notes

- Works best in good lighting conditions.

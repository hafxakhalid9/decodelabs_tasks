# Optical Character Recognition (OCR) App

A basic Python application that performs text recognition on images using EasyOCR (a pre-trained PyTorch-based model) alongside OpenCV and Matplotlib for visual bounding box display.

## Features

- Pre-trained CRAFT + ResNet model via EasyOCR.
- Extracts text content and confidence scores.
- Annotates bounding boxes visually onto the image.

## Prerequisites & Setup

1. **Clone or create project repository:**
```bash
mkdir text-recognition-app
cd text-recognition-app
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Add a target image:**
Place an image containing clear text into the root directory and name it `sample_text.png`.

## Execution

Run the main script:

```bash
python main.py
```
## Understanding Output

- **Terminal Output:** Displays detected text string and confidence score ($0.00$ to $1.00$).
- **Visual Output:** Opens a window showing green bounding boxes around recognized text regions along with predicted text labels.
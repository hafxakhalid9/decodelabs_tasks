import cv2
import easyocr
import matplotlib.pyplot as plt


def run_text_recognition(image_path: str):
    # 1. Initialize the EasyOCR reader with pre-trained models (English language)
    print("[+] Loading pre-trained OCR model...")
    reader = easyocr.Reader(["en"], gpu=False)

    # 2. Perform text recognition on the input image
    print(f"[+] Processing image: {image_path}...")
    results = reader.readtext(image_path)

    # 3. Load original image with OpenCV for visual annotation
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(
            f"Could not load image at path: '{image_path}'. Ensure the file exists."
        )

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print("\n" + "=" * 45)
    print("         RECOGNIZED TEXT OUTPUT")
    print("=" * 45)

    # 4. Process and display model outputs
    for bbox, text, confidence in results:
        print(f"Detected Text: '{text}' | Confidence: {confidence:.2f}")

        # Extract bounding box corner points
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))

        # Draw green bounding box around text
        cv2.rectangle(
            image_rgb, top_left, bottom_right, color=(0, 255, 0), thickness=2
        )

        # Draw label above bounding box
        cv2.putText(
            image_rgb,
            text,
            (top_left[0], max(top_left[1] - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2,
        )

    print("=" * 45 + "\n")

    # 5. Display output image with Matplotlib
    plt.figure(figsize=(10, 8))
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.title("Image Text Recognition (EasyOCR)", fontsize=14)
    plt.show()


if __name__ == "__main__":
    sample_image = "sample_text.png"
    run_text_recognition(sample_image)
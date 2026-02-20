import cv2
import os
import sys
from deepface import DeepFace

# Folder and file name
FACE_FOLDER = "faces"
FACE_FILE = "authorized.jpg"
REGISTERED_FACE_PATH = os.path.join(FACE_FOLDER, FACE_FILE)

MODEL_NAME = "ArcFace"


def register_face():
    print("[JARVIS] Starting face registration...")

    # Create folder if not exists
    if not os.path.exists(FACE_FOLDER):
        os.makedirs(FACE_FOLDER)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Cannot access webcam.")
        return False

    print("[JARVIS] Look at the camera.")
    print("[JARVIS] Press SPACE to capture your face.")
    print("[JARVIS] Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to capture frame.")
            break

        # Draw guide rectangle
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        cv2.rectangle(frame, (cx - 100, cy - 120),
                      (cx + 100, cy + 120), (0, 255, 0), 2)

        cv2.putText(frame,
                    "Align face in box & press SPACE",
                    (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2)

        cv2.imshow("Jarvis - Face Registration", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            try:
                # Check if face is detected
                DeepFace.extract_faces(
                    img_path=frame,
                    detector_backend="opencv"
                )

                cv2.imwrite(REGISTERED_FACE_PATH, frame)
                print(f"[JARVIS] Face saved at: {REGISTERED_FACE_PATH}")

                cap.release()
                cv2.destroyAllWindows()
                return True

            except Exception:
                print("[WARNING] No face detected. Try again.")

        elif key == ord('q'):
            print("[JARVIS] Registration cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return False


def verify_face():
    if not os.path.exists(REGISTERED_FACE_PATH):
        print("[JARVIS] No registered face found.")
        print("Run: python face_auth.py --register")
        return False

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Cannot access webcam.")
        return False

    print("[JARVIS] Verifying identity...")

    MAX_ATTEMPTS = 30
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Jarvis - Face Verification", frame)
        cv2.waitKey(1)

        try:
            result = DeepFace.verify(
                img1_path=frame,
                img2_path=REGISTERED_FACE_PATH,
                model_name=MODEL_NAME,
                detector_backend="opencv",
                enforce_detection=True
            )

            if result["verified"]:
                print("[JARVIS] Identity verified.")
                cap.release()
                cv2.destroyAllWindows()
                return True
            else:
                print("[JARVIS] Face not matched.")
                break

        except Exception:
            attempts += 1
            continue

    cap.release()
    cv2.destroyAllWindows()
    return False


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--register":
        success = register_face()
        if success:
            print("[DONE] Registration complete.")
        else:
            print("[FAILED] Registration failed.")
    else:
        print("Usage:")
        print("python face_auth.py --register")
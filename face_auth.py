import cv2
import os
import sys
from deepface import DeepFace

# Path where your registered face image will be saved
REGISTERED_FACE_PATH = "registered_face.jpg"
MODEL_NAME = "ArcFace"  # Pretrained model from DeepFace


def register_face():
    """
    Run this once to register your face.
    Captures your face from webcam and saves it as the authorized user.
    """
    print("[JARVIS] Starting face registration...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return False

    print("[JARVIS] Look at the camera. Press SPACE to capture your face, or Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read from webcam.")
            break

        # Draw a guide rectangle in the center
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        cv2.rectangle(frame, (cx - 100, cy - 120), (cx + 100, cy + 120), (0, 255, 0), 2)
        cv2.putText(frame, "Align face in box. Press SPACE to capture.", 
                    (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Jarvis - Face Registration", frame)
        key = cv2.waitKey(1)

        if key == ord(' '):  # SPACE to capture
            # Validate that a face exists in the frame before saving
            try:
                DeepFace.extract_faces(img_path=frame, detector_backend='opencv')
                cv2.imwrite(REGISTERED_FACE_PATH, frame)
                print(f"[JARVIS] Face registered successfully! Saved to '{REGISTERED_FACE_PATH}'")
                cap.release()
                cv2.destroyAllWindows()
                return True
            except Exception:
                print("[WARNING] No face detected in frame. Please try again.")

        elif key == ord('q'):  # Q to quit
            print("[JARVIS] Registration cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return False


def verify_face():
    """
    Called every time Jarvis starts.
    Captures a live frame and compares it against the registered face.
    Returns True if identity is verified, False otherwise.
    """
    # Check if a face has been registered
    if not os.path.exists(REGISTERED_FACE_PATH):
        print("[JARVIS] No registered face found. Please run registration first.")
        print("         Run: python face_auth.py --register")
        return False

    print("[JARVIS] Starting face verification...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return False

    MAX_ATTEMPTS = 30  # ~5 seconds at 6fps before giving up
    attempt = 0
    verified = False

    print("[JARVIS] Look at the camera for verification...")

    while attempt < MAX_ATTEMPTS:
        ret, frame = cap.read()
        if not ret:
            break

        # Draw UI
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        cv2.rectangle(frame, (cx - 100, cy - 120), (cx + 100, cy + 120), (255, 255, 0), 2)
        cv2.putText(frame, "Verifying identity...", 
                    (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        cv2.imshow("Jarvis - Identity Verification", frame)
        cv2.waitKey(1)

        try:
            result = DeepFace.verify(
                img1_path=frame,
                img2_path=REGISTERED_FACE_PATH,
                model_name=MODEL_NAME,
                enforce_detection=True,
                detector_backend='opencv'
            )

            if result["verified"]:
                verified = True
                distance = result["distance"]
                print(f"[JARVIS] Identity verified! (Confidence distance: {distance:.4f})")
                break
            else:
                print(f"[JARVIS] Face not matched. (Distance: {result['distance']:.4f})")
                break  # Stop on first confident non-match

        except Exception:
            # No face detected in this frame, try next frame
            attempt += 1
            continue

    cap.release()
    cv2.destroyAllWindows()
    return verified


# ──────────────────────────────────────────────
# Run directly for registration:
#   python face_auth.py --register
# ──────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--register":
        success = register_face()
        if success:
            print("[DONE] You can now start Jarvis. It will recognize your face on startup.")
        else:
            print("[FAILED] Registration failed. Please try again.")
    else:
        print("Usage:")
        print("  python face_auth.py --register   → Register your face (run once)")
        print("  Import verify_face() in main.py  → For authentication on startup")

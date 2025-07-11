import argparse
import os
import sys

import pymupdf
import pyttsx3


def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from file: {pdf_path}")
    doc = pymupdf.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text


def speak_text(text):
    print("Speaking text")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def export_text_to_wav(text, output_path):
    print(f"Saving audio to file: {output_path}")
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF and optionally speak it or save to WAV."
    )
    parser.add_argument("pdf_path", type=str, help="PDF file path")
    parser.add_argument(
        "-o", "--output", type=str, default="output.wav", help="output WAV file path"
    )
    parser.add_argument(
        "-s", "--speak", action="store_true", help="speak the extracted text"
    )
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"File not found: {args.pdf_path}")
        sys.exit(1)

    text = extract_text_from_pdf(args.pdf_path)

    if not text.strip():
        print("No text was extracted from file")
        sys.exit(1)

    if args.speak:
        speak_text(text)
    else:
        export_text_to_wav(text, args.output)

    print("Done")


if __name__ == "__main__":
    main()

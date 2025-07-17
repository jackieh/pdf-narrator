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


def do_with_default_tts_engine(func):
    engine = pyttsx3.init()
    engine.setProperty("volume", 1.0)
    engine.setProperty("rate", 175)
    func(engine)
    engine.runAndWait()
    engine.stop()


def speak_text(text):
    print("Speaking text")
    do_with_default_tts_engine(lambda engine: engine.say(text))


def export_text_to_wav(text, output_path):
    print(f"Saving audio to file: {output_path}")
    do_with_default_tts_engine(lambda engine: engine.save_to_file(text, output_path))


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from PDF and either speak it or save to WAV."
    )
    parser.add_argument("pdf_path", type=str, help="PDF file path")
    parser.add_argument("-o", "--output", type=str, help="output WAV file path")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"File not found: {args.pdf_path}")
        sys.exit(1)

    text = extract_text_from_pdf(args.pdf_path)

    if not text.strip():
        print("No text was extracted from file")
        sys.exit(1)

    if args.output:
        export_text_to_wav(text, args.output)
    else:
        speak_text(text)

    print("Done")


if __name__ == "__main__":
    main()

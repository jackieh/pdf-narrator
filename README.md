# PDF Narrator

Uses system TTS to read a PDF out loud for you

Requires:

- Python 3.9+
- [Poetry](https://python-poetry.org/)
- [Espeak](https://espeak.sourceforge.net/) or [Espeak NG](https://github.com/espeak-ng/espeak-ng) on Linux

## How to run

To install dependencies:

```bash
poetry install
```

To export audio to `output.wav`:

```bash
poetry run pdf-narrator <pdf_path> --output output.wav
```

To speak audio:

```bash
poetry run pdf-narrator <pdf_path>
```

To see all usage options:

```bash
poetry run pdf-narrator --help
```

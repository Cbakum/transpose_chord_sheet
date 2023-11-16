import user_select as user
import music
from docx import Document
import re
import sys


def parse_chords_docx(file_path):
    doc = Document(file_path)
    cleaned_chords = []
    for paragraph in doc.paragraphs:
        chord_matches = re.findall(r'\[([^][]+)]', paragraph.text)
        for item in chord_matches:
            item_cleaned = music.clean_chord(item)
            cleaned_chords.append(item_cleaned)
            #print(f'Original Symbol: {item}\t\tCleaned: {item_cleaned}')
            #print()
    return cleaned_chords

def main(argv):
  # Find word document
  if len(argv) < 2:
    filepath = user.open_file_dialog()
  else:
    filepath = argv[1]

  # Parse document for chords
  chords = parse_chords_docx(filepath)

  # Pick transposition interval
  interval = user.get_transpose_params()["Transpose"]     #consider edge cases here
  print(interval)
  # Apply Transposition

if __name__ == "__main__":
    main(sys.argv)
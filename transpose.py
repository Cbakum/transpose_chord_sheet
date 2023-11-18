#!/usr/bin/env python

import src.doc_parse as doc
import src.music as music
import src.user_select as user
import sys


def main(argv):
    valid_argv = [1, 2, 3]
    arg_len = len(argv)
    # Parse args
    if arg_len not in valid_argv:
        raise ValueError("Invalid number of command-line arguments. Please provide the required number of arguments.")     

    # Allow command line args for development purposes
    if arg_len==3:
        delta_semitones = music.intervals_array[int(argv[2])].value[0]
        delta_pitch_class = music.intervals_array[int(argv[2])].value[1]
        filepath = argv[1]
    elif arg_len==2:
      filepath = argv[1]
      delta_semitones, delta_pitch_class = user.get_transpose_params()
      if delta_semitones == -1:     
         raise ValueError("Transposition not selected")
    else:
      filepath = user.open_file_dialog()
      if not filepath:
         raise ValueError("Open file failed")
      delta_semitones, delta_pitch_class = user.get_transpose_params()
      if delta_semitones == -1:     
         raise ValueError("Transposition not selected")

    # Create transposition dictionary
    chord_mapping = {}
    for old_chord in music.Note:
      # Take user defined parameters to transform old chord into new chord
      new_chord = music.transpose_chord(old_chord.value[0], delta_pitch_class, delta_semitones)
      # Load data into dictionary to define correct transposition
      chord_mapping[old_chord.value[0]] = new_chord

    # Parse document for chords
    # Replace chords with transpositions
    doc.parse_chords_docx(filepath, chord_mapping)

    # Fix bold formatting in document


if __name__ == "__main__":
    main(sys.argv)
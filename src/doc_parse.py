import src.user_select as user
import src.music as music
from docx import Document
import re

def create_target_file_path(original_file_path):
    # Find the index of "doc" in the file name
    index = original_file_path.find(".")

    if index != -1:
        # Extract the file name without the extension and text after "."
        file_name = original_file_path[:index]

        # Create the target file path by appending "_transposed.docx"
        target_file_path = f"{file_name}_transposed.docx"

    else:
        # Create dummy filepath to avoid overwriting source file
        target_file_path = "error_creating_filename.docx"
    
    return target_file_path

def parse_chords_docx(file_path: str, chord_mapping: dict):
    doc = Document(file_path)
    converted_chords = {}
    for paragraph in doc.paragraphs:
        chord_matches = re.findall(r'\[([^][]+)]', paragraph.text)
        # Pass one to mark which chords have been replaced
        for item in chord_matches:
            # disconnect the root from quality in original chord
            root, quality = music.clean_chord(item)
            #transpose root from mapping then reattach the quality
            transposed_chord = chord_mapping[root] + quality
            converted_chords[item] = transposed_chord

            # Attach * flag to indicate chord has been replaced
            # This avoids double replacing a chord on later loops,
            #  which would create incorrect transposition
            transposed_chord = f'{transposed_chord}*'

            # This replaces properly, but messes with formatting
            paragraph.text = paragraph.text.replace(f'[{item}]', f'[{transposed_chord}]')
            #print(f'{item} {transposed_chord}')

        # Pass two to remove marker
        for item in chord_matches:
            # find the transposed chords again
            root, quality = music.clean_chord(item)
            transposed_chord = chord_mapping[root] + quality

            #remove the * flag that indicated chords were replaced
            paragraph.text = paragraph.text.replace(f'[{transposed_chord}*]', f'[{transposed_chord}]')

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            print(run.text)

    target_file_path = create_target_file_path(file_path)
    doc.save(target_file_path)

# Test concept
def concatenate_runs(paragraph):
    concatenated_text = ""
    for run in paragraph.runs:
        concatenated_text += run.text
    return concatenated_text

# Test concept
def replace_chords_docx(file_path, chord_mapping):
    doc = Document(file_path)

    # First pass: Replace old chords with temporary placeholders
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
           print(run.text)
        line_text = concatenate_runs(paragraph)


        #try new approach here to concatenate all bold runs

        print("Original Line:", line_text)
        for run in paragraph.runs:
           print(run.text)
        chord_start = 0
        while '[' in line_text[chord_start:]:
            chord_start = line_text.find('[', chord_start)
            chord_end = line_text.find(']', chord_start)

            if chord_start != -1 and chord_end != -1:
                chord = line_text[chord_start + 1:chord_end]
                #print("Identified Chord:", chord)
                if chord in chord_mapping:
                    transposed_chord = chord_mapping[chord]
                    # Replace old chord with temporary placeholder
                    line_text = line_text[:chord_start] + f'[{transposed_chord}~]' + line_text[chord_end + 1:]
                    chord_start = chord_end + 1
                else:
                    # Move the cursor to avoid an infinite loop
                    chord_start += 1
            else:
                break

        # Update the paragraph text with the processed line
        paragraph.text = line_text.replace('~', '')
        #print("Processed Line:", paragraph.text)

    #print("Saving")
    doc.save("test.docx")

#check chord transpositions
def debug_transpose(old_chords: list, delta_pitch_class, delta_semitones):
   for old_chord in old_chords:
    new_chord = music.transpose_chord(old_chord, delta_pitch_class, delta_semitones)
    print(f'Old Chord: {old_chord}       New Chord: {new_chord}')
from enum import Enum

class Interval(Enum):
    '''
    Structured as a tuple of two elements\n
    Element One: Interval represented numerically as semitones between pitches\n
    Element Two: Scale degree represented numerically as scale degrees between notes
    '''
    UNISON = (0, 0)
    MINOR_SECOND = (1, 1)
    MAJOR_SECOND = (2, 1)
    MINOR_THIRD = (3, 2)
    MAJOR_THIRD = (4, 2)
    PERFECT_FOURTH = (5, 3)
    TRITONE = (6, 3)
    PERFECT_FIFTH = (7, 4)
    MINOR_SIXTH = (8, 5)
    MAJOR_SIXTH = (9, 5)
    MINOR_SEVENTH = (10, 6)
    MAJOR_SEVENTH = (11, 6)

# Order intervals in chromatic sequence
intervals_array = [Interval.UNISON, Interval.MINOR_SECOND,
             Interval.MAJOR_SECOND, Interval.MINOR_THIRD,
             Interval.MAJOR_THIRD, Interval.PERFECT_FOURTH,
             Interval.TRITONE, Interval.PERFECT_FIFTH,
             Interval.MINOR_SIXTH, Interval.MAJOR_SIXTH,
             Interval.MINOR_SEVENTH, Interval.MAJOR_SEVENTH]

class Note(Enum):
   '''
   Structured as a tuple of three elements:\n
   Element One: The text to represent this pitch in the document\n
   Element Two: Pitch represented numerically as semitones above C\n
   Element Three: Scale degree represented numerically as scale degrees above C
   '''
   Cflat  = ("Cb", 11, 0)
   C      = ("C", 0, 0)
   Csharp = ("C#", 1, 0)
   Dflat  = ("Db", 1, 1)
   D      = ("D", 2, 1)
   Dsharp = ("D#", 3, 1)
   Eflat  = ("Eb", 3, 2)
   E      = ("E", 4, 2)
   Esharp = ("E#", 5, 2)
   Fflat  = ("Fb", 4, 3)
   F      = ("F", 5, 3)
   Fsharp = ("F#", 6, 3)
   Gflat  = ("Gb", 6, 4)
   G      = ("G", 7, 4)
   Gsharp = ("G#", 8, 4)
   Aflat  = ("Ab", 8, 5)
   A      = ("A", 9, 5)
   Asharp = ("A#", 10, 5)
   Bflat  = ("Bb", 10, 6)
   B      = ("B", 11, 6)
   Bsharp = ("B#", 0, 6)

class Dir(Enum):
   '''
   For use in the dropdown menu while selecting tranposition parameters
   '''
   UP   = 0
   DOWN = 1

def clean_chord(chord: str):
  '''
  Takes a chord symbol and seperates the root of the chord,
  the quality of the chord, and the bass (if inverted).\n
  args:
      chord (str)- The chord symbol taken from the source .docx
  returns:
      root (str)- The root note of the chord\n
      quality (str)- Any tonality/modifications to the chord\n
      bass (str)- The bass note of the chord (if inverted in the form of root/bass)
  '''
  if len(chord)>1:
    if chord[1] not in ['b', '#']:
        # root is only first letter if not flat or sharp
        root = chord[:1]
        quality = chord[1:]
        bass = ""
    else:
      root = chord[:2]
      quality = chord[2:]
      bass = ""
    
    # Check if inverted. Will need to seperate bass from quality
    if '/' in quality:
       index = quality.find("/")
       bass = quality[index+1:]
       quality = quality[:index+1]

  # Chord is single letter
  else:
     root = chord
     quality = ""
     bass = ""


  return root, quality, bass

def transpose_chord(origin: str, delta_scale_degree: int, delta_semitones: int) -> str:
  '''
  Takes a chord symbol and applies the user chosen parameters to achieve the 
  desired transposition\n
  args:
      origin (str)- Note to be transposed\n
      delta_scale_degree (int)- The number of scale degrees upwards to transpose\n
      delta_semitones (int)- The number of semitones upwards to transpose\n
  returns:
      target_note (str)- The pitch that the input note transposes to
  '''
  note_origin = Note[origin.replace("#", "sharp").replace("b", "flat")]
  target_note = None  

  # Mod7 to account for overflow in scale degree
  target_scale_degree = (note_origin.value[2] + delta_scale_degree) % 7
  # Mod12 to account for overflow in semitones
  target_semitone = (note_origin.value[1] + delta_semitones) % 12

  for note in Note:
    if (note.value[1], note.value[2]) == (target_semitone, target_scale_degree):
        target_note = note.value[0]
        break
  
  # Accounts for edge case where a minor second is really an augmented unison
  # Or case where a tritone is a diminished fifth rather than augmented fourth
  if target_note is None and (delta_scale_degree==1 or delta_scale_degree==3):
     for note in Note:
        # If note object contains the target semiton, but is in the same pitch class
        if (note.value[1], note.value[2]) == (target_semitone, note_origin.value[2]):
          # Select the name from that note
          target_note = note.value[0]
          break

  if target_note is None:
    # Print statements for debugging
    #print(f'\nTransposition error.\nOrigin: {origin}')
    #print(f'Scale Degrees: {note_origin.value[2]} + {delta_scale_degree}')
    #print(f'Semitones: {note_origin.value[1]} + {delta_semitones}')
    target_note = "ERROR"

  return target_note

#check chord transpositions
def debug_transpose(old_chords: list, delta_pitch_class, delta_semitones):
   '''
   Debug function to test correctness of transpose_chord function
   '''
   for old_chord in old_chords:
    new_chord = music.transpose_chord(old_chord, delta_pitch_class, delta_semitones)
    print(f'Old Chord: {old_chord}       New Chord: {new_chord}')
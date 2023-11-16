from enum import Enum

class Interval(Enum):
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

intervals_array = [Interval.UNISON, Interval.MINOR_SECOND,
             Interval.MAJOR_SECOND, Interval.MINOR_THIRD,
             Interval.MAJOR_THIRD, Interval.PERFECT_FOURTH,
             Interval.TRITONE, Interval.PERFECT_FIFTH,
             Interval.MINOR_SIXTH, Interval.MAJOR_SIXTH,
             Interval.MINOR_SEVENTH, Interval.MAJOR_SEVENTH]

class Note(Enum):
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
   UP   = 0
   DOWN = 1

def clean_chord(chord: str):
  if len(chord)>1:
    if chord[1] not in ['b', '#']:
        result = chord[:1]
        remainder = chord[1:]
    else:
      result = chord[:2]
      remainder = chord[2:]
  else:
     result = chord
     remainder = ""
  print(f'Original: {chord}\nCleaned: {result}\nRemainder: {remainder}')
  recreate = result + remainder
  print(f'Recreation: {recreate}\n')
  return result, remainder

def transpose_chord(origin: str, delta_pitch_class: int, delta_semitones: int) -> str:
  note_origin = Note[origin.replace("#", "sharp").replace("b", "flat")]
  target_note = None  

  target_pitch_class = (note_origin.value[2] + delta_pitch_class) % 7
  target_semitone = (note_origin.value[1] + delta_semitones) % 12

  for note in Note:
    if (note.value[1], note.value[2]) == (target_semitone, target_pitch_class):
        target_note = note.value[0]
        break
  
  # Edge case handling
  if target_note is None and delta_pitch_class==1:
     for note in Note:
        if (note.value[1], note.value[2]) == (target_semitone, note_origin.value[2]):
          target_note = note.value[0]
          break

  if target_note is None:
    print(f'\nTransposition error.\nOrigin: {origin}')
    print(f'Scale Degrees: {note_origin.value[2]} + {delta_pitch_class}')
    print(f'Semitones: {note_origin.value[1]} + {delta_semitones}')
    target_note = "ERROR"

  return target_note


from enum import Enum

def clean_chord(chord: str):
  if len(chord)>1:
    if chord[1] not in ['b', '#']:
        result = chord[:1]
    else:
      result = chord[:2]
  else:
     result = chord
  return result

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

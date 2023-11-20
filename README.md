# transpose_chord_sheet

Parses .docx files for chord symbols within brackets **[CHORD]**, transposes them to other keys, and writes new .docx with updated chords

## Description

This program was written to make transposing chord sheets easier and faster for ukulele club. This works with .docx files (can come from Word documents or Google Docs). It preserves the original document and creates a copy with the new chord symbols. The main requirement for this program is that all chord symbols must be contained within square brackets:

**<p style="text-align: center;">[CHORD]</p>**

A simple music transposition library is included to define notes and intervals mathematically (in terms of semitones and scale degrees). String parsing is used to take in any arbitrary chord symbol and perform the proper transpositions. Complex chord symbols are broken down into up to three component pieces before transposition is applied. For example:

**<p style="text-align: center;">[Ebmaj7/Bb]</p>**

The music library will take this chord and break it down into three component pieces:

**Root** = "Eb"

**Quality** = "maj7/"

**Bass** = "Bb"

The root and bass will be transposed while the quality is left alone. Let's say the desire is to transpose upwards by a Major Second. After transposition, all three pieces can be recombined to form:

**<p style="text-align: center;">[Fmaj7/C]</p>**

As of now, if the chords are in bold, this quality is lost when writing to the new document. The next goal is to maintain boldness in the target documents.

## Getting Started

### Dependencies

* Requires python-docx and lxml. Both can be installed with:
```bash
pip install python-docx
```
* All other libraries are included in default Python installations
* All libraries are cross platform and should run on Windows, MacOS, and Linux systems

### Installing

* Repo located at: https://github.com/Cbakum/transpose_chord_sheet
* Install with:
```bash
git clone git@github.com:Cbakum/transpose_chord_sheet.git
```
#### Optional Setup (to set default directory for chord sheets):
* Open src/user_select.py source code
* Go to **open_file_dialog()**
* Uncomment line defining **initialdir** and define the target directory

### Executing program

* Main is contained within tranpose.py:

```
python transpose.py
```


* GUI window appears for file selection. Select target .docx file
* GUI window appears to select transposition. There are two options to choose from here:
    * **Option one:** Pick an interval and a direction. *Ex: a minor 2nd up or a perfect 5th down*
    * **Option two:** Define the original key and the target key. *Ex: transpose from C to D*
* Optional command line arguments:
    * **arg1**: filename of source document to skip first window of GUI
    * **arg2**: number of semitones (upwards) to tranpose to skip second window of GUI
```
python tranpose.py file_to_tranpose.docx 2
```

## Author

[Cbakum](https://github.com/Cbakum/)

# transpose_chord_sheet

Parses .docx files for chord symbols within brackets **[CHORD]**, transposes them to other keys, and writes new .docx with updated chords

## Description

Wrote this program to make transposing chord sheets easier and faster for ukulele club. This works with .docx files (can come from Word documents or Google Docs). Preserves the original document and creates a copy with the new chord symbols. The main requirement for this program is that all chord symbols must be contained within square brackets:

**<p style="text-align: center;">[CHORD]</p>**

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

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Author

[Cbakum](https://github.com/Cbakum/)

 ImagePDF
 Stitch Images to PDF Files!
 Public Release 1.0
 Build Date: 7 October 2020

 Thanks for downloading ImagePDF!

 TL;DR: ImagePDF is a program to stitch together images into one big PDF file.

 ###################
 #   How to Use:   #
 ###################

 At launch, there will be two boxes: One for the source folder, and One
 for the destination folder. Users may either enter their location manually
 or use the '...' button to select a folder through Windows Explorer. (Feature
 not tested on MacOS or Linux). If the user enters a file location ending in
 .PDF, ImagePDF will save the output file there. Otherwise, the file will be
 saved as 'output.pdf' in the destination folder.

 Under the 'Included File Formats' box, users can select which file types
 they would like to include in their final PDF. All files with selected types
 in the source directory will be added to the output PDF.

 The 'Source Image Sort Method' box consists of all the ways the selected
 images can be ordered in the final pdf:
       [Alphanumeric]: This option will sort selected images alphabetically by
                      file name (ABC.....789)
       [Date Created]: This option will sort selected images by the date they
                      were created
       [Date Modified]: This option will sort selected images by the date they
                      were last modified
       [File Size]: This option will sort selected images by their file size.

Clicking 'Begin' will begin sorting and stitching the images.

###################
# Convert to .exe #
###################

**NOTE** This Release Only Consists of the Python file. If you wish to
convert to .exe, you can use pyInstaller!

To convert, navigate to the save location and run the following command:

                pyinstaller --onefile -w ImagePDF.py

Please note this may cause issues with antivirus software, particularly
Windows Defender.


 ########################
 #   Specs for Nerds:   #
 ########################

 Written in Python 3.7.7
 GUI Handled by Tkinter
 PDF Merging Handled by fPDF

 (C) 2020 Robert Sammataro
 robertsammataro@gmail.com

# Automatic-Website-Categorizers

These programs are designed to categorize specified websites.

To use the Titles Searcher Program, you will need to download everything that is described here: http://www.makeuseof.com/tag/read-write-google-sheets-python/. The following Google Doc is referenced by the Titles Searcher Program:
Titles Google Doc: https://docs.google.com/spreadsheets/d/1gzB1_DsoUCSuR2cwySwzvTIeU4TrlyMKna5KuNXtOuI/edit?usp=sharing

To use the Description Searcher Program, first create a textfile called websites.txt with all of the websites that you want to search for. Then run the file descr3.py on that. You will need to convert the Unicode ine results into Ascii. Once you do this plug the results into a GoogleDoc so that you can use the function 'GoogleTranslate' to translate any website descriptions that are not in English. Once this is done, plug these results into a text file called translated.txt and run the program descriptions4_mod.py. Throughout the course of using these programs, you should check to make sure that all of the results match with the relevant websites. Occasionally, website descriptions can have characters that cause GoogleDocs to put parts of the same description in separate rows, resulting in the need to fix the allignment of the results manually.

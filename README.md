# Automatic-Website-Categorizers

These programs are designed to categorize specified websites.

To use the Titles Searcher Program, download the program here: https://github.com/NikolaiT/GoogleScraper and then open a command prompt and enter the following:  GoogleScraper -m http -s "bing" --keyword-file keywords10.txt >output.txt. Then run extract3.py on that output.txt file. (Change pin1 in extract3.py to reference the output file that you created.)


To use the Description Searcher Program, first create a textfile called websites.txt with all of the websites that you want to search for. Then run the file descr3.py on that. You will need to convert the Unicode in the results into Ascii. Once you do this plug the results into a GoogleDoc so that you can use the function 'GoogleTranslate' to translate any website descriptions that are not in English. Once this is done, plug these results into a text file called translated.txt and run the program descriptions4_mod.py. Throughout the course of using these programs, you should check to make sure that all of the results match with the relevant websites. Occasionally, website descriptions can have characters that cause GoogleDocs to put parts of the same description in separate rows, resulting in the need to fix the allignment of the results manually.

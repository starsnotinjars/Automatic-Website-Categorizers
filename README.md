# Automatic-Website-Categorizers

These programs are designed to categorize specified websites.

# Title Searcher
Download  [GoogleScraper](https://github.com/NikolaiT/GoogleScraper):

    pip3 install GoogleScraper

Open a command prompt and enter the following:

    GoogleScraper -m http -s "bing" --keyword-file keyword10.txt > output.txt
    
Run extract3.py on that output.txt file:

    python3 extract3.py 
 (Change pin1 in extract3.py to reference the output file that you created.)

# Description Searcher
Download the prerequisites:

    pip2 install BeautifulSoup4
    pip2 install request
    
Create a textfile called websites.txt with all of the websites that you want to search for. Then run the file descr3.py on that:

    python2.7 descr3.py

You will need to convert the Unicode in the results into ASCII. 

Once you do this plug the results into a GoogleDoc so that you can use the function 'GoogleTranslate' to translate any website descriptions that are not in English. 

Once this is done, plug these results into a text file called translated.txt and run the program descriptions4_mod.py.

Throughout the course of using these programs, you should check to make sure that all of the results match with the relevant websites. Occasionally, website descriptions can have characters that cause GoogleDocs to put parts of the same description in separate rows, resulting in the need to fix the allignment of the results manually.

# Aggregator Identifier

Create a textfile called websites.txt with all of the websites that you want to search. Then run the file aggregators.py on that. You will need to install BeautifulSoup and GoogleScraper as described above for the Title Searcher program and Description Searcher Program. This program will output two lists, one list will be the list of sites that were identified to be aggregators and the other list will be the list of sites that were not identified to be aggregators.

# Twitter Handle/Facebook Page Extractor
Create a textfile called websites.txt with all of the websites that you want to search. Then run the file twitterandfacebook.py on that. This program wilAl output the twitter handles and facebook pages that were found for the websites that were searched. At this point, some minor editing of the output is required.

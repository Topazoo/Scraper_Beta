This scrapes jobs from CalJobs

The Scraper:

    Connects to CalJobs using the Mechanize library. Can be set to record up to 500 jobs in increments of
    10, 25, 50, 100, 500. Can be set to collect from any number of keywords.

    Sometimes the Scraper will timeout, an exception will catch this, and data collected will be saved.
    After the data is saved it is written to a JSON file and stored locally. The end goal is to store it
    online.

The Requirements:
    Stored in requirements.txt.
    CORE:
        BeautifulSoup - Parses HTML and can be used to quickly grab data.
        mechanize - Allows connection to websites.

To Use:
    Can be run with "python scraper.py" in the terminal. Will run and deposit a local JSON file. To render
    in Django, call render with the dict as a parameter and loop through it's VALUES (dict.values) in a 
    template tag.

    Example_views.py gives an example of the dict as a parameter
    
    Read_JSON_test.py will read the JSON file if it is formatted correctly.
    

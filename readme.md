# Hello Comics
## Application usage:
run 'HelloComicApp.py' under 'Driver' folder

## Application Structure
### Data Ingestion
#### website API
* get latest comics number:
    - http://xkcd.com/info.0.json
    - get last "num": 1918
* data scraping of all comics:
    - num: from 1 to last num
    - construct url: https://xkcd.com/{{num}}/info.0.json
    - get "alt": for example: "\"...just got back and didn't see your message until just now. Sorry! -- TIME THIS MESSAGE SAT HALF-FINISHED IN DRAFTS FOLDER: 3 days, 2 hours, 45 minutes.\""

### Functions
#### Word count
display 5 most commonly used words in screen
* input: "alt" text
* function:
    - word split
    - word filtering
        + remove pronouns
        + remove conjunctions
    - word count
* output:
    - word-frequency dictionary
    - alt-comic mapping
    - comic-alt mapping dictionay

#### keyword search and display result
* input: keyword
* output:
    - a list of comics that contains the keyword
    - 5 commonly used words in these comics
        + may using word count

#### Notes
* words restriction:
    - no pronouns
    - no conjunctions
    - consturct lexicons to filter out above words
* no database settings
    - using internal data structure
        + dictionary (python)
        + Linked List with HashMap (Java)


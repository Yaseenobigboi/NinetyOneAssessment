# Top Scorers

Solution for the Ninety One graduate assessment.

## What it does

Reads a CSV file of names and test scores, finds the highest score, and prints all people who achieved that score in alphabetical order.

## How to run

```
cd console
python main.py TestData.csv
```

## Project structure

```
console/
    main.py         entry point, reads the CSV file and prints results
    csv_parser.py   parses the CSV text manually without any libraries
    scorer.py       finds the top score and returns the top scorers
    database.py     saves the scores to a local SQLite database

api/
    app.py          REST API with three endpoints
    database.py     reads and writes to the same database
```

More documentation will be added on completion.


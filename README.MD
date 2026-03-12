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

## How to run the API

```
cd api
python app.py
```

The API runs on http://127.0.0.1:5000

Endpoints:

    POST   /scores                             save a new score
    GET    /scores/<first_name>/<second_name>  get one person's score
    GET    /scores/top                         get the top scorer(s)

Examples:

Get top scorers (open in browser):

    http://127.0.0.1:5000/scores/top

Get one person's score (open in browser):

    http://127.0.0.1:5000/scores/Sipho/Lolo

Post a new score (run in terminal):

    curl -X POST http://127.0.0.1:5000/scores -H "Content-Type: application/json" -d "{\"first_name\":\"Jane\",\"second_name\":\"Doe\",\"score\":90}"

## Security

I would secure the endpoints using JWT tokens. The client logs in to receive a token, then includes it in the Authorization header on each request. This is just from what i know off the top of my head, i will have to research further.

# Design choices

- SQLite was chosen as it requires no setup and is sufficient for local development.
- CSV parsing is done manually without any standard library, as required.
- The console app and the API share the same database file.
- I do not have much knowledge in cloud hosting but am willing to learn and research further



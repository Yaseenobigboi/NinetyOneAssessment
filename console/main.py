import sys
from csv_parser import parse_csv
from scorer import get_top_scorers
from database import save_rows


# Read the CSV file and return the raw text.
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


# Print the top scorers to STDOUT.
def print_results(winners, top_score):
    for person in winners:
        print(f"{person['First Name']} {person['Second Name']}")
    print(f"Score: {top_score}")


file_path = sys.argv[1]
raw_text = read_file(file_path)
rows = parse_csv(raw_text)
save_rows(rows)
winners, top_score = get_top_scorers(rows)
print_results(winners, top_score)



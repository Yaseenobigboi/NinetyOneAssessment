# Find the highest score from a list of rows.
def get_top_score(rows):
    top = 0
    for row in rows:
        score = int(row["Score"])
        if score > top:
            top = score
    return top


# Return all rows that have the top score, sorted alphabetically by full name.
def get_top_scorers(rows):
    top_score = get_top_score(rows)
    winners = []
    for row in rows:
        if int(row["Score"]) == top_score:
            winners.append(row)
    winners.sort(key=lambda r: (r["First Name"], r["Second Name"]))
    return winners, top_score

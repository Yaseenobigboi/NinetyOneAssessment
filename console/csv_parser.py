# Parse a CSV string into a list of dicts keyed by the header row.
def parse_csv(raw_text):    
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]

    rows = []
    for line in lines[1:]:
        fields = [f.strip() for f in line.split(",")]
        
        if len(fields) == len(headers):
            rows.append(dict(zip(headers, fields)))

    return rows

from flask import Flask, request, jsonify
import database

app = Flask(__name__)


# Save a new score.
@app.route("/scores", methods=["POST"])
def post_score():
    body = request.get_json()
    database.add_score(body["first_name"], body["second_name"], body["score"])
    return jsonify(message="Score saved"), 200


# Get the score for one person.
@app.route("/scores/<first_name>/<second_name>", methods=["GET"])
def get_score(first_name, second_name):
    row = database.get_score(first_name, second_name)
    if row is None:
        return jsonify(error="Person not found"), 404
    return jsonify(first_name=row["first_name"], second_name=row["second_name"], score=row["score"])


# Get all top scorers.
@app.route("/scores/top", methods=["GET"])
def get_top():
    rows, top = database.get_top_scorers()
    results = [{"first_name": r["first_name"], "second_name": r["second_name"], "score": r["score"]} for r in rows]
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)


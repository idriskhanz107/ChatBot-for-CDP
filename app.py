from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load pre-scraped links
with open("segment_links.json", "r") as f:
    segment_links = json.load(f)

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question", "").lower()
    
    # Simple matching logic for demo
    if "source" in question and "segment" in question:
        return jsonify({"answer": "To set up a new source in Segment, visit this link: https://segment.com/docs/connections/sources/"})
    return jsonify({"answer": "Sorry, I couldn't find an answer for that."})

if __name__ == "__main__":
    app.run(debug=True)
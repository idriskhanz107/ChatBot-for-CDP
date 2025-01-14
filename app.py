from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load mParticle and Lytics links
with open("mparticle_links.json", "r") as f:
    mparticle_links = json.load(f)

with open("lytics_links.json", "r") as f:
    lytics_links = json.load(f)

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question", "").lower()

    # Example: Match keywords to provide answers
    if "mparticle" in question:
        for link in mparticle_links:
            if "source" in question and "set up" in question:
                return jsonify({
                    "answer": f"To set up a source in mParticle, visit this link: {link['url']}"
                })
    
    if "lytics" in question:
        for link in lytics_links:
            if "audience segment" in question:
                return jsonify({
                    "answer": f"To build an audience segment in Lytics, visit this link: {link['url']}"
                })

    return jsonify({"answer": "Sorry, I couldn't find an answer for that."})

if __name__ == "__main__":
    app.run(debug=True)

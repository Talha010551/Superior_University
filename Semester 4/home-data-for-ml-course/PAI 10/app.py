from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rule-based responses
library_data = {
    "opening hours": "The library is open Monday to Friday 9 AM - 6 PM, Saturday 10 AM - 4 PM.",
    "due date": "Books are due 14 days after borrowing. Late returns incur a small fine.",
    "find book": "Please provide the title or author of the book you are looking for.",
    "python programming": "Yes! 'Python Programming for Beginners' is available on Shelf 3, Aisle 5.",
    "harry potter": "Yes! 'Harry Potter and the Sorcerer's Stone' is available on Shelf 7, Aisle 2."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        # Ensure request is parsed as JSON
        data = request.get_json(force=True)
        if not data or "message" not in data:
            return jsonify({"answer": "No message received"}), 400

        user_input = data["message"].lower()
        response = "Sorry, I don't have information on that. Try asking about books or library hours."

        for key in library_data:
            if key in user_input:
                response = library_data[key]
                break

        return jsonify({"answer": response})

    except Exception as e:
        print("Error:", e)
        return jsonify({"answer": "Something went wrong. Try again."})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, send_file
from io import BytesIO
from fpdf import FPDF
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='.')

# Load OpenRouter API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")  # Make sure index.html exists

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("childName", "Friend")
    animal = data.get("favoriteAnimal", "puppy")
    color = data.get("favoriteColor", "blue")
    theme = data.get("storyTheme", "Bedtime")
    extras = data.get("extraDetails", "")

    prompt = (
        f"Write a magical {theme.lower()} story for a child named {name} who loves {animal}s and the color {color}. "
        f"Make it imaginative, kind, and child-friendly. "
    )
    if extras:
        prompt += f"Include these details: {extras}"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-3.5-turbo",  # You can also try "mistralai/mixtral-8x7b"
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to generate story"}), 500

    result = response.json()
    story = result["choices"][0]["message"]["content"]
    return jsonify({"story": story.strip()})

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    data = request.get_json()
    story_text = data.get("story", "")
    name = data.get("childName", "Your_Story")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, story_text)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{name}_storybook.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway uses this env variable
    app.run(host="0.0.0.0", port=port)











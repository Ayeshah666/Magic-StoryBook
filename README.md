**🌟 Magic Storybook Creator**
A personalized AI-powered storybook web app built with Flask and OpenAI. Kids can enter their name, favorite animal, color, and theme — and receive a unique, magical story generated just for them! 💜📖

✨ Features
🎨 violet-themed UI

🐾 Personalized story generation

💾 Download as PDF (optional)

☁️ Hosted on Railway

🚀 Live Demo
👉 Click here to try it out "https://web-production-490ee.up.railway.app/"

🧠 Powered By
Flask (Backend)

Jinja2 (Templating)

HTML/CSS (Frontend)

OpenAI API via OpenRouter.ai

Deployed using Railway

🛠 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Ayeshah666/Magic-StoryBook.git
cd Magic-Storybook
2. Create and activate virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # on Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set your API key
You can set it via environment variable:

bash
Copy
Edit
export OPENROUTER_API_KEY=your_key_here
Or hard-code it in app.py (not recommended for production).

5. Run locally
bash
Copy
Edit
python app.py
Go to http://127.0.0.1:5000 in your browser.

🐳 Docker Support
Build and run the container:

bash
Copy
Edit
docker build -t magic-storybook .
docker run -p 8080:8080 magic-storybook
📁 Folder Structure
bash
Copy
Edit
/app.py
/index.html      ← Main template in root
/requirements.txt
/Dockerfile
🧚‍♀️ Future Ideas
Voice narration
Save story history


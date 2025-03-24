Flask-Docker API 🚀
A simple REST API built with Flask and Docker that serves random quotes.


🔧 Features
✅ Returns a random quote from a JSON file
✅ Adds new quotes via a POST request
✅ Fully containerized with Docker

📂 Project Structure
bash
Kopieren
Bearbeiten
flask-docker-api/
│── app.py               # Main Flask API
│── requirements.txt     # Python dependencies
│── Dockerfile           # Docker setup
│── docker-compose.yml   # Docker Compose setup (optional)
│── quotes.json     # JSON file with quotes
│── .gitignore           # Ignore unnecessary files
└── README.md            # Project documentation
🚀 Setup & Installation
1️⃣ Install dependencies
bash
Kopieren
Bearbeiten
pip install -r requirements.txt
2️⃣ Run Flask API locally
bash
Kopieren
Bearbeiten
python app.py
Now open http://127.0.0.1:5000/quote in your browser.

🐳 Run with Docker
1️⃣ Build the Docker image
bash
Kopieren
Bearbeiten
docker build -t flask-docker-api .
2️⃣ Run the Docker container
bash
Kopieren
Bearbeiten
docker run -p 5000:5000 flask-docker-api
Now open http://localhost:5000/quote in your browser.

📡 API Endpoints
Method	Endpoint	Description
GET	/quote	Returns a random quote
GET	/quotes	Returns all quotes
POST	/add_quote	Adds a new quote (JSON format: {"quote": "Your quote here"})
🌍 Deployment (Optional)
You can deploy this project to:
🔹 Render: https://render.com/
🔹 Railway: https://railway.app/

👨‍💻 Author
📌 Osman Sahin
🔗 GitHub: github.com/Sabi1337

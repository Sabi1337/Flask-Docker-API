```markdown
# Flask-Docker API 🐳🚀

A containerized REST API built with Flask & Docker that serves random quotes.

## 📌 Features
- ✅ REST API with Flask (GET & POST)
- ✅ Docker container for easy deployment
- ✅ Stores quotes in `quotes.json`
- ✅ Docker Compose for simple startup

## 🚀 Setup & Installation

### 1️⃣ Install Dependencies
If you don’t want to use Docker, install Flask locally:

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Flask API (without Docker)

```bash
python app.py
```

➡ Open: [http://127.0.0.1:5000/quote](http://127.0.0.1:5000/quote)

### 🐳 Using Docker (Recommended)

#### 1️⃣ Build the Docker Image

```bash
docker build -t flask-docker-api .
```

#### 2️⃣ Run the Container

```bash
docker run -p 5000:5000 flask-docker-api
```

➡ Open: [http://localhost:5000/quote](http://localhost:5000/quote)

### 🐙 Using Docker Compose (Simplified Startup)

If you're using Docker Compose:

```bash
docker-compose up --build
```

➡ Stop the container: `CTRL+C` or `docker-compose down`

## 📡 API Endpoints

| Method | Endpoint        | Description                                       |
|--------|-----------------|---------------------------------------------------|
| GET    | /quote          | Returns a random quote                           |
| GET    | /quotes         | Returns all stored quotes                        |
| POST   | /add_quote      | Adds a new quote (JSON: `{"quote": "Your quote here"}`) |

## 📡 Deployment (Optional)
To host this API online, you can:
1️⃣ Deploy on Render or Railway  
2️⃣ Use GitHub Actions to automate Docker builds

## 👨‍💻 Author
📌 Osman Sahin  
🔗 GitHub: [github.com/Sabi1337](https://github.com/Sabi1337)

## 🚀 Next Steps:
- 📌 Add this `README.md` to your repo
- 📌 Improve your Dockerfile with Multi-Stage Builds or CI/CD (optional)

✅ Now your GitHub repository looks professional! 🎉  
➡ Need any more optimizations? 😊🚀
```

Now the directory structure is displayed correctly in a code block. You can copy and paste this into your `README.md`. Let me know if there's anything else!

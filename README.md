# flask-react-app

## 📝 Project Overview

A CRUD web application built with Python (Flask) and JavaScript (React). I am following the [Python + JavaScript - Full Stack App Tutorial](https://www.youtube.com/watch?v=PppslXOR7TA) by [Tech with Tim](https://www.youtube.com/@TechWithTim).

## ▶️ Usage

To run the application, you can either clone this GitHub repository or use the provided docker compose file.

### Cloning the GitHub Repository

```bash
git clone https://github.com/sal-siddiqui/flask-react-app

cd flask-react-app

cd backend
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python main.py

cd ../frontend
npm install
npm run dev
```
### Running Docker Compose
```bash
git clone https://github.com/sal-siddiqui/flask-react-app
docker compose build
```

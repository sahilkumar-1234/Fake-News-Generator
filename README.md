# Fake-News-Generator
These is a Simple Funny Fake News Generator....
# 😂 Fake News Generator

A **funny fake news headline generator** built with Python, Flask, and HTML/JavaScript. It creates hilarious, meme-like fake news headlines for entertainment purposes.

---

## 📂 Project Structure
Fake_Headline_Generator/
├── app.py
├── templates/
│ └── index.html
└── README.md


---

## ⚙️ Features

- Generates endless funny and absurd fake news headlines.
- Interactive HTML page with a button to generate new headlines.
- Loading animation while fetching news.
- Share generated news on Twitter (Facebook sharing placeholder included).
- Parody content for entertainment only.

---

## 🛠️ Technologies Used

- **Python 3** – Backend logic and news generation
- **Flask** – Web server and API endpoint
- **HTML/CSS/JavaScript** – Frontend display and interactivity
- **Font Awesome** – Icons for UI elements

---

## 💻 How It Works

1. Flask backend defines lists of **subjects**, **verbs**, **objects**, and **extra details**.
2. Clicking the "Generate News" button triggers a JavaScript function.
3. The JS function calls the Flask API endpoint `/getnews` and fetches a random headline in JSON format.
4. The headline is displayed dynamically on the webpage without reloading.
5. Users can share the generated news on Twitter.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>

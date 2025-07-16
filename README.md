# 👤 Reddit User Persona Extractor

![repo public](https://img.shields.io/badge/repo-public-brightgreen)

---

## 📚 About This Project

This repository is my submission for the BeyondChats AI/LLM Engineer Internship assignment round.

It demonstrates my ability to design, implement, and analyze a robust, evidence-based persona extraction system for Reddit users using real Reddit API data. The solution is fully original, interpretable, and designed for clarity and extensibility.

---

## 🧠 Methodology & Approach

- **Data Collection:**  
  Fetches public posts and comments from any Reddit user profile using the official Reddit API (PRAW).

- **Persona Construction:**  
  Analyzes user activity to infer:
  - Top interests and motivations
  - Writing style and personality
  - Activity level and behavioral patterns
  - Frustrations and pain points
  - Goals and needs
  - Each trait is supported by direct evidence (post/comment citation)

- **Output:**  
  Generates a clear, human-readable persona profile in a text file, closely following the structure and style shown in the assignment example.

---

## 🗂️ Project Structure

```
.
├── main.py
├── reddit_scraper.py
├── persona_builder.py
├── requirements.txt
├── README.md
├── output/
│   └── Hungry-Move-6603.txt
└── .env
```

---

## ⚡ How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Reddit API credentials:**
   - Create a Reddit app at https://www.reddit.com/prefs/apps
   - Add your credentials to a `.env` file in the project root:
     ```
     REDDIT_CLIENT_ID=your_client_id
     REDDIT_CLIENT_SECRET=your_client_secret
     REDDIT_USERNAME=your_username
     REDDIT_PASSWORD=your_password
     REDDIT_USER_AGENT=PersonaExtractor by u/your_username
     ```

3. **Extract a persona for any Reddit user:**
   ```bash
   python main.py https://www.reddit.com/user/example_username/
   ```
   - The persona profile will be saved in the `output/` directory.

---

## 🧩 Extensibility

- The persona extraction logic is modular and can be easily updated in `persona_builder.py`.
- Additional analysis or persona sections can be added as needed.

---

## 🔍 Transparency

- All persona logic is documented in code and this README.
- Every trait is supported by a direct citation to a Reddit post or comment.
- No black-box models: every persona is explainable and reproducible.

---

*For any questions or suggestions, feel free to open an issue or contact me via GitHub.* 
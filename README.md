# University Dashboard - Py/Shiny

An interactive Shiny for Python application to explore and summarize student data.

---

##  Live Demo

* **Hosted**: To be published via Appsilon RSConnect or similar.
* **Local**: See instructions below to run on your machine.

---

##  Quick Start (Local)

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/University-Dashboard.git
   cd University-Dashboard
   ```

2. **Create & activate a Python virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\\Scripts\\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key**

   * **OpenAI**:

     ```bash
     export OPENAI_API_KEY="sk-..."
     ```
   * **Hugging Face** (optional alternative):

     ```bash
     export HF_TOKEN="hf_..."
     ```

5. **Run the app**

   ```bash
   shiny run --host 0.0.0.0 --port 8000 app.py
   ```

6. **Open** `http://localhost:8000` in your browser.

---

##  Key Features

* **Dynamic Sidebar Filters**: Entry semester, level, class year, sport, major, second degree, GPA range, and advisor.
* **Summary Cards**: Total students, average GPA, and AI-generated student synopsis.
* **Student Table**: Expandable table showing filtered students (ID, name, major, GPA).
* **Search & Detail Panel**: Text input for PACIFIC\_ID lookup and detailed student profile display.
* **Interactive Charts**: GPA distribution histogram and horizontal bar chart for class counts.
* **Theming**: Light/dark mode toggle via CSS injection.

---

##  Project Structure

```
├── app.py             # Main Shiny for Python application
├── helpers.py         # Data loaders and summarize_student() helper
├── fake_data.py.py    # Python code for fake data
├── requirements.txt   # Python dependencies
├── students.csv       # Sample/anonymized student dataset
├── README.md          # This documentation
```

---

##  Deployment Options

1. **ngrok** (instant tunnels):

   ```bash
   ngrok http 8000
   ```
2. **Heroku / Render / Railway** — free tiers, add a `Procfile`:

   ```Procfile
   web: gunicorn app:app
   ```
3. **Appsilon RSConnect** — enterprise-grade Shiny hosting.

---

##  Known Challenges

* **API Quotas**: OpenAI usage incurs token costs; consider caching or switching to a local HF model.
* **Performance**: Large datasets may need pagination or server-side filtering.
* **Shiny for Python**: Components and layouts continue evolving; some patterns may change in future releases.

---

##  References

* Shiny for Python Docs: [https://shiny.posit.co/py/docs/](https://shiny.posit.co/py/docs/)

---

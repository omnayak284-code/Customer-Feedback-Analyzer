# Customer Feedback Analyzer 💬⚡

An intelligent, lightweight CLI application powered by Google's Gemini 2.5 Flash model that transforms unstructured customer reviews, support queries, and bug reports into structured, actionable JSON insights.

---

## Preview

---

## Features

* **Sentiment Analysis:** Classifies feedback into `Positive`, `Negative`, `Neutral`, or `Mixed`.
* **Urgency Scoring:** Tags items as `Low`, `Medium`, or `High` for immediate prioritization.
* **Topic Classification:** Automatically extracts categories (`Billing`, `Bug`, `UX`, `Feature Request`, `Customer Support`, `Other`).
* **Strict JSON Output:** Native structured output format ready for downstream data pipelines and database insertion.
* **Defensive Error Handling:** Validates inputs locally before contacting the API and safely manages network or quota errors.

---

## Tech Stack

* **Language:** Python 3.10+
* **LLM:** Google Gemini 2.5 Flash
* **SDK:** `google-genai`
* **Configuration:** `python-dotenv`

---

## Getting Started

### Prerequisites

* Python 3.10 or higher
* A Gemini API key from [Google AI Studio](https://aistudio.google.com/?utm_source=gemini)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/customer-feedback-analyzer.git
cd customer-feedback-analyzer

```


2. **Create and activate a virtual environment:**
* **Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```


* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Install dependencies:**
```bash
pip install google-genai python-dotenv

```


4. **Set up your API Key:**
* Create a `.env` file in the root directory:
```bash
cp .env.example .env

```


* Add your Gemini API key to `.env`:
```env
GEMINI_API_KEY="your_actual_api_key_here"

```





---

## Usage

Run the CLI script:

```bash
python app.py

```

Enter any review or feedback string when prompted. Type `exit` or `quit` to end the session.

### Example

```text
Enter Feedback >> The app crashed right after I paid, and my account shows I was charged twice!

-------------------- ANALYSIS RESULT --------------------
{
  "sentiment": "Negative",
  "urgency": "High",
  "primary_topic": "Billing",
  "summary": "User experienced a crash during checkout and was charged twice without confirmation.",
  "recommended_action": "Verify duplicate transaction and initiate immediate refund."
}

```

---

## Project Structure

```text
customer-feedback-analyzer/
│
├── app.py              # Core CLI application & Gemini API integration
├── .env.example        # Environment variable template
├── .gitignore          # Ignores .env, venv/, and build caches
├── screenshot.png      # Demo image for documentation
└── README.md           # Project documentation

```

---

## Roadmap

* [ ] Add batch analysis for `.csv` and `.xlsx` files
* [ ] Build an interactive web UI using Streamlit
* [ ] Integrate automatic ticketing via Jira / Slack webhooks

---

## License

Distributed under the [MIT License](https://www.google.com/search?q=LICENSE&utm_source=gemini).

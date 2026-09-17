import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
# 1. Load API Key securely from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
def initialize_client() -> genai.Client:
    """Initializes the Gemini client after validating the API key."""
    if not API_KEY or API_KEY == "AIzaSyYourActualApiKeyHere":
        raise ValueError(
            "Missing or invalid API key. Please add your real GEMINI_API_KEY inside the .env file."
        )
    return genai.Client(api_key=API_KEY)
def analyze_feedback(feedback_text: str) -> dict:
    """Sends user feedback to the LLM and returns structured JSON analysis."""
    clean_input = feedback_text.strip()
    if not clean_input:
        return {"error": "Feedback text cannot be empty."}
    prompt = f"""
You are an expert customer feedback intelligence system.
Analyze the customer feedback text below and output a valid JSON object ONLY.
Feedback:
"{clean_input}"
Strict JSON format to follow:
{{
  "sentiment": "Positive" | "Negative" | "Neutral" | "Mixed",
  "urgency": "Low" | "Medium" | "High",
  "primary_topic": "Billing" | "Bug" | "Feature Request" | "UX" | "Customer Support" | "Other",
  "summary": "1-sentence concise takeaway",
  "recommended_action": "1 concrete operational next step for the product/support team"
}}
"""
    try:
        client = initialize_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.2
            }
        )
        return json.loads(response.text)
    except ValueError as val_err:
        return {"error": str(val_err)}
    except APIError as api_err:
        return {"error": f"Gemini API Error: {str(api_err)}"}
    except json.JSONDecodeError:
        return {"error": "The model response could not be parsed as valid JSON."}
    except Exception as exc:
        return {"error": f"Unexpected error occurred: {str(exc)}"}
def main():
    print("=" * 55)
    print("      CUSTOMER FEEDBACK ANALYZER (CLI)")
    print("=" * 55)
    print("Instructions:")
    print(" - Paste any customer feedback/review and hit Enter.")
    print(" - Type 'exit' or 'quit' to terminate the app.\n")
    while True:
        try:
            user_text = input("Enter Feedback >> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting application. Goodbye!")
            break
        if user_text.lower() in {"exit", "quit"}:
            print("Exiting application. Goodbye!")
            break
        if not user_text:
            print("[!] Please provide non-empty feedback.\n")
            continue
        print("\nProcessing feedback with Gemini LLM...")
        result = analyze_feedback(user_text)
        print("\n" + "-" * 20 + " ANALYSIS RESULT " + "-" * 20)
        print(json.dumps(result, indent=2))
        print("-" * 57 + "\n")
if __name__ == "__main__":
    main()

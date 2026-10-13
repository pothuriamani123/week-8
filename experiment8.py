
!pip -q install langchain-google-genai

import os
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Google API key
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

# Unstructured prompt
prompt1 = """
Describe Python, Java, and C++ in a short paragraph.
"""

# Structured prompt
prompt2 = """
Create a Markdown table about Python, Java, and C++.
Use exactly these columns:
Language, Typing (static/dynamic), Primary Use Case,
Difficulty (Beginner/Intermediate/Advanced).

Include all three languages and no JSON.
"""

# Generate responses using the same model and settings
response1 = llm.invoke(prompt1).content
response2 = llm.invoke(prompt2).content

# Print outputs
print("=== UNSTRUCTURED ===")
print(response1)

print("\n=== STRUCTURED (Markdown Table) ===")
print(response2)

# Comparison
print("\n=== ANALYSIS ===")
print("Unstructured output: Information is presented in paragraph form.")
print("Structured output: Information is organized into rows and columns.")
print("Structured output makes comparison easier, faster, and clearer.")

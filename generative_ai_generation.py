"""Generative-AI synthetic data example (prompt/template only).

This file does not call an external LLM. It shows the prompt contract that could
be sent to an LLM, and then demonstrates the validation step that should still
happen after an LLM returns JSON.
"""
import json

PROMPT = """
Generate one synthetic user profile as JSON with exactly these fields:
Age, Country, State_Province, Has_Purchased_Alcohol.
Rules:
1. Age is 18-75.
2. Country is USA or Canada.
3. USA requires a valid US state abbreviation.
4. Canada requires a valid Canadian province/territory abbreviation.
5. If Age < 21 and Country is USA, Has_Purchased_Alcohol must be No.
Return JSON only.
""".strip()

print("Prompt that could be sent to a generative AI model:\n")
print(PROMPT)

# Example of an LLM-style response. In a real workshop, replace this with the
# response returned by your chosen provider and parse it with json.loads().
example_response = '{"Age": 29, "Country": "Canada", "State_Province": "ON", "Has_Purchased_Alcohol": "Yes"}'
profile = json.loads(example_response)

print("\nExample model response:")
print(json.dumps(profile, indent=2))
print("\nImportant: generative AI should create candidates; deterministic validation\nshould enforce hard business constraints before the record is accepted.")

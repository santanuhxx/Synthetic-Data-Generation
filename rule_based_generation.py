"""Generate synthetic user profiles using explicit business rules."""
from pathlib import Path
import random
import pandas as pd

SEED = 42
N = 100
random.seed(SEED)

US_STATES = ["AL","AK","AZ","AR","CA","CO","CT","FL","GA","IL","MA","MD","MI","MN","MO","NC","NJ","NY","OH","OR","PA","TX","VA","WA"]
CANADA_PROVINCES = ["AB","BC","MB","NB","NL","NS","NT","NU","ON","PE","QC","SK","YT"]

records = []
for _ in range(N):
    age = random.randint(18, 75)
    country = random.choice(["USA", "Canada"])

    if country == "USA":
        state_province = random.choice(US_STATES)
    else:
        state_province = random.choice(CANADA_PROVINCES)

    # Rule 5: under-21 users in the USA cannot have purchased alcohol.
    if age < 21 and country == "USA":
        has_purchased_alcohol = "No"
    else:
        has_purchased_alcohol = random.choice(["Yes", "No"])

    records.append({
        "Age": age,
        "Country": country,
        "State_Province": state_province,
        "Has_Purchased_Alcohol": has_purchased_alcohol,
    })

df = pd.DataFrame(records)
out = Path(__file__).resolve().parent / "rule_based_profiles.csv"
df.to_csv(out, index=False)
print(f"Generated {len(df)} valid profiles: {out}")
print(df.head(10).to_string(index=False))

# Demonstrate validation on deliberately invalid examples.
def validate(record):
    errors = []
    if not 18 <= record["Age"] <= 75:
        errors.append("Rule 1: Age must be between 18 and 75")
    if record["Country"] not in {"USA", "Canada"}:
        errors.append("Rule 2: Country must be USA or Canada")
    if record["Country"] == "USA" and record["State_Province"] not in US_STATES:
        errors.append("Rule 3: invalid US state abbreviation")
    if record["Country"] == "Canada" and record["State_Province"] not in CANADA_PROVINCES:
        errors.append("Rule 4: invalid Canadian province/territory abbreviation")
    if record["Age"] < 21 and record["Country"] == "USA" and record["Has_Purchased_Alcohol"] != "No":
        errors.append("Rule 5: under-21 USA profile must have Has_Purchased_Alcohol = No")
    return errors

examples = [
    {"Age": 19, "Country": "USA", "State_Province": "CA", "Has_Purchased_Alcohol": "Yes"},
    {"Age": 40, "Country": "USA", "State_Province": "XX", "Has_Purchased_Alcohol": "No"},
    {"Age": 31, "Country": "Canada", "State_Province": "ON", "Has_Purchased_Alcohol": "Yes"},
]
print("\nValidation examples:")
for ex in examples:
    errors = validate(ex)
    print(ex)
    print("  VALID" if not errors else "  INVALID -> " + "; ".join(errors))

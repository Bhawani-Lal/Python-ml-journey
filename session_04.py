# ============================================
# SESSION 04 - Tuples, Sets & String Methods
# ============================================

# --- Concept 1: Tuples ---
skills_list = ["Python", "Java", "SQL"]
skills_list[0] = "React"
print(skills_list)

skills_tuple = ("Python", "Java", "SQL")
print(skills_tuple)
print(skills_tuple[0])
print(len(skills_tuple))

# --- Concept 2: Sets ---
skills = {"Python", "Java", "SQL", "Python", "Java"}
print(skills)

skills.add("Docker")
print(skills)

skills.remove("SQL")
print(skills)

print("Python" in skills)
print("React" in skills)

transactions = ["user1", "user2", "user1", "user3", "user2", "user1"]
unique_users = set(transactions)
print(unique_users)
print(len(unique_users))

# --- Concept 3: String Methods ---
name = "  Bhawani Lal  "
print(name.strip())
print(name.strip().upper())
print(name.strip().lower())
print(name.strip().title())

skills = "Python,Java,SQL,Docker,Kafka"
skills_list = skills.split(",")
print(skills_list)

joined = " | ".join(skills_list)
print(joined)

sentence = "I am applying to Google"
print(sentence.replace("Google", "JPMorgan"))

email = "bhawanilal@hotmail.com"
print(email.startswith("bhawani"))
print(email.endswith(".com"))
print(email.find("@"))

# --- Concept 4: String Formatting ---
for i in range(1, 6):
    print(f"Session {i:02d}")

accuracy = 94.56789
print(f"Model accuracy: {accuracy:.2f}%")

raw_names = ["  bhawani lal  ", "JOHN DOE", "jane smith  "]
for name in raw_names:
    cleaned = name.strip().title()
    print(cleaned)

# --- Concept 5: Tuples as Function Return ---
def get_profile():
    name = "Bhawani"
    university = "Strathclyde"
    graduation = 2027
    return name, university, graduation

name, university, graduation = get_profile()
print(name)
print(university)
print(graduation)

def evaluate_model():
    accuracy = 94.5
    precision = 92.3
    recall = 91.8
    return accuracy, precision, recall

acc, prec, rec = evaluate_model()
print(f"Accuracy: {acc:.1f}%")
print(f"Precision: {prec:.1f}%")
print(f"Recall: {rec:.1f}%")

# --- Concept 6: Exception Handling ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Please provide numbers only")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))

# ============================================
# SESSION 04 - TASKS
# ============================================

# --- Task 1: Data Cleaning ---
raw_data = ["  python  ", "JAVA", "  sql  ", "DOCKER", "  kafka  "]
cleaned_list = []

for name in raw_data:
    cleaned = name.strip().title()
    cleaned_list.append(cleaned)

print(cleaned_list)
final_set = set(cleaned_list)
print(final_set)

# --- Task 2: Model Evaluation ---
def analyze_model(model_name, accuracy, total_predictions):
    try:
        error_rate = (100 - accuracy) / total_predictions
        print(f"{model_name} — Accuracy: {accuracy:.2f}% | Error rate: {error_rate:.4f}")
    except ZeroDivisionError:
        print("Error: No predictions made")

analyze_model("LSTM", 94.5678, 1000)
analyze_model("Random Forest", 91.234, 0)
analyze_model("Hybrid Model", 96.789, 1500)

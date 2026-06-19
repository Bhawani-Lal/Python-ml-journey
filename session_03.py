# ============================================
# SESSION 03 - Functions & Dictionaries
# ============================================

# --- Concept 1: Basic Function ---
def greet(name):
    print(f"Hello {name}, welcome!")

greet("Bhawani")
greet("Google Recruiter")

# --- Concept 2: Return Values ---
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
print(add(100, 200))

def is_ready(leetcode_count):
    if leetcode_count >= 100:
        return True
    else:
        return False

print(is_ready(12))
print(is_ready(105))

# --- Concept 3: Default Parameters ---
def greet(name, company="JPMorgan"):
    print(f"Hello {name}, welcome to {company}!")

greet("Bhawani")
greet("Bhawani", "Google")
greet("Bhawani", "BNP Paribas")

# --- Concept 4: Dictionaries ---
profile = {
    "name": "Bhawani",
    "age": 23,
    "university": "Strathclyde",
    "skills": ["Python", "Java", "SQL"]
}

print(profile["name"])
print(profile["university"])
print(profile["skills"])

# --- Concept 5: Dictionary Operations ---
profile = {
    "name": "Bhawani",
    "city": "Glasgow"
}

profile["leetcode"] = 12
print(profile)

profile["leetcode"] = 13
print(profile)

print("name" in profile)
print("salary" in profile)

for key, value in profile.items():
    print(f"{key} → {value}")

# --- Concept 6: Functions + Dictionaries Together ---
def describe_candidate(profile):
    print(f"Name: {profile['name']}")
    print(f"University: {profile['university']}")
    print(f"LeetCode solved: {profile['leetcode']}")

    if profile["leetcode"] >= 150:
        print("Status: Ready for Google")
    elif profile["leetcode"] >= 100:
        print("Status: Ready for JPMorgan")
    else:
        print(f"Status: Keep grinding, {150 - profile['leetcode']} problems to go")

candidate = {
    "name": "Bhawani",
    "university": "Strathclyde",
    "leetcode": 12
}

describe_candidate(candidate)

# ============================================
# SESSION 03 - TASKS
# ============================================

# --- Task 1: check_application function ---
def check_application(company_name, leetcode_count):
    if leetcode_count >= 150:
        print(f"Apply to {company_name} now!")
    elif leetcode_count >= 100:
        print(f"{company_name} - almost ready")
    else:
        print(f"Not ready for {company_name} yet")

check_application("Google", 12)
check_application("JPMorgan", 105)
check_application("Amazon", 150)

# --- Task 2: print_profile function ---
def print_profile(profile):
    for key, value in profile.items():
        print(f"{key} → {value}")

my_profile = {
    "name": "Bhawani",
    "university": "Strathclyde",
    "course": "MSc Advanced Computer Science with Data Science",
    "graduation_year": 2027,
    "skills": ["Python", "Java", "SQL"],
    "leetcode_solved": 15
}

print_profile(my_profile)

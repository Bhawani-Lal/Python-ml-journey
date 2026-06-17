# ============================================
# SESSION 02 - Lists, Conditions & Loops
# ============================================

# --- Concept 1: Lists ---
skills = ["Python", "Java", "SQL", "Spring Boot", "Kafka"]

print(skills)           # entire list
print(skills[0])        # first item
print(skills[-1])       # last item
print(len(skills))      # total count

# --- Concept 2: List Operations ---
skills = ["Python", "Java", "SQL"]

skills.append("Docker")
print(skills)

skills.remove("SQL")
print(skills)

print("Java" in skills)    # True
print("React" in skills)   # False

# --- Concept 3: Conditions (if/elif/else) ---
score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Fail")

# --- Concept 4: For Loop ---
skills = ["Python", "Java", "SQL", "Docker"]

for skill in skills:
    print(f"I know {skill}")

# --- Concept 5: Range Loop ---
# Print numbers 0 to 4
for i in range(5):
    print(i)

# Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers 2 to 10
for i in range(2, 11, 2):
    print(i)

# --- Concept 6: While Loop ---
count = 1

while count <= 5:
    print(f"Count is {count}")
    count += 1

print("Done")

# --- Task 1: Companies Loop ---
companies = ["JPMorgan", "Google", "Microsoft", "Amazon", "G4S"]

for company in companies:
    print(f"I am applying to {company}")

# --- Task 2: LeetCode Condition ---
leetcode_solved = 12

if leetcode_solved >= 150:
    print("Ready for Google")
elif leetcode_solved >= 100:
    print("Ready for JPMorgan")
elif leetcode_solved >= 50:
    print("Halfway there")
else:
    print(f"Keep grinding - current count: {leetcode_solved}")

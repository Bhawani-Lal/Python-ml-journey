# ============================================
# SESSION 05 - List Comprehensions & File Handling
# ============================================


# --- Concept 1: Basic List Comprehension ---

numbers = [1, 2, 3, 4, 5]

# Old way
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)      # [1, 4, 9, 16, 25]

# New way — list comprehension
squared = [n ** 2 for n in numbers]
print(squared)      # [1, 4, 9, 16, 25]

# More examples
names = ["bhawani", "google", "jpmorgan"]
upper = [name.upper() for name in names]
print(upper)        # ['BHAWANI', 'GOOGLE', 'JPMORGAN']

lengths = [len(name) for name in names]
print(lengths)      # [7, 6, 7]


# --- Concept 2: List Comprehension with Condition ---

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if n % 2 == 0]
print(evens)        # [2, 4, 6, 8, 10]

odds = [n for n in numbers if n % 2 != 0]
print(odds)         # [1, 3, 5, 7, 9]

big = [n for n in numbers if n > 5]
print(big)          # [6, 7, 8, 9, 10]

skills = ["Python", "Java", "SQL", "Docker", "Kafka", "Excel"]
tech_skills = [s for s in skills if s != "Excel"]
print(tech_skills)  # ['Python', 'Java', 'SQL', 'Docker', 'Kafka']

# Real world — filter invalid sensor readings
readings = [120, -1, 340, 0, 520, -5, 890]
valid = [r for r in readings if r > 0]
print(valid)        # [120, 340, 520, 890]


# --- Concept 3: List Comprehension with Transformation ---

raw_data = ["  python  ", "  JAVA  ", "  sql  ", "  DOCKER  "]

# Old way
cleaned = []
for item in raw_data:
    cleaned.append(item.strip().title())
print(cleaned)

# New way
cleaned = [item.strip().title() for item in raw_data]
print(cleaned)      # ['Python', 'Java', 'Sql', 'Docker']

# Convert strings to numbers
str_numbers = ["1", "2", "3", "4", "5"]
integers = [int(n) for n in str_numbers]
print(integers)     # [1, 2, 3, 4, 5]

# Cap RUL at 125 — SmartMaintain dissertation pattern
raw_rul = [180, 90, 125, 200, 45, 130]
capped_rul = [min(r, 125) for r in raw_rul]
print(capped_rul)   # [125, 90, 125, 125, 45, 125]


# --- Concept 4: File Handling — Writing Files ---

# Old way
file = open("engineer.txt", "w")
file.write("Name: Bhawani Lal\n")
file.write("University: Strathclyde\n")
file.write("Target: Data Engineer\n")
file.write("LeetCode: 15 solved\n")
file.close()

print("File created successfully!")

# Better way — using with (auto closes file)
with open("engineer.txt", "w") as file:
    file.write("Name: Bhawani Lal\n")
    file.write("University: Strathclyde\n")
    file.write("Target: Data Engineer\n")
    file.write("LeetCode: 15 solved\n")

print("File written successfully!")


# --- Concept 5: File Handling — Reading Files ---

# Write data first
with open("skills.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("SQL\n")
    file.write("Apache Kafka\n")
    file.write("Machine Learning\n")

# Read entire file
with open("skills.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("skills.txt", "r") as file:
    for line in file:
        print(f"Skill: {line.strip()}")

# Read all lines into a list
with open("skills.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    print(f"Total skills: {len(lines)}")


# --- Concept 6: File Handling with List Comprehension ---

companies = ["JPMorgan", "Google", "Amazon", "BNP Paribas", "G4S"]

with open("targets.txt", "w") as file:
    for company in companies:
        file.write(f"{company}\n")

print("Companies saved!")

# Read back and clean in one line
with open("targets.txt", "r") as file:
    loaded = [line.strip() for line in file]

print(loaded)
print(f"Total targets: {len(loaded)}")

# Filter while reading
with open("targets.txt", "r") as file:
    big_names = [line.strip() for line in file if len(line.strip()) > 5]

print(big_names)


# ============================================
# SESSION 05 - TASKS
# ============================================

# --- Task 1: Skills File ---
skills = ["Python", "Java", "SQL", "Machine Learning", "Apache Kafka", "Docker"]

with open("my_skills.txt", "w") as file:
    for skill in skills:
        file.write(f"{skill}\n")

print("File created!")

with open("my_skills.txt", "r") as file:
    for index, skill in enumerate(file, 1):
        print(f"Skill {index}: {skill.strip()}")


# --- Task 2: LeetCode Log ---
weekly = [3, 5, 2, 8, 4]

# Filter weeks with more than 3 solved
high = [w for w in weekly if w > 3]

# Write to file
with open("leetcode_log.txt", "w") as file:
    for week in high:
        file.write(f"{week}\n")

# Read back
with open("leetcode_log.txt", "r") as file:
    loaded = [int(line.strip()) for line in file]

print(f"High performance weeks: {loaded}")
print(f"Total high performance weeks: {len(loaded)}")

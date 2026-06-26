# === Random Module ===


# ========== TABLE OF CONTENTS ==========
#
# 1. BASIC RANDOM NUMBERS
# 2. RANDOM FROM SEQUENCES (choice, sample, shuffle)
# 3. PROBABILITY DISTRIBUTIONS
# 4. SEEDS (REPRODUCIBLE RANDOMNESS)
# 5. WEIGHTED RANDOM
# 6. SECURE RANDOM (secrets)
# 7. RANDOM STRINGS & PASSWORDS
# 8. PRACTICAL PATTERNS (dice, lottery, sampling, Monte Carlo)
#
# ========================================


# Definition: The random module generates pseudo‑random numbers.
# For cryptographic security, use the secrets module instead.


# ---------- 1. BASIC RANDOM NUMBERS ----------

import random
import secrets          # for secure random
import string
import datetime

# Random float in [0.0, 1.0)
random.random()                          # e.g., 0.548813

# Random float in [a, b]
random.uniform(1.5, 5.5)                 # e.g., 3.721

# Random integer: a <= x <= b
random.randint(1, 10)                    # e.g., 7

# Random integer with step (start, stop, step)
random.randrange(0, 100, 5)              # 0,5,10,…,95


# ---------- 2. RANDOM FROM SEQUENCES (choice, sample, shuffle) ----------

items = ["apple", "banana", "cherry", "date", "elderberry"]

# Single random element
random.choice(items)                     # e.g., "cherry"

# Multiple random elements with replacement (can repeat)
random.choices(items, k=3)               # e.g., ["banana","apple","banana"]

# Multiple random elements without replacement (unique)
random.sample(items, k=3)                # e.g., ["date","apple","cherry"]

# Shuffle a list in‑place (no return value)
cards = ["A♠", "K♠", "Q♠", "J♠"]
random.shuffle(cards)                    # cards is now shuffled

# Create a shuffled copy (original unchanged)
original = [1, 2, 3, 4, 5]
shuffled = random.sample(original, k=len(original))


# ---------- 3. PROBABILITY DISTRIBUTIONS ----------

# Normal/Gaussian (mean, standard deviation)
random.gauss(0, 1)                       # e.g., -0.234

# Exponential (lambda = 1/mean)
random.expovariate(1.5)                  # e.g., 0.723

# Triangular (low, high, mode)
random.triangular(1, 10, 5)              # e.g., 4.321

# Beta distribution (alpha, beta)
random.betavariate(0.5, 0.5)             # e.g., 0.234


# ---------- 4. SEEDS (REPRODUCIBLE RANDOMNESS) ----------

# Set a seed – same seed produces the same sequence.
random.seed(42)
a = random.random()                      # always 0.639...
random.seed()                            # reset to system time

# Save and restore the generator state.
state = random.getstate()                # save current state
# ... perform some random operations ...
random.setstate(state)                   # restore exact state


# ---------- 5. WEIGHTED RANDOM ----------

items = ["common", "uncommon", "rare", "epic", "legendary"]
weights = [50, 30, 15, 4, 1]            # probabilities (sum = 100)

# Weighted choices (with replacement)
random.choices(items, weights=weights, k=10)

# Using cumulative weights directly
cum_weights = [50, 80, 95, 99, 100]
random.choices(items, cum_weights=cum_weights, k=5)


# ---------- 6. SECURE RANDOM (secrets) ----------

# Use secrets for passwords, tokens, etc. (cryptographically strong)
secrets.randbelow(100)                   # 0 ≤ x < 100
secrets.choice(items)                    # secure random choice
secrets.token_hex(16)                    # 32‑character hex string
secrets.token_urlsafe(16)                # URL‑safe base64 string

# Regular random is NOT suitable for security.
random.randint(0, 99)                    # OK for games, NOT for passwords


# ---------- 7. RANDOM STRINGS & PASSWORDS ----------

# Characters sets
letters = string.ascii_letters           # 'a‑zA‑Z'
digits = string.digits                   # '0‑9'
punctuation = string.punctuation         # '!@#$%...'

# Strong random password (12 characters)
all_chars = letters + digits + punctuation
password = ''.join(random.choices(all_chars, k=12))

# XKCD‑style memorable password (using a word list)
words = ["correct", "horse", "battery", "staple"]
password = '-'.join(random.choices(words, k=4))

# Random hexadecimal color
color = f"#{secrets.token_hex(3)}"       # e.g., '#a3f5c2'


# ---------- 8. PRACTICAL PATTERNS (dice, lottery, sampling, Monte Carlo) ----------

# Dice roll (function)
def roll_dice(sides=6, count=1):
    return [random.randint(1, sides) for _ in range(count)]

# Random date between two dates
start = datetime.date(2020, 1, 1)
end = datetime.date(2023, 12, 31)
random_date = start + datetime.timedelta(days=random.randint(0, (end - start).days))

# Lottery numbers (unique, sorted)
def lottery_numbers(pool=49, picks=6):
    return sorted(random.sample(range(1, pool + 1), k=picks))

# Random sampling for testing (100 unique indices)
data = list(range(1000))
test_set = random.sample(data, k=100)

# Monte Carlo estimation of π
inside = 0
total = 1_000_000
for _ in range(total):
    x, y = random.random(), random.random()
    if x*x + y*y <= 1:                   # inside unit circle
        inside += 1
pi_estimate = 4 * inside / total
# === Random Module ===

import random
import secrets  # For cryptographic security

# === BASIC RANDOM NUMBERS ===

# Random float: 0.0 <= x < 1.0
random.random()                            # e.g., 0.548813...

# Random float in range [a, b]
random.uniform(1.5, 5.5)                   # e.g., 3.721...

# Random integer: a <= x <= b
random.randint(1, 10)                      # e.g., 7

# Random integer with step
random.randrange(0, 100, 5)                # 0, 5, 10, ..., 95

# === RANDOM FROM SEQUENCES ===

items = ["apple", "banana", "cherry", "date", "elderberry"]

# Single random choice
random.choice(items)                       # e.g., "cherry"

# Multiple random choices (with replacement)
random.choices(items, k=3)                 # e.g., ["banana", "apple", "banana"]

# Multiple unique choices (without replacement)
random.sample(items, k=3)                  # e.g., ["date", "apple", "cherry"]

# Shuffle list (in-place)
cards = ["A♠", "K♠", "Q♠", "J♠"]
random.shuffle(cards)                      # cards is now shuffled

# Create shuffled copy
original = [1, 2, 3, 4, 5]
shuffled = random.sample(original, k=len(original))

# === PROBABILITY DISTRIBUTIONS ===

# Normal/Gaussian distribution (mean, standard deviation)
random.gauss(0, 1)                         # e.g., -0.234...

# Exponential distribution (lambda = 1/mean)
random.expovariate(1.5)                    # e.g., 0.723...

# Triangular distribution (low, high, mode)
random.triangular(1, 10, 5)                # e.g., 4.321...

# Beta distribution (alpha, beta)
random.betavariate(0.5, 0.5)               # e.g., 0.234...

# === SEEDS (REPRODUCIBLE RANDOMNESS) ===

# Set seed for reproducibility
random.seed(42)                            # Same seed = same sequence
a = random.random()                        # Always 0.639... with seed(42)

# Reset to random seed
random.seed()                              # Uses system time

# Get/set state
state = random.getstate()                  # Save current state
# ... some random operations ...
random.setstate(state)                     # Restore exact state

# === WEIGHTED RANDOM ===

items = ["common", "uncommon", "rare", "epic", "legendary"]
weights = [50, 30, 15, 4, 1]               # Probabilities

# Weighted choice
random.choices(items, weights=weights, k=10)

# Cumulative weights
cum_weights = [50, 80, 95, 99, 100]        # Cumulative sum
random.choices(items, cum_weights=cum_weights, k=5)

# === SECURE RANDOM (CRYPTOGRAPHY) ===

# Cryptographically secure random
secrets.randbelow(100)                     # 0 <= x < 100 (secure)
secrets.choice(items)                      # Secure random choice
secrets.token_hex(16)                      # 32-char hex string
secrets.token_urlsafe(16)                  # URL-safe string

# Compare: NOT secure for cryptography!
random.randint(0, 99)                      # OK for games, NOT for passwords

# === RANDOM STRINGS & PASSWORDS ===

import string

# Random string
letters = string.ascii_letters             # 'a-zA-Z'
digits = string.digits                     # '0-9'
punctuation = string.punctuation           # '!@#$%^&*()_+'

# Random password
all_chars = letters + digits + punctuation
password = ''.join(random.choices(all_chars, k=12))

# Pronounceable password (xkcd style)
words = ["correct", "horse", "battery", "staple"]
password = '-'.join(random.choices(words, k=4))

# Random hexadecimal color
color = f"#{secrets.token_hex(3)}"         # e.g., '#a3f5c2'

# === PRACTICAL PATTERNS ===

# Dice roll
def roll_dice(sides=6, count=1):
    return [random.randint(1, sides) for _ in range(count)]

# Random date
import datetime
start = datetime.date(2020, 1, 1)
end = datetime.date(2023, 12, 31)
random_date = start + datetime.timedelta(days=random.randint(0, (end - start).days))

# Lottery numbers (unique)
def lottery_numbers(pool=49, picks=6):
    return sorted(random.sample(range(1, pool + 1), k=picks))

# Random sampling for testing
data = list(range(1000))
test_set = random.sample(data, k=100)      # 100 unique test samples

# Monte Carlo simulation (estimating pi)
inside = 0
total = 1000000
for _ in range(total):
    x, y = random.random(), random.random()
    if x*x + y*y <= 1:                     # Inside unit circle
        inside += 1
pi_estimate = 4 * inside / total           # Approximates π
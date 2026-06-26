# --- sleep.py ---
# Two ways to generate a sequence of sheep emojis: list vs. generator (yield).


# --- List (stores everything in memory) ---
# Builds a list of n strings, each with i sheep emojis.
# Uses O(n) memory. Suitable for small n.
"""
def main():
    n = int(input("What´s n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
"""


# --- Generator (yields one value at a time) ---
# Uses yield to produce values lazily without storing the whole list.
# Uses O(1) memory. Ideal for large n or infinite sequences.
def main():
    n = int(input("What´s n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()

# Key difference:
# - List version returns a complete list – simple but memory‑heavy.
# - Generator version yields each item on the fly – memory‑efficient and faster for large n.
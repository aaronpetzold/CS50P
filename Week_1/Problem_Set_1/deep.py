answer = input(
    "What is the answer to the Great Question of Life, the Universe and Everything: "
)

answer = answer.strip().lower().replace(" ", "").replace("-", "")

if answer == "42" or answer == "fortytwo":
    print("Yes")
else:
    print("No")

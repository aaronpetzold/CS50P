# --- Problem Set 1 ---

"""
# deep.py
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    text = check(answer)
    print(text)

def check(a):
    if a == "42" or a == "forty-two" or a == "fortytwo":
    # or: if a in("42", "forty-two", "fortytwo")
        t = "Yes"
    else: 
        t = "No"
    return t 

if __name__ == "__main__":
    main()


    
# bank.py
def main():
    greeting = get_greeting()
    money = check_greeting(greeting)
    print(f"${money}")

def get_greeting():
    g = input("Greeting: ").lower().strip()
    return g

def check_greeting(g):
    if g == "hello":
        m = 0
    elif g.startswith("h"):
        m = 20
    else: 
        m = 100
    return m

if __name__ == "__main__":
    main()


    
# extenstions.py
def main():
    file_name, suffix = get_file_name()
    media_type = get_media_type(suffix)
    print(media_type)

def get_file_name():
    file_name = input("File name: ").strip()
    if "." in file_name:
        prefix, suffix = file_name.rsplit(".", 1)
        return file_name, suffix.lower()
    else: 
        return file_name, ""

def get_media_type(s):
    if s == "gif": 
        media_type = "image/gif"
    elif s == "jpg" or s == "jpeg": 
        media_type = "image/jpeg"
    elif s == "png": 
        media_type = "image/png"
    elif s == "pdf": 
        media_type = "application/pdf"
    elif s == "txt": 
        media_type = "text/plain"
    elif s == "zip": 
        media_type = "application/zip"
    else: 
        media_type = "application/octet-stream"
    return media_type

if __name__ == "__main__":
    main()


    
# interpreter.py
def main():
    x, y, z = get_input()
    solution = get_solution(x, y, z)
    print(f"{solution: .1f}")

def get_input():
    x, y, z = input("Expression: ").split()
    x = float(x)
    z = float(z)
    return x, y, z

def get_solution(x, y, z):
    if y == "+":
        solution = x + z
    elif y == "-":
        solution = x - z
    elif y == "*":
        solution = x * z
    elif y == "/":
        solution = x / z
    else:
        print("Invalid")
        return 0
    return solution

if __name__ == "__main__":
    main()

    

# meal.py
def main():
    time = get_time()
    output = get_output(time)
    print(output)

def get_time():
    time_str = input("What time is it? ")
    hour, minute = time_str.split(":")
    time = float(hour) + float(minute) / 60
    return time

def get_output(time):
    if 7.0 <= time <= 8.0:
        output= "breakfast time"
    elif 12.0 <= time <= 13.0: 
        output = "lunch time"
    elif 18.0 <= time <= 19.0:
        output = "dinner time"
    else: 
        output = ""
    return output

if __name__ == "__main__":
    main()
"""
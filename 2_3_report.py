
def main():
    spacecraft = {"name":"James Webb Space Telescope"}
    spacecraft["age"] = 19
    spacecraft.update({"orbit":"Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ====== REPORT ======

    Name : {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Age: {spacecraft["age"]}
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ====================
    """

main()

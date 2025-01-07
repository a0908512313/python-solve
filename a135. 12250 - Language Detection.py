data = {
    "HELLO": "ENGLISH",
    "HOLA": "SPANISH",
    "HALLO": "GERMAN",
    "BONJOUR": "FRENCH",
    "CIAO": "ITALIAN",
    "ZDRAVSTVUJTE": "RUSSIAN"
}
results = list()
case_number = 1
while True:
    s = input()
    if s == "#":
        break
    temp = data.get(s, "UNKNOWN")
    results.append(f"Case {case_number}: {temp}")
    case_number += 1

print("\n".join(results))

import random

actors = {
    "Richard Gadd": "Gadd's performance was praised for its emotional complexity and its ability to convey the character's flaws and vulnerabilities.",
    "Gemma Gunning": "Gunning's performance was also praised for its ability to convey the character's flaws and vulnerabilities, and her chemistry with Gadd was noted as a highlight of the show.",
    "Rita Gadd": "Rita Gadd's performance was praised for its ability to convey the character's flaws and vulnerabilities, and her chemistry with Gadd was noted as a highlight of the show.",
    "Jim Gunning": "Jim Gunning's performance was praised for its ability to convey the character's flaws and vulnerabilities, and his chemistry with Gadd was noted as a highlight of the show.",
}

random_actor = random.choice(list(actors.keys()))
print(f"The randomly selected actor/actress is: {random_actor}")
print(f"Description of their performance: {actors[random_actor]}")
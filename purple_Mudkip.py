horse = {
  "name": "Flightline",
  "sex": "C",
  "race_history": [
    {"race_name": "Breeders Cup", "grade": "G1", "finish": 1, "track": "KEE"},
    {"race_name": "Pacific Classic", "grade": "G1", "finish": 1, "track": "DMR"}
  ]
}

print(horse)

for race in horse["race_history"]:
    print(f"{race['race_name']} finish: {race['finish']} place")
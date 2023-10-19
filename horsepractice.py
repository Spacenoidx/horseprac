# Okay, so here I have made a dictionary. The dictionary (same as an object in JSON, right?) contains key/value pairs for the name and sex, and a key and value of a list of dictionaries for the tracks raced.

horse = {
    'name': 'Flightline',
            'sex': 'C',

# Following your lead, I defined the horse's main attributes.

# Then, I tried to create dictionaries inside the list, with the values being stored as the track_Name and the times_Raced.

'tracks_Raced':
[
    {'track_Name': 'Keeneland', 'times_Raced': 1},
    {'track_Name': 'Belmont Park', 'times_Raced': 1},
    {'track_Name': 'Santa Anita', 'times_Raced': 2},
    {'track_Name': 'Del Mar', 'times_Raced': 2}
]

}

testTracks = horse['tracks_Raced']
print(testTracks)

for i in testTracks:
    print('Appeared at', i['track_Name'] , "a total of" , i['times_Raced'] , "times.")
    print(f'{i["track_Name"]}')
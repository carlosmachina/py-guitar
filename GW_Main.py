__author__ = 'carlosmachina'

notes_arr = {
"Cbb": {"Tb": "", "TJ": "Cbb", "T#": "Cb", "2o": "", "2b": "", "2M": "Dbb", "2#": "Db", "3o": "", "3b": "", "3M": "Ebb",
        "3#": "Eb", "4o": "", "4J": "Fbb", "4#": "Fb", "5o": "", "5J": "Gbb", "5#": "Gb", "6o": "", "6b": "",
        "6M": "Abb", "6#": "Ab", "7o": "", "7m": "", "7+": "Bbb"},
"Cb": {"Tb": "Cbb", "TJ": "Cb", "T#": "C", "2o": "", "2b": "Dbb", "2M": "Db", "2#": "D", "3o": "", "3b": "Ebb",
       "3M": "Eb", "3#": "E", "4o": "Fbb", "4J": "Fb", "4#": "F", "5o": "Gbb", "5J": "Gb", "5#": "G", "6o": "",
       "6b": "Abb", "6M": "Ab", "6#": "A", "7o": "", "7m": "Bbb", "7+": "Bb"},
"C": {"Tb": "Cb", "TJ": "C", "T#": "C#", "2o": "Dbb", "2b": "Db", "2M": "D", "2#": "D#", "3o": "Ebb", "3b": "Eb",
      "3M": "E", "3#": "E#", "4o": "Fb", "4J": "F", "4#": "F#", "5o": "Gb", "5J": "G", "5#": "G#", "6o": "Abb",
      "6b": "Ab", "6M": "A", "6#": "A#", "7o": "Bbb", "7m": "Bb", "7+": "B"},
"C#": {"Tb": "C", "TJ": "C#", "T#": "C##", "2o": "Db", "2b": "D", "2M": "D#", "2#": "D##", "3o": "Eb", "3b": "E",
       "3M": "E#", "3#": "E##", "4o": "F", "4J": "F#", "4#": "F##", "5o": "G", "5J": "G#", "5#": "G##", "6o": "Ab",
       "6b": "A", "6M": "A#", "6#": "A##", "7o": "Bb", "7m": "B", "7+": "B#"},
"C##": {"Tb": "C#", "TJ": "C##", "T#": "", "2o": "D", "2b": "D#", "2M": "D##", "2#": "", "3o": "E", "3b": "E#",
        "3M": "E##", "3#": "", "4o": "F#", "4J": "F##", "4#": "", "5o": "G#", "5J": "G##", "5#": "", "6o": "A",
        "6b": "A#", "6M": "A##", "6#": "", "7o": "B", "7m": "B#", "7+": "B##"},
"Dbb": {"Tb": "", "TJ": "Dbb", "T#": "Db", "2o": "", "2b": "", "2M": "Ebb", "2#": "Eb", "3o": "", "3b": "Fbb",
        "3M": "Fb", "3#": "F", "4o": "", "4J": "Gbb", "4#": "Gb", "5o": "", "5J": "Abb", "5#": "Ab", "6o": "", "6b": "",
        "6M": "Bbb", "6#": "Bb", "7o": "", "7m": "Cbb", "7+": "Cb"},
"Db": {"Tb": "Dbb", "TJ": "Db", "T#": "D", "2o": "", "2b": "Ebb", "2M": "Eb", "2#": "E", "3o": "Fbb", "3b": "Fb",
       "3M": "F", "3#": "F#", "4o": "Gbb", "4J": "Gb", "4#": "G", "5o": "Abb", "5J": "Ab", "5#": "A", "6o": "",
       "6b": "Bbb", "6M": "Bb", "6#": "B", "7o": "Cbb", "7m": "Cb", "7+": "C"},
"D": {"Tb": "Db", "TJ": "D", "T#": "D#", "2o": "Ebb", "2b": "Eb", "2M": "E", "2#": "E#", "3o": "Fb", "3b": "F",
      "3M": "F#", "3#": "F##", "4o": "Gb", "4J": "G", "4#": "G#", "5o": "Ab", "5J": "A", "5#": "A#", "6o": "Bbb",
      "6b": "Bb", "6M": "B", "6#": "B#", "7o": "Cb", "7m": "C", "7+": "C#"},
"D#": {"Tb": "D", "TJ": "D#", "T#": "D##", "2o": "Eb", "2b": "E", "2M": "E#", "2#": "E##", "3o": "F", "3b": "F#",
       "3M": "F##", "3#": "", "4o": "G", "4J": "G#", "4#": "G##", "5o": "A", "5J": "A#", "5#": "A##", "6o": "Bb",
       "6b": "B", "6M": "B#", "6#": "B##", "7o": "C", "7m": "C#", "7+": "C##"},
"D##": {"Tb": "D#", "TJ": "D##", "T#": "", "2o": "E", "2b": "E#", "2M": "E##", "2#": "", "3o": "F#", "3b": "F##",
        "3M": "", "3#": "", "4o": "G#", "4J": "G##", "4#": "", "5o": "A#", "5J": "A##", "5#": "", "6o": "B", "6b": "B#",
        "6M": "B##", "6#": "", "7o": "C#", "7m": "C##", "7+": ""},
"Ebb": {"Tb": "", "TJ": "Ebb", "T#": "Eb", "2o": "", "2b": "Fbb", "2M": "Fb", "2#": "F", "3o": "", "3b": "Gbb",
        "3M": "Gb", "3#": "Gb", "4o": "", "4J": "Abb", "4#": "Ab", "5o": "", "5J": "Bbb", "5#": "Bb", "6o": "",
        "6b": "Cbb", "6M": "Cb", "6#": "C", "7o": "", "7m": "Dbb", "7+": "Db"},
"Eb": {"Tb": "Ebb", "TJ": "Eb", "T#": "E", "2o": "Fbb", "2b": "Fb", "2M": "F", "2#": "F#", "3o": "Gbb", "3b": "Gb",
       "3M": "G", "3#": "G", "4o": "Abb", "4J": "Ab", "4#": "A", "5o": "Bbb", "5J": "Bb", "5#": "B", "6o": "Cbb",
       "6b": "Cb", "6M": "C", "6#": "C#", "7o": "Dbb", "7m": "Db", "7+": "D"},
"E": {"Tb": "Eb", "TJ": "E", "T#": "E#", "2o": "Fb", "2b": "F", "2M": "F#", "2#": "F##", "3o": "Gb", "3b": "G",
      "3M": "G#", "3#": "G#", "4o": "Ab", "4J": "A", "4#": "A#", "5o": "Bb", "5J": "B", "5#": "B#", "6o": "Cb",
      "6b": "C", "6M": "C#", "6#": "C##", "7o": "Db", "7m": "D", "7+": "D#"},
"E#": {"Tb": "E", "TJ": "E#", "T#": "E##", "2o": "F", "2b": "F#", "2M": "F##", "2#": "", "3o": "G", "3b": "G#",
       "3M": "G##", "3#": "G##", "4o": "A", "4J": "A#", "4#": "A##", "5o": "B", "5J": "B#", "5#": "B##", "6o": "C",
       "6b": "C#", "6M": "C##", "6#": "", "7o": "D", "7m": "D#", "7+": "D##"},
"E##": {"Tb": "E#", "TJ": "E##", "T#": "", "2o": "F#", "2b": "F##", "2M": "", "2#": "", "3o": "G#", "3b": "G##",
        "3M": "", "3#": "", "4o": "A#", "4J": "A##", "4#": "", "5o": "B#", "5J": "B##", "5#": "", "6o": "C#",
        "6b": "C##", "6M": "", "6#": "", "7o": "D#", "7m": "D##", "7+": ""},
"Fbb": {"Tb": "", "TJ": "Fbb", "T#": "Fb", "2o": "", "2b": "", "2M": "Gbb", "2#": "Gb", "3o": "", "3b": "", "3M": "Abb",
        "3#": "Ab", "4o": "", "4J": "", "4#": "Bbb", "5o": "", "5J": "Cbb", "5#": "Cb", "6o": "", "6b": "", "6M": "Dbb",
        "6#": "Db", "7o": "", "7m": "", "7+": "Ebb"},
"Fb": {"Tb": "Fbb", "TJ": "Fb", "T#": "F", "2o": "", "2b": "Gbb", "2M": "Gb", "2#": "G", "3o": "", "3b": "Abb",
       "3M": "Ab", "3#": "A", "4o": "", "4J": "Bbb", "4#": "Bb", "5o": "Cbb", "5J": "Cb", "5#": "C", "6o": "",
       "6b": "Dbb", "6M": "Db", "6#": "D", "7o": "", "7m": "Ebb", "7+": "Eb"},
"F": {"Tb": "Fb", "TJ": "F", "T#": "F#", "2o": "Gbb", "2b": "Gb", "2M": "G", "2#": "G#", "3o": "Abb", "3b": "Ab",
      "3M": "A", "3#": "A#", "4o": "Bbb", "4J": "Bb", "4#": "B", "5o": "Cb", "5J": "C", "5#": "C#", "6o": "Dbb",
      "6b": "Db", "6M": "D", "6#": "D#", "7o": "Ebb", "7m": "Eb", "7+": "E"},
"F#": {"Tb": "F", "TJ": "F#", "T#": "F##", "2o": "Gb", "2b": "G", "2M": "G#", "2#": "G##", "3o": "Ab", "3b": "A",
       "3M": "A#", "3#": "A##", "4o": "Bb", "4J": "B", "4#": "B#", "5o": "C", "5J": "C#", "5#": "C##", "6o": "Db",
       "6b": "D", "6M": "D#", "6#": "D##", "7o": "Eb", "7m": "E", "7+": "E#"},
"F##": {"Tb": "F#", "TJ": "F##", "T#": "", "2o": "G", "2b": "G#", "2M": "G##", "2#": "", "3o": "A", "3b": "A#",
        "3M": "A##", "3#": "", "4o": "B", "4J": "B#", "4#": "B##", "5o": "C#", "5J": "C##", "5#": "", "6o": "D",
        "6b": "D#", "6M": "D##", "6#": "", "7o": "E", "7m": "E#", "7+": "E##"},
"Gbb": {"Tb": "", "TJ": "Gbb", "T#": "Gb", "2o": "", "2b": "", "2M": "Abb", "2#": "Ab", "3o": "", "3b": "", "3M": "Bbb",
        "3#": "Bb", "4o": "", "4J": "Cbb", "4#": "Cb", "5o": "", "5J": "Dbb", "5#": "Db", "6o": "", "6b": "",
        "6M": "Ebb", "6#": "Eb", "7o": "", "7m": "Fbb", "7+": "Fb"},
"Gb": {"Tb": "Gbb", "TJ": "Gb", "T#": "G", "2o": "", "2b": "Abb", "2M": "Ab", "2#": "A", "3o": "", "3b": "Bbb",
       "3M": "Bb", "3#": "B", "4o": "Cbb", "4J": "Cb", "4#": "C", "5o": "Dbb", "5J": "Db", "5#": "D", "6o": "",
       "6b": "Ebb", "6M": "Eb", "6#": "E", "7o": "Fbb", "7m": "Fb", "7+": "F"},
"G": {"Tb": "Gb", "TJ": "G", "T#": "G#", "2o": "Abb", "2b": "Ab", "2M": "A", "2#": "A#", "3o": "Bbb", "3b": "Bb",
      "3M": "B", "3#": "B#", "4o": "Cb", "4J": "C", "4#": "C#", "5o": "Db", "5J": "D", "5#": "D#", "6o": "Ebb",
      "6b": "Eb", "6M": "E", "6#": "E#", "7o": "Fb", "7m": "F", "7+": "F#"},
"G#": {"Tb": "G", "TJ": "G#", "T#": "G##", "2o": "Ab", "2b": "A", "2M": "A#", "2#": "A##", "3o": "Bb", "3b": "B",
       "3M": "B#", "3#": "B##", "4o": "C", "4J": "C#", "4#": "C##", "5o": "D", "5J": "D#", "5#": "D##", "6o": "Eb",
       "6b": "E", "6M": "E#", "6#": "E##", "7o": "F", "7m": "F#", "7+": "F##"},
"G##": {"Tb": "G#", "TJ": "G##", "T#": "", "2o": "A", "2b": "A#", "2M": "A##", "2#": "", "3o": "B", "3b": "B#",
        "3M": "B##", "3#": "", "4o": "C#", "4J": "C##", "4#": "", "5o": "D#", "5J": "D##", "5#": "", "6o": "E",
        "6b": "E#", "6M": "E##", "6#": "", "7o": "F#", "7m": "F##", "7+": ""},
"Abb": {"Tb": "", "TJ": "Abb", "T#": "Ab", "2o": "", "2b": "", "2M": "Bbb", "2#": "Bb", "3o": "", "3b": "Cbb",
        "3M": "Cb", "3#": "C", "4o": "", "4J": "Dbb", "4#": "Db", "5o": "", "5J": "Ebb", "5#": "Eb", "6o": "",
        "6b": "Fbb", "6M": "Fb", "6#": "F", "7o": "", "7m": "Gbb", "7+": "Gb"},
"Ab": {"Tb": "Abb", "TJ": "Ab", "T#": "A", "2o": "", "2b": "Bbb", "2M": "Bb", "2#": "B", "3o": "Cbb", "3b": "Cb",
       "3M": "C", "3#": "C#", "4o": "Dbb", "4J": "Db", "4#": "D", "5o": "Ebb", "5J": "Eb", "5#": "E", "6o": "Fbb",
       "6b": "Fb", "6M": "F", "6#": "F#", "7o": "Gbb", "7m": "Gb", "7+": "G"},
"A": {"Tb": "Ab", "TJ": "A", "T#": "A#", "2o": "Bbb", "2b": "Bb", "2M": "B", "2#": "B#", "3o": "Cb", "3b": "C",
      "3M": "C#", "3#": "C##", "4o": "Db", "4J": "D", "4#": "D#", "5o": "Eb", "5J": "E", "5#": "E#", "6o": "Fb",
      "6b": "F", "6M": "F#", "6#": "F##", "7o": "Gb", "7m": "G", "7+": "G#"},
"A#": {"Tb": "A", "TJ": "A#", "T#": "A##", "2o": "Bb", "2b": "B", "2M": "B#", "2#": "B##", "3o": "C", "3b": "C#",
       "3M": "C##", "3#": "", "4o": "D", "4J": "D#", "4#": "D##", "5o": "E", "5J": "E#", "5#": "E##", "6o": "F",
       "6b": "F#", "6M": "F##", "6#": "", "7o": "G", "7m": "G#", "7+": "G##"},
"A##": {"Tb": "A#", "TJ": "A##", "T#": "", "2o": "B", "2b": "B#", "2M": "B##", "2#": "", "3o": "C#", "3b": "C##",
        "3M": "", "3#": "", "4o": "D#", "4J": "D##", "4#": "", "5o": "E#", "5J": "E##", "5#": "", "6o": "F#",
        "6b": "F##", "6M": "", "6#": "", "7o": "G#", "7m": "G##", "7+": ""},
"Bbb": {"Tb": "", "TJ": "Bbb", "T#": "Bb", "2o": "", "2b": "Cbb", "2M": "Cb", "2#": "C", "3o": "", "3b": "Dbb",
        "3M": "Db", "3#": "D", "4o": "", "4J": "Ebb", "4#": "Eb", "5o": "Fbb", "5J": "Fb", "5#": "F", "6o": "",
        "6b": "Gbb", "6M": "Gb", "6#": "G", "7o": "", "7m": "Abb", "7+": "Ab"},
"Bb": {"Tb": "Bbb", "TJ": "Bb", "T#": "B", "2o": "Cbb", "2b": "Cb", "2M": "C", "2#": "C#", "3o": "Dbb", "3b": "Db",
       "3M": "D", "3#": "D#", "4o": "Ebb", "4J": "Eb", "4#": "E", "5o": "Fb", "5J": "F", "5#": "F#", "6o": "Gbb",
       "6b": "Gb", "6M": "G", "6#": "G#", "7o": "Abb", "7m": "Ab", "7+": "A"},
"B": {"Tb": "Bb", "TJ": "B", "T#": "B#", "2o": "Cb", "2b": "C", "2M": "C#", "2#": "C##", "3o": "Db", "3b": "D",
      "3M": "D#", "3#": "D##", "4o": "Eb", "4J": "E", "4#": "E#", "5o": "F", "5J": "F#", "5#": "F##", "6o": "Gb",
      "6b": "G", "6M": "G#", "6#": "G##", "7o": "Ab", "7m": "A", "7+": "A#"},
"B#": {"Tb": "B", "TJ": "B#", "T#": "B##", "2o": "C", "2b": "C#", "2M": "C##", "2#": "", "3o": "D", "3b": "D#",
       "3M": "D##", "3#": "", "4o": "E", "4J": "E#", "4#": "E##", "5o": "F#", "5J": "F##", "5#": "", "6o": "G",
       "6b": "G#", "6M": "G##", "6#": "", "7o": "A", "7m": "A#", "7+": "A##"},
"B##": {"Tb": "B#", "TJ": "B##", "T#": "", "2o": "C#", "2b": "C##", "2M": "", "2#": "", "3o": "D#", "3b": "D##",
        "3M": "", "3#": "", "4o": "E#", "4J": "E##", "4#": "", "5o": "F##", "5J": "", "5#": "", "6o": "G#", "6b": "G##",
        "6M": "", "6#": "", "7o": "A#", "7m": "A##", "7+": ""}}

modes_arr = {"ionian": ["TJ", "2M", "3M", "4J", "5J", "6M", "7+"],
         "dorian": ["TJ", "2M", "3b", "4J", "5J", "6M", "7m"],
         "phrygian": ["TJ", "2b", "3b", "4J", "5J", "6b", "7m"],
         "lidian": ["TJ", "2M", "3M", "4#", "5J", "6M", "7+"],
         "mixolidian": ["TJ", "2M", "3M", "4J", "5J", "6M", "7m"],
         "eolian": ["TJ", "2M", "3b", "4J", "5J", "6b", "7m"],
         "locrian": ["TJ", "2b", "3b", "4J", "5o", "6b", "7m"],
         "jonian 5#": ["TJ", "2M", "3M", "4J", "5#", "6M", "7+"],
         "dorian 4#": ["TJ", "2M", "3b", "4#", "5J", "6M", "7m"],
         "phrygian maj": ["TJ", "2b", "3M", "4J", "5J", "6b", "7m"],
         "lidian 9": ["TJ", "2#", "3M", "4#", "5J", "6M", "7+"],
         "mixolidian 1#": ["T#", "2M", "3M", "4J", "5J", "6M", "7m"],
         "eolian 7+": ["TJ", "2M", "3b", "4J", "5J", "6b", "7m"],
         "locrian 6": ["TJ", "2b", "3b", "4J", "5o", "6M", "7m"],
         "jonian 1#": ["T#", "2M", "3M", "4J", "5J", "6M", "7+"],
         "dorian 7+": ["TJ", "2M", "3b", "4J", "5J", "6M", "7+"],
         "phrygian 6": ["TJ", "2b", "3b", "4J", "5J", "6M", "7m"],
         "lidian 5#": ["TJ", "2M", "3M", "4#", "5#", "6M", "7+"],
         "mixolidian 4#": ["TJ", "2M", "3M", "4#", "5J", "6M", "7m"],
         "eolian maj": ["TJ", "2M", "3M", "4J", "5J", "6b", "7m"],
         "locrian 9": ["TJ", "2M", "3b", "4J", "5o", "6b", "7m"]
}

input_mode = "ionian"
root = "C"


def search_interval(root, target):
    root_intervals = notes_arr[root]
    targets_interval = dict((v,k) for (k,v) in root_intervals.items())
    return targets_interval[target]


def calculate_scale(root, input_mode):
    calc_scale = []
    for grade in range(7):
        calc_scale.append(notes_arr[root][modes_arr[input_mode][grade]])
        # print(calc_scale[grade] + " | ", end="")
    return calc_scale


def calculate_chord(root, chord_struct):
    root_intervals = notes_arr[root]
    calc_chord = []
    for intervals in chord_struct:
        calc_chord.append(root_intervals[intervals])
    return calc_chord



def calculate_field(root, input_mode, chord_size):
    scale = calculate_scale(root, input_mode)
    calc_chord = []
    calc_field = []
    grade = 0
    for note in scale:
        for i in range(chord_size):
            if grade < 7:
                calc_chord.append(notes_arr[root][modes_arr[input_mode][grade]])
            elif grade <14:
                calc_chord.append(notes_arr[root][modes_arr[input_mode][grade - 7]])
            else:
                calc_chord.append(notes_arr[root][modes_arr[input_mode][grade - 14]])
            grade += 2
        calc_field.append(calc_chord)
        calc_chord = []
        grade -= (chord_size * 2) -1
    return calc_field


def calculate_tab_chord(notes_chord):
    tab_chord = []
    for grade in range(len(notes_chord)):
        tab_chord.append(search_interval(notes_chord[0], notes_chord[grade]))
    return tab_chord


def calculate_tab_field(root, input_mode):
    note_field = calculate_field(root, input_mode)
    tab_field = []
    for chord in note_field:
        tab_field.append(calculate_tab_chord(chord))
    return tab_field


# print(search_interval("C", "Eb"))
# print(calculate_scale("C", "ionian"))
print(calculate_field("C", "ionian", 7))
# print(calculate_chord("C", ["TJ", "3M", "5J"]))
# print(calculate_tab_field("C", "ionian"))
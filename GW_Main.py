__author__ = 'carlosmachina'

import guitar_data as gd

input_mode = "ionian"
root = "C"


def search_interval(root, target):
    root_intervals = gd.notes_arr[root]
    targets_interval = dict((v,k) for (k,v) in root_intervals.items())
    return targets_interval[target]


def calculate_scale(root, input_mode):
    calc_scale = []
    for grade in range(7):
        calc_scale.append(gd.notes_arr[root][gd.modes_arr[input_mode][grade]])
        # print(calc_scale[grade] + " | ", end="")
    return calc_scale


def calculate_chord(root, chord_struct):
    root_intervals = gd.notes_arr[root]
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
                calc_chord.append(gd.notes_arr[root][gd.modes_arr[input_mode][grade]])
            elif grade <14:
                calc_chord.append(gd.notes_arr[root][gd.modes_arr[input_mode][grade - 7]])
            else:
                calc_chord.append(gd.notes_arr[root][gd.modes_arr[input_mode][grade - 14]])
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


def calculate_tab_field(root, input_mode, chord_size):
    note_field = calculate_field(root, input_mode, chord_size)
    tab_field = []
    for chord in note_field:
        tab_field.append(calculate_tab_chord(chord))
    return tab_field


# print(search_interval("C", "Eb"))
# print(calculate_scale("C", "ionian"))
#print(calculate_field("C", "ionian", 7))
# print(calculate_chord("C", ["TJ", "3M", "5J"]))
print(calculate_tab_field("C", "ionian", 4))
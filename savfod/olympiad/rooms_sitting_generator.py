#!/bin/sh python3
import random

ROOMS_FILE = 'rooms.txt' #tab separated file: grade cab desks_count are_desks_divisible
PUPILS_FILE = 'participants.txt' #tab separated file: Surname Name Birthdate Class School
SCHOOL_ALIASES_FILES = 'alias.txt' #tab separated file: Main_name other_name other_name
RESULTS_FILE = 'seating.txt'

THRESHOLD_INCREASING_SPEED = 1/1000
SIZE_TRESHOLD = 4
ALEAS_DICT=None

def init_aleas_dict():
    global ALEAS_DICT
    ALEAS_DICT = dict()
    for l in open(SCHOOL_ALIASES_FILES):
        l = l.strip()
        if l.startswith('#'): # '#' means comment
            continue

        main_name = l.split('\t')[0]
        aliases = l.split('\t')[1:]

        ALEAS_DICT[main_name.lower()] = main_name
        for a in aliases:
            ALEAS_DICT[a.lower()] = main_name

def get_canonical_school_name(name):
    name = name.strip().lower()
    name = name.replace('№', '')
    name = name.replace('гбоу', '')
    name = name.replace('cош', '')
    name = name.replace('москва', '')
    name = name.replace('гимназия', '')
    name = name.strip()

    if ALEAS_DICT is None:
        init_aleas_dict()
    return ALEAS_DICT.get(name, name)

def normalize_name(str):
    return str.title()

class Participant:
    def __init__(self, data):
        self.data = data.strip()
        self.surname, self.name, self.burthdate, self.grade, self.school = self.data.split('\t')[:5]
        #self.grade - not number, but string - participant group label

        self.surname = normalize_name(self.surname)
        self.name = normalize_name(self.name)
        self.data_with_normalized_names = '\t'.join([self.surname, self.name] + self.data.split('\t')[2:])
        self.school = get_canonical_school_name(self.school)

def read_participants(file_name):
    participants = []
    for line in open(file_name, 'r'):
        if not line.strip().startswith('#'): # '#' means comment
            participants.append(Participant(line))

    return participants

class Room:
    def __init__(self, data):
        self.data = data.strip()
        self.grade, self.label, self.desks_count, self.are_desks_divisible = self.data.split('\t')[:4]
        #self.grade - not number, but string - participant group label

        self.desks_count = int(self.desks_count)
        self.are_desks_divisible = True if self.are_desks_divisible.lower()=='yes' else False

def read_rooms(file_name):
    rooms = []
    for line in open(file_name, 'r'):
        if not line.strip().startswith('#'): # '#' means comment
            rooms.append(Room(line))

    return rooms


def calculate_penalty(room, people_in_room):
    if people_in_room <= room.desks_count:
        penalty = people_in_room - room.desks_count

    else:
        if room.are_desks_divisible:
            coefficient = 1
        else:
            coefficient = 3
        penalty = coefficient * (people_in_room - room.desks_count)

    return penalty / room.desks_count

def log_rooms_counts(rooms, seating):
    people_counts = dict()
    for label, participants in seating.items():
        people_counts[label] = len(participants)
    for r in rooms:
        print("room %s: %d of %d people. Penalty is %f (desks are divisible = %s)" % (r.label, people_counts[r.label], r.desks_count, calculate_penalty(r, people_counts[r.label]), r.are_desks_divisible))


def calculate_rooms_people_counts(rooms, participants_count):
    people_counts = dict()
    labels = [r.label for r in rooms]
    for label in labels:
        people_counts[label] = 0

    for i in range(participants_count):
        #find most perspective room
        min_room_label, min_penalty = rooms[0].label, calculate_penalty(rooms[0], people_counts[rooms[0].label] + 1)
        for r in rooms:
            penalty = calculate_penalty(r, people_counts[r.label] + 1)
            if penalty < min_penalty:
                min_room_label, min_penalty = r.label, penalty

        people_counts[min_room_label] += 1

    return people_counts


def try_generating_seating(participants, rooms):
    seating = dict()
    counts = calculate_rooms_people_counts(rooms, len(participants))
    for r in rooms:
        seating[r.label] = []

    schools = set([p.school for p in participants])
    grouped_pupils = []
    for s in schools:
        grouped_pupils.append([p for p in participants if p.school == s])
        #print(s,'\t',len([p for p in participants if p.school == s])) #debug
    random.shuffle(grouped_pupils) #no random can lead to brother problem

    room_labels = [r.label for r in rooms]
    for group in grouped_pupils:
        random.shuffle(group)
        for p in group:
            room_with_least_people_share = sorted(room_labels, key=lambda label: len(seating[label])/counts[label])[0]
            seating[room_with_least_people_share].append(p)

    return seating

#seating is dict: room_label -> participants
def test_brothers(seating):
    for room_label, participants in seating.items():
        surnames = [p.surname for p in participants]
        surnames = sorted(surnames)
        for i in range(len(surnames) - 1):
            min_length = min(len(surnames[i]), len(surnames[i + 1]))
            if min_length >= 5:
                if surnames[i][:min_length - 2] == surnames[i + 1][:min_length - 2]:
                    #богатый, богатая
                    #print("similar", surnames[i], surnames[i+1])
                    return False
    return True

def generate_schools_list(seating):
    schools = set()
    for room_label, participants in seating.items():
        for p in participants:
            schools.add(p.school)
    return schools


def test_school_uniformness(seating, threshold):
    #seating is callsed school uniform if for every school exists no such pair of rooms A, B,
    #with a_share < b_share share of participants from this school in this rooms
    #that after moving threshold count of people from B to A, we have a_new_share < b_new_share

    schools = generate_schools_list(seating)
    for s in schools:
        min_shares = []
        max_shares = []
        for room_label, participants in seating.items():
            schools_in_room = [p.school for p in participants]
            min_shares.append((schools_in_room.count(s) - threshold) / len(schools_in_room))
            max_shares.append((schools_in_room.count(s) + threshold) / len(schools_in_room))

        if sorted(min_shares)[-1] > sorted(max_shares)[0]:
            return False

    return True

def test_is_ok(seating, threshold):
    return test_brothers(seating) and test_school_uniformness(seating, threshold)

def generate_seating(participant, rooms):
    iteration = 0
    threshold = 1
    seating = try_generating_seating(participant, rooms)
    while not test_is_ok(seating, threshold):
       seating = try_generating_seating(participant, rooms)
       iteration += 1
       threshold = 1 + iteration * THRESHOLD_INCREASING_SPEED

    print(test_brothers(seating))
    return seating, iteration + 1

def seating_to_string(seating):
    string = ""
    for room_label, participants in seating.items():
        for p in participants:
            string += room_label + '\t' + p.data_with_normalized_names + '\n'
    return string

def log_result(grade, seating, rooms, iteration):
    print("Result for grade %s is generated on %d iteration" % (grade, iteration))
    log_rooms_counts(rooms, seating)

def write_result(result):
    f = open(RESULTS_FILE, 'w')
    f.write(result)


def main():
    participants = read_participants(PUPILS_FILE)
    rooms = read_rooms(ROOMS_FILE)

    result = ""
    grades = set([p.grade for p in participants])
    for grade in grades:
        grade_rooms = [r for r in rooms if r.grade == grade]
        grade_participants = [p for p in participants if p.grade == grade]
        seating, iteration = generate_seating(grade_participants, grade_rooms)

        log_result(grade, seating, grade_rooms, iteration)

        result += seating_to_string(seating)

    write_result(result)

if __name__ == "__main__":
    main()


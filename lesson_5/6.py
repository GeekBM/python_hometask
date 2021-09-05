subj = {}
with open('test_6.txt', 'r') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'{subj}')

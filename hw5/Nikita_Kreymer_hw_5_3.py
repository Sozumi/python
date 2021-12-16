from itertools import zip_longest, islice

tutors = ['Василий', 'Светлана', 'Анастасия', 'Александр', 'Надежда', 'Людмила', 'Анатолий', 'Михаил', 'Мария']
klasses = ['9А', '10В', '10А', '11Б', '9Б', '10Б', '11А']
klass_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))

print(*islice(klass_gen, len(tutors)), sep='\n')

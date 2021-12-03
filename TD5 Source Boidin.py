from copy import deepcopy
import random
villes = ['Agadir',
          'Aj Hoœima',
          'Casablanca',
          'Ceuta',
          'El Jadida',
          'Erfoud',
          'Essaouira',
          'Fes',
          'Ksar es Souk',
          'Larache',
          'Marrakech',
          'Meknes',
          'Melilla',
          'Ouarzazate',
          'Oujda',
          'Rabat',
          'Safi',
          'Tanger',
          'Taroudannt',
          'Taza',
          'Tetouan',
          'Tiznlt',
          'Zagora']
dist = [[0, 1055, 520, 547, 425, 753, 174, 790, 685, 803, 306, 759, 1119, 337, 1130, 614, 308, 891, 81, 905, 906, 91, 545],
        [1055, 0, 560, 323, 654, 690, 914, 270, 590, 383, 755, 331, 167, 950, 271, 470, 813, 337, 981, 159, 281, 1152, 1118],
        [520, 560, 0, 431, 95, 596, 350, 293, 496, 286, 237, 233, 635, 440, 634, 93, 250, 371, 602, 409, 385, 612, 605],
        [547, 323, 431, 0, 523, 752, 784, 332, 641, 141, 667, 303, 480, 861, 576, 334, 678, 100, 1031, 447, 42, 1042, 1041],
        [425, 654, 95, 523, 0, 664, 254, 390, 695, 379, 199, 331, 732, 390, 730, 190, 152, 466, 505, 502, 482, 535, 563],
        [753, 690, 596, 752, 664, 0, 746, 421, 101, 580, 570, 441, 571, 378, 612, 539, 731, 677, 674, 580, 621, 835, 255],
        [174, 914, 350, 784, 254, 746, 0, 645, 671, 633, 170, 586, 982, 366, 984, 445, 138, 720, 254, 754, 739, 265, 534],
        [790, 270, 293, 332, 390, 421, 645, 0, 320, 216, 488, 60, 325, 678, 339, 200, 540, 325, 705, 116, 274, 881, 840],
        [685, 590, 496, 641, 695, 101, 671, 320, 0, 477, 499, 337, 471, 305, 533, 437, 657, 579, 605, 479, 512, 770, 358],
        [803, 383, 286, 141, 379, 580, 633, 216, 477, 0, 514, 182, 436, 706, 631, 192, 532, 88, 873, 332, 105, 890, 871],
        [306, 755, 237, 667, 199, 570, 170, 488, 499, 514, 0, 449, 808, 195, 823, 335, 157, 600, 226, 604, 842, 383, 360],
        [759, 331, 233, 303, 331, 441, 586, 60, 337, 182, 449, 0, 387, 647, 399, 140, 485, 279, 678, 175, 290, 831, 814],
        [1119, 167, 635, 480, 732, 571, 982, 325, 471, 436, 808, 387, 0, 1010, 156, 545, 887, 495, 1027, 205, 436, 1198, 845],
        [337, 950, 440, 861, 390, 378, 366, 678, 305, 706, 195, 647, 1010, 0, 1021, 517, 352, 788, 297, 793, 798, 465, 167],
        [1130, 271, 634, 576, 730, 612, 984, 339, 533, 631, 823, 399, 156, 1021, 0, 549, 893, 585, 1049, 225, 524, 1218, 878],
        [614, 470, 93, 334, 190, 539, 445, 200, 437, 192, 335, 140, 545, 517, 549, 0, 344, 276, 695, 316, 291, 705, 687],
        [308, 813, 250, 678, 152, 731, 138, 540, 657, 532, 157, 485, 887, 352, 893, 344, 0, 618, 388, 655, 638, 401, 530],
        [891, 337, 371, 100, 466, 677, 720, 325, 579, 88, 600, 279, 495, 788, 585, 276, 618, 0, 977, 443, 58, 986, 963],
        [81, 981, 602, 1031, 505, 674, 254, 705, 605, 873, 226, 678, 1027, 297, 1049, 695, 388, 977, 0, 814, 968, 158, 472],
        [905, 159, 409, 447, 502, 580, 754, 116, 479, 332, 604, 175, 205, 793, 225, 316, 655, 443, 814, 0, 398, 997, 855],
        [906, 281, 385, 42, 482, 621, 739, 274, 512, 105, 842, 290, 436, 798, 524, 291, 638, 58, 968, 398, 0, 991, 968],
        [91, 1152, 612, 1042, 535, 835, 265, 881, 770, 890, 383, 831, 1198, 465, 1218, 705, 401, 986, 158, 997, 991, 0, 625],
        [545, 1118, 605, 1041, 563, 255, 534, 840, 358, 871, 360, 814, 845, 167, 878, 687, 530, 963, 472, 855, 968, 625, 0]]

# initialisation des indivius.
population = 100
indiv = [[]]
for i in range(23):
    indiv[0].append(i)
for i in range(population - 1):
    indiv.append(deepcopy(indiv[0]))
for i in range(population):
    random.shuffle(indiv[i])
    indiv[i].append(indiv[i][0])

record = 0
stop = 0
while stop != 1:
    # Fitness.
    fit = []
    for i in range(population):
        traj = 0
        for j in range(23):
            traj += dist[indiv[i][j]][indiv[i][j + 1]]
        # print(i, 'Trajet : ', traj)
        fit.append(traj)
    # print('fit : ', fit)

    # Sélection.
    parents = []
    sfit = deepcopy(fit)
    sfit.sort()
    if record != sfit[1]:
        record = sfit[1]
    else:
        stop = 1
    # print('sfit : ', sfit)
    i = 0
    while len(parents) < 10:
        if fit.index(sfit[i]) not in parents:
            parents.append(fit.index(sfit[i]))
            i += 1
        else:
            i += 1
    print('Numéros des parents : ', parents, '\n')

    # Reproduction.
    enfants = []
    for i in range(10):
        for j in range(10):
            if i != j:
                enfants.append(indiv[parents[i]][:random.randint(0, 23)])
                for k in range(23):
                    if indiv[parents[j]][k] not in enfants[len(enfants) - 1]:
                        enfants[len(enfants) - 1].append(indiv[parents[j]][k])
                enfants[len(enfants) - 1].append(enfants[len(enfants) - 1][0])

    # Ajout d'individus "mutants".
    for i in range(3):  # Nombre de 3 individus mutants.
        random.shuffle(indiv[random.randint(0, population - 1)])

    # Nouvelle population.
    for i in range(len(parents)):
        indiv[i] = indiv[parents[i]]
    for i in range(len(enfants)):
        indiv[i + len(parents)] = enfants[i]

print('Meilleure fitness : ', record, 'km.')
print('Meilleur trajet trouvé : ')
for i in range(24):
    print(villes[indiv[parents[1]][i]])

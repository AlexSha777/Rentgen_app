head = []
abdominal_cavity = []

cervical = {
    "С1 позвонка": ["передней дуги", "задней дуги", "поперечного отростка", "латеральной массы", "заднего бугорка"],
    "С1 позвонка": ["передняя дуга", "задняя дуга", "поперечный отросток", "латеральная масса", "задний бугорок"],
    "С2 позвонка": ["тело", "зубовидный отросток", "поперечный отросток", "нижний суставной отросток", "остистый отросток"],
    "С3 позвонка": ["тело", "дуга", "поперечный отросток", "нижний суставной отросток", "верхний суставной отросток", "остистый отросток"],
    "С4 позвонка": ["тело", "дуга", "поперечный отросток", "нижний суставной отросток", "верхний суставной отросток", "остистый отросток"],
    "С5 позвонка": ["тело", "дуга", "поперечный отросток", "нижний суставной отросток", "верхний суставной отросток", "остистый отросток"],
    "С6 позвонка": ["тело", "дуга", "поперечный отросток", "нижний суставной отросток", "верхний суставной отросток", "остистый отросток"],
    "С7 позвонка": ["тело", "дуга", "поперечный отросток", "нижний суставной отросток", "верхний суставной отросток", "остистый отросток"],
}

cervical_artic = [
    "атлантозатылочного сустава",
    "латерального атлантоосевого сустава",
    "медиального атлантоосевого сустава",
    "дугоотростчатые суставы",
    "межпозвонкового диска"
]

thoracal = {
    "Th1 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th2 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th3 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th4 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th5 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th6 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th7 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th8 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th9 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th10 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th11 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
    "Th12 позвонка": ["тела", "ножки дуги", "пластинки дуги", "остистого отростка", "поперечного отростка", "верхнего суставного отростка"],
}

thoracal_artic = [
    "сустава головки ребра",
    "реберно-поперечного сустава",
    "дугоотростчатого сустава",
    "межпозвонкового диска"
]


lumbal = {
    "L1 позвонка": ["тела", "дужки", "остистого отростка", "поперечного отростка", "нижнего суставного отростка","верхнего суставного отростка"],
    "L2 позвонка": ["тела", "дужки", "остистого отростка", "поперечного отростка", "нижнего суставного отростка","верхнего суставного отростка"],
    "L3 позвонка": ["тела", "дужки", "остистого отростка", "поперечного отростка", "нижнего суставного отростка","верхнего суставного отростка"],
    "L4 позвонка": ["тела", "дужки", "остистого отростка", "поперечного отростка", "нижнего суставного отростка","верхнего суставного отростка"],
    "L5 позвонка": ["тела", "дужки", "остистого отростка", "поперечного отростка", "нижнего суставного отростка","верхнего суставного отростка"],
}

lumbal_artic = [
    "дугоотростчатого сустава",
    "межпозвонкового диска",
]


sacral_coc = {
    "крестца": ["боковой массы", "верхнего суставного отростка", "тела"], 
    "копчика": [],
}

sacral_coc_artic = [
    "крестцово-копчикового сустава",
    "крестцово-подвздошного сустава",
]

vertebra_cerv_segments = [
    "C1-C2 сегмента",
    "C2-C3 сегмента",
    "C3-C4 сегмента",
    "C5-C6 сегмента",
    "C6-C7 сегмента",
    "C7-Th1 сегмента",
]

vertebra_thor_segments = [
    "C7-Th1 сегмента",
    "Th1-Th2 сегмента",
    "Th2-Th3 сегмента",
    "Th3-Th4 сегмента",
    "Th4-Th5 сегмента",
    "Th5-Th6 сегмента",
    "Th6-Th7 сегмента",
    "Th7-Th8 сегмента",
    "Th9-Th10 сегмента",
    "Th10-Th11 сегмента",
    "Th11-Th12 сегмента",
    "Th12-L1 сегмента",
]

vertebra_lumb_segments = [
    "Th12-L1 сегмента",
    "L1-L2 сегмента",
    "L2-L3 сегмента",
    "L3-L4 сегмента",
    "L5-S1 сегмента",
]


thorax = {
    "грудины": ["тела", "рукоятки", "мечевидного отростка"],
    "I ребра":[], 
    "II ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "III ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "IV ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "V ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "VI ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "VII ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "VIII ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "IX ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "X ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "XI ребра": ["по ключичной линии", "по подмышечной линии", "по лопаточной линии", "по околопозвоночной линии"],
    "XII ребра":[],
}


pelvis = {
    "подвздошной кости": ["тела", "гребня", "крыла"],
    "лобковой кости": ["тела", "верхней ветви", "нижней ветви"],
    "седалищной кости": ["тела", "бугра", "ветви"],
    "вертлужной впадины": ["края", "передней колонны", "задней колонны"],
}

pelvis_artic = [
    "крестцово-подвздошного сочленения",
    "лобкового сочленения",
    "тазобедренного сустава",
]


up_extr = {
    "ключицы": ["акромиального конца", "диафиза", "стернального конца"],
    "лопатки": ["суставной поверхности", "шейки", "акромиона", "клювовидного отростка", "ости", "тела"],
    "плечевой кости": ["головки", "хирургической шейки", "большого бугорка", "малого бугорка", 
                        "верхней трети диафиза", "средней трети диафиза",
                        "нижней трети диафиза", "дистального метаэпифиза", 
                        "латерального надмыщелка", "медиального надмыщелка", 
                        "блока", "головчатого возвышения"],
    "лучевой кости": ["головки", "шейки", "бугристости", "проксимального метаэпифиза", 
                      "верхней трети диафиза", "средней трети диафиза", 
                      "нижней трети диафиза", "дистального метаэпифиза", 
                      "дистального эпифиза", "шиловидного отростка"],

    "локтевой кости": ["локтевого отростка", "венечного отростка",
                      "проксимального метаэпифиза", 
                      "верхней трети диафиза", "средней трети диафиза", 
                      "нижней трети диафиза", "дистального метаэпифиза", 
                      "дистального эпифиза",  "головки", "шиловидного отростка"],
}

up_extr_artic = [
    "грудиноключичного сочленения",
    "акромиальноключичного сочленения",
    "плечевого сустава",
    "локтевого сустава",
    "лучезапястного сустава",
    "проксимального лучелоктевого сочленения",
    "дистального лучелоктевого сочленения",
]


wrist_carpus = {
    "ладьевидной кости":[], 
    "полулунной кости":[],
    "трехгранной кости":[],
    "гороховидной кости":[],
    "кости трапеции":[],
    "трапециевидной кости":[],
    "головчатой кости":[],
    "крючковидной кости":[],
}

wrist_carpus_artic = [
    "лучезапястного сустава"
    "среднезапястного сустава",
    "запястнопястного сустава",
]

wrist_metacarpus = {
    "первой пястной кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "второй пястной кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "третьей пястной кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "четвертой пястной кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "пятой пястной кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
}

wrist_metacarpus_artic = [
    "запястнопястного сустава",
    "первого пястнофалангового сустава",
    "второго пястнофалангового сустава",
    "третьего пястнофалангового сустава",
    "четвертого пястнофалангового сустава",
    "пятого пястнофалангового сустава",
]



wrist_fingers = {
    "первого пальца ": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "второго пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                        {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                        {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "третьего пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "четвертого пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                           {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                           {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                          ],
    "пятого пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                       {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                       {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                      ],
}

wrist_fingers_artic = [
    "проксимального межфалангового сустава",
    "дистального межфалангового сустава",
    "межфалангового сустава",
]

wrist_segments = [
    "1 луча кисти",
    "2 луча кисти",
    "3 луча кисти",
    "4 луча кисти",
    "5 луча кисти",
    "1 пальца кисти",
    "2 пальца кисти",
    "3 пальца кисти",
    "4 пальца кисти",
    "5 пальца кисти",
]


low_extr = {
    "бедренной кости": ["головки", "шейки", "основания шейки", "большого вертела", "малого вертела", "межвертельной области", 
                        "чрезвертельной области", "верхней трети диафиза", "средней трети диафиза", "нижней трети диафиза", 
                        "дистального метаэпифиза", "дистального эпифиза", "латерального мыщелка", "медиального мыщелка", 
                        "надмыщелковой области", "медиального надмыщелка", "латерального надмыщелка"],
    "надколенника":[],
    "большеберцовой кости": ["латерального мыщелка", "медиального мыщелка", "межмыщелкового возвышения", "бугристости", "проксимального эпифиза", 
                         "проксимального метаэпифиза", "верхней трети диафиза", "средней трети диафиза", "нижней трети диафиза", 
                         "дистального метаэпифиза", "дистального эпифиза", "заднего края дистального метаэпифиза", "медиальной лодыжки", 
                         "малоберцовой вырезки дистального метаэпифиза"],
    "малоберцовой кости": ["верхушки головки", "головки", "шейки", "верхней трети диафиза", "средней трети диафиза", "нижней трети диафиза", 
                       "наружной лодыжки"],
}


low_extr_artic = [
    "крестцово-подвздошного сочленения",
    "лобкового сочленения",
    "тазобедренного сустава",
    "коленного сустава",
    "проксимального межберцового сочленения",
    "дистального межберцового сочленения",
    "голеностопного сустава",
    "подтаранного сустава"
]


foot_tar = {
    "таранной кости": ["тела", "шейки", "головки", "заднего отростка"],  
    "пяточной кости": ["бугра", "суставной поверхности"],
    "ладьевидной кости":[],
    "кубовидной кости":[],
    "медиальной клиновидной кости":[],
    "промежуточной клиновидной кости":[],
    "латеральной клиновидной кости":[],
    }


foot_tar_artic = [
    "голеностопного сустава"
    "подтаранного сустава",
    "таранноладьевидного сустава",
    "пяточнокубовидного сустава",
    "сустава Шопара",
    "клиновидноладьевидного сустава",
    "клиновиднокубовидного сустава",
]


foot_metatar = {
    "первой плюсневой кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки", 
                               "сесамовидной кости головки"],
    "второй плюсневой кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "третьей плюсневой кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "четвертой плюсневой кости": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"],
    "пятой плюсневой кость ": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки",  "головки"],
}

foot_metatar_artic = [
    "сустава Лисфранка",
    "первого плюснефалангового сустава",
    "второго плюснефалангового сустава",
    "третьего плюснефалангового сустава",
    "четвертого плюснефалангового сустава",
    "пятого плюснефалангового сустава",
]


foot_fingers = {
    "первого пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "второго пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                        {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                        {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "третьего пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                         {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                        ],
    "четвертого пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                           {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                           {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                          ],
    "пятого пальца": [{"проксимальной фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                       {"средней фаланги": ["основания", "проксимальной части диафиза", "дистальной части диафиза", "шейки", "головки"]},
                       {"дистальной фаланги": ["основания", "диафиза", "бугристости"]},
                      ],
}

foot_fingers_artic = [
    "проксимального межфалангового сустава",
    "дистального межфалангового сустава",
    "межфалангового сустава",
]

foot_segments = [
    "1 луча стопы",
    "2 луча стопы",
    "3 луча стопы",
    "4 луча стопы",
    "5 луча стопы",
    "1 пальца стопы",
    "2 пальца стопы",
    "3 пальца стопы",
    "4 пальца стопы",
    "5 пальца стопы",
]
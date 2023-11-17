from bone_localization import *


rent_zones = [
"черепа",
"шейного отдела позвоночника",
"грудного отдела позвоночника",
"грудо-поясничного отдела позвоночника",
"поясничного отдела позвоночника",
"пояснично-крестцового отдела позвоночника",
"крестцового отдела позвоночника",
"грудной клетки",
"грудины",
"брюшной полости",
"таза",
"ключицы",
"лопатки",
"плечевого сустава",
"плечевой кости",
"локтевого сустава",
"предплечья",
"лучезапястного сустава",
"кисти",
"пальцев кисти",
"тазобедренного сустава",
"бедренной кости",
"коленного сустава",
"голени",
"голеностопного сустава",
"стопы",
"пальцев стопы"
]


def new_list_formation(*args):
    new_list = []
    for arg in args:
        for element in arg:
            new_list.append(element)

    return new_list

def new_dict_formation(*args):
    new_dict = {}
    for arg in args:
        new_dict.update(arg)
        
    return new_dict



rent_zones_bone_loc = {
"черепа": [[], head, []],
"шейного отдела позвоночника":[cervical_artic, cervical, vertebra_cerv_segments],
"грудного отдела позвоночника": [thoracal_artic, thoracal, vertebra_thor_segments ],
"грудо-поясничного отдела позвоночника": [
                                           new_list_formation(thoracal_artic.copy(),lumbal_artic.copy()), 
                                           new_dict_formation(thoracal.copy(), lumbal.copy()), 
                                           
                                           new_list_formation(vertebra_thor_segments.copy(),vertebra_lumb_segments.copy())
                                         ],
"поясничного отдела позвоночника": [lumbal_artic, lumbal, vertebra_lumb_segments],
"пояснично-крестцового отдела позвоночника": [
                                               new_list_formation(lumbal_artic.copy(),sacral_coc_artic.copy()), 
                                               new_dict_formation(lumbal.copy(), sacral_coc.copy()),
                                               [],
                                             ],
"крестцового отдела позвоночника": [sacral_coc_artic, sacral_coc, [] ],

"грудной клетки": [[],thorax,[]],
"грудины": [[up_extr_artic[0]],thorax,[]],
"брюшной полости": [[],abdominal_cavity,[]],
"таза": [pelvis_artic, pelvis, []],

"ключицы": [up_extr_artic[:3], up_extr, []],
"лопатки": [up_extr_artic[:3], up_extr, []],
"плечевого сустава": [up_extr_artic[:3], up_extr, []],
"плечевой кости": [up_extr_artic[:4], up_extr, []],
"локтевого сустава": [[up_extr_artic[3]],up_extr, []],
"предплечья": [up_extr_artic[3:5], up_extr, []],
"лучезапястного сустава": [up_extr_artic[4:], up_extr, []],

"кисти": [new_list_formation(wrist_carpus_artic, wrist_metacarpus_artic, wrist_fingers_artic), 
          new_dict_formation(wrist_carpus, wrist_metacarpus,wrist_fingers), 
          wrist_segments,
         ],

"пальцев кисти": [wrist_fingers_artic, wrist_fingers, wrist_segments],

"тазобедренного сустава": [low_extr_artic[:3], low_extr, []],
"бедренной кости": [low_extr_artic [:4], low_extr, []],
"коленного сустава": [low_extr_artic[3:5], low_extr, []],
"голени": [low_extr_artic[3:7], low_extr, []],
"голеностопного сустава": [foot_tar_artic, 
                           new_dict_formation(low_extr, foot_tar),
                           [],
                          ],
"стопы": [new_list_formation(foot_tar_artic, foot_metatar_artic, foot_fingers_artic), 
          new_dict_formation(foot_tar, foot_metatar, foot_fingers), 
          foot_segments,
         ],
"пальцев стопы": [new_list_formation(foot_metatar_artic, foot_fingers_artic), 
                  new_dict_formation(foot_metatar, foot_fingers),
                  foot_segments,
                 ] 
}


#for k, v in rent_zones_bone_loc.items():
#    print(type(v),k)
#    print("...")
#    for i in v:
#        print(type(i))
#    print("...")
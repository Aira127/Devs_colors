file = open("sapphire.txt").read().split()
array = []
for unedit in file:
  edit = unedit[3:5] + unedit[6:] + "999"
  array.append(edit)
to_copy = f''' 
    "TUT_MOVEMENT": [
        {array[0]}
    ],
    "TUT_SHOOTINGRANGE": [
        {array[1]}
    ],
    "SLUGGER": [
        {array[2]}
    ],
    "TUT_FROG": [
        {array[3]}
    ],
    "TUT_JUMP": [
        {array[4]}
    ],
    "GRID_TUT_BALLOON": [
        {array[5]}
    ],
    "TUT_BOMB2": [
        {array[6]}
    ],
    "TUT_BOMBJUMP": [
        {array[7]}
    ],
    "TUT_FASTTRACK": [
        {array[8]}
    ],
    "GRID_PORT": [
        {array[9]}
    ],
    "GRID_PAGODA": [
        {array[10]}
    ],
    "TUT_RIFLE": [
        {array[11]}
    ],
    "TUT_RIFLEJOCK": [
        {array[12]}
    ],
    "TUT_DASHENEMY": [
        {array[13]}
    ],
    "GRID_JUMPDASH": [
        {array[14]}
    ],
    "GRID_SMACKDOWN": [
        {array[15]}
    ],
    "GRID_MEATY_BALLOONS": [
        {array[16]}
    ],
    "GRID_FAST_BALLOON": [
        {array[17]}
    ],
    "GRID_DRAGON2": [
        {array[18]}
    ],
    "GRID_DASHDANCE": [
        {array[19]}
    ],
    "TUT_GUARDIAN": [
        {array[20]}
    ],
    "TUT_UZI": [
        {array[21]}
    ],
    "TUT_JUMPER": [
        {array[22]}
    ],
    "TUT_BOMB": [
        {array[23]}
    ],
    "GRID_DESCEND": [
        {array[24]}
    ],
    "GRID_STAMPEROUT": [
        {array[25]}
    ],
    "GRID_CRUISE": [
        {array[26]}
    ],
    "GRID_SPRINT": [
        {array[27]}
    ],
    "GRID_MOUNTAIN": [
        {array[28]}
    ],
    "GRID_SUPERKINETIC": [
        {array[29]}
    ],
    "GRID_ARRIVAL": [
        {array[30]}
    ],
    "FLOATING": [
        {array[31]}
    ],
    "GRID_BOSS_YELLOW": [
        {array[32]}
    ],
    "GRID_HOPHOP": [
        {array[33]}
    ],
    "GRID_RINGER_TUTORIAL": [
        {array[34]}
    ],
    "GRID_RINGER_EXPLORATION": [
        {array[35]}
    ],
    "GRID_HOPSCOTCH": [
        {array[36]}
    ],
    "GRID_BOOM": [
        {array[37]}
    ],
    "GRID_SNAKE_IN_MY_BOOT": [
        {array[38]}
    ],
    "GRID_FLOCK": [
        {array[39]}
    ],
    "GRID_BOMBS_AHOY": [
        {array[40]}
    ],
    "GRID_ARCS": [
        {array[41]}
    ],
    "GRID_APARTMENT": [
        {array[42]}
    ],
    "TUT_TRIPWIRE": [
        {array[43]}
    ],
    "GRID_TANGLED": [
        {array[44]}
    ],
    "GRID_HUNT": [
        {array[45]}
    ],
    "GRID_CANNONS": [
        {array[46]}
    ],
    "GRID_FALLING": [
        {array[47]}
    ],
    "TUT_SHOCKER2": [
        {array[48]}
    ],
    "TUT_SHOCKER": [
        {array[49]}
    ],
    "GRID_PREPARE": [
        {array[50]}
    ],
    "GRID_TRIPMAZE": [
        {array[51]}
    ],
    "GRID_RACE": [
        {array[52]}
    ],
    "TUT_FORCEFIELD2": [
        {array[53]}
    ],
    "GRID_SHIELD": [
        {array[54]}
    ],
    "SA L VAGE2": [
        {array[55]}
    ],
    "GRID_VERTICAL": [
        {array[56]}
    ],
    "GRID_MINEFIELD": [
        {array[57]}
    ],
    "TUT_MIMIC": [
        {array[58]}
    ],
    "GRID_MIMICPOP": [
        {array[59]}
    ],
    "GRID_SWARM": [
        {array[60]}
    ],
    "GRID_SWITCH": [
        {array[61]}
    ],
    "GRID_TRAPS2": [
        {array[62]}
    ],
    "TUT_ROCKETJUMP": [
        {array[63]}
    ],
    "TUT_ZIPLINE": [
        {array[64]}
    ],
    "GRID_CLIMBANG": [
        {array[65]}
    ],
    "GRID_ROCKETUZI": [
        {array[66]}
    ],
    "GRID_CRASHLAND": [
        {array[67]}
    ],
    "GRID_ESCALATE": [
        {array[68]}
    ],
    "GRID_SPIDERCLAUS": [
        {array[69]}
    ],
    "GRID_FIRECRACKER_2": [
        {array[70]}
    ],
    "GRID_SPIDERMAN": [
        {array[71]}
    ],
    "GRID_DESTRUCTION": [
        {array[72]}
    ],
    "GRID_HEAT": [
        {array[73]}
    ],
    "GRID_BOLT": [
        {array[74]}
    ],
    "GRID_PON": [
        {array[75]}
    ],
    "GRID_CHARGE": [
        {array[76]}
    ],
    "GRID_MIMICFINALE": [
        {array[77]}
    ],
    "GRID_BARRAGE": [
        {array[78]}
    ],
    "GRID_1GUN": [
        {array[79]}
    ],
    "GRID_HECK": [
        {array[80]}
    ],
    "GRID_ANTFARM": [
        {array[81]}
    ],
    "GRID_FORTRESS": [
        {array[82]}
    ],
    "GRID_GODTEMPLE_ENTRY": [
        {array[83]}
    ],
    "GRID_BOSS_GODSDEATHTEMPLE": [
        {array[84]}
    ],
    "GRID_EXTERMINATOR": [
        {array[85]}
    ],
    "GRID_FEVER": [
        {array[86]}
    ],
    "GRID_SKIPSLIDE": [
        {array[87]}
    ],
    "GRID_CLOSER": [
        {array[88]}
    ],
    "GRID_HIKE": [
        {array[89]}
    ],
    "GRID_SKIP": [
        {array[90]}
    ],
    "GRID_CEILING": [
        {array[91]}
    ],
    "GRID_BOOP": [
        {array[92]}
    ],
    "GRID_TRIPRAP": [
        {array[93]}
    ],
    "GRID_ZIPRAP": [
        {array[94]}
    ],
    "TUT_ORIGIN": [
        {array[95]}
    ],
    "GRID_BOSS_RAPTURE": [
        {array[96]}
    ],
    "SIDEQUEST_OBSTACLE_PISTOL": [
        {array[97]}
    ],
    "SIDEQUEST_OBSTACLE_PISTOL_SHOOT": [
        {array[98]}
    ],
    "SIDEQUEST_OBSTACLE_MACHINEGUN": [
        {array[99]}
    ],
    "SIDEQUEST_OBSTACLE_RIFLE_2": [
        {array[100]}
    ],
    "SIDEQUEST_OBSTACLE_UZI2": [
        {array[101]}
    ],
    "SIDEQUEST_OBSTACLE_SHOTGUN": [
        {array[102]}
    ],
    "SIDEQUEST_OBSTACLE_ROCKETLAUNCHER": [
        {array[103]}
    ],
    "SIDEQUEST_RAPTURE_QUEST": [
        {array[104]}
    ],
    "SIDEQUEST_DODGER": [
        {array[105]}
    ],
    "GRID_GLASSPATH": [
        {array[106]}
    ],
    "GRID_GLASSPATH2": [
        {array[107]}
    ],
    "GRID_HELLVATOR": [
        {array[108]}
    ],
    "GRID_GLASSPATH3": [
        {array[109]}
    ],
    "SIDEQUEST_ALL_SEEING_EYE": [
        {array[110]}
    ],
    "SIDEQUEST_RESIDENTSAWB": [
        {array[111]}
    ],
    "SIDEQUEST_RESIDENTSAW": [
        {array[112]}
    ],
    "SIDEQUEST_SUNSET_FLIP_POWERBOMB": [
        {array[113]}
    ],
    "GRID_BALLOONLAIR": [
        {array[114]}
    ],
    "SIDEQUEST_BARREL_CLIMB": [
        {array[115]}
    ],
    "SIDEQUEST_FISHERMAN_SUPLEX": [
        {array[116]}
    ],
    "SIDEQUEST_STF": [
        {array[117]}
    ],
    "SIDEQUEST_ARENASIXNINE": [
        {array[118]}
    ],
    "SIDEQUEST_ATTITUDE_ADJUSTMENT": [
        {array[119]}
    ],
    "SIDEQUEST_ROCKETGODZ": [
        {array[120]}
    ] 
'''

print(to_copy)
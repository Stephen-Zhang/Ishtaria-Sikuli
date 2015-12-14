from sikuli import *

class Map(object):
    normal = []
    armored = []
    strong = []
    boss = []

class Map1(Map):
    normal = [
        Pattern("skeleton_null.png").similar(0.80),"skeleton_red.png","skeleton_blue.png","gargoyle_blue.png","gargoyle_null.png","gargoyle_green.png","gargoyle_red.png",Pattern("cat_null.png").similar(0.80),"savage_null.png","savage_green.png",Pattern("wolf_blue.png").similar(0.80),Pattern("wolf_red.png").similar(0.80),Pattern("wolf_null.png").similar(0.80),"wizard_null.png","wizard_null_2.png","bat_null.png"
    ]
    armored = [
        Pattern("armor_null.png").similar(0.80)
    ]
    strong = [
        Pattern("garm_null.png").similar(0.80)
    ]
    boss = [
        Pattern("boss_1_stage_1.png").similar(0.69),Pattern("boss_1_stage_2.png").similar(0.69),Pattern("boss_1_stage_3.png").similar(0.69),
    ]
class Map2(Map):
    normal = [
        "gargoyle_blue.png",Pattern("wolf_blue.png").similar(0.80),"skeleton_blue.png","savage_blue.png","wolf_red.png","cat_blue.png","bat_green.png","bee_blue.png","frog_null.png","savage_red.png",Pattern("snake_null.png").similar(0.69),"savage_null.png","savage_green.png"
    ]
    armored = [
        Pattern("crab_null.png").similar(0.80),Pattern("scorpion_blue.png").similar(0.80)
    ]
    strong = [
        Pattern("garm_null.png").similar(0.80)
    ]
    boss = [
        Pattern("boss_2_stage_1.png").similar(0.60),Pattern("boss_2_stage_2.png").similar(0.60),Pattern("boss_2_stage_3.png").similar(0.69),Pattern("boss_2_stage_4.png").similar(0.69)
    ]
class Map3(Map):
    normal = [
        "savage_red.png","frog_green.png","skeleton_red.png","wolf_green.png",Pattern("snake_red.png").similar(0.80),"bat_green.png","bat_blue.png",Pattern("chicken_null.png").similar(0.80),"gargoyle_red.png","frog_blue.png","frog_red.png","frog_null.png",Pattern("bee_red.png").similar(0.80),"bat_red.png","cat_red.png"
    ]
    armored = [
        Pattern("crab_green.png").similar(0.80),Pattern("crab_null.png").similar(0.80),"turtle_null.png"
    ]
    strong = [
        Pattern("big_dog_red.png").similar(0.80),Pattern("liger_red.png").similar(0.80)
    ]
    boss = [
        Pattern("boss_3_stage_1.png").similar(0.80),Pattern("boss_3_stage_2.png").similar(0.80),Pattern("boss_3_stage_3.png").similar(0.80),Pattern("boss_3_stage_4.png").similar(0.80)
    ]
class Map4(Map):
    normal = [
        
    ]
    armored = [
        
    ]
    strong = [
        "big_dog_green.png"
    ]
    boss = [
        
    ]
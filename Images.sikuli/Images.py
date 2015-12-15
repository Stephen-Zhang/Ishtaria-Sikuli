from sikuli import *

class Map(object):
    normal = []
    armored = []
    strong = []
    boss = []

class Map1(Map):
    normal = [
        "skeleton_null.png",
        "skeleton_red.png",
        "skeleton_blue.png",
        "gargoyle_blue.png",
        "gargoyle_null.png",
        "gargoyle_green.png",
        "gargoyle_red.png",
        "cat_null.png",
        "savage_null.png",
        "savage_green.png",
        "wolf_blue.png",
        "wolf_red.png",
        "wolf_null.png",
        "wizard_null.png",
        "wizard_null_2.png",
        "bat_null.png"
    ]
    armored = [
        "armor_null.png"
    ]
    strong = [
        "garm_null.png"
    ]
    boss = [
        Pattern("boss_1_stage_1.png").similar(0.69),
        Pattern("boss_1_stage_2.png").similar(0.69),
        Pattern("boss_1_stage_3.png").similar(0.69)
    ]
class Map2(Map):
    normal = [
        "gargoyle_blue.png",
        "wolf_blue.png",
        "skeleton_blue.png",
        "savage_blue.png",
        "wolf_red.png",
        "cat_blue.png",
        "bat_green.png",
        "bee_blue.png",
        "frog_null.png",
        "savage_red.png",
        "snake_null.png",
        "savage_null.png",
        "savage_green.png"
    ]
    armored = [
        "crab_null.png",
        "scorpion_blue.png"
    ]
    strong = [
        "garm_null.png"
    ]
    boss = [
        Pattern("boss_2_stage_1.png").similar(0.60),
        Pattern("boss_2_stage_2.png").similar(0.60),
        Pattern("boss_2_stage_3.png").similar(0.69),
        Pattern("boss_2_stage_4.png").similar(0.69)
    ]
class Map3(Map):
    normal = [
        "savage_red.png",
        "frog_green.png",
        "skeleton_red.png",
        "wolf_green.png",
        "snake_red.png",
        "bat_green.png",
        "bat_blue.png",
        "chicken_null.png",
        "gargoyle_red.png",
        "frog_blue.png",
        "frog_red.png",
        "frog_null.png",
        "bee_red.png",
        "bat_red.png",
        "cat_red.png"
    ]
    armored = [
        "crab_green.png",
        "crab_null.png",
        "turtle_null.png"
    ]
    strong = [
        "big_dog_red.png",
        "liger_red.png"
    ]
    boss = [
        Pattern("boss_3_stage_1.png").similar(0.80),
        Pattern("boss_3_stage_2.png").similar(0.80),
        Pattern("boss_3_stage_3.png").similar(0.80),
        Pattern("boss_3_stage_4.png").similar(0.80)
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
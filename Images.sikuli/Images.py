from sikuli import *

class Map(object):
    normal = []
    armored = []
    strong = []
    boss = []
    lions = [
        "blue_lion_2.png", "red_lion_2.png", "green_lion_2.png", "null_lion_2.png"
    ] 

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
        "garm_red.png"
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
        "garm_red.png"
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
        "frog_green.png",
        "snake_green.png",
        "bee_null.png",
        "wolf_blue.png",
        "chicken_red.png",
        "chicken_green.png",
        "bee_green.png",
        "savage_green.png", "savage_blue.png", "cat_green.png", "skeleton_green.png"
        
    ]
    armored = [
        "armor_null.png",
        "turtle_green.png", "scorpion_red.png", "crab_null.png"
    ]
    strong = [
        "big_dog_green.png", "reaper_null.png", "garm_blue.png"
    ]
    boss = [
        Pattern("boss_4_stage_1.png").similar(0.80),
        Pattern("boss_4_stage_2.png").similar(0.80),
        Pattern("boss_4_stage_3.png").similar(0.80),
        Pattern("boss_4_stage_4.png").similar(0.80)
    ]

class Map5(Map):
    normal = [
        "wolf_red.png",
        "frog_null.png",
        "bee_blue.png",
        "chicken_blue.png",
        "skeleton_blue.png",    
        "skeleton_red.png"
        "snake_blue.png",
        "cat_blue.png",
        "bat_blue.png",
        "cat_red.png", "cat_green.png", "cat_null.png"
        "boss_5_mob.png"
    ]
    armored = [
        "crab_blue.png", "crab_green.png",
        "turtle_blue.png"
        "scorpion_green.png"
    ]
    
    strong = [
        "big_dog_blue.png",
        "liger_blue.png",
        "garm_green.png",
        "minotaur_red_null.png"
    ]
    
    boss = [
        Pattern("boss_5_stage_1.png").similar(0.80),
        Pattern("boss_5_stage_2.png").similar(0.80),
        Pattern("boss_5_stage_3.png").similar(0.80),
        Pattern("boss_5_stage_4.png").similar(0.80)
    ]

class Map6(Map):
    normal = [
        "snake_green.png",
        "savage_red.png",
        "skeleton_null.png",
        "gargoyle_null.png",
        "bee_green.png",
        "bat_blue.png",
        "gargoyle_blue.png",
        "bat_green.png",
        "gargoyle_green.png",
        "gargoyle_red.png"
    ]
    armored = [
        "turtle_red.png",
        "armor_null.png",
        "armored_purple_null.png",
        "scorpion_null.png",
        "crab_red.png"
    ]
    strong = [
        "big_dog_green.png",
        "garm_blue.png",
        "big_dog_null.png",
        "garm_red.png",
        "reaper_null.png",
        "minotaur_blue_null.png",
        "reaper_red_null.png",
        "big_dog_red.png",
        "big_dog_blue.png",
        "garm_null.png",
        "liger_null.png"
    ]
    boss = [
        Pattern("boss_6_stage_1.png").similar(0.80),
        Pattern("boss_6_stage_2.png").similar(0.80),
        Pattern("boss_6_stage_3.png").similar(0.80),
        Pattern("boss_6_stage_4.png").similar(0.80)
    ]

class Map7(Map):
    normal = [
        "snake_red.png",
        "snake_green.png",
        "chicken_red.png",
        "chicken_null.png",
        "crow_red.png",
        "crow_green.png",
        "savage_null.png",
        "savage_red.png",
        "skeleton_red.png",
        "crow_null.png",
        "wolf_blue.png",
        "wold_red.png"
    ]
    armored = [
        "scorpion_green.png",
        "scorpion_red.png",
        "scorpion_null.png",
        "turtle_null.png"
    ]
    strong = [
        "worm_null.png",
        "worm_red.png",
        "liger_red.png",
        "big_dog_null.png",
        "big_dog_red.png",
        "liger_null.png",
        "minotaur_blue_null.png",
        "minotaur_red_null.png"
    ]
    boss = [
        "stage_7_boss_1.png", "stage_7_boss_2.png", "stage_7_boss_3.png"
    ]
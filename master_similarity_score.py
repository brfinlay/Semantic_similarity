import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import rpy2

master_list = ['airplane', 'ambulance', 'angel', 'ant', 'anvil', 'apple', 'arm', 'asparagus', 'axe', 'backpack', 'banana', 'bandage', 'barn', 'baseball', 'basket', 'basketball', 'bat', 'bathtub', 'beach', 'bear', 'beard', 'bed', 'bee', 'belt', 'bench', 'bicycle', 'binoculars', 'bird', 'blackberry', 'blueberry', 'book', 'boomerang', 'bowtie', 'bracelet', 'brain', 'bread', 'bridge', 'broccoli', 'broom', 'bucket', 'bulldozer', 'bus', 'bush', 'butterfly', 'cactus', 'cake', 'calculator', 'calendar', 'camel', 'camera', 'camouflage', 'campfire', 'candle', 'cannon', 'canoe', 'car', 'carrot', 'castle', 'cat', 'cello', 'chair', 'chandelier', 'church', 'circle', 'clarinet', 'clock', 'cloud', 'compass', 'computer', 'cookie', 'cooler', 'couch', 'cow', 'crab', 'crayon', 'crocodile', 'crown', 'cup', 'diamond', 'dishwasher', 'dog', 'dolphin', 'door', 'dragon', 'dresser', 'drill', 'duck', 'dumbbell', 'ear', 'elbow', 'elephant', 'envelope', 'eraser', 'eye', 'eyeglasses', 'face', 'fan', 'feather', 'fence', 'finger', 'fireplace', 'firetruck', 'fish', 'flamingo', 'flashlight', 'flower', 'foot', 'fork', 'frog', 'garden', 'giraffe', 'goatee', 'grass', 'guitar', 'hamburger', 'hammer', 'hand', 'harp', 'hat', 'headphones', 'hedgehog', 'helicopter', 'helmet', 'hexagon', 'horse', 'hospital', 'hourglass', 'house', 'hurricane', 'jacket', 'jail', 'kangaroo', 'key', 'keyboard', 'knee', 'knife', 'ladder', 'lantern', 'laptop', 'leaf', 'leg', 'lighter', 'lighthouse', 'lightning', 'line', 'lion', 'lipstick', 'lobster', 'lollipop', 'mailbox', 'map', 'marker', 'megaphone', 'mermaid', 'microphone', 'microwave', 'monkey', 'moon', 'mosquito', 'motorbike', 'mountain', 'mouse', 'moustache', 'mouth', 'mug', 'mushroom', 'nail', 'necklace', 'nose', 'ocean', 'octagon', 'octopus', 'onion', 'oven', 'owl', 'paintbrush', 'panda', 'pants', 'parachute', 'parrot', 'passport', 'peanut', 'pear', 'pencil', 'penguin', 'piano', 'pig', 'pillow', 'pineapple', 'pizza', 'pliers', 'pond', 'pool', 'popsicle', 'postcard', 'potato', 'purse', 'rabbit', 'raccoon', 'radio', 'rain', 'rainbow', 'rake', 'rhinoceros', 'rifle', 'river', 'sailboat', 'sandwich', 'saw', 'saxophone', 'scissors', 'scorpion', 'screwdriver', 'shark', 'sheep', 'shoe', 'shorts', 'shovel', 'sink', 'skateboard', 'skull', 'skyscraper', 'snail', 'snake', 'snorkel', 'snowflake', 'snowman', 'sock', 'speedboat', 'spider', 'spoon', 'spreadsheet', 'square', 'squiggle', 'squirrel', 'stairs', 'star', 'steak', 'stereo', 'stethoscope', 'stove', 'strawberry', 'streetlight', 'submarine', 'suitcase', 'sun', 'swan', 'sweater', 'swing', 'sword', 'syringe', 'table', 'teapot', 'telephone', 'television', 'tent', 'tiger', 'toaster', 'toe', 'toilet', 'tooth', 'toothbrush', 'toothpaste', 'tornado', 'tractor', 'train', 'tree', 'triangle', 'trombone', 'truck', 'trumpet', 'umbrella', 'underwear', 'van', 'vase', 'violin', 'watermelon', 'whale', 'wheel', 'windmill', 'wristwatch', 'yoga', 'zebra', 'zigzag']

def get_synset(a_list):
    synset_list = []
    for word in a_list:
        a = wn.synsets(word)[:1] 
        synset_list.append(a)
    return synset_list
master_synsets = get_synset(master_list)


def wn_syns(given_list): 
       synset_wn = []
       for word in given_list:
           synset_wn.append("wn.[%s]" % word)
       return synset_wn
master_wn = wn_syns(master_synsets)


def lower(list):
    new_list = []
    for word in list:
        new_list.append(word.lower())
    return new_list
lower_m = lower(master_wn)


def clean(a_list): 
    new_list = []
    for word in a_list:
        w = word.replace("[", "").replace("]", "").replace("wn.synset", "").replace("(", "").replace(")", "").replace("'", "")
        new_list.append(w)
    return new_list
clean_m = clean(lower_m)


# Assigning Variables to correct synsets found in 'master_definitions&synsets.py'
syn_airplane = wn.synset('airplane.n.01')
syn_ambulance = wn.synset('ambulance.n.01')
syn_angel = wn.synset('angel.n.01')
syn_ant = wn.synset('ant.n.01')
syn_anvil = wn.synset('anvil.n.01')
syn_apple = wn.synset('apple.n.01')
syn_arm = wn.synset('arm.n.01')
syn_asparagus = wn.synset('asparagus.n.01')
syn_axe = wn.synset('ax.n.01')
syn_backpack = wn.synset('backpack.n.01')
syn_banana = wn.synset('banana.n.01')
syn_bandage = wn.synset('bandage.n.01')
syn_barn = wn.synset('barn.n.01')
syn_baseball = wn.synset('baseball.n.01')
syn_basket = wn.synset('basket.n.01')
syn_basketball = wn.synset('basketball.n.01')
syn_bat = wn.synset('bat.n.01')
syn_bathtub = wn.synset('bathtub.n.01')
syn_beach = wn.synset('beach.n.01')
syn_bear = wn.synset('bear.n.01')
syn_beard = wn.synset('beard.n.01')
syn_bed = wn.synset('bed.n.01')
syn_bee = wn.synset('bee.n.01')
syn_belt = wn.synset('belt.n.01')
syn_bench = wn.synset('bench.n.01')
syn_bicycle = wn.synset('bicycle.n.01')
syn_binoculars = wn.synset('binoculars.n.01')
syn_bird = wn.synset('bird.n.01')
syn_blackberry = wn.synset('blackberry.n.01')
syn_blueberry = wn.synset('blueberry.n.01')
syn_book = wn.synset('book.n.01')
syn_boomerang = wn.synset('boomerang.n.01')
syn_bowtie = wn.synset('bow_tie.n.01')
syn_bracelet = wn.synset('watchband.n.01')
syn_brain = wn.synset('brain.n.01')
syn_bread = wn.synset('bread.n.01')
syn_bridge = wn.synset('bridge.n.01')
syn_broccoli = wn.synset('broccoli.n.01')
syn_broom = wn.synset('broom.n.01')
syn_bucket = wn.synset('bucket.n.01')
syn_bulldozer = wn.synset('bulldozer.n.01')
syn_bus = wn.synset('bus.n.01')
syn_bush = wn.synset('shrub.n.01')
syn_butterfly = wn.synset('butterfly.n.01')
syn_cactus = wn.synset('cactus.n.01')
syn_cake = wn.synset('cake.n.03')
syn_calculator = wn.synset('calculator.n.01')
syn_calendar = wn.synset('calendar.n.01')
syn_camel = wn.synset('camel.n.01')
syn_camera = wn.synset('camera.n.01')
syn_camouflage = wn.synset('disguise.n.01')
syn_campfire = wn.synset('campfire.n.01')
syn_candle = wn.synset('candle.n.01')
syn_cannon = wn.synset('cannon.n.01')
syn_canoe = wn.synset('canoe.n.01')
syn_car = wn.synset('car.n.01')
syn_carrot = wn.synset('carrot.n.01')
syn_castle = wn.synset('palace.n.01')
syn_cat = wn.synset('cat.n.01')
syn_cello = wn.synset('cello.n.01')
syn_chair = wn.synset('chair.n.01')
syn_chandelier = wn.synset('chandelier.n.01')
syn_church = wn.synset('church.n.02')
syn_circle = wn.synset('circle.n.01')
syn_clarinet = wn.synset('clarinet.n.01')
syn_clock = wn.synset('clock.n.01')
syn_cloud = wn.synset('cloud.n.01')
syn_compass = wn.synset('compass.n.01')
syn_computer = wn.synset('computer.n.01')
syn_cookie = wn.synset('cookie.n.01')
syn_cooler = wn.synset('cooler.n.01')
syn_couch = wn.synset('sofa.n.01')
syn_cow = wn.synset('cow.n.01')
syn_crab = wn.synset('crab.n.01')
syn_crayon = wn.synset('crayon.n.01')
syn_crocodile = wn.synset('crocodile.n.01')
syn_crown = wn.synset('crown.n.01')
syn_cup = wn.synset('cup.n.01')
syn_diamond = wn.synset('diamond.n.01')
syn_dishwasher = wn.synset('dishwasher.n.01')
syn_dog = wn.synset('dog.n.01')
syn_dolphin = wn.synset('dolphin.n.02')
syn_door = wn.synset('door.n.01')
syn_dragon = wn.synset('dragon.n.01')
syn_dresser = wn.synset('chest_of_drawers.n.01')
syn_drill = wn.synset('drill.n.01')
syn_duck = wn.synset('duck.n.01')
syn_dumbbell = wn.synset('dumbbell.n.01')
syn_ear = wn.synset('ear.n.01')
syn_elbow = wn.synset('elbow.n.01')
syn_elephant = wn.synset('elephant.n.01')
syn_envelope = wn.synset('envelope.n.01')
syn_eraser = wn.synset('eraser.n.01')
syn_eye = wn.synset('eye.n.01')
syn_eyeglasses = wn.synset('spectacles.n.01')
syn_face = wn.synset('face.n.01')
syn_fan = wn.synset('fan.n.01')
syn_feather = wn.synset('feather.n.01')
syn_fence = wn.synset('fence.n.01')
syn_finger = wn.synset('finger.n.01')
syn_fireplace = wn.synset('fireplace.n.01')
syn_fish = wn.synset('fish.n.01')
syn_flamingo = wn.synset('flamingo.n.01')
syn_flashlight = wn.synset('flashlight.n.01')
syn_flower = wn.synset('flower.n.01')
syn_foot = wn.synset('foot.n.01')
syn_fork = wn.synset('fork.n.01')
syn_frog = wn.synset('frog.n.01')
syn_garden = wn.synset('garden.n.01')
syn_giraffe = wn.synset('giraffe.n.01')
syn_goatee = wn.synset('goatee.n.01')
syn_grass = wn.synset('grass.n.01')
syn_guitar = wn.synset('guitar.n.01')
syn_hamburger = wn.synset('hamburger.n.01')
syn_hammer = wn.synset('hammer.n.01')
syn_hand = wn.synset('hand.n.01')
syn_harp = wn.synset('harp.n.01')
syn_hat = wn.synset('hat.n.01')
syn_headphones = wn.synset('earphone.n.01')
syn_hedgehog = wn.synset('porcupine.n.01')
syn_helicopter = wn.synset('helicopter.n.01')
syn_helmet = wn.synset('helmet.n.01')
syn_hexagon = wn.synset('hexagon.n.01')
syn_horse = wn.synset('horse.n.01')
syn_hospital = wn.synset('hospital.n.01')
syn_hourglass = wn.synset('hourglass.n.01')
syn_house = wn.synset('house.n.01')
syn_hurricane = wn.synset('hurricane.n.01')
syn_jacket = wn.synset('jacket.n.01')
syn_jail = wn.synset('jail.n.01')
syn_kangaroo = wn.synset('kangaroo.n.01')
syn_key = wn.synset('key.n.01')
syn_keyboard = wn.synset('keyboard.n.01')
syn_knee = wn.synset('knee.n.01')
syn_knife = wn.synset('knife.n.01')
syn_ladder = wn.synset('ladder.n.01')
syn_lantern = wn.synset('lantern.n.01')
syn_laptop = wn.synset('laptop.n.01')
syn_leaf = wn.synset('leaf.n.01')
syn_leg = wn.synset('leg.n.01')
syn_lighter = wn.synset('igniter.n.01')
syn_lighthouse = wn.synset('beacon.n.03')
syn_lightning = wn.synset('lightning.n.01')
syn_lion = wn.synset('lion.n.01')
syn_lipstick = wn.synset('lipstick.n.01')
syn_lobster = wn.synset('lobster.n.01')
syn_lollipop = wn.synset('ice_lolly.n.01')
syn_mailbox = wn.synset('mailbox.n.01')
syn_map = wn.synset('map.n.01')
syn_marker = wn.synset('marker.n.01')
syn_megaphone = wn.synset('megaphone.n.01')
syn_mermaid = wn.synset('mermaid.n.01')
syn_microphone = wn.synset('microphone.n.01')
syn_microwave = wn.synset('microwave.n.01')
syn_monkey  = wn.synset('monkey.n.01')
syn_moon = wn.synset('moon.n.01')
syn_mosquito = wn.synset('mosquito.n.01')
syn_motorbike = wn.synset('minibike.n.01')
syn_mountain = wn.synset('mountain.n.01')
syn_mouse = wn.synset('mouse.n.01')
syn_moustache = wn.synset('mustache.n.01')
syn_mouth = wn.synset('mouth.n.01')
syn_mug = wn.synset('mug.n.01')
syn_mushroom = wn.synset('mushroom.n.01')
syn_nail = wn.synset('nail.n.01')
syn_necklace = wn.synset('necklace.n.01')
syn_nose = wn.synset('nose.n.01')
syn_ocean = wn.synset('ocean.n.01')
syn_octagon = wn.synset('octagon.n.01')
syn_octopus = wn.synset('octopus.n.02')
syn_onion = wn.synset('onion.n.01')
syn_oven = wn.synset('oven.n.01')
syn_owl = wn.synset('owl.n.01')
syn_paintbrush = wn.synset('paintbrush.n.01')
syn_panda = wn.synset('giant_panda.n.01')
syn_pants = wn.synset('bloomers.n.01')
syn_parachute = wn.synset('parachute.n.01')
syn_parrot = wn.synset('parrot.n.01')
syn_passport = wn.synset('pass.n.05')
syn_peanut = wn.synset('peanut.n.01')
syn_pear = wn.synset('pear.n.01')
syn_pencil = wn.synset('pencil.n.01')
syn_penguin = wn.synset('penguin.n.01')
syn_piano = wn.synset('piano.n.01')
syn_pig = wn.synset('hog.n.03')
syn_pillow = wn.synset('pillow.n.01')
syn_pineapple = wn.synset('pineapple.n.01')
syn_pizza = wn.synset('pizza.n.01')
syn_pliers = wn.synset('pliers.n.01')
syn_pond = wn.synset('pond.n.01')
syn_pool = wn.synset('pool.n.01')
syn_popsicle = wn.synset('ice_lolly.n.01')
syn_postcard = wn.synset('postcard.n.01')
syn_potato = wn.synset('potato.n.01')
syn_purse = wn.synset('bag.n.04')
syn_rabbit = wn.synset('rabbit.n.01')
syn_raccoon = wn.synset('raccoon.n.02')
syn_radio = wn.synset('radio.n.01')
syn_rain = wn.synset('rain.n.01')
syn_rainbow = wn.synset('rainbow.n.01')
syn_rake = wn.synset('rake.n.03')
syn_rhinoceros = wn.synset('rhinoceros.n.01')
syn_rifle = wn.synset('rifle.n.01')
syn_river = wn.synset('river.n.01')
syn_sailboat = wn.synset('sailboat.n.01')
syn_sandwich = wn.synset('sandwich.n.01')
syn_saw = wn.synset('saw.n.02')
syn_saxophone = wn.synset('sax.n.02')
syn_scissors = wn.synset('scissors.n.01')
syn_scorpion = wn.synset('scorpion.n.03')
syn_screwdriver = wn.synset('screwdriver.n.01')
syn_shark = wn.synset('shark.n.01')
syn_sheep = wn.synset('sheep.n.01')
syn_shoe = wn.synset('shoe.n.01')
syn_shorts = wn.synset('short_pants.n.01')
syn_shovel = wn.synset('shovel.n.01')
syn_sink = wn.synset('sink.n.01')
syn_skateboard = wn.synset('skateboard.n.01')
syn_skull = wn.synset('skull.n.01')
syn_skyscraper = wn.synset('skyscraper.n.01')
syn_snail = wn.synset('snail.n.01')
syn_snake = wn.synset('snake.n.01')
syn_snorkel = wn.synset('snorkel.n.01')
syn_snowflake = wn.synset('snowflake.n.01')
syn_snowman = wn.synset('snowman.n.01')
syn_sock = wn.synset('sock.n.01')
syn_speedboat = wn.synset('speedboat.n.01')
syn_spider = wn.synset('spider.n.01')
syn_spoon = wn.synset('spoon.n.01')
syn_spreadsheet = wn.synset('spreadsheet.n.01')
syn_square = wn.synset('square.n.01')
syn_squirrel = wn.synset('squirrel.n.01')
syn_stairs = wn.synset('stairs.n.01')
syn_star = wn.synset('star.n.01')
syn_steak = wn.synset('steak.n.01')
syn_stereo = wn.synset('stereo.n.01')
syn_stethoscope = wn.synset('stethoscope.n.01')
syn_stove = wn.synset('stove.n.01')
syn_strawberry = wn.synset('strawberry.n.01')
syn_streetlight = wn.synset('streetlight.n.01')
syn_submarine = wn.synset('submarine.n.01')
syn_suitcase = wn.synset('bag.n.06')
syn_sun = wn.synset('sun.n.01')
syn_swan = wn.synset('swan.n.01')
syn_sweater = wn.synset('sweater.n.01')
syn_swing = wn.synset('swing.n.02')
syn_sword = wn.synset('sword.n.01')
syn_syringe = wn.synset('syringe.n.01')
syn_table = wn.synset('table.n.02')
syn_teapot = wn.synset('teapot.n.01')
syn_telephone = wn.synset('telephone.n.01')
syn_television = wn.synset('television.n.02')
syn_tent = wn.synset('tent.n.01')
syn_tiger = wn.synset('tiger.n.01')
syn_toaster = wn.synset('toaster.n.02')
syn_toe = wn.synset('toe.n.01')
syn_toilet = wn.synset('toilet.n.01')
syn_tooth = wn.synset('tooth.n.01')
syn_toothbrush = wn.synset('toothbrush.n.01')
syn_toothpaste = wn.synset('toothpaste.n.01')
syn_tornado = wn.synset('tornado.n.01')
syn_tractor = wn.synset('tractor.n.01')
syn_train = wn.synset('train.n.01')
syn_tree = wn.synset('tree.n.01')
syn_trombone = wn.synset('trombone.n.01')
syn_truck = wn.synset('truck.n.01')
syn_trumpet = wn.synset('cornet.n.01')
syn_umbrella = wn.synset('umbrella.n.01')
syn_underwear = wn.synset('underwear.n.01')
syn_van = wn.synset('van.n.05')
syn_vase = wn.synset('vase.n.01')
syn_violin = wn.synset('violin.n.01')
syn_watermelon = wn.synset('watermelon.n.01')
syn_whale = wn.synset('whale.n.02')
syn_wheel = wn.synset('wheel.n.01')
syn_windmill = wn.synset('windmill.n.01')
syn_wristwatch = wn.synset('wristwatch.n.01')
syn_zebra = wn.synset('zebra.n.01')


assigned_syns = [syn_airplane, syn_ambulance, syn_angel, syn_ant, syn_anvil, syn_apple, syn_arm, syn_asparagus, syn_axe, syn_backpack, syn_banana, syn_bandage, syn_barn, syn_baseball, syn_basket, syn_basketball, syn_bat, syn_bathtub, syn_beach, syn_bear, syn_beard, syn_bed, syn_bee, syn_belt, syn_bench, syn_bicycle, syn_binoculars, syn_bird, syn_blackberry, syn_blueberry, syn_book, syn_boomerang, syn_bowtie, syn_bracelet, syn_brain, syn_bread, syn_bridge, syn_broccoli, syn_broom, syn_bucket, syn_bulldozer, syn_bus, syn_bush, syn_butterfly, syn_cactus, syn_cake, syn_calculator, syn_calendar, syn_camel, syn_camera, syn_camouflage, syn_campfire, syn_candle, syn_cannon, syn_canoe, syn_car, syn_carrot, syn_castle, syn_cat, syn_cello, syn_chair, syn_chandelier, syn_church, syn_circle, syn_clarinet, syn_clock, syn_cloud, syn_compass, syn_computer, syn_cookie, syn_cooler, syn_couch, syn_cow, syn_crab, syn_crayon, syn_crocodile, syn_crown, syn_cup, syn_diamond, syn_dishwasher, syn_dog, syn_dolphin, syn_door, syn_dragon, syn_dresser, syn_drill, syn_duck, syn_dumbbell, syn_ear, syn_elbow, syn_elephant, syn_envelope, syn_eraser, syn_eye, syn_eyeglasses, syn_face, syn_fan, syn_feather, syn_fence, syn_finger, syn_fireplace, syn_fish, syn_flamingo, syn_flashlight, syn_flower, syn_foot, syn_fork, syn_frog, syn_garden, syn_giraffe, syn_goatee, syn_grass, syn_guitar, syn_hamburger, syn_hammer, syn_hand, syn_harp, syn_hat, syn_headphones, syn_hedgehog, syn_helicopter, syn_helmet, syn_hexagon, syn_horse, syn_hospital, syn_hourglass, syn_house, syn_hurricane, syn_jacket, syn_jail, syn_kangaroo, syn_key, syn_keyboard, syn_knee, syn_knife, syn_ladder, syn_lantern, syn_laptop, syn_leaf, syn_leg, syn_lighter, syn_lighthouse, syn_lightning, syn_lion, syn_lipstick, syn_lobster, syn_lollipop, syn_mailbox, syn_map, syn_marker, syn_megaphone, syn_mermaid, syn_microphone, syn_microwave, syn_monkey, syn_moon, syn_mosquito, syn_motorbike, syn_mountain, syn_mouse, syn_moustache, syn_mouth, syn_mug, syn_mushroom, syn_nail, syn_necklace, syn_nose, syn_ocean, syn_octagon, syn_octopus, syn_onion, syn_oven, syn_owl, syn_paintbrush, syn_panda, syn_pants, syn_parachute, syn_parrot, syn_passport, syn_peanut, syn_pear, syn_pencil, syn_penguin, syn_piano, syn_pig, syn_pillow, syn_pineapple, syn_pizza, syn_pliers, syn_pond, syn_pool, syn_popsicle, syn_postcard, syn_potato, syn_purse, syn_rabbit, syn_raccoon, syn_radio, syn_rain, syn_rainbow, syn_rake, syn_rhinoceros, syn_rifle, syn_river, syn_sailboat, syn_sandwich, syn_saw, syn_saxophone, syn_scissors, syn_scorpion, syn_screwdriver, syn_shark, syn_sheep, syn_shoe, syn_shorts, syn_shovel, syn_sink, syn_skateboard, syn_skull, syn_skyscraper, syn_snail, syn_snake, syn_snorkel, syn_snowflake, syn_snowman, syn_sock, syn_speedboat, syn_spider, syn_spoon, syn_spreadsheet, syn_square, syn_squirrel, syn_stairs, syn_star, syn_steak, syn_stereo, syn_stethoscope, syn_stove, syn_strawberry, syn_streetlight, syn_submarine, syn_suitcase, syn_sun, syn_swan, syn_sweater, syn_swing, syn_sword, syn_syringe, syn_table, syn_teapot, syn_telephone, syn_television, syn_tent, syn_tiger, syn_toaster, syn_toe, syn_toilet, syn_tooth, syn_toothbrush, syn_toothpaste, syn_tornado, syn_tractor, syn_train, syn_tree, syn_trombone, syn_truck, syn_trumpet, syn_umbrella, syn_underwear, syn_van, syn_vase, syn_violin, syn_watermelon, syn_whale, syn_wheel, syn_windmill, syn_wristwatch, syn_zebra]


## Get Semantic Similarity Scores ##
# 1st: Leacock_Chordorow
def get_lch_similarity(list):
    pairs = {}
    for word1 in list:
        for word2 in list:
            l = word1.lch_similarity(word2)
            pairs.update({(word1, word2): l})
    return pairs
#lch = get_lch_similarity(assigned_syns)

# Save pairs
#df = pd.DataFrame()
#df['Pairs'] = list(lch.keys())
#df['LCH Score'] = list(lch.values())
#df.to_csv('/Users/brendafinlay/Documents/Cusack_Lab/lch_similarity_scores.csv', index=False)

# Make and save matrix
#ob = len(assigned_syns)
#rdm = np.zeros([ob, ob])
#for ind1, o1 in enumerate(assigned_syns):
 #   for ind2, o2 in enumerate(assigned_syns):
  #      rdm[ind1, ind2] = lch[(o1, o2)]
#pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/lch_rsm.csv', index=(assigned_syns))

# Make heatmap
#df = pd.read_csv('/Users/brendafinlay/Documents/lch_rsm.csv', index_col=0)
#fig,ax = plt.subplots(figsize=(7,7))
#sns.heatmap(df, center=0.05, ax=ax)
#plt.show()
#plt.savefig('/Users/brendafinlay/Documents/heatmap_lch.pdf')
#plt.close()





############# Konkle Categorised Object List ################
animate = [syn_angel, syn_ant, syn_bear, syn_bee, syn_bird, syn_butterfly, syn_camel, syn_cow, syn_crab, syn_crocodile, syn_dog, syn_dolphin, syn_dragon, syn_duck, syn_elephant, syn_cat, syn_campfire, syn_face, syn_fish, syn_flamingo, syn_frog, syn_giraffe, syn_hedgehog, syn_horse, syn_hurricane, syn_kangaroo, syn_lightning, syn_lion, syn_lobster, syn_mermaid, syn_monkey, syn_mosquito, syn_mouse, syn_ocean, syn_arm, syn_ear, syn_elbow, syn_eye, syn_leg, syn_nose, syn_mouth, syn_octopus, syn_owl, syn_panda, syn_parrot, syn_penguin, syn_pig, syn_rabbit, syn_raccoon, syn_rain, syn_rhinoceros, syn_river, syn_scorpion, syn_shark, syn_sheep, syn_snail, syn_snake, syn_spider, syn_squirrel, syn_star, syn_swan, syn_tiger, syn_toe, syn_tornado, syn_zebra, syn_windmill]
inab = [syn_airplane, syn_ambulance, syn_anvil, syn_axe, syn_barn, syn_bathtub, syn_bed, syn_bench, syn_bicycle, syn_bridge, syn_bulldozer, syn_bus, syn_bush, syn_cactus, syn_cannon, syn_canoe, syn_car, syn_castle, syn_cello, syn_chair, syn_chandelier, syn_church, syn_cloud, syn_computer, syn_couch, syn_dishwasher, syn_door, syn_dresser, syn_fence, syn_fireplace, syn_garden, syn_helicopter, syn_hospital, syn_house, syn_jail, syn_ladder, syn_laptop, syn_lighthouse, syn_mailbox, syn_microwave, syn_moon, syn_mountain, syn_oven, syn_parachute, syn_piano, syn_pond, syn_pool, syn_rainbow, syn_sailboat, syn_sink, syn_skyscraper, syn_snowman, syn_speedboat, syn_stairs, syn_stove, syn_streetlight, syn_submarine, syn_suitcase, syn_sun, syn_swing, syn_sword, syn_table, syn_television, syn_tent, syn_toilet, syn_tractor, syn_train, syn_tree, syn_truck, syn_van, syn_whale, syn_wheel]
inas = [syn_apple, syn_asparagus, syn_backpack, syn_banana, syn_bandage, syn_baseball, syn_basket, syn_basketball, syn_bat, syn_belt, syn_binoculars, syn_blackberry, syn_blueberry, syn_book, syn_boomerang, syn_bowtie, syn_bracelet, syn_brain, syn_bread, syn_broccoli, syn_broom, syn_bucket, syn_cake, syn_calculator, syn_calendar, syn_camera, syn_candle, syn_carrot, syn_clarinet, syn_clock, syn_compass, syn_cookie, syn_cooler, syn_crayon, syn_crown, syn_cup, syn_diamond, syn_drill, syn_dumbbell, syn_envelope, syn_eraser, syn_eyeglasses, syn_fan, syn_feather, syn_finger, syn_flashlight, syn_flower, syn_foot, syn_fork, syn_goatee, syn_grass, syn_guitar, syn_hamburger, syn_hammer, syn_hand, syn_harp, syn_hat, syn_headphones, syn_helmet, syn_hourglass, syn_jacket, syn_key, syn_keyboard, syn_knee, syn_knife, syn_lantern, syn_leaf, syn_lighter, syn_lipstick, syn_lollipop, syn_map, syn_marker, syn_megaphone, syn_microphone, syn_motorbike, syn_moustache, syn_mug, syn_mushroom, syn_nail, syn_necklace, syn_onion, syn_paintbrush, syn_pants, syn_passport, syn_peanut, syn_pear, syn_pencil, syn_pillow, syn_pineapple, syn_pizza, syn_pliers, syn_popsicle, syn_postcard, syn_potato, syn_purse, syn_radio, syn_rake, syn_rifle, syn_sandwich, syn_saw, syn_saxophone, syn_scissors, syn_screwdriver, syn_shoe, syn_shorts, syn_shovel, syn_skateboard, syn_skull, syn_snorkel, syn_snowflake, syn_sock, syn_spoon, syn_spreadsheet, syn_steak, syn_stereo, syn_stethoscope, syn_strawberry, syn_sweater, syn_syringe, syn_teapot, syn_telephone, syn_toaster, syn_tooth, syn_toothbrush, syn_toothpaste, syn_trombone, syn_trumpet, syn_umbrella, syn_underwear, syn_vase, syn_violin, syn_watermelon, syn_wristwatch]
konkle_combined = animate + inab + inas

scores = get_lch_similarity(konkle_combined)

# Saved to matrix CSV
ob = len(konkle_combined)
rdm = np.zeros([ob, ob])
for ind1, o1 in enumerate(konkle_combined):
    for ind2, o2 in enumerate(konkle_combined):
        rdm[ind1, ind2] = scores[(o1, o2)]
pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/konkle_matrix.csv', index=konkle_combined)


# Konkle seaborn heatmap
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/konkle_matrix_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(15,15))
sns.heatmap(df, center=0.05, ax=ax, xticklabels=True, yticklabels=True)
sns.set(font_scale= 0.25)
#plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_konkle_lch.pdf')
plt.close()

# Interactive Heatmap #
import chart_studio.plotly as csply
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.figure_factory as ff
import plotly.io as pio
pio.renderers
pio.renderers.default = "chrome"
import psutil

df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/konkle_matrix_headings.csv', index_col=0)
figure = ff.create_annotated_heatmap(z=df.values, x=list(df.columns), y=list(df.index), annotation_text=None, showscale=True)
figure.show()





 
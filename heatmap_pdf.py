import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import rpy2


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


############# Konkle Categorised Object List ordered by AOA (low to high) ################
animate = [syn_hand, syn_dog, syn_nose, syn_leg, syn_toe, syn_arm, syn_spider, syn_finger, syn_foot, syn_duck, syn_bird, syn_bear, syn_mouth, syn_rain, syn_ear, syn_butterfly, syn_cat, syn_face, syn_eye, syn_pig, syn_star, syn_cow, syn_rabbit, syn_angel, syn_tiger, syn_fish, syn_horse, syn_monkey, syn_sheep, syn_ant, syn_frog, syn_lion, syn_squirrel, syn_ocean, syn_lightning, syn_elbow, syn_zebra, syn_elephant, syn_bat, syn_river, syn_mouse, syn_bee, syn_giraffe, syn_snake, syn_camel, syn_crocodile, syn_campfire, syn_crab, syn_windmill, syn_shark, syn_kangaroo, syn_dragon, syn_parrot, syn_panda, syn_mermaid, syn_penguin, syn_snail, syn_rhinoceros, syn_dolphin, syn_mosquito, syn_owl, syn_tornado, syn_octopus, syn_flamingo, syn_swan, syn_raccoon, syn_hurricane, syn_lobster, syn_scorpion, syn_hedgehog, syn_knee]
inab = [syn_bed, syn_door, syn_house, syn_bathtub, syn_car, syn_sun, syn_chair, syn_snowman, syn_toilet, syn_tree, syn_cloud, syn_couch, syn_truck, syn_bus, syn_airplane, syn_train, syn_television, syn_bench, syn_stairs, syn_bicycle, syn_rainbow, syn_dresser, syn_stove, syn_table, syn_ladder, syn_wheel, syn_sink, syn_barn, syn_sailboat, syn_beach, syn_moon, syn_bush, syn_church, syn_pool, syn_pond, syn_tent, syn_van, syn_helicopter, syn_garden, syn_sword, syn_whale, syn_piano, syn_tractor, syn_hospital, syn_bridge, syn_bulldozer, syn_oven, syn_jail, syn_castle, syn_streetlight, syn_axe, syn_lighthouse, syn_mailbox, syn_mountain, syn_ambulance, syn_fence, syn_speedboat, syn_canoe, syn_cactus, syn_parachute, syn_dishwasher, syn_fireplace, syn_microwave, syn_cannon, syn_submarine, syn_suitcase, syn_skyscraper, syn_chandelier, syn_computer, syn_cello, syn_anvil, syn_laptop]
inas = [syn_spoon, syn_shoe, syn_carrot, syn_sock, syn_flower, syn_crayon, syn_pants, syn_cake, syn_hat, syn_toothpaste, syn_cookie, syn_pillow, syn_cup, syn_bread, syn_key, syn_tooth, syn_fork, syn_book, syn_banana, syn_popsicle, syn_lollipop, syn_grass, syn_underwear, syn_jacket, syn_shorts, syn_pear, syn_pencil, syn_apple, syn_knife, syn_strawberry, syn_watermelon, syn_toothbrush, syn_clock, syn_scissors, syn_leaf, syn_belt, syn_telephone, syn_feather, syn_pizza, syn_sandwich, syn_baseball, syn_potato, syn_marker, syn_eyeglasses, syn_eraser, syn_necklace, syn_peanut, syn_mug, syn_radio, syn_broccoli, syn_hamburger, syn_sweater, syn_basketball, syn_guitar, syn_rake, syn_snowflake, syn_saw, syn_candle, syn_backpack, syn_moustache, syn_hammer, syn_lipstick, syn_nail, syn_broom, syn_purse, syn_map, syn_bucket, syn_flashlight, syn_fan, syn_basket, syn_bracelet, syn_umbrella, syn_helmet, syn_brain, syn_calendar, syn_bandage, syn_stereo, syn_camera, syn_screwdriver, syn_onion, syn_cooler, syn_blueberry, syn_paintbrush, syn_teapot, syn_envelope, syn_microphone, syn_pineapple, syn_shovel, syn_trumpet, syn_skull, syn_mushroom, syn_diamond, syn_steak, syn_toaster, syn_postcard, syn_asparagus, syn_binoculars, syn_skateboard, syn_pliers, syn_lighter, syn_drill, syn_wristwatch, syn_violin, syn_harp, syn_dumbbell, syn_headphones, syn_crown, syn_trombone, syn_rifle, syn_vase, syn_bowtie, syn_motorbike, syn_calculator, syn_compass, syn_stethoscope, syn_lantern, syn_hourglass, syn_blackberry, syn_saxophone, syn_snorkel, syn_clarinet, syn_keyboard, syn_boomerang, syn_megaphone, syn_syringe, syn_goatee, syn_passport, syn_spreadsheet]
konkle_combined = animate + inab + inas

## Leacock-Chordorow Similarity Score ##
def get_lch_similarity(list):
    pairs = {}
    for word1 in list:
        for word2 in list:
            l = word1.lch_similarity(word2)
            pairs.update({(word1, word2): l})
    return pairs

scores = get_lch_similarity(konkle_combined)


# Konkle categorized, ordered by AOA Seaborn heatmap.pdf
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/ordered_konklematrix_272_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(15,15))
# To create contrasting colours for high and low scores, keeping centre light i.e. diverging colour palette. Saved as category&ordered_r.pdf
cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
sns.set(font_scale= 0.25)
plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_konkle&ordered_r.pdf')
plt.close()

################# Huth Categorised - Ordered by AOA low to high ######################
## Entire list ordered by AOA ##
words = [syn_spoon, syn_shoe, syn_carrot, syn_hand, syn_dog, syn_bed, syn_sock, syn_nose, syn_leg, syn_toe, syn_door, syn_flower, syn_house, syn_crayon, syn_bathtub, syn_pants, syn_arm, syn_cake, syn_hat, syn_toothpaste, syn_car, syn_cookie, syn_sun, syn_spider, syn_chair, syn_finger, syn_foot, syn_snowman, syn_pillow, syn_duck, syn_bird, syn_toilet, syn_tree, syn_cup, syn_bear, syn_mouth, syn_bread, syn_key, syn_rain, syn_tooth, syn_ear, syn_cloud, syn_fork, syn_butterfly, syn_cat, syn_book, syn_couch, syn_face, syn_eye, syn_banana, syn_popsicle, syn_truck, syn_pig, syn_bus, syn_star, syn_lollipop, syn_cow, syn_rabbit, syn_airplane, syn_grass, syn_underwear, syn_jacket, syn_shorts, syn_angel, syn_tiger, syn_train, syn_pear, syn_fish, syn_pencil, syn_television, syn_horse, syn_apple, syn_knife, syn_monkey, syn_bench, syn_strawberry, syn_stairs, syn_watermelon, syn_sheep, syn_bicycle, syn_rainbow, syn_dresser, syn_ant, syn_frog, syn_stove, syn_toothbrush, syn_table, syn_ladder, syn_wheel, syn_lion, syn_clock, syn_squirrel, syn_sink, syn_barn, syn_scissors, syn_leaf, syn_belt, syn_telephone, syn_sailboat, syn_feather, syn_pizza, syn_ocean, syn_lightning, syn_elbow, syn_zebra, syn_sandwich, syn_elephant, syn_beach, syn_moon, syn_baseball, syn_potato, syn_beard, syn_bat, syn_marker, syn_river, syn_bush, syn_eyeglasses, syn_mouse, syn_eraser, syn_bee, syn_giraffe, syn_necklace, syn_peanut, syn_snake, syn_camel, syn_crocodile, syn_campfire, syn_church, syn_pool, syn_mug, syn_pond, syn_tent, syn_radio, syn_van, syn_broccoli, syn_hamburger, syn_sweater, syn_helicopter, syn_crab, syn_basketball, syn_windmill, syn_guitar, syn_rake, syn_snowflake, syn_garden, syn_saw, syn_candle, syn_backpack, syn_moustache, syn_hammer, syn_lipstick, syn_nail, syn_sword, syn_shark, syn_whale, syn_piano, syn_tractor, syn_broom, syn_purse, syn_kangaroo, syn_hospital, syn_dragon, syn_parrot, syn_bridge, syn_map, syn_bulldozer, syn_bucket, syn_flashlight, syn_fan, syn_panda, syn_oven, syn_basket, syn_mermaid, syn_penguin, syn_bracelet, syn_umbrella, syn_helmet, syn_jail, syn_brain, syn_snail, syn_castle, syn_calendar, syn_bandage, syn_stereo, syn_rhinoceros, syn_camera, syn_screwdriver, syn_dolphin, syn_onion, syn_streetlight, syn_mosquito, syn_axe, syn_lighthouse, syn_mailbox, syn_cooler, syn_mountain, syn_ambulance, syn_owl, syn_tornado, syn_blueberry, syn_paintbrush, syn_teapot, syn_envelope, syn_microphone, syn_pineapple, syn_octopus, syn_fence, syn_shovel, syn_trumpet, syn_flamingo, syn_swan, syn_skull, syn_mushroom, syn_diamond, syn_speedboat, syn_canoe, syn_steak, syn_cactus, syn_toaster, syn_postcard, syn_raccoon, syn_asparagus, syn_binoculars, syn_skateboard, syn_parachute, syn_pliers, syn_lighter, syn_drill, syn_dishwasher, syn_wristwatch, syn_hurricane, syn_fireplace, syn_lobster, syn_violin, syn_harp, syn_dumbbell, syn_microwave, syn_headphones, syn_crown, syn_trombone, syn_scorpion, syn_rifle, syn_vase, syn_cannon, syn_submarine, syn_bowtie, syn_motorbike, syn_suitcase, syn_calculator, syn_skyscraper, syn_compass, syn_stethoscope, syn_lantern, syn_hourglass, syn_hedgehog, syn_chandelier, syn_blackberry, syn_saxophone, syn_snorkel, syn_clarinet, syn_keyboard, syn_knee, syn_computer, syn_boomerang, syn_cello, syn_megaphone, syn_syringe, syn_anvil, syn_goatee, syn_passport, syn_laptop, syn_spreadsheet]

biological = [syn_hand, syn_dog, syn_nose, syn_leg, syn_toe, syn_flower, syn_arm, syn_spider, syn_finger, syn_foot, syn_duck, syn_bird, syn_tree, syn_bear, syn_mouth, syn_tooth, syn_ear, syn_butterfly, syn_cat, syn_face, syn_eye, syn_pig, syn_cow, syn_rabbit, syn_grass, syn_angel , syn_tiger, syn_fish, syn_horse, syn_monkey, syn_sheep, syn_ant, syn_frog, syn_lion, syn_squirrel, syn_elbow, syn_zebra, syn_elephant, syn_bat, syn_bush, syn_mouse, syn_bee, syn_giraffe, syn_snake, syn_camel, syn_crocodile, syn_crab, syn_shark, syn_whale, syn_kangaroo, syn_dragon , syn_parrot, syn_panda, syn_penguin, syn_mermaid , syn_brain, syn_snail, syn_rhinoceros, syn_dolphin, syn_mosquito, syn_owl, syn_octopus, syn_flamingo, syn_swan, syn_skull, syn_cactus, syn_raccoon, syn_lobster, syn_scorpion, syn_hedgehog, syn_knee]
civilisation = [syn_spoon, syn_shoe, syn_bed, syn_sock, syn_door, syn_house, syn_crayon, syn_bathtub, syn_pants, syn_cake, syn_hat, syn_toothpaste, syn_car, syn_cookie, syn_chair, syn_pillow, syn_toilet, syn_cup, syn_key, syn_fork, syn_book, syn_couch, syn_face, syn_popsicle, syn_truck, syn_bus, syn_lollipop, syn_airplane, syn_underwear, syn_jacket, syn_shorts, syn_train, syn_pencil, syn_television, syn_knife, syn_bench, syn_stairs, syn_bicycle, syn_dresser, syn_stove, syn_toothbrush, syn_table, syn_ladder, syn_wheel, syn_clock, syn_sink, syn_barn, syn_scissors, syn_belt, syn_telephone, syn_sailboat, syn_pizza, syn_sandwich, syn_baseball, syn_marker, syn_eyeglasses, syn_eraser, syn_necklace, syn_campfire, syn_church, syn_pool, syn_mug, syn_tent, syn_radio, syn_van, syn_hamburger, syn_sweater, syn_helicopter, syn_basketball, syn_windmill, syn_guitar, syn_rake, syn_garden, syn_saw, syn_candle, syn_backpack, syn_hammer, syn_lipstick, syn_nail, syn_sword, syn_piano, syn_tractor, syn_broom, syn_purse, syn_hospital, syn_bridge, syn_map, syn_bulldozer, syn_bucket, syn_flashlight, syn_fan, syn_oven, syn_basket, syn_bracelet, syn_umbrella, syn_helmet, syn_jail, syn_castle, syn_calendar, syn_bandage, syn_stereo, syn_camera, syn_screwdriver, syn_streetlight, syn_axe, syn_lighthouse, syn_mailbox, syn_cooler, syn_ambulance, syn_paintbrush, syn_teapot, syn_envelope, syn_microphone, syn_fence, syn_shovel, syn_trumpet, syn_speedboat, syn_canoe, syn_toaster, syn_postcard, syn_binoculars, syn_skateboard, syn_parachute, syn_pliers, syn_lighter, syn_drill, syn_dishwasher, syn_wristwatch, syn_fireplace, syn_violin, syn_harp, syn_dumbbell, syn_microwave, syn_headphones, syn_crown, syn_trombone, syn_rifle, syn_vase, syn_cannon, syn_submarine, syn_bowtie, syn_motorbike, syn_suitcase, syn_calculator, syn_skyscraper, syn_compass, syn_stethoscope, syn_lantern, syn_hourglass, syn_chandelier, syn_saxophone, syn_snorkel, syn_clarinet, syn_keyboard, syn_computer, syn_boomerang, syn_cello, syn_megaphone, syn_syringe, syn_anvil, syn_passport, syn_laptop, syn_spreadsheet]
nature = [syn_carrot, syn_dog, syn_flower, syn_sun, syn_spider, syn_snowman, syn_duck, syn_bird, syn_tree, syn_bear, syn_bread, syn_rain, syn_cloud, syn_butterfly, syn_cat, syn_banana, syn_pig, syn_star, syn_cow, syn_rabbit, syn_grass, syn_tiger, syn_pear, syn_fish, syn_horse, syn_apple, syn_monkey, syn_strawberry, syn_watermelon, syn_sheep, syn_rainbow, syn_ant, syn_frog, syn_lion, syn_squirrel, syn_leaf, syn_feather, syn_ocean, syn_lightning, syn_zebra, syn_elephant, syn_beach, syn_moon, syn_potato, syn_bat, syn_river, syn_bush, syn_mouse, syn_bee, syn_giraffe, syn_peanut, syn_snake, syn_camel, syn_crocodile, syn_pond, syn_broccoli, syn_crab, syn_snowflake, syn_shark, syn_whale, syn_kangaroo, syn_parrot, syn_panda, syn_penguin, syn_snail, syn_rhinoceros, syn_dolphin, syn_onion, syn_mosquito, syn_mountain, syn_owl, syn_tornado, syn_blueberry, syn_pineapple, syn_octopus, syn_flamingo, syn_swan, syn_mushroom, syn_diamond, syn_steak, syn_cactus, syn_raccoon, syn_asparagus, syn_hurricane, syn_lobster, syn_scorpion, syn_hedgehog, syn_blackberry]
social = [syn_couch, syn_face, syn_pizza, syn_campfire, syn_church, syn_radio, syn_guitar, syn_piano, syn_microphone, syn_trumpet, syn_violin, syn_harp, syn_trombone, syn_saxophone, syn_megaphone]

# Objects that do not fit into Huth Categorization = syn_goatee, syn_beach, syn_beard, syn_moustache #

# Ordered non_bio in Excel by AOA low to high 
get_nb = list(set(konkle_combined) - set(biological))
non_bio = [syn_spoon, syn_shoe, syn_carrot, syn_bed, syn_sock, syn_door, syn_house, syn_crayon, syn_bathtub, syn_pants, syn_cake, syn_toothpaste, syn_hat, syn_car, syn_cookie, syn_sun, syn_chair, syn_snowman, syn_pillow, syn_toilet, syn_cup, syn_key, syn_bread, syn_rain, syn_fork, syn_cloud, syn_book, syn_couch, syn_banana, syn_popsicle, syn_truck, syn_bus, syn_lollipop, syn_star, syn_underwear, syn_airplane, syn_shorts, syn_jacket, syn_pear, syn_train, syn_pencil, syn_television, syn_apple, syn_knife, syn_bench, syn_strawberry, syn_stairs, syn_watermelon, syn_bicycle, syn_rainbow, syn_dresser, syn_stove, syn_toothbrush, syn_table, syn_wheel, syn_ladder, syn_clock, syn_sink, syn_scissors, syn_barn, syn_leaf, syn_belt, syn_telephone, syn_sailboat, syn_pizza, syn_feather, syn_ocean, syn_lightning, syn_sandwich, syn_beach , syn_moon, syn_baseball, syn_potato, syn_beard, syn_marker, syn_river, syn_eyeglasses, syn_eraser, syn_necklace, syn_peanut, syn_campfire, syn_pool, syn_church, syn_mug, syn_tent, syn_pond, syn_radio, syn_broccoli, syn_van, syn_hamburger, syn_sweater, syn_helicopter, syn_basketball, syn_snowflake, syn_windmill, syn_rake, syn_guitar, syn_garden, syn_saw, syn_candle, syn_backpack, syn_moustache, syn_hammer, syn_nail, syn_lipstick, syn_sword, syn_tractor, syn_broom, syn_piano, syn_purse, syn_hospital, syn_bridge, syn_map, syn_bulldozer, syn_bucket, syn_flashlight, syn_fan, syn_oven, syn_basket, syn_bracelet, syn_umbrella, syn_helmet, syn_jail, syn_castle, syn_calendar, syn_bandage, syn_stereo, syn_camera, syn_screwdriver, syn_onion, syn_streetlight, syn_lighthouse, syn_cooler, syn_mailbox, syn_axe, syn_mountain, syn_ambulance, syn_tornado, syn_blueberry, syn_paintbrush, syn_teapot, syn_microphone, syn_pineapple, syn_envelope, syn_trumpet, syn_shovel, syn_fence, syn_mushroom, syn_diamond, syn_speedboat, syn_canoe, syn_steak, syn_toaster, syn_postcard, syn_binoculars, syn_asparagus, syn_skateboard, syn_parachute, syn_pliers, syn_lighter, syn_drill, syn_dishwasher, syn_wristwatch, syn_hurricane, syn_fireplace, syn_violin, syn_harp, syn_dumbbell, syn_microwave, syn_headphones, syn_crown, syn_trombone, syn_rifle, syn_vase, syn_cannon, syn_submarine, syn_bowtie, syn_motorbike, syn_calculator, syn_skyscraper, syn_compass, syn_stethoscope, syn_lantern, syn_hourglass, syn_chandelier, syn_blackberry, syn_saxophone, syn_snorkel, syn_clarinet, syn_keyboard, syn_computer, syn_boomerang, syn_cello, syn_megaphone, syn_syringe, syn_anvil, syn_goatee, syn_passport, syn_laptop, syn_spreadsheet]

# Ordered non_social in Excel by AOA low to high
get_ns = list(set(konkle_combined) - set(social))
non_social = [syn_spoon, syn_shoe, syn_carrot, syn_hand, syn_dog, syn_bed, syn_sock, syn_nose, syn_toe, syn_leg, syn_door, syn_flower, syn_house, syn_crayon, syn_bathtub, syn_pants, syn_arm, syn_cake, syn_toothpaste, syn_hat, syn_car, syn_cookie, syn_sun, syn_chair, syn_finger, syn_spider, syn_foot, syn_snowman, syn_pillow, syn_duck, syn_bird, syn_toilet, syn_cup, syn_tree, syn_mouth, syn_key, syn_bread, syn_bear, syn_rain, syn_tooth, syn_ear, syn_fork, syn_cloud, syn_butterfly, syn_cat, syn_book, syn_eye, syn_banana, syn_truck, syn_pig, syn_bus, syn_lollipop, syn_star, syn_underwear, syn_airplane, syn_grass, syn_rabbit, syn_cow, syn_shorts, syn_jacket, syn_pear, syn_tiger, syn_angel, syn_train, syn_fish, syn_pencil, syn_television, syn_apple, syn_knife, syn_horse, syn_bench, syn_strawberry, syn_monkey, syn_stairs, syn_watermelon, syn_sheep, syn_bicycle, syn_rainbow, syn_dresser, syn_ant, syn_frog, syn_stove, syn_toothbrush, syn_table, syn_wheel, syn_ladder, syn_lion, syn_clock, syn_squirrel, syn_sink, syn_scissors, syn_barn, syn_leaf, syn_belt, syn_telephone, syn_sailboat, syn_feather, syn_ocean, syn_lightning, syn_elbow, syn_sandwich, syn_zebra, syn_elephant, syn_beach, syn_moon, syn_baseball, syn_potato, syn_beard, syn_bat, syn_marker, syn_river, syn_eyeglasses, syn_bush, syn_mouse, syn_eraser, syn_necklace, syn_peanut, syn_bee, syn_giraffe, syn_snake, syn_crocodile, syn_camel, syn_pool, syn_mug, syn_tent, syn_pond, syn_broccoli, syn_van, syn_hamburger, syn_sweater, syn_helicopter, syn_crab, syn_basketball, syn_snowflake, syn_windmill, syn_rake, syn_garden, syn_saw, syn_candle, syn_backpack, syn_moustache, syn_hammer, syn_nail, syn_lipstick, syn_sword, syn_whale, syn_shark, syn_tractor, syn_broom, syn_purse, syn_hospital, syn_kangaroo, syn_bridge, syn_parrot, syn_dragon, syn_map, syn_bulldozer, syn_bucket, syn_flashlight, syn_fan, syn_panda, syn_oven, syn_basket, syn_bracelet, syn_penguin, syn_mermaid, syn_umbrella, syn_helmet, syn_jail, syn_brain, syn_snail, syn_castle, syn_calendar, syn_bandage, syn_stereo, syn_rhinoceros, syn_camera, syn_screwdriver, syn_dolphin, syn_onion, syn_streetlight, syn_mosquito, syn_lighthouse, syn_cooler, syn_mailbox, syn_axe, syn_mountain, syn_ambulance, syn_tornado, syn_owl, syn_blueberry, syn_paintbrush, syn_teapot, syn_pineapple, syn_envelope, syn_octopus, syn_shovel, syn_fence, syn_swan, syn_flamingo, syn_skull, syn_mushroom, syn_diamond, syn_speedboat, syn_canoe, syn_steak, syn_toaster, syn_cactus, syn_postcard, syn_raccoon, syn_binoculars, syn_asparagus, syn_skateboard, syn_parachute, syn_pliers, syn_lighter, syn_drill, syn_dishwasher, syn_wristwatch, syn_hurricane, syn_fireplace, syn_lobster, syn_dumbbell, syn_microwave, syn_headphones, syn_crown, syn_scorpion, syn_rifle, syn_vase, syn_cannon, syn_submarine, syn_bowtie, syn_motorbike, syn_calculator, syn_skyscraper, syn_compass, syn_stethoscope, syn_lantern, syn_hourglass, syn_chandelier, syn_hedgehog, syn_blackberry, syn_snorkel, syn_clarinet, syn_keyboard, syn_knee, syn_computer, syn_boomerang, syn_cello, syn_syringe, syn_anvil, syn_goatee, syn_passport, syn_laptop, syn_spreadsheet]


# Next, make heatmaps for each Huth subcategory
# # # 1. Bio vs Non Bio

# Get similarity scores
bio = biological + non_bio
bio_score = get_lch_similarity(bio)

# Save as matrix 
df = pd.DataFrame()
ob = len(bio)
rdm = np.zeros([ob, ob])
for ind1, o1 in enumerate(bio):
    for ind2, o2 in enumerate(bio):
        rdm[ind1, ind2] = bio_score[(o1, o2)]
pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_bio.csv', index=(bio))

# (Index put into csv manually, re-saved as rsm_bio_headings.csv)
## Must close rsm_headings file before running heatmap script
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_bio_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(15,15))
cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
sns.set(font_scale= 0.25)
plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_HuthBio&ordered_r.pdf')
plt.close()

# # 2. Nature vs Civilisation

together = nature + civilisation
natciv_score = get_lch_similarity(together)

#Save as matrix
ob = len(together)
rdm = np.zeros([ob, ob])
for ind1, o1 in enumerate(together):
    for ind2, o2 in enumerate(together):
        rdm[ind1, ind2] = natciv_score[(o1, o2)]
pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_natciv.csv', index=together)

# Seaborn heatmap Nature/Civilisation
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_natciv_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(15,15))
cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
sns.set(font_scale= 0.5)
plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_HuthNatCiv&ordered_r.pdf')
plt.close()

# # 3. Social vs Non-Social
socnon = social + non_social
social_score = get_lch_similarity(socnon)

# Save as matrix
ob = len(socnon)
rdm = np.zeros([ob, ob])
for ind1, o1 in enumerate(socnon):
    for ind2, o2 in enumerate(socnon):
        rdm[ind1, ind2] = social_score[(o1, o2)]
pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_socnon.csv', index=socnon)

# Seaborn map for Social/Non-Social
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_socnon_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(15,15))
cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
sns.set(font_scale= 0.25)
plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_HuthSocialNonS&ordered_r.pdf')
plt.close()

########### Faces, Scenes, Bodyparts (Downing&Peelin)(Kanwisher&Epstein) ################
faces = [syn_mouth, syn_tooth, syn_face, syn_beard, syn_eyeglasses, syn_moustache, syn_goatee]
scenes = [syn_rain, syn_cloud, syn_barn, syn_ocean, syn_lightning, syn_beach, syn_campfire, syn_church, syn_pool, syn_pond, syn_windmill, syn_garden, syn_hospital, syn_bridge, syn_jail, syn_castle, syn_lighthouse, syn_mountain, syn_tornado, syn_hurricane, syn_fireplace, syn_skyscraper]
bodyparts = [syn_hand, syn_nose, syn_leg, syn_toe, syn_arm, syn_finger, syn_foot, syn_ear, syn_eye, syn_elbow, syn_nail, syn_knee]
category = faces + scenes + bodyparts

# Get Scores
kanwisher_scores = get_lch_similarity(category)

# Save as matrix
ob = len(category)
rdm = np.zeros([ob, ob])
for ind1, o1 in enumerate(category):
    for ind2, o2 in enumerate(category):
        rdm[ind1, ind2] = kanwisher_scores[(o1, o2)]
pd.DataFrame(rdm).to_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_facescenebody.csv', index=category)

# Seaborn heatmap
df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_facescenebody_headings.csv', index_col=0)
fig,ax = plt.subplots(figsize=(7,7))
cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
sns.set(font_scale=0.4)
plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_KanwisherDowning&ordered_r.pdf')
plt.close()


# How generic colour palette maps were made from normalised data. Note df/max, no cmap specification. Map saved as 'category&ordered.pdf' #

#df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/rsm_facescenebody_headings.csv', index_col=0)
#fig,ax = plt.subplots(figsize=(7,7))
#sns.heatmap(df/3.63758616, center=0.05, ax=ax, xticklabels=True, yticklabels=True)
#sns.set(font_scale=0.4)
#plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_KanwisherDowning&ordered.pdf')
#plt.close()



# Script for how diverging palette pdfs were made: #
# RSM data not normalised, saved as 'category&prdered_r.pdf'. _r denotes inverted palette.

#df = pd.read_csv('/Users/brendafinlay/Documents/Cusack_Lab/ordered_konklematrix_272_headings.csv', index_col=0)
#fig,ax = plt.subplots(figsize=(15,15))
# To create contrasting colours for high and low scores, keeping centre light i.e. diverging colour palette. Saved as category&ordered_r.pdf
#cmap = sns.diverging_palette(240, 10, n=9, as_cmap=True)
#sns.heatmap(df, center=1.5, ax=ax, xticklabels=True, yticklabels=True, cmap=cmap)
#sns.set(font_scale= 0.25)
#plt.savefig('/Users/brendafinlay/Documents/Cusack_Lab/heatmap_konkle&ordered_r.pdf')
#plt.close()
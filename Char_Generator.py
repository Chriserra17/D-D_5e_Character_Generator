Character_Level = 1
def Dice_Roller():
    import random
    dice_counter = 0
    list1 = []
    while dice_counter < 4:
        b = random.randint(1, 6)
        list1.append(b)
        dice_counter += 1
    exit
    list1.sort()
    list1.pop(0)
    d = sum(list1)
    return d
    # Stat_Gen will run the Dice_Roller 6 times, in order to get the stats for the character.


def Stat_Gen():
    a = 0
    list2 = []
    while a <= 5:
        b = int(Dice_Roller())
        list2.append(b)
        a += 1
    exit
    list2.sort(reverse=True)
    return list2
    # Class_Gen will randomly select a class from list3


def Class_Gen():
    import random
    global Class_a
    list3 = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer',
             'Warlock', 'Wizard']
    b = random.randint(0, 11)
    return list3[b]
    # Race_Gen will randomly select a race for the character.


def Race_Gen():
    import random
    list4 = ['Human', 'Half-Orc', 'Half-Elf', 'Elf', 'Dwarf', 'Tiefling', 'Dragonborn', 'Halfling', 'Gnome']
    b = random.randint(0, 8)
    return list4[b]
    # Sex_Gen will randomly select the sex of the character.


def Sex_Gen():
    import random
    list5 = ['Male', 'Female']
    b = random.randint(0, 1)
    return list5[b]
    # Stat Assign, just assign the highest Stat_Gen scores relevant to it's class.


def Stat_Assign():
    global Class_a, Stat
    Class_a = Class_Gen()
    Stat = Stat_Gen()
    f = {}
    if str('Barbarian') == Class_a:
        f['Str'] = Stat[0]
        f['Dex'] = Stat[2]
        f['Con'] = Stat[1]
        f['Int'] = Stat[4]
        f['Wis'] = Stat[3]
        f['Cha'] = Stat[5]
    elif str('Bard') == Class_a:
        f['Str'] = Stat[5]
        f['Dex'] = Stat[1]
        f['Con'] = Stat[2]
        f['Int'] = Stat[4]
        f['Wis'] = Stat[3]
        f['Cha'] = Stat[0]
    elif str('Cleric') == Class_a:
        f['Str'] = Stat[1]
        f['Dex'] = Stat[5]
        f['Con'] = Stat[2]
        f['Int'] = Stat[4]
        f['Wis'] = Stat[0]
        f['Cha'] = Stat[3]
    elif str('Druid') == Class_a:
        f['Str'] = Stat[5]
        f['Dex'] = Stat[2]
        f['Con'] = Stat[1]
        f['Int'] = Stat[3]
        f['Wis'] = Stat[0]
        f['Cha'] = Stat[4]
    elif str('Fighter') == Class_a:
        import random
        g = random.randint(0, 1)
        if g == 0:
            f['Str'] = Stat[0]
            f['Dex'] = Stat[2]
            f['Con'] = Stat[1]
            f['Int'] = Stat[3]
            f['Wis'] = Stat[5]
            f['Cha'] = Stat[4]
        else:
            f['Str'] = Stat[2]
            f['Dex'] = Stat[0]
            f['Con'] = Stat[1]
            f['Int'] = Stat[5]
            f['Wis'] = Stat[4]
            f['Cha'] = Stat[3]
    elif str('Monk') == Class_a:
        f['Str'] = Stat[3]
        f['Dex'] = Stat[0]
        f['Con'] = Stat[2]
        f['Int'] = Stat[5]
        f['Wis'] = Stat[1]
        f['Cha'] = Stat[4]
    elif str('Paladin') == Class_a:
        import random
        h = random.randint(0, 3)
        if h == 0:
            f['Str'] = Stat[0]
            f['Dex'] = Stat[5]
            f['Con'] = Stat[2]
            f['Int'] = Stat[3]
            f['Wis'] = Stat[4]
            f['Cha'] = Stat[1]
        elif h == 1:
            f['Str'] = Stat[1]
            f['Dex'] = Stat[5]
            f['Con'] = Stat[2]
            f['Int'] = Stat[3]
            f['Wis'] = Stat[4]
            f['Cha'] = Stat[0]
        elif h == 2:
            f['Str'] = Stat[0]
            f['Dex'] = Stat[5]
            f['Con'] = Stat[1]
            f['Int'] = Stat[3]
            f['Wis'] = Stat[4]
            f['Cha'] = Stat[2]
        elif h == 3:
            f['Str'] = Stat[2]
            f['Dex'] = Stat[5]
            f['Con'] = Stat[1]
            f['Int'] = Stat[3]
            f['Wis'] = Stat[4]
            f['Cha'] = Stat[0]
    elif str('Ranger') == Class_a:
        f['Str'] = Stat[3]
        f['Dex'] = Stat[0]
        f['Con'] = Stat[2]
        f['Int'] = Stat[5]
        f['Wis'] = Stat[1]
        f['Cha'] = Stat[4]
    elif str('Rogue') == Class_a:
        f['Str'] = Stat[5]
        f['Dex'] = Stat[0]
        f['Con'] = Stat[2]
        f['Int'] = Stat[1]
        f['Wis'] = Stat[4]
        f['Cha'] = Stat[3]
    elif str('Sorcerer') == Class_a:
        f['Str'] = Stat[5]
        f['Dex'] = Stat[4]
        f['Con'] = Stat[1]
        f['Int'] = Stat[2]
        f['Wis'] = Stat[3]
        f['Cha'] = Stat[0]
    elif str('Warlock') == Class_a:
        f['Str'] = Stat[4]
        f['Dex'] = Stat[2]
        f['Con'] = Stat[1]
        f['Int'] = Stat[5]
        f['Wis'] = Stat[3]
        f['Cha'] = Stat[0]
    elif str('Wizard') == Class_a:
        import random
        h = random.randint(0, 2)
        if h == 0:
            f['Str'] = Stat[4]
            f['Dex'] = Stat[5]
            f['Con'] = Stat[1]
            f['Int'] = Stat[0]
            f['Wis'] = Stat[2]
            f['Cha'] = Stat[3]
        elif h == 1:
            f['Str'] = Stat[3]
            f['Dex'] = Stat[1]
            f['Con'] = Stat[2]
            f['Int'] = Stat[0]
            f['Wis'] = Stat[5]
            f['Cha'] = Stat[4]
        else:
            f['Str'] = Stat[5]
            f['Dex'] = Stat[4]
            f['Con'] = Stat[2]
            f['Int'] = Stat[0]
            f['Wis'] = Stat[3]
            f['Cha'] = Stat[1]
    return f
    # Now we attempt to assign sub races, so that I can then give ability bonuses.


def Sub_Race():
    race = []
    global Race_a
    global Race
    Race_a = str(Race_Gen())
    if str('Dwarf') == Race_a:
        import random
        Area = ('Hill Dwarf', 'Mountain Dwarf')
        s = random.randint(0, 1)
        race.append(Area[s])
    elif str('Elf') == Race_a:
        import random
        Area = ['High Elf', 'Wood Elf', 'Dark Elf (Drow)']
        s = random.randint(0, 2)
        race.append(Area[s])
    elif str('Halfling') == Race_a:
        import random
        Area = ['Lightfoot Halfling', 'Stout Halfling']
        s = random.randint(0, 1)
        race.append(Area[s])
    elif str('Human') == Race_a:
        import random
        Area = ['Calashite Human', 'Chondatan Human', 'Damaran Human', 'Illuskan Human', 'Mulan Human', 'Rashemi Human',
                'Shou Human', 'Tethyrian Human', 'Turami Human', 'Human']
        s = random.randint(0, 9)
        race.append(Area[s])
    elif str('Dragonborn') == Race_a:
        import random
        ancestry = ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White']
        s = random.randint(0, 9)
        race.append(ancestry[s] + ' ' + 'Dragonborn')
    elif str('Gnome') == Race_a:
        import random
        Area = ['Forest Gnome', 'Rock Gnome']
        s = random.randint(0, 1)
        race.append(Area[s])
    elif str('Half-Elf'):
        import random
        Area = ['Diplomat Half-Elf', 'Wanderer Half-Elf', 'Half-Elf']
        s = random.randint(0, 2)
        race.append(Area[s])
    elif str('Half-Orc') == Race_a:
        race.append('Half-Orc')
    elif str('Tiefling') == Race_a:
        race.append('Tiefling')
    return race[0]
    # Here we will modify the stats of the character based on it's race. Giving them that sweet Ability Score Increase.


def Stat_Modifier():
    import random
    #    import time
    global Race
    global Ability_a
    Race = Sub_Race()
    Ability_a = Stat_Assign()
    # alpha = dict(Ability_a)
    # The following print was for testing if the script was adding the race stats.
    #    print('Original Stats ' + str(Ability_a))
    #    time.sleep(3)
    if str('Hill Dwarf') == Race:
        Ability_a['Con'] = Ability_a['Con'] + 2
        Ability_a['Wis'] = Ability_a['Wis'] + 1
    elif str('Mountain Dwarf') == Race:
        Ability_a['Con'] = Ability_a['Con'] + 2
        Ability_a['Str'] = Ability_a['Str'] + 2
    elif str('High Elf') == Race:
        Ability_a['Int'] = Ability_a['Int'] + 1
        Ability_a['Dex'] = Ability_a['Dex'] + 2
    elif str('Wood Elf') == Race:
        Ability_a['Dex'] = Ability_a['Dex'] + 2
        Ability_a['Wis'] = Ability_a['Wis'] + 1
    elif str('Dark Elf (Drow)') == Race:
        Ability_a['Dex'] = Ability_a['Dex'] + 2
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    elif str('Lightfoot Halfling') == Race:
        Ability_a['Dex'] = Ability_a['Dex'] + 2
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    elif str('Stout Halfling') == Race:
        Ability_a['Dex'] = Ability_a['Dex'] + 2
        Ability_a['Con'] = Ability_a['Con'] + 1
    elif str('Gnome') == Race:
        Ability_a['Int'] = Ability_a['Int'] + 2
    elif str('Forest Gnome') == Race:
        Ability_a['Int'] = Ability_a['Int'] + 2
        Ability_a['Dex'] = Ability_a['Dex'] + 1
    elif str('Rock Gnome') == Race:
        Ability_a['Int'] = Ability_a['Int'] + 2
        Ability_a['Con'] = Ability_a['Con'] + 1
    elif str('Half-Orc') == Race:
        Ability_a['Str'] = Ability_a['Str'] + 2
        Ability_a['Con'] = Ability_a['Con'] + 1
    elif str('Tiefling') == Race:
        Ability_a['Int'] = Ability_a['Int'] + 1
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    elif str('Half-Elf') == Race:
        Ability_a['Cha'] = Ability_a['Cha'] + 2
        import random
        l = ['Str', 'Dex', 'Con', 'Int', 'Wis']
        s = random.randint(0, 4)
        d = random.randint(0, 4)
        Ability_a[l[s]] = Ability_a[l[s]] + 1
        Ability_a[l[d]] = Ability_a[l[d]] + 1
    elif str('Human') == Race:
        Ability_a['Str'] = Ability_a['Str'] + 1
        Ability_a['Dex'] = Ability_a['Dex'] + 1
        Ability_a['Con'] = Ability_a['Con'] + 1
        Ability_a['Int'] = Ability_a['Int'] + 1
        Ability_a['Wis'] = Ability_a['Wis'] + 1
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    elif str('Human') == Race.split()[1]:
        Ability_a['Str'] = Ability_a['Str'] + 1
        Ability_a['Dex'] = Ability_a['Dex'] + 1
        Ability_a['Con'] = Ability_a['Con'] + 1
        Ability_a['Int'] = Ability_a['Int'] + 1
        Ability_a['Wis'] = Ability_a['Wis'] + 1
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    elif str('Half-Elf') == Race.split()[1]:
        Ability_a['Cha'] = Ability_a['Cha'] + 2
        import random
        l = ['None', 'Str', 'Dex', 'Con', 'Int', 'Wis']
        s = random.randint(1, 4)
        d = random.randint(1, 4)
        Ability_a[l[s]] = Ability_a[l[s]] + 1
        Ability_a[l[d]] = Ability_a[l[d]] + 1
    elif str('Dragonborn') == Race.split()[1]:
        Ability_a['Str'] = Ability_a['Str'] + 2
        Ability_a['Cha'] = Ability_a['Cha'] + 1
    return Ability_a
    # Well, lt's start with gearing them up. Here we will begin with Generating Armor.


def Armor_Gen():
    import random
    global Ability_a
    armor = []
    if str('Barbarian') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Bard') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Cleric') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Druid') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Fighter') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        if Ability_a['Str'] >= Ability_a['Dex']:
            armor.append('Heavy Armor')
        else:
            s = random.randint(0, 1)
            armor.append(armor_a[s])
    elif str('Monk') == Class_a:
        armor.append('None')
    elif str('Paladin') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor', 'Heavy Armor']
        s = random.randint(0, 2)
        armor.append(armor_a[s])
    elif str('Ranger') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Rogue') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Sorcerer') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Warlock') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    elif str('Wizard') == Class_a:
        armor_a = ['Light Armor', 'Medium Armor']
        s = random.randint(0, 1)
        armor.append(armor_a[s])
    return armor
    # In order to start getting character skills, and health. I need to know the level
    # def Character_Level():
    #     Level_Input = os.environ['Level']
    #     if Level_Input == '':
    #         Level_Set = 1
    #     else:
    #         Level_Set = int(Level_Input)
    #     Character_Level = int(Leven)
    #     return Level_Set
    # Well now that we have the armor type that they will use, lets assign which piece it is that they're using


def Gear_Gen():
    global Armor
    import random
    global Character_Level
    Armor = Armor_Gen()
    # Character_Level = Character_Level()
    gear = []
    if any('Light' in s for s in Armor):
        if int(Character_Level) <= 10:
            s = random.randint(0, 1)
            if s == 0:
                gear.append('Light Armor: Padded | +11 AC + Dex Modifier')
            else:
                gear.append('Light Armor: Leather | +11 AC + Dex Modifier')
        else:
            s = random.randint(0, 2)
            if s == 0:
                gear.append('Light Armor: Padded | +11 AC + Dex Modifier')
            elif s == 1:
                gear.append('Light Armor: Leather | +11 AC + Dex Modifier')
            else:
                gear.append('Light Armor: Studded Leather | +12 + Dex Modifier')

    elif any('Medium' in s for s in Armor):
        if int(Character_Level) <= 10:
            s = random.randint(0, 1)
            if s == 0:
                gear.append('Medium Armor: Hide | +12 AC + Dex Modifier')
            else:
                gear.append('Medium Armor: Chain Shirt | +13 AC + Dex Modifier')
        else:
            s = random.randint(0, 4)
            if s == 0:
                gear.append('Medium Armor: Hide | +12 AC + Dex Modifier')
            elif s == 1:
                gear.append('Medium Armor: Chain Shirt | +13 AC + Dex Modifier')
            elif s == 2:
                gear.append('Medium Armor: Scale Mail | +14 AC + Dex Modifier')
            elif s == 3:
                gear.append('Medium Armor: Breastplate | +14 AC + Dex Modifier')
            else:
                gear.append('Medium Armor: Half Plate | +14 AC + Dex Modifier')
    elif any('Heavy' in s for s in Armor):
        if int(Character_Level) <= 10:
            s = random.randint(0, 1)
            if s == 0:
                gear.append('Heavy Armor: Ring Mail | +14 AC')
            elif s == 1:
                gear.append('Heavy Armor: Chain Mail | +16 AC')
        else:
            s = random.randint(0, 3)
            if s == 0:
                gear.append('Heavy Armor: Ring Mail | +14 AC')
            elif s == 1:
                gear.append('Heavy Armor: Chain Mail | +16 AC')
            elif s == 2:
                gear.append('Heavy Armor: Splint | +17 AC')
            else:
                gear.append('Heavy Armor: Plate | +18 AC')
    else:
        gear.append('None')
    return gear
    # Creating some variables and functions to make the next step more pythonic.


dagger = 'Dagger: 1d4 Piercing | Finesse | Light | Thrown (range 20/60)'
greataxe = 'Greataxe: 1d8 Slashing | Heavy Two-Handed'
handaxe = 'Handaxe: 1d6 Slashing | Light | Thrown (Range 20/60)'
rapier = 'Rapier: 1d8 Piercing | Finesse'
javelin = 'Javeling: 1d6 Piercing | Thrown (Range 20/60)'
explorer = "Explorer's Pack"
entertainer = "Entertainer's Pack"
longsword = 'Longsword: 1d8 Slashing | Versatile (1d10)'
diplomat = "Diplomat's Pack"
holy_symbol = 'Holy Symbol'
mace = 'Mace: 1d6 Bludgeoning'
warhammer = 'Warhammer: 1d8 Bludgeoning | Versatile (1d10)'
shield = 'Shield | +2 AC'


# Function for Martial Melee Weapons
def Martial_Melee_Weapon():
    import random
    Held = []
    d = random.randint(0, 16)
    if d == 0:
        Held.append('Battleaxe: 1d8 Slashing | Varsatile (1d10)')
    elif d == 1:
        Held.append('Flail: 1d8 Bludgeoning')
    elif d == 2:
        Held.append('Glaive: 1d10 Slashing | Heavy | Reach | Two-Handed')
    elif d == 3:
        Held.append('Greatsword: 2d6 Slashing | Heavy | Two-Handed')
    elif d == 4:
        Held.append('Halberd: 1d10 Slashing | Heavy | Reach | Two-Handed')
    elif d == 5:
        Held.append('Lance: 1d12 Piercing | Reach | Special')
    elif d == 6:
        Held.append('Longsword: 1d8 Slashing | Versatile (1d10)')
    elif d == 7:
        Held.append('Maul: 2d6 Bludgeoning | Heavy | Two-Handed')
    elif d == 8:
        Held.append('Morningstar: 1d8 Piercing')
    elif d == 9:
        Held.append('Pike: 1d10 Piercing | Heavy | Reach | Two-Handed')
    elif d == 10:
        Held.append('Rapier: 1d8 Piercing | Finesse')
    elif d == 11:
        Held.append('Scimitar: 1d6 Slashing | Finesse | Light')
    elif d == 12:
        Held.append('Shortsword: 1d6 Piercing | Finesse | Light')
    elif d == 13:
        Held.append('Trident: 1d6 Piercing | Thrown (Range 20/60) | Versatile (1d8)')
    elif d == 14:
        Held.append('War Pick: 1d8 Piercing')
    elif d == 15:
        Held.append('Warhammer: 1d8 Bludgeoning | Versatile (1d10)')
    elif d == 16:
        Held.append('Whip: 1d4 Slashing | Finesse | Reach')
    return Held[0]


# Now a Martial Weapon that includes range
def Martial_Weapon():
    import random
    Held = []
    d = random.randint(0, 21)
    if d == 0:
        Held.append('Battleaxe: 1d8 Slashing | Varsatile (1d10)')
    elif d == 1:
        Held.append('Flail: 1d8 Bludgeoning')
    elif d == 2:
        Held.append('Glaive: 1d10 Slashing | Heavy | Reach | Two-Handed')
    elif d == 3:
        Held.append('Greatsword: 2d6 Slashing | Heavy | Two-Handed')
    elif d == 4:
        Held.append('Halberd: 1d10 Slashing | Heavy | Reach | Two-Handed')
    elif d == 5:
        Held.append('Lance: 1d12 Piercing | Reach | Special')
    elif d == 6:
        Held.append('Longsword: 1d8 Slashing | Versatile (1d10)')
    elif d == 7:
        Held.append('Maul: 2d6 Bludgeoning | Heavy | Two-Handed')
    elif d == 8:
        Held.append('Morningstar: 1d8 Piercing')
    elif d == 9:
        Held.append('Pike: 1d10 Piercing | Heavy, Reach | Two-Handed')
    elif d == 10:
        Held.append('Rapier: 1d8 Piercing | Finesse')
    elif d == 11:
        Held.append('Scimitar: 1d6 Slashing | Finesse | Light')
    elif d == 12:
        Held.append('Shortsword: 1d6 Piercing | Finesse | Light')
    elif d == 13:
        Held.append('Trident: 1d6 Piercing | Thrown (Range 20/60) | Versatile (1d8)')
    elif d == 14:
        Held.append('War Pick: 1d8 Piercing')
    elif d == 15:
        Held.append('Warhammer: 1d8 Bludgeoning | Versatile (1d10)')
    elif d == 16:
        Held.append('Whip: 1d4 Slashing | Finesse | Reach')
    elif d == 17:
        Held.append('Blowgun: 1 Piercing | Ammunition (Range 25/100) | Loading')
    elif d == 18:
        Held.append('Hand Crossbow: 1d6 Piercing | Ammunition (Range 30/120) | Light | Loading | 10 Bolts')
    elif d == 19:
        Held.append(
            'Heavy Crossbow: 1d8 Piercing | Ammunition (Range 100/400) | Heavy | Loading | Two Handed | 10 Bolts')
    elif d == 20:
        Held.append('Longbow: 1d8 Piercing | Ammunition (Range 150/600) | Heavy | Two-Handed')
    elif d == 21:
        Held.append('Net: No Damage | Special | Thrown (Range 5/15)')
    return Held[0]


# Now a funtion for Simple Melee Weapons
def Simple_Melee_Weapon():
    import random
    Held = []
    g = random.randint(0, 9)
    if g == 0:
        Held.append('Club: 1d4 Bludgeoning | Light')
    elif g == 1:
        Held.append('Dagger: 1d4 Piercing | Finesse | Light | Thrown (range 20/60)')
    elif g == 2:
        Held.append('Greatclub: 1d8 Bludgeoning | Two-Handed')
    elif g == 3:
        Held.append('Handaxe: 1d6 Slashing | Light | Thrown (Range 20/60)')
    elif g == 4:
        Held.append('Javeling: 1d6 Piercing | Thrown (Range 20/60)')
    elif g == 5:
        Held.append('Light Hammer: 1d4 Bludgeoning | Light | Thrown (Range 20/60)')
    elif g == 6:
        Held.append('Mace: 1d6 Bludgeoning')
    elif g == 7:
        Held.append('Quarterstaff: 1d6 Bludgeoning | Versatile (1d8)')
    elif g == 8:
        Held.append('Sickle: 1d4 Slashing | Light')
    elif g == 9:
        Held.append('Spear: 1d6 Piercing | Thrown (Range 20/60) | Versatile (1d8)')
    return Held[0]


# Now Making Simple Weapons counting the ranged ones.
def Simple_Weapon():
    import random
    Held = []
    g = random.randint(0, 13)
    if g == 0:
        Held.append('Club: 1d4 Bludgeoning | Light')
    elif g == 1:
        Held.append('Dagger: 1d4 Piercing | Finesse | Light | Thrown (range 20/60)')
    elif g == 2:
        Held.append('Greatclub: 1d8 Bludgeoning | Two-Handed')
    elif g == 3:
        Held.append('Handaxe: 1d6 Slashing | Light | Thrown (Range 20/60)')
    elif g == 4:
        Held.append('Javeling: 1d6 Piercing | Thrown (Range 20/60)')
    elif g == 5:
        Held.append('Light Hammer: 1d4 Bludgeoning | Light | Thrown (Range 20/60)')
    elif g == 6:
        Held.append('Mace: 1d6 Bludgeoning')
    elif g == 7:
        Held.append('Quarterstaff: 1d6 Bludgeoning | Versatile (1d8)')
    elif g == 8:
        Held.append('Sickle: 1d4 Slashing | Light')
    elif g == 9:
        Held.append('Spear: 1d6 Piercing | Thrown (Range 20/60) | Versatile (1d8)')
    elif g == 10:
        Held.append('Light Crossbow: 1d8 Piercing | Ammunition (Range 80/320) Loading | Two-Handed | 10 Bolts')
    elif g == 11:
        Held.append('Dart: 1d4 Piercing | Finesse, Thrown (Range 20/60) | Ammo 10')
    elif g == 12:
        Held.append('Shortbow: 1d6 Piercing | Ammunition (Range 80/320) | Two Handed | 20 Arrows')
    elif g == 13:
        Held.append('Sling: 1d4 Bludgeoning | Ammunition (Range 30/120)')
    return Held[0]


# Now we can Generate Weapons, and items that they're carrying, I went with the options listed in the Player's Handbook.
def Weapon_Assign():
    import random
    Held = []
    if str('Barbarian') == Class_a:
        Held.append(str(explorer))
        Held.append(str(javelin))
        Held.append(str(javelin))
        Held.append(str(javelin))
        Held.append(str(javelin))
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(greataxe))
        elif s == 1:
            Held.append(str(Martial_Melee_Weapon))
        f = random.randint(0, 1)
        if f == 0:
            Held.append(str(handaxe))
            Held.append(str(handaxe))
        elif f == 1:
            Held.append(str(Simple_Weapon))
    if str('Bard') == Class_a:
        Held.append(str(dagger))
        s = random.randint(0, 2)
        if s == 0:
            Held.append(str(rapier))
        elif s == 1:
            Held.append(str(longsword))
        elif s == 2:
            Held.append(str(Simple_Weapon))
        d = random.randint(0, 1)
        if d == 0:
            Held.append(str(diplomat))
        elif d == 1:
            Held.append(str(entertainer))
        c = random.randint(0, 1)
        if c == 0:
            Held.append('Lute')
        elif c == 1:
            list_4 = ['Fiddle', 'Flute', 'Bagpipes']
            e = random.randint(0, 2)
            Held.append(list_4[e])
    elif str('Cleric') == Class_a:
        Held.append(str(holy_symbol))
        Held.append(str(shield))
        s = random.randint(0, 1)
        if s == 0:
            Held.append('Mace: 1d6 Bludgeoning')
        elif s == 1:
            Held.append(str(warhammer))
        d = random.randint(0, 1)
        if d == 0:
            Held.append('Light Crossbow: 1d6 Piercing | Ammunition (20 Bolts)')
        elif d == 1:
            Held.append(str(Simple_Weapon))
        f = random.randint(0, 1)
        if f == 0:
            Held.append("Priest's Pack")
        elif f == 1:
            Held.append("Explorer's Pack")
    elif str('Druid') == Class_a:
        Held.append("Explorer's Pack")
        Held.append('Druidic Focus')
        s = random.randint(0, 1)
        if s == 0:
            Held.append('Scimitar: 1d6 Slashing | Finesse | Light')
        elif s == 1:
            Held.append(str(Simple_Melee_Weapon))
        d = random.randint(0, 1)
        if d == 0:
            Held.append(str(shield))
        elif d == 1:
            Held.append(str(Simple_Weapon))
    elif str('Fighter') == Class_a:
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(Simple_Weapon))
            Held.append(str(shield))
        elif s == 1:
            Held.append(str(Simple_Weapon))
            Held.append(str(Simple_Weapon))
        f = random.randint(0, 1)
        if f == 0:
            Held.append('Light Crossbow: 1d6 Piercing | Ammunition (20 Bolts)')
        elif f == 1:
            Held.append(str(handaxe))
            Held.append(str(handaxe))
        g = random.randint(0, 1)
        if g == 0:
            Held.append("Dungeoneer's Pack")
        elif g == 1:
            Held.append("Explorer's Pack")
        t = random.randint(0, 1)
        if any('Medium' in s for s in Armor):
            Held.append('Longbow: 1d8 Piercing | Ammunition (Range 150/600) | Heavy | Two-Handed | 20 Arrows')
    elif str('Monk') == Class_a:
        Held.append('Dart: 1d4 Piercing | Finesse | Thrown (Range 10/60) | Ammo 10')
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(Simple_Weapon))
        elif s == 1:
            Held.append('Shortsword: 1d6 Piercing | Finesse | Light')
        j = random.randint(0, 1)
        if j == 0:
            Held.append("Dungeoneer's Pack")
        elif j == 1:
            Held.append("Explorer's Pack")
    elif str('Paladin') == Class_a:
        Held.append(holy_symbol)
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(Martial_Weapon))

            Held.append(str(shield))
        elif s == 1:
            Held.append(str(Martial_Weapon))
            Held.append(str(Martial_Weapon))
        b = random.randint(0, 1)
        if b == 0:
            Held.append(str(Simple_Melee_Weapon))
        if b == 1:
            Held.append(str(javelin))
            Held.append(str(javelin))
            Held.append(str(javelin))
            Held.append(str(javelin))
            Held.append(str(javelin))
        o = random.randint(0, 1)
        if o == 0:
            Held.append("Priest's Pack")
        elif o == 1:
            Held.append("Explorer's Pack")
    elif str('Ranger') == Class_a:
        Held.append("Longbow: 1d8 Piercing | Ammunition (Range 150/600) | Heavy | Two-Handed")
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(longsword))
            Held.append(str(longsword))
        elif s == 1:
            Held.append(str(Simple_Melee_Weapon))
            Held.append(str(Simple_Melee_Weapon))
        b = random.randint(0, 1)
        if b == 0:
            Held.append("Dungeoneer's Pack")
        elif b == 1:
            Held.append("Explorer's Pack")
    elif str('Rogue') == Class_a:
        Held.append("Thieve's Tool")
        Held.append(str(dagger))
        Held.append(str(dagger))
        s = random.randint(0, 1)
        if s == 0:
            Held.append(str(rapier))
        elif s == 1:
            Held.append("Shortsword: 1d6 Piercing | Finesse | Light")
        e = random.randint(0, 1)
        if e == 0:
            Held.append("Shortbow: 1d6 Piercing | Ammunition (Range 80/320 | Ammo 20")
        elif e == 1:
            Held.append("Shortsword: 1d6 Piercing | Finesse | Light")
        w = random.randint(0, 2)
        if w == 0:
            Held.append("Burglar's Pack")
        elif w == 1:
            Held.append("Dungeoneer's Pack")
        elif w == 2:
            Held.append("Explorer's Pack")
    elif str('Sorcerer') == Class_a:
        Held.append(str(dagger))
        Held.append(str(dagger))
        s = random.randint(0, 1)
        if s == 0:
            Held.append("Light Crossbow: 1d8 Piercing | Ammunition (Range 80/320) Loading | Two-Handed | 10 Bolts")
        elif s == 1:
            Held.append(str(Simple_Weapon))
        e = random.randint(0, 1)
        if e == 0:
            Held.append("Component Pouch")
        elif e == 1:
            Held.append("Arcane Focus")
        w = random.randint(0, 1)
        if w == 0:
            Held.append("Dungeoneer's Pack")
        elif w == 1:
            Held.append("Explorer's Pack")
    elif str('Warlock') == Class_a:
        Held.append(str(dagger))
        Held.append(str(dagger))
        Held.append(str(Simple_Weapon))
        s = random.randint(0, 1)
        if s == 0:
            Held.append("Light Crossbow: 1d6 Piercing | Ammunition (20 Bolts)")
        elif s == 1:
            Held.append(str(Simple_Weapon))
        e = random.randint(0, 1)
        if e == 0:
            Held.append("Component Pouch")
        elif e == 1:
            Held.append("Arcane Focus")
        w = random.randint(0, 1)
        if w == 0:
            Held.append("Scholar's Pack")
        elif w == 1:
            Held.append("Dungeoneer's Pack")
    elif str('Wizard') == Class_a:
        Held.append('Spellbook')
        s = random.randint(0, 1)
        if s == 0:
            Held.append("Quarterstaff: 1d6 Bludgeoning | Versatile (1d8)")
        elif s == 1:
            Held.append(str(dagger))
        e = random.randint(0, 1)
        if e == 0:
            Held.append("Component Pouch")
        elif e == 1:
            Held.append("Arcane Focus")
        w = random.randint(0, 1)
        if w == 0:
            Held.append("Scholar's Pack")
        elif w == 1:
            Held.append("Explorer's Pack")
    return str(Held)


# Assigning Class hit dice
def Hit_Dice():
    Hit_Dice = []
    if str('Barbarian') == Class_a:
        Hit_Dice = 12
    elif str('Bard') == Class_a:
        Hit_Dice = 8
    elif str('Cleric') == Class_a:
        Hit_Dice = 8
    elif str('Druid') == Class_a:
        Hit_Dice = 8
    elif str('Fighter') == Class_a:
        Hit_Dice = 10
    elif str('Monk') == Class_a:
        Hit_Dice = 8
    elif str('Paladin') == Class_a:
        Hit_Dice = 10
    elif str('Ranger') == Class_a:
        Hit_Dice = 10
    elif str('Rogue') == Class_a:
        Hit_Dice = 8
    elif str('Sorcerer') == Class_a:
        Hit_Dice = 6
    elif str('Warlock') == Class_a:
        Hit_Dice = 8
    elif str('Wizard') == Class_a:
        Hit_Dice = 6
    return Hit_Dice


# And now to Get the health of the character depending on their level.
def Hit_Dice_Total():
    import random
    global Hit_Dice
    global Character_Level
    Health = []
    if int(Character_Level) == 1:
        List_One = []
        if Ability_a['Con'] == 1:
            List_One.append(Hit_Dice - 4)
        elif Ability_a['Con'] >= 4 and Ability_a['Con'] <= 5:
            List_One.append(Hit_Dice - 3)
        elif Ability_a['Con'] >= 6 and Ability_a['Con'] <= 7:
            List_One.append(Hit_Dice - 2)
        elif Ability_a['Con'] >= 8 and Ability_a['Con'] <= 9:
            List_One.append(Hit_Dice - 1)
        elif Ability_a['Con'] >= 10 and Ability_a['Con'] <= 11:
            List_One.append(Hit_Dice)
        elif Ability_a['Con'] >= 12 and Ability_a['Con'] <= 13:
            List_One.append(Hit_Dice + 1)
        elif Ability_a['Con'] >= 14 and Ability_a['Con'] <= 15:
            List_One.append(Hit_Dice + 2)
        elif Ability_a['Con'] >= 16 and Ability_a['Con'] <= 17:
            List_One.append(Hit_Dice + 3)
        elif Ability_a['Con'] >= 18 and Ability_a['Con'] <= 19:
            List_One.append(Hit_Dice + 4)
        elif Ability_a['Con'] >= 20 and Ability_a['Con'] <= 21:
            List_One.append(Hit_Dice + 5)
        Health = sum(List_One)
    elif int(Character_Level) >= 2:
        Level_Counter = int(Character_Level) - 1
        a = 0
        List_One = []
        while a < Level_Counter:
            b = random.randint(1, Hit_Dice)
            if Ability_a['Con'] == 1:
                List_One.append(b - 4)
            elif Ability_a['Con'] >= 4 and Ability_a['Con'] <= 5:
                List_One.append(b - 3)
            elif Ability_a['Con'] >= 6 and Ability_a['Con'] <= 7:
                List_One.append(b - 2)
            elif Ability_a['Con'] >= 8 and Ability_a['Con'] <= 9:
                List_One.append(b - 1)
            elif Ability_a['Con'] >= 10 and Ability_a['Con'] <= 11:
                List_One.append(b)
            elif Ability_a['Con'] >= 12 and Ability_a['Con'] <= 13:
                List_One.append(b + 1)
            elif Ability_a['Con'] >= 14 and Ability_a['Con'] <= 15:
                List_One.append(b + 2)
            elif Ability_a['Con'] >= 16 and Ability_a['Con'] <= 17:
                List_One.append(b + 3)
            elif Ability_a['Con'] >= 18 and Ability_a['Con'] <= 19:
                List_One.append(b + 4)
            elif Ability_a['Con'] >= 20 and Ability_a['Con'] <= 21:
                List_One.append(b + 5)
            a += 1
        exit
        List_One.append(Hit_Dice)
        Health = sum(List_One)
    return Health


# And now for Spells.
def Spell_Gen():
    import random
    global Class_a
    global Character_Level
    global Ability_a
    spells_known = []
    AmountOfSpells = []
    Cantrips_List = []
    First_Level_List = []
    Second_Level_List = []
    Third_Level_List = []
    Fourth_Level_List = []
    Fifth_Level_List = []
    Sixth_Level_List = []
    Seventh_Level_List = []
    Eight_Level_List = []
    Ninth_Level_List = []
    if str('Bard') == Class_a:
        Cantrips_List = ['Blade Ward', 'Dancing Lights', 'Friends', 'Light', 'Mage Hand', 'Mending', 'Message',
                         'Minor Illusion',
                         'Prestidigitation', 'True Strike', 'Vicious Mockery']
        First_Level_List = ['Animal Friendship', 'Bane', 'Charm Person', 'Comprehend Languages', 'Cure Wounds',
                            'Detect Magic',
                            'Disguise Self', 'Dissonant Whispers', "Faerie Fire", 'Feather Fall', 'Healing Word',
                            'Heroism',
                            'Identify', 'Illusory Script', 'Longstrider', 'Silent Image', 'Sleep', 'Speak with Animals',
                            "Tasha's Hideous Laughter", 'Thunderwave', 'Unseen Servant']
        Second_Level_List = ['Animal Mssenger', "Blindness/Deafness", 'Calm Emotions', 'Cloud of Daggers',
                             'Crown of Madness',
                             'Detet Thoughts', 'Enhance Ability', 'Enthrall', 'Heat Metal', 'Hold Person',
                             'Invisibility',
                             'Knock', 'Lesser Restoration', 'Locate Animal or Plants', 'Locate Object', 'Magic Mouth',
                             'Phantasmal Force', 'See Invisibility', 'Shatter', 'Silence', 'Suggestion',
                             'Zone of Truth']
        Third_Level_List = ['Bestow Curse', 'Clairvoyance', 'Dispel Magic', 'Fear', 'Feign Death', 'Glyph of Warding',
                            'Hypnotic Pattern', "Leomund's Tiny Hut", 'Major Image', 'Nondetection', 'Plant Growth',
                            'Sending', 'Speak with Dead', 'Speak with Plants', 'Stinking Cloud', 'Tongues']
        Fourth_Level_List = ['Compulsion', 'Confusion', 'Dimension Door', 'Freedom of Movement', 'Greater Invisibility',
                             'Hallucinatory Terrain', 'Locate Creature', 'Polymorph']
        Fifth_Level_List = ['Animate Object', 'Awaken', 'Dominate Person', 'Dream', 'Geas', 'Greater Restoration',
                            'Hold Monster', 'Legend Lore', 'Mass Cure Wounds', 'Mislead', 'Modify Memory',
                            'Planar Binding',
                            'Raise Dead', 'Scrying', 'Seeming', 'Teleportation Circle']
        Sixth_Level_List = ['Eyebite', 'Find the Path', 'Guards and Wards', 'Mass Suggestion',
                            "Otto's Irresistible Dance",
                            'Programmed Illusion', 'True Seeing']
        Seventh_Level_List = ['Ethereal', 'Forcecage', 'Mirage Arcane', "Mordenkainen's Magnificent Mansion",
                              "Mordenkainen's Sword",
                              'Project Image', 'Regenerate', 'Resurrection', 'Symbol', 'Teleport']
        Eight_Level_List = ['Dominate Monster', 'Feeblemind', 'Glibness', 'Mind Blank', 'Power Word Stun']
        Ninth_Level_List = ['Foresight', 'Power Word Heal', 'Power Word Kill', 'True Polymorph']
        if int(Character_Level) == 1:
            AmountOfSpells = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [2, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [3, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [3, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [3, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [3, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [3, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [3, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [3, 4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif int(Character_Level) == 18:
            AmountOfSpells = [3, 4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif int(Character_Level) == 19:
            AmountOfSpells = [3, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif int(Character_Level) == 20:
            AmountOfSpells = [3, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Cleric') == Class_a:
        Cantrips_List = ['Guidance', 'Light', 'Mending', 'Resistance', 'Sacred Flame', 'Spare the Dying', 'Thaumaturgy']
        First_Level_List = ['Bane', 'Bless', 'Command', 'Create of Destroy Water', 'Cure Wounds',
                            'Detect Evil and Good',
                            'Detect Magic', 'Detect Poison or Disease', 'Guiding Bolt', 'Healing Word',
                            'Inflict Wounds',
                            'Protection from Evil and Good', 'Purify Food and Drink', 'Sanctuary', 'Shield of Faith']
        Second_Level_List = ['Aid', 'Augury', 'Blindness/Deafness', 'Calm Emotions', 'Continual Flame',
                             'Enhance Ability',
                             'Find Traps', 'Gentle Repose', 'Hold Person', 'Lesser Restoration', 'Locate Object',
                             'Prayer of Healing',
                             'Protection from Poison', 'Silence', 'Spiritual Weapon', 'Warding Bond', 'Zone of Truth']
        Third_Level_List = ['Animate Dead', 'Beacon of Hope', 'Bestow Curse', 'Clairvoyance', 'Create Food and Water',
                            'Daylight', 'Dispel Magic', 'Feign Death', 'Glyph of Warding', 'Magic Circle',
                            'Mass HEaling Word',
                            'Meld into Stone', 'Protection from Energy', 'Remove Curse', 'Revivify', 'Sending',
                            'Speak with Dead',
                            'Spirit Guardian', 'Tongues', 'Water Walk']
        Fourth_Level_List = ['Banishment', 'Control Water', 'Death Ward', 'Divination', 'Freedom of Movement',
                             'Guardian of Faith',
                             'Locate Creature', 'Stone Shape']
        Fifth_Level_List = ['Commune', 'Contagion', 'Dispel Eil and Good', 'Flame Strike', 'Geas',
                            'Greater Restoration',
                            'Hallow', 'Insect Plague', 'Legend Lore', 'Mass Cure Wounds', 'Planar Binding',
                            'Raise Dead',
                            'Scrying']
        Sixth_Level_List = ['Blade Barrier', 'Create Undead', 'Find the Path', 'Forbiddance', 'Harm', 'Heal',
                            'Heroes Feast',
                            'Planar Ally', 'True Seeing', 'Word of Recall']
        Seventh_Level_List = ['Conjure Celestial', 'Divine Word', 'Etherealness', 'Fire Storm', 'Plane Shift',
                              'Regenerate',
                              'Resurrection', 'Symbol']
        Eight_Level_List = ['Antimagic Field', 'Control Weather', 'Earthquake', 'Holy Aura']
        Ninth_Level_List = ['Astral Projection', 'Gate', 'Mass Heal', 'True Resurrection']
        if int(Character_Level) == 1:
            AmountOfSpells = [3, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [3, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [3, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [4, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [4, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [4, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [4, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [4, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [4, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif int(Character_Level) == 18:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif int(Character_Level) == 19:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif int(Character_Level) == 20:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 2, 2, 1, 1]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Druid') == Class_a:
        Cantrips_List = ['Druidcraft', 'Guidance', 'Mending', 'Poison Spray', 'Produce Flame', 'Resistance',
                         'Shillelagh', 'Thorn Whip']
        First_Level_List = ['Animal Friendship', 'Charm Person', 'Create or Destroy Water', 'Cure Wounds',
                            'Detect Magic', 'Detect Poison and Disease', 'Entangle',
                            'Faerie Fire', 'Fog Cloud', 'Goodberry', 'Healing Word', 'Jump', 'Longstrider',
                            'Purify Food and Drink', 'Speak with Animals', 'Thunderwave']
        Second_Level_List = ['Animal Messenger', 'Barkskin', 'Beast Sense', 'Darkvision', 'Enhance Ability',
                             'Find Traps', 'Flame Blade', 'Flaming Sphere',
                             'Gust of Wind', 'Heat Metal', 'Hold Person', 'Lesser Restoration',
                             'Locate Animals or Plants', 'Locate Object', 'Moonbeam', 'Pass without Trace',
                             'Protection from Poison', 'Spike Growth']
        Third_Level_List = ['Call Lightning', 'Conjure Anmals', 'Daylight', 'Dispel Magic', 'Feign Death',
                            'Meld into Stone', 'Plant Growth',
                            'Protection from Energy', 'Sleet Storm', 'Speak with Plants', 'Water Breathing',
                            'Water Walk', 'Wind Wall']
        Fourth_Level_List = ['Blight', 'Confusion', 'Conjure Minor Elemental', 'Conjure Woodland Beigns',
                             'Control Water',
                             'Dominate Beast', 'Freedom of Movement', 'Giant Insect', 'Grasping Vine',
                             'Hallucinatory Terrain', 'Ice Storm', 'Locate Creature',
                             'Polymorph', 'Stone Shape', 'Stoneskin', 'Wall of Fire']
        Fifth_Level_List = ['Antilife Shell', 'Awaken', 'Commune with Nature', 'Conjure Elemental', 'Contagion', 'Geas',
                            'Greater Restoration',
                            'Insect Plague', 'Mass Cure Wounds', 'Planar Binding', 'Reincarnate', 'Scrying',
                            'Tree Stride', 'Wall of Stone']
        Sixth_Level_List = ['Conjure Fey', 'Find the Path', 'Heal', "Heroes' Feast", 'Move Earth', 'Sunbeam',
                            'Transport via Plants',
                            'Wall of Thorns', 'Wind Walk']
        Seventh_Level_List = ['Fire Storm', 'Mirage Arcane', 'Plane Shift', 'Regenerate', 'Reverse Gravity']
        Eight_Level_List = ['Animal Shapes', 'Antipathy/Sympathy', 'Control Weather', 'Earthquake', 'Feeblemind',
                            'Sunburst', 'Tsunami']
        Ninth_Level_List = ['Foresight', 'Shapechange', 'Storm of Vengeance', 'True Resurrection']
        if int(Character_Level) == 1:
            AmountOfSpells = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [2, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [3, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [3, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [3, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [3, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [3, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [3, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [4, 4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif int(Character_Level) == 18:
            AmountOfSpells = [4, 4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif int(Character_Level) == 19:
            AmountOfSpells = [4, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif int(Character_Level) == 20:
            AmountOfSpells = [4, 4, 3, 3, 3, 3, 2, 2, 1, 1]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Paladin') == Class_a:
        First_Level_List = ['Bless', 'Command', 'Compelled Duel', 'Cure Wounds', 'Detect Evil and Good', 'Detect Magic',
                            'Detect Poison and Disease',
                            'Divine Favor', 'Heroism', 'Protection from Evil and Good', 'Purify Food and Drink',
                            'Searing Smite', 'Shield of Faith',
                            'Thunderous Smite', 'Wrathful Smite']
        Second_Level_List = ['Aid', 'Branding Smite', 'Find Steed', 'Lesser Restoration', 'Locate Object',
                             'Magical Weapon',
                             'Protection from Poison', 'Zone of Truth']
        Third_Level_List = ['Aura of Vitality', 'Blinding Smite', 'Create Food and Water', "Crusader's Mantle",
                            'Daylight',
                            'Dispel Magic', 'Elemental Weapon', 'Magic Circle', 'Remove Curse', 'Revivify']
        Fourth_Level_List = ['Aura of Life', 'Aura of Purify', 'Banishment', 'Death Ward', 'Locate Creatures',
                             'Staggering Smite']
        Fifth_Level_List = ['Banishment Smite', 'Circle of Power', 'Destructive Wave', 'Dispel Evil and Good', 'Geas',
                            'Raise Dead']
        if int(Character_Level) == 1:
            AmountOfSpells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [0, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [0, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [0, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [0, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [0, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [0, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [0, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [0, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [0, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Cantrips_List) == 18:
            AmountOfSpells = [0, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 19:
            AmountOfSpells = [0, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 20:
            AmountOfSpells = [0, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Ranger') == Class_a:
        First_Level_List = ['Alarm', 'Animal Friendship', 'Cure Wounds', 'Detect Magic', 'Detect Poison and Disease',
                            'Ensnaring Strike',
                            'Fog Cloud', 'Goodberry', 'Hail of Thorns', "Hunter's Mark", 'Jump', 'Longstrider',
                            'Speak with Animals']
        Second_Level_List = ['Animal Messenger', 'Barkskin', 'Beast Sense', 'Cordon of Arrows', 'Darkvision',
                             'Find Traps', 'Lesser Restoration',
                             'Locate Animals or Plants', 'Locate Object', 'Pass without Trace',
                             'Protection from Poison', 'Silence', 'Spike Growth']
        Third_Level_List = ['Conjure Animals', 'Conjure Barrage', 'Daylight', 'Lightning Arrow', 'Nondetection',
                            'Plant Growth',
                            'Protection from Energy', 'Speak with Plants', 'Water Breathing', 'Water Walk', 'Wind Wall']
        Fourth_Level_List = ['Conjure Woodland Beings', 'Freedom of Movement', 'Grasping Vine', 'Locate Creature',
                             'Stoneskin']
        Fifth_Level_List = ['Commune with Nature', 'Conjure Volley', 'Swifft Quiver', 'Tree Stride']
        if int(Character_Level) == 1:
            AmountOfSpells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [0, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [0, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [0, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [0, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [0, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [0, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [0, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [0, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [0, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 18:
            AmountOfSpells = [0, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 19:
            AmountOfSpells = [0, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 20:
            AmountOfSpells = [0, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Sorcerer') == Class_a:
        Cantrips_List = ['Acid Splash', 'Blade Ward', 'Chill Touch', 'Dancing Light', 'Fire Bolt', 'Friends', 'Light',
                         'Mage Hand',
                         'Mending', 'Message', 'Minor Illusion', 'Poison Spray', 'Prestidigitation', 'Ray of Frost',
                         'Shocking Grasp', 'True Strike']
        First_Level_List = ['Burning Hands', 'Charm Person', 'Chromatic Orb', 'Color Spray', 'Comprehend Languages',
                            'Detect Magic',
                            'Disguise Self', 'Expeditious Retreat', 'False Life', 'Feather Fall', 'Fog Cloud', 'Jump',
                            'Mage Armor', 'Magic Missile',
                            'Ray of Sickness', 'Shield', 'Silent Image', 'Sleep', 'Thunderwave', 'Witch Bolt']
        Second_Level_List = ['Alter Self', 'Blindness/Deafness', 'Blur', 'Cloud of Daggers', 'Crown of Madness',
                             'Darkness',
                             'Darkvision', 'Detect Thoughts', 'Enhance Ability', 'Enlarge/Reduce', 'Gust of Wind',
                             'Hold Person', 'Invisibility',
                             'Knock', 'Levitate', 'Mirror Image', 'Misty Step', 'Phantasmal Force', 'Scorching Ray',
                             'See Invisibility', 'Shatter', 'Spider Climb',
                             'Suggestion', 'Web']
        Third_Level_List = ['Blink', 'Clairvoyance', 'Counterspell', 'Daylight', 'Dispel Magic', 'Fear', 'Fireball',
                            'Fly', 'Gaseous Form',
                            'Haste', 'Hypnotic Pattern', 'Lightning Bolt', 'Major Image', 'Protection from Energy',
                            'Sleet Storm', 'Slow', 'Stinking Cloud',
                            'Tongues', 'Water Breathing', 'Water Walk']
        Fourth_Level_List = ['Banishment', 'Blight', 'Confusion', 'Dimension Door', 'Dominate Beast',
                             'Greater Invisibility',
                             'Ice Storm', 'Polymorph', 'Stoneskin', 'Wall of Fire']
        Fifth_Level_List = ['Animate Object', 'Cloudkill', 'Cone of Cold', 'Creation', 'Dominate Person',
                            'Hold Monster',
                            'Insect Plague', 'Seeming', 'Telekinesis', 'Teleportation Circle', 'Wall of Stone']
        Sixth_Level_List = ['Arcane Gate', 'Chain Lightning', 'Circle of Death', 'Disintegrate', 'Eyebite',
                            'Globe of Invulnerability',
                            'Mass Suggestion', 'Move Earth', 'Sunbeam', 'True Seeing']
        Seventh_Level_List = ['Delayed Blast Fireball', 'Etherealness', 'Finger of Death', 'Fire Storm', 'Plane Shift',
                              'Prismatic Spray', 'Reverse Gravity', 'Teleport']
        Eight_Level_List = ['Dominate Monster', 'Earthquake', 'Incendiary Cloud', 'Power Word Stun', 'Sunburst']
        Ninth_Level_List = ['Gate', 'Meteor Swarm', 'Power Word Kill', 'Time Stop', 'Wish']
        if int(Character_Level) == 1:
            AmountOfSpells = [4, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [4, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [4, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [5, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [5, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [5, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [5, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [5, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [5, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) == 11:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 12:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) == 13:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 14:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif int(Character_Level) == 15:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 16:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [6, 4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif int(Character_Level) == 18:
            AmountOfSpells = [6, 4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif int(Character_Level) == 19:
            AmountOfSpells = [6, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif int(Character_Level) == 20:
            AmountOfSpells = [6, 4, 3, 3, 3, 3, 2, 2, 1, 1]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Wizard') == Class_a:
        Cantrips_List = ['Acid Splash', 'Blade Ward', 'Chill Touch', 'Dancing Light', 'Fire Bolt', 'Friends', 'Light',
                         'Mage Hand',
                         'Mending', 'Message', 'Minor Illusion', 'Poison Spray', 'Prestidigitation', 'Ray of Frost',
                         'Shocking Grasp', 'True Strike']
        First_Level_List = ['Alarm', 'Burning Hand', 'Charm Person', 'Chromatic Orb', 'Color Spray',
                            'Comprehend Languages',
                            'Detect Magic', 'Disguise Self', 'Expeditious Retreat', 'False Life', 'Feather Fall',
                            'Find Familiar', 'Fog Cloud',
                            'Grease', 'Identify', 'Illusory Script', 'Jump', 'Longstrider', 'Mage Armor',
                            'Magic Missile', 'Protection from Evil and Good',
                            'Ray of Sickness', 'Shield', 'Silent Image', 'Sleep', "Tasha's Hideous Laughter",
                            "Tenser's Floating Disk", 'Thunderwave',
                            'Unseen Servant', 'Witch Bolt']
        Second_Level_List = ['Alter Self', 'Arcane Lock', 'Blindness/Deafness', 'Blur', 'Cloud of Daggers',
                             'Continual Flame', 'Crown of Madness',
                             'Darkness', 'Darkvsion', 'Detect Thoughts', 'Enlarge/Reduce', 'Flaming Sphere',
                             'Gentle Response', 'Gust of Wind', 'Hold Person',
                             'Invisibility', 'Knock', 'Levitate', 'Locate Object', 'Magic Mouth', 'Magic Weapon',
                             "Melf's Acid Arrow", 'Mirror Image',
                             'Misty Step', "Nystul's Magic Aura", 'Phantasmal Force', 'Ray of Enfeeblement',
                             'Rope Trick', 'Scorching Ray', 'See Invisibility',
                             'Shatter', 'Spider Climb', 'Suggestion', 'Web']
        Third_Level_List = ['Animate Dead', 'Bestow Curse', 'Blink', 'Clairvoyance', 'Counterspell', 'Dispel Magic',
                            'Fear', 'Feign Death', 'Fireball',
                            'Fly', 'Gaseous Form', 'Glyph of Warding', 'Haste', 'Hypnotic Pattern',
                            "Leomund's Tiny Hut", 'Lightning Bolt', 'Magic Circle',
                            'Major Image', 'Nondetection', 'Phantom Steed', 'Protection from Energy', 'Remove Curse',
                            'Sending', 'Sleet Storm', 'Slow',
                            'Stinking CLoud', 'Tongues', 'Vampiric Touch', 'Water Breathing']
        Fourth_Level_List = ['Arcane Eye', 'Banishment', 'Blight', 'Confusion', 'Cpnjure Minor Elementals',
                             'Control Water',
                             'Dimension Door', "Evard's Black Tentacles", 'Fabricate', 'Fire Shield',
                             'Greater Invisibility', 'Hallucinatory', 'Ice Storm',
                             "Leomund's Secret Chest", 'Locate Creature', "Mordenkainen's Private Sanctum",
                             "Otiluke's Resilient Sphere", 'Phantasmal Killer',
                             'Polymorph', 'Stone Shape', 'Stoneskin', 'Wall of Fire']
        Fifth_Level_List = ['Animate Object', "Bigby's Hand", 'Cloudkill', 'Cone of Cold', 'Conjure Elemental',
                            'Contact Other Plane',
                            'Creation', 'Dominate Person', 'Dream', 'Geas', 'Hold Monster', 'Legend Lore', 'Mislead',
                            'Modify Memory', 'Passwall',
                            'Planar Binding', "Rary's Telepathy Bond", 'Scrying', 'Seeming', 'Telekinesis',
                            'Teleportation Circle', 'Wall of Force',
                            'Wall of Stone']
        Sixth_Level_List = ['Arcane Gate', 'Chain Lightning', 'Circle of Death', 'Contingency', 'Create Undead',
                            'Disintegrate',
                            "Drawmij's Instant Summons", 'Eyebite', 'Flesh of Stone', 'Globe of Invulnerability',
                            'Guards and Wards', 'Magic Jar',
                            'Mass Suggestion', 'Move Earth', "Otiluke's Freezing Sphere", "Otto's Irresistible Dance",
                            'Programmed Illusion',
                            'Sunbeam', 'True Seeing', 'Wall of Ice']
        Seventh_Level_List = ['Delayed Blast Fireball', 'Etherealness', 'Finger of Death', 'Forcecage', 'Mirage Arcane',
                              "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", 'Plane Shift',
                              'Prismatic Spray', 'Project Image',
                              'Reverse Gravity', 'Sequester', 'Simulacrum', 'Symbol', 'Teleport']
        Eight_Level_List = ['Antimagic Field', 'Antipathy/Sympathy', 'Clone', 'Control Weather', 'Demiplane',
                            'Dominate Monster',
                            'Feeblemind', 'Incendiary Cloud', 'Maze', 'Mind Blank', 'Power Word Stun', 'Sunburst',
                            'Telepathy']
        Ninth_Level_List = ['Astral Projection', 'Foresight', 'Gate', 'Imprisonment', 'Meteor Swarm', 'Power Word Kill',
                            'Prismatic Wall', 'Shapechange', 'Time Stop', 'True Polymorph', 'Weird', 'Wish']
        if int(Character_Level) == 1:
            AmountOfSpells = [3, 6, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [3, 6, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [3, 4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 4:
            AmountOfSpells = [4, 4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 5:
            AmountOfSpells = [4, 4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 6:
            AmountOfSpells = [4, 4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 7:
            AmountOfSpells = [4, 4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 8:
            AmountOfSpells = [4, 4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 9:
            AmountOfSpells = [4, 4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif int(Character_Level) == 10:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif int(Character_Level) >= 13 and int(Character_Level) <= 14:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 2, 1, 0, 0]
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif int(Character_Level) == 17:
            AmountOfSpells = [5, 4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif int(Character_Level) == 18:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif int(Character_Level) == 19:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif int(Character_Level) == 20:
            AmountOfSpells = [5, 4, 3, 3, 3, 3, 2, 2, 1, 1]
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Warlock') == Class_a:
        Cantrips_List = ['Blade Ward', 'Chill Touch', 'Eldritch Blast', 'Friends', 'Mage Hands', 'Minor Illusion',
                         'Poison Spray',
                         'Prestidigitation', 'True Strike']
        First_Level_List = ['Armor of Agathys', 'Arms of Hadar', 'Charm Person', 'Comprehend Languages',
                            'Expeditious Retreat',
                            'Hellish Rebuke', 'Hex', 'Illosory', 'Protection from Evil and Good', 'Unseen Servant',
                            'Witch Bolt']
        Second_Level_List = ['Cloud of Daggers', 'Crown of Madness', 'Darkness', 'Enthrall', 'Hold Person',
                             'Hold Person',
                             'Invisibility', 'Mirror Image', 'Misty Step', 'Ray of Enfeeblement', 'Shatter',
                             'Spider Climb', 'Suggestion']
        Third_Level_List = ['Counterspell', 'Dispel Magic', 'Fear', 'Fly', 'Gaseous Form', 'Hunger of Hadar',
                            'Hypnotic Pattern',
                            'Magic Circle', 'Major Image', 'Remove Curse', 'Tongues', 'Vampiric Touch']
        Fourth_Level_List = ['Banishment', 'Blight', 'Dimension Door', 'Hallucinatory Terrain']
        Fifth_Level_List = ['Contact Other Plane', 'Dream', 'Hold Monster', 'Scrying']
        Sixth_Level_List = ['Arcane Gate', 'Circle of Death', 'Conjure Fey', 'Create Undead', 'Eyebite',
                            'Flesh to Stone',
                            'Mass Suggestion', 'True Seeing']
        Seventh_Level_List = ['Etherealness', 'Finger of Death', 'Forcecage', 'Plane Shift']
        Eight_Level_List = ['Demiplane', 'Dominate Monster', 'Feeblemind', 'Glibness', 'Power Word Stun']
        Ninth_Level_List = ['Astral Projection', 'Foresight', 'Imprisonment', 'Power Word Kill', 'True Polymorph']
        if int(Character_Level) == 1:
            AmountOfSpells = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 2:
            AmountOfSpells = [2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif int(Character_Level) == 3:
            AmountOfSpells = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 3):
                b = random.randint(1, 2)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 4:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 4):
                b = random.randint(1, 2)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 5:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 5):
                b = random.randint(1, 3)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 6:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 6):
                b = random.randint(1, 3)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 7:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 7):
                b = random.randint(1, 4)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 8:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 8):
                b = random.randint(1, 4)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 9:
            AmountOfSpells = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        elif int(Character_Level) == 10:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 1, 0, 0, 0]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        elif int(Character_Level) >= 13 and int(Character_Level) <= 14:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 1, 1, 0, 0]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 1, 1, 1, 0]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        elif int(Character_Level) >= 17 and int(Character_Level) <= 18:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1]
            for x in range(0, 9):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        else:
            AmountOfSpells = [4, 0, 0, 0, 0, 0, 1, 1, 1, 1]
            for x in range(0, 10):
                b = random.randint(1, 5)
                AmountOfSpells[b] += 1
        if AmountOfSpells[1] != 0:
            First = random.sample(range(0, len(First_Level_List)), AmountOfSpells[1])
            for number in First:
                spells_known.append(First_Level_List[number])
        if AmountOfSpells[2] != 0:
            Second = random.sample(range(0, len(Second_Level_List)), AmountOfSpells[2])
            for number in Second:
                spells_known.append(Second_Level_List[number])
        if AmountOfSpells[3] != 0:
            Third = random.sample(range(0, len(Third_Level_List)), AmountOfSpells[3])
            for number in Third:
                spells_known.append(Third_Level_List[number])
        if AmountOfSpells[4] != 0:
            Fourth = random.sample(range(0, len(Fourth_Level_List)), AmountOfSpells[4])
            for number in Fourth:
                spells_known.append(Fourth_Level_List[number])
        if AmountOfSpells[5] != 0:
            Fifth = random.sample(range(0, len(Fifth_Level_List)), AmountOfSpells[5])
            for number in Fifth:
                spells_known.append(Fifth_Level_List[number])
        if AmountOfSpells[6] != 0:
            Sixth = random.sample(range(0, len(Sixth_Level_List)), AmountOfSpells[6])
            for number in Sixth:
                spells_known.append(Sixth_Level_List[number])
        if AmountOfSpells[7] != 0:
            Seventh = random.sample(range(0, len(Seventh_Level_List)), AmountOfSpells[7])
            for number in Seventh:
                spells_known.append(Seventh_Level_List[number])
        if AmountOfSpells[8] != 0:
            Eight = random.sample(range(0, len(Eight_Level_List)), AmountOfSpells[8])
            for number in Eight:
                spells_known.append(Eight_Level_List[number])
        if AmountOfSpells[9] != 0:
            Ninth = random.sample(range(0, len(Ninth_Level_List)), AmountOfSpells[9])
            for number in Ninth:
                spells_known.append(Ninth_Level_List[number])
    elif str('Rogue') == Class_a:
        spells_known.append('None')
    elif str('Fighter') == Class_a:
        spells_known.append('None')
    elif str('Barbarian') == Class_a:
        spells_known.append('None')
    elif str('Monk') == Class_a:
        spells_known.append('None')
    if str('Bard') == Class_a:
        if int(Character_Level) == 1:
            while len(spells_known) > 4:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 2:
            while len(spells_known) > 5:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 3:
            while len(spells_known) > 6:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 4:
            while len(spells_known) > 7:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 5:
            while len(spells_known) > 8:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 6:
            while len(spells_known) > 9:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 7:
            while len(spells_known) > 10:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 8:
            while len(spells_known) > 11:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 9:
            while len(spells_known) > 12:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 10:
            while len(spells_known) > 14:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            while len(spells_known) > 15:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 13:
            while len(spells_known) > 16:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 14:
            while len(spells_known) > 18:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            while len(spells_known) > 19:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 17:
            while len(spells_known) > 20:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        else:
            while len(spells_known) > 22:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
    if str('Druid') == Class_a:
        AbilityMod = 0
        if Ability_a['Wis'] == 1:
            AbilityMod = -5
        elif Ability_a['Wis'] >= 2 and Ability_a['Wis'] <= 3:
            AbilityMod = -4
        elif Ability_a['Wis'] >= 4 and Ability_a['Wis'] <= 5:
            AbilityMod = -3
        elif Ability_a['Wis'] >= 6 and Ability_a['Wis'] <= 7:
            AbilityMod = -2
        elif Ability_a['Wis'] >= 8 and Ability_a['Wis'] <= 9:
            AbilityMod = -1
        elif Ability_a['Wis'] >= 10 and Ability_a['Wis'] <= 11:
            AbilityMod = 0
        elif Ability_a['Wis'] >= 12 and Ability_a['Wis'] <= 13:
            AbilityMod = 1
        elif Ability_a['Wis'] >= 14 and Ability_a['Wis'] <= 15:
            AbilityMod = 2
        elif Ability_a['Wis'] >= 16 and Ability_a['Wis'] <= 17:
            AbilityMod = 3
        elif Ability_a['Wis'] >= 18 and Ability_a['Wis'] <= 19:
            AbilityMod = 4
        elif Ability_a['Wis'] >= 20 and Ability_a['Wis'] <= 21:
            AbilityMod = 5
        elif Ability_a['Wis'] >= 22 and Ability_a['Wis'] <= 23:
            AbilityMod = 6
        elif Ability_a['Wis'] >= 24 and Ability_a['Wis'] <= 25:
            AbilityMod = 7
        elif Ability_a['Wis'] >= 26 and Ability_a['Wis'] <= 27:
            AbilityMod = 8
        elif Ability_a['Wis'] >= 28 and Ability_a['Wis'] <= 29:
            AbilityMod = 9
        else:
            AbilityMod = 10
        if int(Character_Level) > 1:
            while len(spells_known) > ((int(AbilityMod) + int(Character_Level))):
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
    if str('Ranger') == Class_a:
        if int(Character_Level) >= 5 and int(Character_Level) <= 6:
            while len(spells_known) > 4:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 7 and int(Character_Level) <= 8:
            while len(spells_known) > 5:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 9 and int(Character_Level) <= 10:
            while len(spells_known) > 6:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            while len(spells_known) > 7:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 13 and int(Character_Level) <= 14:
            while len(spells_known) > 8:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            while len(spells_known) > 9:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 17 and int(Character_Level) <= 18:
            while len(spells_known) > 10:
                rremover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 19:
            while len(spells_known) > 11:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
    if str('Cleric') == Class_a:
        AbilityMod = 0
        if Ability_a['Wis'] == 1:
            AbilityMod = -5
        elif Ability_a['Wis'] >= 2 and Ability_a['Wis'] <= 3:
            AbilityMod = -4
        elif Ability_a['Wis'] >= 4 and Ability_a['Wis'] <= 5:
            AbilityMod = -3
        elif Ability_a['Wis'] >= 6 and Ability_a['Wis'] <= 7:
            AbilityMod = -2
        elif Ability_a['Wis'] >= 8 and Ability_a['Wis'] <= 9:
            AbilityMod = -1
        elif Ability_a['Wis'] >= 10 and Ability_a['Wis'] <= 11:
            AbilityMod = 0
        elif Ability_a['Wis'] >= 12 and Ability_a['Wis'] <= 13:
            AbilityMod = 1
        elif Ability_a['Wis'] >= 14 and Ability_a['Wis'] <= 15:
            AbilityMod = 2
        elif Ability_a['Wis'] >= 16 and Ability_a['Wis'] <= 17:
            AbilityMod = 3
        elif Ability_a['Wis'] >= 18 and Ability_a['Wis'] <= 19:
            AbilityMod = 4
        elif Ability_a['Wis'] >= 20 and Ability_a['Wis'] <= 21:
            AbilityMod = 5
        elif Ability_a['Wis'] >= 22 and Ability_a['Wis'] <= 23:
            AbilityMod = 6
        elif Ability_a['Wis'] >= 24 and Ability_a['Wis'] <= 25:
            AbilityMod = 7
        elif Ability_a['Wis'] >= 26 and Ability_a['Wis'] <= 27:
            AbilityMod = 8
        elif Ability_a['Wis'] >= 28 and Ability_a['Wis'] <= 29:
            AbilityMod = 9
        else:
            AbilityMod = 10
        if int(Character_Level) > 1:
            while len(spells_known) > ((int(AbilityMod) + int(Character_Level))):
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
    if str('Paladin') == Class_a:
        AbilityMod = 0
        if Ability_a['Cha'] == 1:
            AbilityMod = -5
        elif Ability_a['Cha'] >= 2 and Ability_a['Cha'] <= 3:
            AbilityMod = -4
        elif Ability_a['Cha'] >= 4 and Ability_a['Cha'] <= 5:
            AbilityMod = -3
        elif Ability_a['Cha'] >= 6 and Ability_a['Cha'] <= 7:
            AbilityMod = -2
        elif Ability_a['Cha'] >= 8 and Ability_a['Cha'] <= 9:
            AbilityMod = -1
        elif Ability_a['Cha'] >= 10 and Ability_a['Cha'] <= 11:
            AbilityMod = 0
        elif Ability_a['Cha'] >= 12 and Ability_a['Cha'] <= 13:
            AbilityMod = 1
        elif Ability_a['Cha'] >= 14 and Ability_a['Cha'] <= 15:
            AbilityMod = 2
        elif Ability_a['Cha'] >= 16 and Ability_a['Cha'] <= 17:
            AbilityMod = 3
        elif Ability_a['Cha'] >= 18 and Ability_a['Cha'] <= 19:
            AbilityMod = 4
        elif Ability_a['Cha'] >= 20 and Ability_a['Cha'] <= 21:
            AbilityMod = 5
        elif Ability_a['Cha'] >= 22 and Ability_a['Cha'] <= 23:
            AbilityMod = 6
        elif Ability_a['Cha'] >= 24 and Ability_a['Cha'] <= 25:
            AbilityMod = 7
        elif Ability_a['Cha'] >= 26 and Ability_a['Cha'] <= 27:
            AbilityMod = 8
        elif Ability_a['Cha'] >= 28 and Ability_a['Cha'] <= 29:
            AbilityMod = 9
        else:
            AbilityMod = 10
        if int(Character_Level) > 1:
            while len(spells_known) > (int(AbilityMod) + round(int(Character_Level) / 2)):
                remover = random.randint(0, len(spells_known) - 1)
                del spells_known[remover]
    if str('Wizard') == Class_a:
        AbilityMod = 0
        if Ability_a['Int'] == 1:
            AbilityMod = -5
        elif Ability_a['Int'] >= 2 and Ability_a['Int'] <= 3:
            AbilityMod = -4
        elif Ability_a['Int'] >= 4 and Ability_a['Int'] <= 5:
            AbilityMod = -3
        elif Ability_a['Int'] >= 6 and Ability_a['Int'] <= 7:
            AbilityMod = -2
        elif Ability_a['Int'] >= 8 and Ability_a['Int'] <= 9:
            AbilityMod = -1
        elif Ability_a['Int'] >= 10 and Ability_a['Int'] <= 11:
            AbilityMod = 0
        elif Ability_a['Int'] >= 12 and Ability_a['Int'] <= 13:
            AbilityMod = 1
        elif Ability_a['Int'] >= 14 and Ability_a['Int'] <= 15:
            AbilityMod = 2
        elif Ability_a['Int'] >= 16 and Ability_a['Int'] <= 17:
            AbilityMod = 3
        elif Ability_a['Int'] >= 18 and Ability_a['Int'] <= 19:
            AbilityMod = 4
        elif Ability_a['Int'] >= 20 and Ability_a['Int'] <= 21:
            AbilityMod = 5
        elif Ability_a['Int'] >= 22 and Ability_a['Int'] <= 23:
            AbilityMod = 6
        elif Ability_a['Int'] >= 24 and Ability_a['Int'] <= 25:
            AbilityMod = 7
        elif Ability_a['Int'] >= 26 and Ability_a['Int'] <= 27:
            AbilityMod = 8
        elif Ability_a['Int'] >= 28 and Ability_a['Int'] <= 29:
            AbilityMod = 9
        else:
            AbilityMod = 10
        if int(Character_Level) >= 1 and int(Character_Level) <= 3:
            while len(spells_known) > 6:
                remover = random.randint(0, len(spells_known))
                del spells_known[remover]
        else:
            while len(spells_known) > ((int(AbilityMod) + int(Character_Level))):
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
    if str('Sorcerer') == Class_a:
        if int(Character_Level) == 1:
            while len(spells_known) > 2:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 2:
            while len(spells_known) > 3:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 3:
            while len(spells_known) > 4:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 4:
            while len(spells_known) > 5:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 5:
            while len(spells_known) > 6:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 6:
            while len(spells_known) > 7:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 7:
            while len(spells_known) > 8:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 8:
            while len(spells_known) > 9:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 9:
            while len(spells_known) > 10:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 10:
            while len(spells_known) > 11:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            while len(spells_known) > 12:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 13 and int(Character_Level) <= 14:
            while len(spells_known) > 13:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            while len(spells_known) > 14:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 17:
            while len(spells_known) > 15:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
    if str('Warlock') == Class_a:
        if int(Character_Level) == 1:
            while len(spells_known) > 2:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 2:
            while len(spells_known) > 3:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 3:
            while len(spells_known) > 4:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 4:
            while len(spells_known) > 5:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 5:
            while len(spells_known) > 6:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 6:
            while len(spells_known) > 7:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 7:
            while len(spells_known) > 8:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) == 8:
            while len(spells_known) > 9:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 9 and int(Character_Level) <= 10:
            while len(spells_known) > 10:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 11 and int(Character_Level) <= 12:
            while len(spells_known) > 11:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 13 and int(Character_Level) <= 14:
            while len(spells_known) > 12:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 15 and int(Character_Level) <= 16:
            while len(spells_known) > 13:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        elif int(Character_Level) >= 17 and int(Character_Level) <= 18:
            while len(spells_known) > 14:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        else:
            while len(spells_known) > 15:
                remover = random.randint(0, (len(spells_known) - 1))
                del spells_known[remover]
        if AmountOfSpells[0] != 0:
            Cantrips = random.sample(range(0, len(Cantrips_List)), AmountOfSpells[0])
            for number in Cantrips:
                spells_known.append(Cantrips_List[number])
        Invocations = ['Armor of Shadows', 'Beast Speech', 'Beguiling Influence', "Devil's Sight", 'Eldritch Sight',
                       'Eyes of the Rune Keeper', 'Fiendish Vigor', 'Gaze of Two Minds', 'Mask of Many Faces',
                       'Misty Visions',
                       'Thief of Five Fates']
        Pact = []
        if int(Character_Level) >= 3:
            pacts = ['Pact of the Chain', 'Pact of the Blade', 'Pact of the Tome']
            b = random.randint(0, 2)
            Pact.append(pacts[b])
        if str('Eldritch Blast') in spells_known:
            Invocations.append('Agonizing Blast')
            Invocations.append('Eldritch Spear')
            Invocations.append('Repelling Blast')
        if int(Character_Level) >= 5:
            Invocations.append('Mire the Mind')
            Invocations.append('One with Shadows')
            Invocations.append('Sign of Ill Omen')
        if int(Character_Level) >= 5 and Pact == 'Pact of the Blade':
            Invocations.append('Thirsting Blade')
        if int(Character_Level) >= 7:
            Invocations.append('Bewitching Whispers')
            Invocations.append('Dreadful Word')
            Invocations.append('Sculptor of Flesh')
        if int(Character_Level) >= 9:
            Invocations.append('Ascendant Step')
            Invocations.append('Minions of Chaos')
            Invocations.append('Otherworldly Leap')
            Invocations.append('Whispers of the Grave')
        if Pact == 'Pact of the Tome':
            Invocations.append('Book of Ancient Secrets')
            ALPHA = ['Blade Ward', 'Dancing Lights', 'Friends', 'Light', 'Mage Hand', 'Mending', 'Message',
                     'Minor Illusion',
                     'Prestidigitation', 'True Strike', 'Vicious Mockery', 'Guidance', 'Light', 'Mending', 'Resistance',
                     'Sacred Flame',
                     'Spare the Dying', 'Thaumaturgy', 'Druidcraft', 'Guidance', 'Mending', 'Poison Spray',
                     'Produce Flame', 'Resistance',
                     'Shillelagh', 'Thorn Whip', 'Acid Splash', 'Blade Ward', 'Chill Touch', 'Dancing Light',
                     'Fire Bolt', 'Friends',
                     'Light', 'Mage Hand', 'Mending', 'Message', 'Minor Illusion', 'Poison Spray', 'Prestidigitation',
                     'Ray of Frost',
                     'Shocking Grasp,True Strike', 'Acid Splash', 'Blade Ward', 'Chill Touch', 'Dancing Light',
                     'Fire Bolt', 'Friends',
                     'Light', 'Mage Hand', 'Mending', 'Message', 'Minor Illusion', 'Poison Spray', 'Prestidigitation',
                     'Ray of Frost',
                     'Shocking Grasp', 'True Strike', 'Blade Ward', 'Chill Touch', 'Eldritch Blast', 'Friends',
                     'Mage Hands', 'Minor Illusion',
                     'Posion Spray', 'Prestidigitation', 'True Strike', ]
            First = random.sample(range(0, len(ALPHA)), 2)
            for number in First:
                spells_known.append(ALPHA[number])
        if Pact == 'Pact of the Chain':
            Invocations.append('Voice of the Chain Master')
        if Pact == 'Pact of the Chain':
            spells_known.append('Find Familiar')
        if int(Character_Level) >= 12 and Pact == 'Pact of the Blade':
            Invocations.append('Lifedrinker')
        if int(Character_Level) >= 15:
            Invocations.append('Master of Myriad Forms')
            Invocations.append('Visions of Distant Realms')
            Invocations.append('Witch Sight')
        if int(Character_Level) >= 15 and Pact == 'Pact of the Chain':
            Invocations.append('Chains of Carceri')
        Known_Invocations = []
        if int(Character_Level) >= 2 and int(Character_Level) <= 4:
            First = random.sample(range(0, len(Invocations)), 2)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 5 and int(Character_Level) <= 6:
            First = random.sample(range(0, len(Invocations)), 3)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 7 and int(Character_Level) <= 8:
            First = random.sample(range(0, len(Invocations)), 4)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 9 and int(Character_Level) <= 11:
            First = random.sample(range(0, len(Invocations)), 5)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 12 and int(Character_Level) <= 14:
            First = random.sample(range(0, len(Invocations)), 6)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 15 and int(Character_Level) <= 17:
            First = random.sample(range(0, len(Invocations)), 7)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        elif int(Character_Level) >= 18:
            First = random.sample(range(0, len(Invocations)), 8)
            for ability in First:
                Known_Invocations.append(Invocations[ability])
        if str('Book of Ancient Secrets') in Known_Invocations:
            OMEGA = ['Animal Friendship', 'Bane', 'Charm Person', 'Comprehend Languages', 'Cure Wounds', 'Detect Magic',
                     'Disguise Self',
                     'Dissonant Whispers', "Faerie Fire", 'Feather Fall', 'Healing Word', 'Heroism', 'Identify',
                     'Illusory Script', 'Longstrider',
                     'Silent Image', 'Sleep', 'Speak with Animals', "Tasha's Hideous Laughter", 'Thunderwave',
                     'Unseen Servant', 'Bane',
                     'Bless', 'Command', 'Create of Destroy Water', 'Detect Evil and Good', 'Detect Poison or Disease',
                     'Guiding Bolt',
                     'Inflict Wounds', 'Protection from Evil and Good', 'Purify Food and Drink', 'Sanctuary',
                     'Shield of Faith',
                     'Create or Destroy Water', 'Detect Poison and Disease', 'Entangle', 'Faerie Fire', 'Fog Cloud',
                     'Goodberry',
                     'Jump', 'Compelled Duel', 'Divine Favor', 'Searing Smite', 'Thunderous Smite', 'Wrathful Smite',
                     'Alarm', 'Ensnaring Strike',
                     'Hail of Thorns', "Hunter's Mark", 'Burning Hands', 'Chromatic Orb', 'Color Spray',
                     'Expeditious Retreat', 'False Life',
                     'Mage Armor', 'Magic Missile', 'Ray of Sickness', 'Shield', 'Witch Bolt', 'Burning Hand',
                     'Find Familiar', 'Grease',
                     "Tenser's Floating Disk", 'Armor of Agathys', 'Arms of Hadar', 'Hellish Rebuke', 'Hex', 'Illosory']
            First = random.sample(range(0, len(OMEGA)), 2)
            for number in First:
                spells_known.append(OMEGA[number])
        for special in Known_Invocations:
            spells_known.append(special)
    return spells_known


# Making a better display for the stats.
# def Stat_Displayer():
#    f = []
#    global Stat_Display_Items
#    for a, b in Stat_Display_items:
#        f.append(a, b)
#    return f
# Here are the Variables
Race = Sub_Race()
Race_a = Race_Gen()
Class_a = Class_Gen()
Stat = Stat_Gen()
Ability_a = Stat_Assign()
Stat_Mod = Stat_Modifier()
Armor = Armor_Gen()
# Character_Level = Character_Level()
Gear = Gear_Gen()
Hit_Dice = Hit_Dice()
Health_a = Hit_Dice_Total()
Stat_Display_Items = list(Stat_Mod.items())
Simple_Weapon = Simple_Weapon()
Simple_Melee_Weapon = Simple_Melee_Weapon()
Martial_Weapon = Martial_Weapon()
Martial_Melee_Weapon = Martial_Melee_Weapon()
Weapon_Assign = Weapon_Assign()
Spells_Known = Spell_Gen()

# print(Race.split()[1])
# And the print that will show it all
# print('Race: {0}\nSex: {1}\nClass: {2}\nAbility Scores: {3}'.format(str(Race), str(Sex_Gen()), str(Class_a), str(Stat_Mod)))
print('Race: ' + str(Race) + '\n'
    'Sex: ' + str(Sex_Gen()) + '\n''Class: ' + str(Class_a) + '\n'
    'Health Points: ' + str(Health_a) + '\n' '\n' '-----------------------------------------------------' '\n'
    'Ability Score' + '\n' '-----------------------------------------------------' '\n' + str("\n".join("{}: {}".format(k, v) for k, v in Stat_Mod.items())) + '\n'
    '\n' '-----------------------------------------------------' + '\n'
    'Armor''\n' '-----------------------------------------------------''\n' + str('\n'.join(Gear)) + '\n' '\n'
    '-----------------------------------------------------' '\n'
    'Weapons and Items' + '\n' '-----------------------------------------------------' '\n' + Weapon_Assign[1:-1].replace(",", '\n')[0:]
    + '\n' '\n' '-----------------------------------------------------' + '\n' + 'Known Spells' + '\n'
    '-----------------------------------------------------' '\n' + str(Spells_Known)[1:-1].replace(",", "\n"))

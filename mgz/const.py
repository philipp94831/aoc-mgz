"""Constants."""

# pylint: disable=too-many-lines

VERSIONS = {
    'VER 9.9': 'userpatch 1.3',
    'VER 9.A': 'userpatch 1.4 rc 1',
    'VER 9.B': 'userpatch 1.4 rc 2',
    'VER 9.C': 'userpatch 1.4 rc 2',
    'VER 9.D': 'userpatch 1.4',
    'VER 9.E': 'userpatch 1.5',
    'VER 9.F': 'userpatch 1.5'
}

MODS = {
    1: 'Wololo Kingdoms',
    2: 'Portuguese Civilization Mod III',
    3: 'Age of Chivalry'
}

SPEEDS = {
    100: 'slow',
    150: 'standard',
    178: 'standard', # up15
    200: 'fast'
}

MAP_NAMES = {
    9: 'Arabia',
    10: 'Archipelago',
    11: 'Baltic',
    12: 'Black Forest',
    13: 'Coastal',
    14: 'Continental',
    15: 'Crater Lake',
    16: 'Fortress',
    17: 'Gold Rush',
    18: 'Highland',
    19: 'Islands',
    20: 'Mediterranean',
    21: 'Migration',
    22: 'Rivers',
    23: 'Team Islands',
    24: 'Random',
    25: 'Scandinavia',
    26: 'Mongolia',
    27: 'Yucatan',
    28: 'Salt Marsh',
    29: 'Arena',
    30: 'King of the Hill',
    31: 'Oasis',
    32: 'Ghost Lake',
    33: 'Nomad',
    34: 'Iberia',
    35: 'Britain',
    36: 'Mideast',
    37: 'Texas',
    38: 'Italy',
    39: 'Central America',
    40: 'France',
    41: 'Norse Lands',
    42: 'Sea of Japan (East Sea)',
    43: 'Byzantinum',
    48: 'Blind Random',
    49: 'Acropolis',
    50: 'Budapest',
    51: 'Cenotes',
    52: 'City of Lakes',
    53: 'Golden Pit',
    54: 'Hideout',
    55: 'Hill Fort',
    56: 'Lombardia',
    57: 'Steppe',
    58: 'Valley',
    59: 'MegaRandom',
    60: 'Hamburger',
    61: 'CtR Random',
    62: 'CtR Monsoon',
    63: 'CtR Pyramid Descent',
    64: 'CtR Spiral',
    66: 'Acropolis',
    67: 'Budapest',
    68: 'Cenotes',
    69: 'City of Lakes',
    70: 'Golden Pit',
    71: 'Hideout',
    72: 'Hill Fort',
    73: 'Lombardia',
    74: 'Steppe',
    75: 'Valley',
    76: 'MegaRandom',
    77: 'Hamburger',
    78: 'CtR Random',
    79: 'CtR Monsoon',
    80: 'CtR Pyramid Descent',
    81: 'CtR Spiral',
    82: 'Kilimanjaro',
    83: 'Mountain Pass',
    84: 'Nile Delta',
    85: 'Serengeti',
    86: 'Socotra',
    87: 'Amazon',
    88: 'China',
    89: 'Horn of Africa',
    90: 'India',
    91: 'Madagascar',
    92: 'West Africa',
    93: 'Bohemia',
    94: 'Earth',
    95: 'Canyons',
    96: 'Enemy Archipelago',
    97: 'Enemy Islands',
    98: 'Far Out',
    99: 'Front Line',
    100: 'Inner Circle',
    101: 'Motherland',
    102: 'Open Plains',
    103: 'Ring of Water',
    104: 'Snakepit',
    105: 'The Eye'
}


MAP_SIZES = {
    120: 'tiny',
    144: 'small',
    168: 'medium',
    200: 'normal',
    220: 'large',
    240: 'giant'
}


CIVILIZATION_NAMES = {
    1: 'Britons',
    2: 'Franks',
    3: 'Goths',
    4: 'Teutons',
    5: 'Japanese',
    6: 'Chinese',
    7: 'Byzantines',
    8: 'Persians',
    9: 'Saracens',
    10: 'Turks',
    11: 'Vikings',
    12: 'Mongols',
    13: 'Celts',
    14: 'Spanish',
    15: 'Aztecs',
    16: 'Mayans',
    17: 'Huns',
    18: 'Koreans',
    19: 'Italians',
    20: 'Indians',
    21: 'Incas',
    22: 'Magyars',
    23: 'Slavs',
    24: 'Portuguese',
    25: 'Ethiopians',
    26: 'Malians',
    27: 'Berbers',
    28: 'Khmer',
    29: 'Malay',
    30: 'Burmese',
    31: 'Vietnamese'
}


PLAYER_COLORS = {
    0: 'blue',
    1: 'red',
    2: 'green',
    3: 'yellow',
    4: 'teal',
    5: 'purple',
    6: 'gray',
    7: 'orange'
}


COMPASS = {
    'northwest': [1/3.0, 0],
    'southeast': [1/3.0, 2/3.0],
    'southwest': [0, 1/3.0],
    'northeast': [2/3.0, 1/3.0],
    'center': [1/3.0, 1/3.0],
    'west': [0, 0],
    'north': [2/3.0, 0],
    'east': [2/3.0, 2/3.0],
    'south': [0, 2/3.0]
}


TECHNOLOGIES = {
    2: 'Elite Tarkan',
    3: 'Yeomen',
    4: 'El Dorado',
    5: 'Furor Celtica',
    6: 'Drill',
    7: 'Mahouts',
    8: 'Town Watch',
    9: 'Zealotry',
    10: 'Artillery',
    11: 'Crenellations',
    12: 'Crop Rotation',
    13: 'Heavy Plow',
    14: 'Horse Collar',
    15: 'Guilds',
    16: 'Anarchy',
    17: 'Banking',
    19: 'Cartography',
    21: 'Atheism',
    22: 'Loom',
    23: 'Coinage',
    24: 'Garland Wars',
    27: 'Elite Plumed Archer',
    34: 'War Galley',
    35: 'Galleon',
    37: 'Cannon Galleon',
    39: 'Husbandry',
    45: 'Faith',
    47: 'Chemistry',
    48: 'Caravan',
    49: 'Berserkergang',
    50: 'Masonry',
    51: 'Architecture',
    52: 'Rocketry',
    54: 'Treadmill Crane',
    55: 'Gold Mining',
    59: 'Kataparuto',
    60: 'Elite Conquistador',
    61: 'Logistica',
    63: 'Keep',
    64: 'Bombard Tower',
    65: 'Gillnets',
    67: 'Forging',
    68: 'Iron Casting',
    74: 'Scale Mail Armor',
    75: 'Blast Furnace',
    76: 'Chain Mail Armor',
    77: 'Plate Mail Armor',
    80: 'Plate Barding Armor',
    81: 'Scale Barding Armor',
    82: 'Chain Barding Armor',
    83: 'Bearded Axe',
    85: 'Hand Cannon',
    90: 'Tracking',
    93: 'Ballistics',
    94: 'Scorpion',
    96: 'Capped Ram',
    98: 'Elite Skirmisher',
    100: 'Crossbowman',
    101: 'Feudal Age',
    102: 'Castle Age',
    103: 'Imperial Age',
    104: 'Dark Age',
    140: 'Guard Tower',
    182: 'Gold Shaft Mining',
    188: 'Bombard Cannon',
    194: 'Fortified Wall',
    197: 'Pikeman',
    199: 'Fletching',
    200: 'Bodkin Arrow',
    201: 'Bracer',
    202: 'Double-Bit Axe',
    203: 'Bow Saw',
    207: 'Long Swordsman',
    209: 'Cavalier',
    211: 'Padded Archer Armor',
    212: 'Leather Archer Armor',
    213: 'Wheelbarrow',
    215: 'Squires',
    217: 'Two-Handed Swordsman',
    218: 'Heavy Cav Archer',
    219: 'Ring Archer Armor',
    221: 'Two-Man Saw',
    222: 'Man-at-Arms',
    226: 'Coinage',
    227: 'Coinage',
    230: 'Block Printing',
    231: 'Sanctity',
    233: 'Illumination',
    236: 'Heavy Camel',
    237: 'Arbalest',
    239: 'Heavy Scorpion',
    244: 'Heavy Demolition Ship',
    246: 'Fast Fire Ship',
    249: 'Hand Cart',
    252: 'Fervor',
    254: 'Light Cavalry',
    255: 'Siege Ram',
    257: 'Onager',
    261: 'Maghrabi Camels',
    262: 'Farimba',
    264: 'Champion',
    265: 'Paladin',
    278: 'Stone Mining',
    279: 'Stone Shaft Mining',
    280: 'Town Patrol',
    285: 'Tusk Swords',
    287: 'Double Crossbow',
    289: 'Forced Levy',
    306: 'Paper Money',
    314: 'Elite Rattan Archer',
    315: 'Conscription',
    316: 'Redemption',
    319: 'Atonement',
    320: 'Siege Onager',
    321: 'Sappers',
    322: 'Murder Holes',
    360: 'Elite Longbowman',
    361: 'Elite Cataphract',
    362: 'Elite Chu Ko Nu',
    363: 'Elite Throwing Axeman',
    364: 'Elite Teutonic Knight',
    365: 'Elite Huskarl',
    366: 'Elite Samurai',
    367: 'Elite War Elephant',
    368: 'Elite Mameluke',
    369: 'Elite Janissary',
    370: 'Elite Woad Raider',
    371: 'Elite Mangudai',
    372: 'Elite Longboat',
    373: 'Shipwright',
    374: 'Careening',
    375: 'Dry Dock',
    376: 'Elite Cannon Galleon',
    377: 'Siege Engineers',
    379: 'Hoardings',
    380: 'Heated Shot',
    384: 'Eagle Warrior',
    398: 'Elite Berserk',
    408: 'Spies/Treason',
    428: 'Hussar',
    429: 'Halberdier',
    432: 'Elite Jaguar Warrior',
    434: 'Elite Eagle Warrior',
    435: 'Bloodlines',
    436: 'Parthian Tactics',
    437: 'Thumb Ring',
    438: 'Theocracy',
    439: 'Heresy',
    440: 'Supremacy',
    441: 'Herbal Medicine',
    445: 'Shinkichon',
    448: 'Elite Turtle Ship',
    450: 'Elite War Wagon',
    457: 'Perfusion',
    460: 'Atlatl',
    461: 'Warwolf',
    462: 'Great Wall',
    463: 'Chieftains',
    464: 'Greek Fire',
    468: 'Elite Genoese Crossbowman',
    472: 'Elite Magyar Huszar',
    481: 'Elite Elephant Archer',
    482: 'Stronghold',
    483: 'Marauders',
    484: 'Yasama',
    485: 'Obsidian Arrows',
    486: 'Panokseon',
    487: 'Nomads',
    488: 'Boiling Oil',
    489: 'Ironclad',
    490: 'Madrasah',
    491: 'Sipahi',
    492: 'Inquisition',
    493: 'Chivalry',
    494: 'Pavise',
    499: 'Silk Road',
    504: 'Elite Boyar',
    506: 'Sultans',
    507: 'Shatagni',
    509: 'Elite Kamayuk',
    512: 'Orthodoxy',
    513: 'Druzhina',
    514: 'Mercenaries',
    515: 'Recurve Bow',
    516: 'Andean Sling',
    517: 'Couriers',
    521: 'Imperial Camel',
    525: 'Revetments',
    526: 'Hunting Dogs',
    527: 'Fire Tower',
    529: 'Britons',
    530: 'Franks',
    531: 'Goths',
    532: 'Teutons',
    533: 'Japanese',
    534: 'Chinese',
    535: 'Byzantines',
    536: 'Persians',
    537: 'Saracens',
    538: 'Turks',
    539: 'Vikings',
    540: 'Mongols',
    541: 'Celts',
    542: 'Spanish',
    543: 'Aztecs',
    544: 'Mayans',
    545: 'Huns',
    546: 'Koreans',
    547: 'Italians',
    548: 'Indians',
    549: 'Incas',
    550: 'Magyars',
    551: 'Slavs',
    555: 'Enable Sheep',
    556: 'Enable Llamas',
    557: 'Enable Cows',
    558: 'Enable Turkeys',
    563: 'Elite Organ Gun',
    565: 'Elite Camel Archer',
    567: 'Elite Gbeto',
    569: 'Elite Shotel Warrior',
    572: 'Carrack',
    573: 'Arquebus',
    574: 'Royal Heirs',
    575: 'Torsion Engines',
    576: 'Tigui',
    577: 'Farimba',
    578: 'Kasbah',
    579: 'Maghrabi Camels',
    580: 'Portuguese',
    581: 'Ethiopians',
    582: 'Malians',
    583: 'Berbers',
    597: 'Elite Caravel',
    599: 'Elite Genitour',
    600: 'Free Cartography',
    602: 'Arson',
    608: 'Arrowslits',
    615: 'Elite Ballista Elephant',
    617: 'Elite Karambit Warrior',
    619: 'Elite Arambai',
    621: 'Elite Rattan Archer',
    622: 'Tusk Swords',
    623: 'Double Crossbow',
    624: 'Thalassocracy',
    625: 'Forced Levy',
    626: 'Howdah',
    627: 'Manipur Cavalry',
    628: 'Chatras',
    629: 'Paper Money',
    631: 'Elite Battle Elephant',
    650: 'Khmer',
    651: 'Malay',
    652: 'Burmese',
    653: 'Vietnamese',
    655: 'Imperial Skirmisher',
    658: 'Set maximum population (no Houses)',
    665: 'Disable Vietnamese Vision'
}

UNITS = {
    1: 'Legionary',
    4: 'Archer',
    5: 'Hand Cannoneer',
    6: 'Elite Skirmisher',
    7: 'Skirmisher',
    8: 'Longbowman',
    9: 'Arrow',
    10: 'Archery Range',
    11: 'Mangudai',
    12: 'Barracks',
    13: 'Fishing Ship',
    14: 'Archery Range',
    15: 'Junk',
    17: 'Trade Cog',
    18: 'Blacksmith',
    19: 'Blacksmith',
    20: 'Barracks',
    21: 'War Galley',
    24: 'Crossbowman',
    25: 'Teutonic Knight',
    26: 'Dead crossbowman',
    30: 'Monastery',
    31: 'Monastery',
    32: 'Monastery',
    33: 'Fortress',
    35: 'Battering Ram',
    36: 'Bombard Cannon',
    37: 'Light Cavalry',
    38: 'Knight',
    39: 'Cavalry Archer',
    40: 'Cataphract',
    41: 'Huskarl',
    42: 'Trebuchet',
    45: 'Dock',
    46: 'Janissary',
    47: 'Dock',
    48: 'Wild Boar',
    49: 'Siege Workshop',
    50: 'Farm',
    51: 'Dock',
    52: 'Royal Janissary',
    53: 'Fish (Perch)',
    54: 'Arrow',
    56: 'Fisherman',
    57: 'Fisherman',
    59: 'Forage Bush',
    61: 'Dolphin',
    63: 'Gate',
    64: 'Gate',
    65: 'Deer',
    66: 'Gold Mine',
    67: 'Gate',
    68: 'Mill',
    69: 'Shore Fish',
    70: 'House',
    71: 'Town Center',
    72: 'Palisade Wall',
    73: 'Chu Ko Nu',
    74: 'Militia',
    75: 'Man-at-Arms',
    76: 'Heavy Swordsman',
    77: 'Long Swordsman',
    78: 'Gate',
    79: 'Watch Tower',
    80: 'Gate',
    81: 'Gate',
    82: 'Castle',
    83: 'Villager',
    84: 'Market',
    85: 'Gate',
    86: 'Stable',
    87: 'Archery Range',
    88: 'Gate',
    89: 'Dire Wolf',
    90: 'Gate',
    91: 'Gate',
    92: 'Gate',
    93: 'Spearman',
    94: 'Berserk',
    95: 'Gate',
    96: 'Hawk',
    97: 'Arrow',
    101: 'Stable',
    102: 'Stone Mine',
    103: 'Blacksmith',
    104: 'Monastery',
    105: 'Blacksmith',
    109: 'Town Center',
    110: 'Trade Workshop',
    111: 'Dead knight',
    112: 'Flare',
    116: 'Market',
    117: 'Stone Wall',
    118: 'Builder',
    119: 'Fortified Palisade Wall',
    120: 'Forager',
    122: 'Hunter',
    123: 'Lumberjack',
    124: 'Stone Miner',
    125: 'Monk',
    126: 'Wolf',
    128: 'Trade Cart',
    129: 'Mill',
    130: 'Mill',
    131: 'Mill',
    132: 'Barracks',
    133: 'Dock',
    137: 'Market',
    141: 'Town Center',
    142: 'Town Center',
    143: 'Rubble 1 x 1',
    144: 'Rubble 2 x 2',
    145: 'Rubble 3 x 3',
    146: 'Rubble 4 x 4',
    147: 'Rubble 6 x 6',
    148: 'Rubble 8 x 8',
    150: 'Siege Workshop',
    153: 'Stable',
    155: 'Fortified Wall',
    156: 'Repairer',
    159: 'Relic Cart',
    160: 'Richard the Lionheart',
    161: 'The Black Prince',
    163: 'Friar Tuck',
    164: 'Sheriff of Nottingham',
    165: 'Charlemagne',
    166: 'Roland',
    167: 'Belisarius',
    168: 'Theodoric the Goth',
    169: 'Aethelfirth',
    170: 'Siegfried',
    171: 'Erik the Red',
    172: 'Tamerlane',
    173: 'King Arthur',
    174: 'Lancelot',
    175: 'Gawain',
    176: 'Mordred',
    177: 'Archbishop',
    179: 'Trade Workshop',
    180: 'Dead long swordman',
    184: 'Condottiero',
    185: 'Slinger',
    188: 'Flamethrower',
    190: 'Fire Tower',
    191: 'Rubble 2 x 2',
    192: 'Rubble 2 x 2',
    193: 'Vlad Dracula',
    195: 'Kitabatake',
    196: 'Minamoto',
    197: 'Alexander Nevski',
    198: 'El Cid',
    199: 'Fish Trap',
    200: 'Robin Hood',
    202: 'Rabid Wolf',
    204: 'Trade Cart',
    206: 'VMDL',
    207: 'Imperial Camel',
    209: 'University',
    210: 'University',
    212: 'Builder',
    214: 'Farmer',
    216: 'Hunter',
    218: 'Lumberjack',
    220: 'Stone Miner',
    221: 'Falcon',
    222: 'Repairer',
    229: 'Falcon',
    231: 'Aqueduct',
    232: 'Woad Raider',
    234: 'Guard Tower',
    235: 'Keep',
    236: 'Bombard Tower',
    239: 'War Elephant',
    241: 'Cracks',
    246: 'Osman',
    248: 'Pile of Stone',
    250: 'Longboat',
    251: 'Amphitheatre',
    252: 'Pile of Gold',
    253: 'Pile of Wood',
    259: 'Farmer',
    262: 'Pile of Food',
    263: 'Colosseum',
    264: 'Cliff 1',
    265: 'Cliff 2',
    266: 'Cliff 3',
    267: 'Cliff 4',
    268: 'Cliff 5',
    269: 'Cliff 6',
    270: 'Cliff 7',
    271: 'Cliff 8',
    272: 'Cliff 9',
    273: 'Cliff 10',
    274: 'Flare',
    275: 'Centurion',
    276: 'Wonder',
    278: 'Dead Fish Trap',
    279: 'Scorpion',
    280: 'Mangonel',
    281: 'Throwing Axeman',
    282: 'Mameluke',
    283: 'Cavalier',
    284: 'Tree TD',
    285: 'Relic',
    286: 'Monk with Relic',
    287: 'British Relic',
    288: 'Byzantine Relic',
    289: 'Chinese Relic',
    290: 'Frankish Relic',
    291: 'Samurai',
    292: 'Gothic Relic',
    293: 'Villager',
    294: 'Japanese Relic',
    295: 'Persian Relic',
    296: 'Saracen Relic',
    297: 'Teutonic Relic',
    298: 'Turkish Relic',
    299: 'Bandit',
    301: 'Grass Patch',
    302: 'Bush',
    303: 'Seagulls',
    304: 'Bonfire',
    305: 'Llama',
    306: 'Black Tile',
    307: 'Cuauhtemoc',
    309: 'Monk with Turkish Relic',
    310: 'Mountain 1',
    311: 'Mountain 2',
    312: 'Arrow',
    315: 'Arrow',
    316: 'Arrow',
    317: 'Arrow',
    318: 'Arrow',
    319: 'Arrow',
    320: 'Arrow',
    321: 'Arrow',
    322: 'Arrow',
    328: 'Arrow',
    329: 'Camel',
    330: 'Heavy Camel',
    331: 'Trebuchet (Packed)',
    332: 'Flare',
    333: 'Deer',
    334: 'Flowers 1',
    335: 'Flowers 2',
    336: 'Flowers 3',
    337: 'Flowers 4',
    338: 'Path 4',
    339: 'Path 1',
    340: 'Path 2',
    341: 'Path 3',
    345: 'Ruins',
    348: 'Bamboo Forest Tree',
    349: 'Oak Forest Tree',
    350: 'Pine Forest Tree',
    351: 'Palm Forest Tree',
    352: 'Army Tent',
    354: 'Forager',
    357: 'Dead Farm',
    358: 'Pikeman',
    359: 'Halberdier',
    360: 'Arrow',
    361: 'Nordic Swordsman',
    363: 'Arrow',
    364: 'Arrow',
    365: 'Arrow',
    366: 'Arrow',
    370: 'City Wall',
    372: 'Arrow',
    373: 'Arrow',
    375: 'Arrow',
    376: 'Arrow',
    377: 'Arrow',
    381: 'Osman',
    389: 'Sea Rocks 1',
    390: 'Pagoda',
    396: 'Sea Rocks 2',
    397: 'Sanchi Stupa',
    398: 'Gol Gumbaz',
    399: 'Tree A',
    400: 'Tree B',
    401: 'Tree C',
    402: 'Tree D',
    403: 'Tree E',
    404: 'Tree F',
    405: 'Tree G',
    406: 'Tree H',
    407: 'Tree I',
    408: 'Tree J',
    409: 'Tree K',
    410: 'Tree L',
    411: 'Forest Tree',
    #TODO
    #412: 'Some ECL tree',
    413: 'Snow Pine Tree',
    414: 'Jungle Tree',
    415: 'Stump',
    420: 'Cannon Galleon',
    422: 'Capped Ram',
    424: 'Charles Martel',
    425: 'Francisco de Orellana',
    426: 'Harald Hardraade',
    427: 'Gonzalo Pizarro',
    428: 'Hrolf the Ganger',
    429: 'Frederick Barbarossa',
    430: 'Joan the Maid',
    432: 'William Wallace',
    434: 'King',
    437: 'Prithviraj',
    439: 'Francesco Sforza',
    440: 'Petard',
    441: 'Hussar',
    442: 'Galleon',
    445: 'Poenari Castle',
    446: 'Port',
    448: 'Scout Cavalry',
    450: 'Great Fish (Marlin)',
    451: 'Great Fish (Marlin)',
    452: 'Dolphin',
    455: 'Fish (Dorado)',
    456: 'Fish (Salmon)',
    457: 'Fish (Tuna)',
    458: 'Fish (Snapper)',
    463: 'House',
    464: 'House',
    465: 'House',
    466: 'Arrow',
    472: 'Loot',
    473: 'Two-Handed Swordsman',
    474: 'Heavy Cavalry Archer',
    475: 'Arrow',
    476: 'Arrow',
    477: 'Arrow',
    478: 'Arrow',
    481: 'Town Center',
    482: 'Town Center',
    483: 'Town Center',
    484: 'Town Center',
    485: 'Arrow',
    486: 'Bear',
    487: 'Gate',
    488: 'Gate',
    490: 'Gate',
    491: 'Gate',
    492: 'Arbalest',
    493: 'Advanced Heavy Crossbowman',
    498: 'Barracks',
    499: 'Torch',
    501: 'Dead pikeman',
    503: 'Arrow',
    504: 'Arrow',
    505: 'Arrow',
    507: 'Arrow',
    508: 'Arrow',
    509: 'Arrow',
    510: 'Arrow',
    511: 'Arrow',
    512: 'Arrow',
    514: 'Arrow',
    515: 'Arrow',
    516: 'Arrow',
    517: 'Arrow',
    518: 'Arrow',
    519: 'Arrow',
    520: 'Arrow',
    521: 'Arrow',
    522: 'Arrow',
    523: 'Arrow',
    524: 'Arrow',
    525: 'Arrow',
    527: 'Demolition Ship',
    528: 'Heavy Demolition Ship',
    529: 'Fire Ship',
    530: 'Elite Longbowman',
    531: 'Elite Throwing Axeman',
    532: 'Fast Fire Ship',
    533: 'Elite Longboat',
    534: 'Elite Woad Raider',
    539: 'Galley',
    542: 'Heavy Scorpion',
    545: 'Transport Ship',
    546: 'Light Cavalry',
    547: 'Dead light cavalry',
    548: 'Siege Ram',
    550: 'Onager',
    553: 'Elite Cataphract',
    554: 'Elite Teutonic Knight',
    555: 'Elite Huskarl',
    556: 'Elite Mameluke',
    557: 'Elite Janissary',
    558: 'Elite War Elephant',
    559: 'Elite Chu Ko Nu',
    560: 'Elite Samurai',
    561: 'Elite Mangudai',
    562: 'Lumber Camp',
    563: 'Lumber Camp',
    564: 'Lumber Camp',
    565: 'Lumber Camp',
    566: 'Watch Tower',
    567: 'Champion',
    569: 'Paladin',
    579: 'Gold Miner',
    581: 'Gold Miner',
    583: 'Genitour',
    584: 'Mining Camp',
    585: 'Mining Camp',
    586: 'Mining Camp',
    587: 'Mining Camp',
    588: 'Siege Onager',
    590: 'Shepherd',
    592: 'Shepherd',
    594: 'Sheep',
    596: 'Elite Genitour',
    597: 'Town Center',
    598: 'Outpost',
    599: 'Cathedral',
    600: 'Flag A',
    601: 'Flag B',
    602: 'Flag C',
    603: 'Flag D',
    604: 'Flag E',
    605: 'Bridge A--Top',
    606: 'Bridge A--Middle',
    607: 'Bridge A--Bottom',
    608: 'Bridge B--Top',
    609: 'Bridge B--Middle',
    610: 'Bridge B--Bottom',
    611: 'Town Center',
    612: 'Town Center',
    613: 'Town Center',
    614: 'Town Center',
    615: 'Town Center',
    616: 'Town Center',
    617: 'Town Center',
    618: 'Town Center',
    619: 'Town Center',
    620: 'Town Center',
    621: 'Town Center',
    623: 'Rock 1',
    624: 'Pavilion',
    625: 'Pavilion',
    626: 'Pavilion',
    629: 'Joan of Arc',
    632: 'Frankish Paladin',
    633: 'Cuauhtemoc',
    634: 'Sieur de Metz',
    636: 'Sieur Bertrand',
    637: 'Temple of Heaven',
    638: 'Duke D\'Alençon',
    639: 'Penguin',
    640: 'La Hire',
    642: 'Lord de Graville',
    644: 'Jean de Lorrain',
    646: 'Constable Richemont',
    648: 'Guy Josselyne',
    650: 'Jean Bureau',
    652: 'Sir John Fastolf',
    655: 'Mosque',
    659: 'Gate',
    660: 'Gate',
    661: 'Gate',
    662: 'Gate',
    663: 'Gate',
    664: 'Gate',
    665: 'Gate',
    666: 'Gate',
    667: 'Gate',
    668: 'Gate',
    669: 'Gate',
    670: 'Gate',
    671: 'Gate',
    672: 'Gate',
    673: 'Gate',
    674: 'Gate',
    678: 'Reynald de Chatillon',
    680: 'Master of the Templar',
    682: 'Bad Neighbor',
    683: 'God\'s Own Sling',
    684: 'The Accursed Tower',
    685: 'The Tower of Flies',
    686: 'Archers of the Eyes',
    688: 'Piece of the True Cross',
    689: 'Pyramid',
    690: 'Dome of the Rock',
    691: 'Elite Cannon Galleon',
    692: 'Berserk',
    694: 'Elite Berserk',
    696: 'Great Pyramid',
    698: 'Subotai',
    700: 'Hunting Wolf',
    702: 'Kushluk',
    704: 'Shah',
    705: 'Cow',
    706: 'Saboteur',
    707: 'Ornlu the Wolf',
    709: 'Cactus',
    710: 'Skeleton',
    711: 'Rugs',
    712: 'Yurt',
    713: 'Yurt',
    714: 'Yurt',
    715: 'Yurt',
    716: 'Yurt',
    717: 'Yurt',
    718: 'Yurt',
    719: 'Yurt',
    720: 'Nine Bands',
    721: 'Shipwreck',
    722: 'Shipwreck',
    723: 'Crater',
    725: 'Jaguar Warrior',
    726: 'Elite Jaguar Warrior',
    728: 'Ice',
    729: 'God\'s Own Sling (Packed)',
    730: 'Bad Neighbor (Packed)',
    731: 'Genghis Khan',
    733: 'Emperor in a Barrel',
    737: 'Bamboo Stump',
    738: 'Bridge A--Cracked',
    739: 'Bridge A--Broken Top',
    740: 'Bridge A--Broken Bottom',
    741: 'Bridge B--Cracked',
    742: 'Bridge B--Broken Top',
    743: 'Bridge B--Broken Bottom',
    744: 'Mountain 3',
    745: 'Mountain 4',
    748: 'Cobra Car',
    751: 'Eagle Scout',
    752: 'Elite Eagle Warrior',
    753: 'Eagle Warrior',
    755: 'Tarkan',
    757: 'Elite Tarkan',
    758: 'Burned building',
    759: 'Huskarl',
    761: 'Elite Huskarl',
    763: 'Plumed Archer',
    765: 'Elite Plumed Archer',
    771: 'Conquistador',
    773: 'Elite Conquistador',
    775: 'Missionary',
    777: 'Attila the Hun',
    778: 'Canoe',
    779: 'Bleda the Hun',
    781: 'Pope Leo I',
    783: 'Scythian Wild Woman',
    785: 'Sea Tower',
    788: 'Sea Wall',
    789: 'Palisade Gate',
    790: 'Palisade Gate',
    791: 'Palisade Gate',
    792: 'Palisade Gate',
    793: 'Palisade Gate',
    794: 'Palisade Gate',
    795: 'Palisade Gate',
    796: 'Palisade Gate',
    797: 'Palisade Gate',
    798: 'Palisade Gate',
    799: 'Palisade Gate',
    800: 'Palisade Gate',
    801: 'Palisade Gate',
    802: 'Palisade Gate',
    803: 'Palisade Gate',
    804: 'Palisade Gate',
    805: 'Dock',
    806: 'Dock',
    807: 'Dock',
    808: 'Dock',
    809: 'Stump',
    810: 'Iron Boar',
    812: 'Jaguar',
    814: 'Horse',
    816: 'Macaw',
    817: 'Statue',
    818: 'Plant',
    819: 'Sign',
    820: 'Grave',
    821: 'Head',
    822: 'Javelina',
    824: 'El Cid Campeador',
    825: 'Amazon Warrior',
    826: 'Monument',
    827: 'War Wagon',
    829: 'Elite War Wagon',
    831: 'Turtle Ship',
    832: 'Elite Turtle Ship',
    833: 'Turkey',
    835: 'Wild Horse',
    837: 'Map Revealer',
    838: 'King Sancho',
    839: 'Rock (Stone)',
    840: 'King Alfonso',
    841: 'Rock (Gold)',
    842: 'Imam',
    844: 'Admiral Yi Sun-shin',
    845: 'Nobunaga',
    846: 'Donkey',
    847: 'Henry V',
    849: 'William the Conqueror',
    850: 'Amazon Archer',
    851: 'ES Flag',
    852: 'Scythian Scout',
    853: 'Torch (Converting)',
    854: 'Torch (Converting)',
    855: 'Old Stone Head',
    856: 'Roman Ruins',
    857: 'Hay Stack',
    858: 'Broken Cart',
    859: 'Flower Bed',
    860: 'Furious the Monkey Boy',
    862: 'Stormy Dog',
    863: 'Rubble 1 x 1',
    864: 'Rubble 2 x 2',
    865: 'Rubble 3 x 3',
    866: 'Genoese Crossbowman',
    868: 'Elite Genoese Crossbowman',
    869: 'Magyar Huszar',
    871: 'Elite Magyar Huszar',
    872: 'Quimper Cathedral',
    873: 'Elephant Archer',
    875: 'Elite Elephant Archer',
    876: 'Boyar',
    878: 'Elite Boyar',
    879: 'Kamayuk',
    881: 'Elite Kamayuk',
    882: 'Condottiero',
    884: 'Wild Camel',
    885: 'Siege Tower',
    886: 'Tarkan',
    887: 'Elite Tarkan',
    #TODO
    #Hidden Cup Qualifier 7 (PoV) vs 10 g2.mgz
    #888: 'Some building',
    #TODO
    #TheViper-VS-TaToH--hideout-20171025..mgz
    #890: 'Some building',
    892: 'Heavy Pikeman',
    894: 'Eastern Swordsman',
    896: 'Waterfall',
    897: 'Camel (Gaia)',
    899: 'Arch of Constantine',
    900: 'Rain',
    901: 'Flag F',
    902: 'Smoke',
    904: 'Wooden Bridge A--Top',
    905: 'Wooden Bridge A--Middle',
    906: 'Wooden Bridge A--Bottom',
    907: 'Wooden Bridge B--Top',
    908: 'Wooden Bridge B--Middle',
    909: 'Wooden Bridge B--Bottom',
    910: 'Impaled Corpse',
    914: 'Quarry',
    915: 'Lumber',
    916: 'Goods',
    917: 'Vulture',
    918: 'Rock 2',
    922: 'Monk with Relic',
    923: 'Queen',
    925: 'Sanyogita',
    926: 'Prithvi',
    927: 'Chand Bhai',
    929: 'Saladin',
    930: 'Khosrau',
    931: 'Jarl',
    932: 'Savaran',
    933: 'Barrels',
    934: 'Alfred the Alpaca',
    936: 'Elephant',
    938: 'Dragon Ship',
    939: 'Flame 1',
    940: 'Flame 2',
    941: 'Flame 3',
    942: 'Flame 4',
    943: 'Osman',
    944: 'Relic Cart',
    1001: 'Organ Gun',
    1003: 'Elite Organ Gun',
    1004: 'Caravel',
    1006: 'Elite Caravel',
    1007: 'Camel Archer',
    1009: 'Elite Camel Archer',
    1010: 'Genitour',
    1012: 'Elite Genitour',
    1013: 'Gbeto',
    1015: 'Elite Gbeto',
    1016: 'Shotel Warrior',
    1018: 'Elite Shotel Warrior',
    1019: 'Zebra',
    1021: 'Feitoria',
    1023: 'Priest',
    1025: 'Monk with Relic',
    1026: 'Ostrich',
    1028: 'Stork',
    1029: 'Lion',
    1031: 'Crocodile',
    1033: 'Savannah Grass Patch',
    1034: 'Musa ibn Nusayr',
    1035: 'Sundjata',
    1036: 'Tariq ibn Ziyad',
    1037: 'Richard de Clare',
    1038: 'Tristan',
    1039: 'Princess Yodit',
    1040: 'Henry II',
    1041: 'Mountain 5',
    1042: 'Mountain 6',
    1043: 'Mountain 7',
    1044: 'Mountain 8',
    1045: 'Snow Mountain 1',
    1046: 'Snow Mountain 2',
    1047: 'Snow Mountain 3',
    1048: 'Rock Formation 1',
    1049: 'Rock Formation 2',
    1050: 'Rock Formation 3',
    1051: 'Dragon Tree',
    1052: 'Baobab Tree',
    1053: 'Bush 2',
    1054: 'Bush 3',
    1055: 'Arrow',
    1056: 'Falcon',
    1059: 'Fruit Bush',
    1060: 'Goat',
    1062: 'Fence',
    1063: 'Acacia Tree',
    1064: 'Yekuno Amlak',
    1065: 'Rubble 1 x 1',
    1066: 'Yodit',
    1067: 'Itzcoatl',
    1068: 'Mustafa Pasha',
    1069: 'Pacal II',
    1070: 'Babur',
    1071: 'Abraha Elephant',
    1072: 'Guglielmo Embriaco',
    1073: 'Su Dingfang',
    1074: 'Pachacuti',
    1075: 'Huayna Capac',
    1076: 'Miklos Toldi',
    1077: 'Little John',
    1078: 'Zawisza the Black',
    1080: 'Sumanguru',
    1081: 'Storage',
    1082: 'Hut',
    1083: 'Hut',
    1084: 'Hut',
    1085: 'Hut',
    1086: 'Hut',
    1087: 'Hut',
    1088: 'Hut',
    1089: 'Granary',
    1090: 'Barricade',
    1091: 'Animal skeleton',
    1092: 'Stelae A',
    1093: 'Stelae B',
    1094: 'Stelae C',
    1095: 'Gallow',
    1096: 'Palace',
    1097: 'Tent',
    1098: 'Tent',
    1099: 'Tent',
    1100: 'Tent',
    1101: 'Tent',
    1102: 'Sea Fortification',
    1103: 'Fire Galley',
    1104: 'Demolition Raft',
    1105: 'Siege Tower',
    1106: 'Dagnajan',
    1109: 'Gidajan',
    1120: 'Ballista Elephant',
    1122: 'Elite Ballista Elephant',
    1123: 'Karambit Warrior',
    1125: 'Elite Karambit Warrior',
    1126: 'Arambai',
    1128: 'Elite Arambai',
    1129: 'Rattan Archer',
    1131: 'Elite Rattan Archer',
    1132: 'Battle Elephant',
    1134: 'Elite Battle Elephant',
    1135: 'Komodo Dragon',
    1137: 'Tiger',
    1139: 'Rhinoceros',
    1141: 'Box Turtles',
    1142: 'Water Buffalo',
    1144: 'Mangrove Tree',
    1146: 'Rainforest Tree',
    1148: 'Rock (Beach)',
    1149: 'Rock (Jungle)',
    1150: 'Flag G',
    1151: 'Flag H',
    1152: 'Flag I',
    1153: 'Flag J',
    1155: 'Imperial Skirmisher',
    1157: 'Gajah Mada',
    1158: 'Jayanegara',
    1159: 'Raden Wijaya',
    1160: 'Sunda Royal Fighter',
    1162: 'Suryavarman I',
    1163: 'Udayadityavarman I',
    1164: 'Jayaviravarman',
    1165: 'Bayinnaung',
    1166: 'Tabinshwehti',
    1169: 'Arrow',
    1170: 'Arrow',
    1171: 'Buddha Statue A',
    1172: 'Buddha Statue B',
    1173: 'Buddha Statue C',
    1174: 'Buddha Statue D',
    1175: 'Fern Patch',
    1176: 'Trowulan Gate',
    1177: 'Vases',
    1178: 'Le Loi',
    1179: 'Le Lai',
    1180: 'Le Lai',
    1181: 'Le Trien',
    1182: 'Luu Nhan Chu',
    1183: 'Bui Bi',
    1184: 'Dinh Le',
    1185: 'Wang Tong',
    1186: 'Envoy',
    1187: 'Rice Farm',
    1188: 'Dead Rice Farm',
    1189: 'Harbor',
    1191: 'Stupa',
    1192: 'Farmer',
    1196: 'Army Tent',
    1197: 'Army Tent',
    1198: 'Army Tent',
    1199: 'Army Tent',
    1200: 'Army Tent',
    1201: 'Pagoda',
    1202: 'Pagoda',
    1203: 'Pagoda',
    1204: 'Bridge C--Top',
    1205: 'Bridge C--Middle',
    1206: 'Bridge C--Bottom',
    1207: 'Bridge D--Top',
    1208: 'Bridge D--Middle',
    1209: 'Bridge D--Bottom',
    1210: 'Bridge C--Cracked',
    1211: 'Bridge C--Broken Top',
    1212: 'Bridge C--Broken Bottom',
    1213: 'Bridge D--Cracked',
    1214: 'Bridge D--Broken Top',
    1215: 'Bridge D--Broken Bottom',
    1216: 'Sanchi Stupa',
    1217: 'Gol Gumbaz',
    1218: 'Barricade',
    1219: 'Barricade',
    1220: 'Barricade',
    1222: 'Sharkatzor',
    1223: 'Arrow',
    # WololoKingdoms
    106: 'Organ Gun',
    114: 'Elite Organ Gun',
    162: 'Caravel',
    183: 'Elite Caravel',
    203: 'Camel Archer',
    208: 'Elite Camel Archer',
    223: 'Genitour',
    230: 'Elite Genitour',
    260: 'Gbeto',
    418: 'Elite Gbeto',
    453: 'Shotel Warrior',
    459: 'Elite Shotel Warrior',
    467: 'Fire Ship',
    494: 'Siege Tower',
    653: 'Demolition Ship',
    732: 'Genitour',
    734: 'Feitoria',
    760: 'Ballista Elephant',
    762: 'Imperial Skirmisher',
    766: 'Elite Battle Elephant',
    774: 'Battle Elephant',
    782: 'Elite Rattan Archer',
    784: 'Rattan Archer',
    811: 'Elite Arambai',
    823: 'Arambai',
    830: 'Elite Karambit Warrior',
    836: 'Karambit Warrior',
    891: 'Elite Ballista Elephant'
}

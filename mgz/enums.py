"""Enumerations."""

from construct import Enum, Pass

# pylint: disable=invalid-name

def BuildingEnum(ctx):
    """Buildings Enumeration (in Action context)."""
    return Enum(
        ctx,
        dock=45,
        tc=621,
        default=Pass
    )

def GameTypeEnum(ctx):
    """Game Type Enumeration."""
    return Enum(
        ctx,
        RM=0,
        Regicide=1,
        DM=2,
        Scenario=3
    )

def ColorIdEnum(ctx):
    return Enum(
        ctx,
        blue=1,
        red=2,
        green=3,
        yellow=4,
        teal=5,
        purple=6,
        gray=7,
        orange=8
        )

def ColorEnum(ctx):
    return Enum(
        ctx,
        blue=0,
        red=1,
        green=2,
        yellow=3,
        teal=4,
        purple=5,
        gray=6,
        orange=7,
        #GAIA
        none=13
        )

def CivEnum(ctx):
    return Enum(
        ctx,
        Gaia=0,
        Britons=1,
        Franks=2,
        Goths=3,
        Teutons=4,
        Japanese=5,
        Chinese=6,
        Byzantines=7,
        Persians=8,
        Saracens=9,
        Turks=10,
        Vikings=11,
        Mongols=12,
        Celts=13,
        Spanish=14,
        Aztecs=15,
        Mayans=16,
        Huns=17,
        Koreans=18,
        Italians=19,
        Indians=20,
        Incas=21,
        Magyars=22,
        Slavs=23,
        Portuguese=24,
        Ethiopians=25,
        Malians=26,
        Berbers=27,
        Khmer=28,
        Malay=29,
        Burmese=30,
        Vietnamese=31,
        default="unknown"
    )

def ObjectTypeEnum(ctx):
    """Object Type Enumeration."""
    return Enum(
        ctx,
        gaia=10, # eyecandy
        other=20, # flag
        doppelganger=25,
        fish=30, # dead fish
        bird=40,
        projectile=60,
        unit=70, # creatable
        building=80,
        default=Pass
    )

def PlayerTypeEnum(ctx):
    """Player Type Enumeration."""
    return Enum(
        ctx,
        invalid=0,
        unknown=1,
        human=2,
        computer=4
    )

def DifficultyEnum(ctx):
    """Difficulty Enumeration."""
    return Enum(
        ctx,
        hardest=0,
        hard=1,
        standard=2,
        easy=3,
        easiest=4
    )

def OperationEnum(ctx):
    """Operation Enumeration."""
    return Enum(
        ctx,
        action=1,
        sync=2,
        message=4,
        default="savedchapter"
    )

def MessageEnum(ctx):
    """Message Type Enumeration."""
    return Enum(
        ctx,
        start=500,
        default="chat"
    )

def ResourceEnum(ctx):
    """Resource Type Enumeration."""
    return Enum(
        ctx,
        food=0,
        wood=1,
        stone=2,
        gold=3,
        decay=12,
        fish=17,
        default="unknown" # lots of resource types exist
    )

def VictoryEnum(ctx):
    """Victory Type Enumeration."""
    return Enum(
        ctx,
        standard=0,
        conquest=1,
        time_limit=7,
        score=8,
        last_man=11
    )

def ResourceLevelEnum(ctx):
    """Resource Level Enumeration."""
    return Enum(
        ctx,
        none=-1,
        standard=0,
        low=1,
        medium=2,
        high=3
    )

def RevealMapEnum(ctx):
    """Reveal Map Enumeration."""
    return Enum(
        ctx,
        normal=0,
        explored=1,
        all_visible=2
    )

def StartingAgeEnum(ctx):
    """Starting Age Enumeration."""
    return Enum(
        ctx,
        what=-2,
        unset=-1,
        dark=0,
        feudal=1,
        castle=2,
        imperial=3,
        postimperial=4,
        dmpostimperial=6
    )

def TheirDiplomacyEnum(ctx):
    """Other Player's Diplomacy Enumeration."""
    return Enum(
        ctx,
        ally_or_self=0,
        enemy=3
    )

def DiplomacyStanceEnum(ctx):
    """Diplomacy stance."""
    return Enum(
        ctx,
        allied=0,
        neutral=1,
        enemy=3
    )

def GameActionModeEnum(ctx):
    """Game Action Modes."""
    return Enum(
        ctx,
        diplomacy=0,
        speed=1,
        instant_build=2,
        quick_build=4,
        allied_victory=5,
        cheat=6,
        unk0=9,
        spy=10,
        unk1=11,
        farm_queue=13,
        farm_unqueue=14,
        default=Pass
    )

def OrderTypeEnum(ctx):
    """Types of Orders."""
    return Enum(
        ctx,
        packtreb=1,
        unpacktreb=2,
        garrison=5,
        default="unknown"
    )

def ReleaseTypeEnum(ctx):
    """Types of Releases."""
    return Enum(
        ctx,
        all=0,
        selected=3,
        sametype=4,
        notselected=5,
        inversetype=6,
        default=Pass
    )

def MyDiplomacyEnum(ctx):
    """Player's Diplomacy Enumeration."""
    return Enum(
        ctx,
        gaia=0,
        self=1,
        ally=2,
        neutral=3,
        enemy=4,
        invalid_player=-1
    )

def ActionEnum(ctx):
    """Action Enumeration."""
    return Enum(
        ctx,
        interact=0,
        stop=1,
        ai_interact=2,
        move=3,
        ai_move=10,
        resign=11,
        spec=15,
        waypoint=16,
        stance=18,
        guard=19,
        follow=20,
        patrol=21,
        formation=23,
        save=27,
        ai_waypoint=31,
        chapter=32,
        ai_queue=100,
        research=101,
        build=102,
        game=103,
        wall=105,
        delete=106,
        attackground=107,
        tribute=108,
        repair=110,
        release=111,
        multiqueue=112,
        togglegate=114,
        flare=115,
        order=117,
        queue=119,
        gatherpoint=120,
        sell=122,
        buy=123,
        droprelic=126,
        townbell=127,
        backtowork=128,
        postgame=255,
        default=Pass
    )

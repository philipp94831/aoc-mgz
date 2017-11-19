from construct import ExprAdapter
from mgz.const import VERSIONS, SPEEDS, MAP_NAMES, UNITS, TECHNOLOGIES

def UnitAdapter(ctx):
    return ExprAdapter(
        ctx,
        encoder = lambda obj,ctx: None,
        decoder = lambda obj,ctx: UNITS.get(obj, 'Unknown' + str(obj))
        )

def MapAdapter(ctx):
    return ExprAdapter(
        ctx,
        encoder = lambda obj,ctx: None,
        decoder = lambda obj,ctx: MAP_NAMES.get(obj, 'Custom')
        )


def SpeedAdapter(ctx):
    return ExprAdapter(
        ctx,
        encoder = lambda obj,ctx: None,
        decoder = lambda obj,ctx: SPEEDS.get(obj, 'Unknown')
        )


def VersionAdapter(ctx):
    return ExprAdapter(
        ctx,
        encoder = lambda obj,ctx: None,
        decoder = lambda obj,ctx: VERSIONS.get(obj, 'Unknown')
        )


def TechAdapter(ctx):
    return ExprAdapter(
        ctx,
        encoder = lambda obj,ctx: None,
        decoder = lambda obj,ctx: TECHNOLOGIES.get(obj, 'Unknown')
        )
import sc2
from sc2.constants import UnitTypeId
import py_trees
from py_trees.common import Status


def Invert(child, name, bot: sc2.BotAI, properties: dict):
    return py_trees.decorators.Inverter(child)

def OneShot(child, name, bot, properties):
    return py_trees.decorators.OneShot(child)

all_decorators = {'Invert':Invert, 'One Shot':OneShot}

def generate_decorator(decorator: dict, bot: sc2.BotAI, child):
    properties = {}
    for prop in decorator.get('properties', []):
        properties[prop['name']] = prop['value']
    dec = all_decorators.get(decorator['type'], None)
    if dec:
        return dec(child, decorator['type'], bot, properties)


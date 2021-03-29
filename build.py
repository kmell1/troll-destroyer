from moves import *

class CharacterBuild:
  def __init__(build, stats, weapon, accessory, backpack):
    build.stats = stats
    build.weapon = weapon
    build.accessory = accessory
    build.backpack = backpack

#stat spreads


class StatSpread:
  def __init__(stats, spread, hp, max_hp, strength, toughness, dexterity,
  intelligence, charisma):
    stats.spread = spread
    stats.hp = hp
    stats.max_hp = max_hp
    stats.toughness = toughness
    stats.strength = strength
    stats.dexterity = dexterity
    stats.intelligence = intelligence
    stats.charisma = charisma

warrior = StatSpread("Warrior", 75, 75, 9, 9, 6, 4, 5)
rogue = StatSpread("Rogue", 60, 60, 7, 5, 9, 5, 7)
wizard = StatSpread("Wizard", 50, 50, 4, 4, 4, 9, 6)
cleric = StatSpread("Cleric", 65, 65, 7, 6, 4, 7, 8)


class Weapon:
  def __init__(weapon, name, basic_attack, special_attack, hit, dmg,
  spell_power, desc):
    weapon.name = name
    weapon.basic_attack = basic_attack
    weapon.special_attack = special_attack
    weapon.hit = hit
    weapon.dmg = dmg
    weapon.spell_power = spell_power
    weapon.desc = desc

sword = Weapon("Sword", attack, sword_spec, 75, 15, 0,
"A sturdy sword.")
dagger = Weapon("Dagger", attack, dagger_spec, 85, 10, 0,
"A small, sharp blade.")
staff = Weapon("Staff", attack, staff_spec, 70, 6, 5,
"A staff that channels magic power.")
mace = Weapon("Mace", attack, mace_spec, 80, 12, 3,
"A blunt weapon favored by clerics.")


class Accessory:
  def __init__(accessory, name, moveset, phys_hit_up, phys_dmg_up, tough_up,
  mag_hit_up, mag_dmg_up, desc):
    accessory.name = name
    accessory.moveset = moveset
    accessory.phys_hit_up = phys_hit_up
    accessory.phys_dmg_up = phys_dmg_up
    accessory.tough_up = tough_up
    accessory.mag_hit_up = mag_hit_up
    accessory.mag_dmg_up= mag_dmg_up
    accessory.desc = desc

shield = Accessory("Shield", shield_moves, 5, 0, 7, 0, 0, "A sturdy shield.")
spellbook = Accessory("Spellbook", spells, 0, 0, 0, 8, 7, "A book of spells.")
holy_symbol = Accessory("Holy Symbol", prayers, 0, 0, 2, 7, 8, "A holy symbol.")
poison_kit = Accessory("Poison Kit", poisons, 4, 4, 0, 0, 0,
"A collection of foul poisons, favored by underhanded combatants.")

class Consumable:
  def __init__(consumable, name, hp, phys_hit_up, dmg, uses, desc):
    consumable.name = name
    consumable.hp = hp
    consumable.phys_hit_up = phys_hit_up
    consumable.dmg = dmg
    consumable.uses = uses
    consumable.desc = desc

potion = Consumable("Potion", 25, 0, 0, 3, "A healing potion.")
bomb = Consumable("Bomb", 0, 0, 35, 3, "Throw this at a bad guy.")

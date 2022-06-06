from dataclasses import dataclass
from typing import Dict # necessary because JupyterLite/Binder is still on Python 3.7

# type aliases
UnitLevel = str
ActionLevel = str
ActionType = str

@dataclass
class UnitLevelStats:
    attack: int
    defense: int
    
@dataclass
class ActionLevelStats:
    hasty: int
    deliberate: int
    
@dataclass
class GameRules:
    unit_stats: Dict[UnitLevel, UnitLevelStats]
    action_stats: Dict[ActionLevel, ActionLevelStats]
    adjacent_unit_defense_bonus: int

def get_required_roll_to_win(rules, num_lvl1_attackers, num_lvl2_attackers, defender_level, action_modifier, num_adjacent_defenders):
    attack_modifier = (num_lvl1_attackers * rules.unit_stats["level1"]["attack"]) + (num_lvl2_attackers * rules.unit_stats["level2"]["attack"]) + action_modifier
    defense_modifier = rules.unit_stats[defender_level]["defense"] + (num_adjacent_defenders * rules.adjacent_unit_defense_bonus)  
    return defense_modifier + 1 - attack_modifier
    
@dataclass
class UnitGroup:
    level1: int
    level2: int

@dataclass
class Scenario:
    name: str
    rules: GameRules
    attackers: UnitGroup
    defender_level: UnitLevel
    action: (ActionLevel, ActionType)
    adjacent_defenders: int
    
    def get_roll_to_win(self):
        action_level, action_type = self.action
        return get_required_roll_to_win(self.rules, self.attackers.level1, self.attackers.level2, self.defender_level, self.rules.action_stats[action_level][action_type], self.adjacent_defenders)

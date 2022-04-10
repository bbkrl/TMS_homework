import ammo


class Armor:
    """thickness (толщина брони)
     type(тип брони)
     """

    def __init__(self, thickness, thickness_type: str):
        self.thickness = thickness
        self.type = thickness_type

    def is_penetrated(self, ammo_object: ammo):
        return True if ammo_object.get_damage() > self.thickness * 1.2 else False


class HArmour(Armor):
    def is_penetrated(self, ammo_object: ammo):
        if ammo_object == ammo.HECartridge:
            return True if ammo_object.get_penetration() > self.thickness * 1.2 else False
        elif ammo_object == ammo.HEATCartridge:
            return True if ammo_object.get_penetration() > self.thickness * 1 else False
        elif ammo_object == ammo.APCartridge:
            return True if ammo_object.get_penetration() > self.thickness * 0.7 else False

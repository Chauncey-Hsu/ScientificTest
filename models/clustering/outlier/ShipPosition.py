class ShipPosition(object):

    def __init__(self, id, shipname, longitude, latitude, equipmentid, cell):
        self.id = id
        self.shipname = shipname
        self.longitude = longitude
        self.latitude = latitude
        self.equipmentid = equipmentid
        self.cell = cell

    def print_info(self):
        print('%s, %s, %s, %s, %s, %s, %s' % (
        self.id, self.shipname, self.longitude, self.latitude, self.equipmentid, self.cell))

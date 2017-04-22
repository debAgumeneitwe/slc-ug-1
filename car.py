class Car(object):
    def __init__(self, name='General', model='GM', car_type='Saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.car_type != 'trailer':
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8
    def is_saloon(self):
        if self.car_type != 'trailer':
            return True
        else:
            return False
    def drive(self, num):
        """drive car by altering speed
        this method as returns the updated car object.
        """
        if self.car_type == 'Saloon':
            self.speed = 10 ** num
        else:
            self.speed = 77
        return self
    
    

class Switch:
    def __init__(self,name,status=False):
        self.name = name
        self.status = status

    def __str__(self):
        if self.status:
            return f"switch({self.name}) is on"
        else:
            return f"switch({self.name}) is off"

    def turn(self):
        self.status = not(self.status)
    
    def clone(self):
        return Switch(name=self.name+".copy",status=self.status)
    
class Light(Switch):
    def __init__(self,name,switch):
        self.name = name
        self.switch = switch

    def __str__(self):
        if self.switch.status:
            return f"light({self.name}) with switch({self.switch.name}) is on"
        else:
            return f"light({self.name}) with switch({self.switch.name}) is off"

    def turn(self):
        self.switch.status = not(self.switch.status)

    def get_status(self):
        return self.switch.status
    
    def set_switch(self,new_switch):
        self.switch = new_switch

    def clone(self):
        return Light(name=self.name+".copy",switch=self.switch.clone())
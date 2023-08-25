class Radio:
    def __init__(self, mode="FM",frequency=87.5) -> None:
        self.mode = mode
        self.frequency = frequency

    def __str__(self) -> str:
        if self.mode == "FM":
            return f"{self.mode} Radio: {self.frequency :.1f} MHz"
        else:
            return f"{self.mode} Radio: {self.frequency :.1f} kHz"

    def set_mode(self,mode):
        self.mode = mode
        if mode == "FM":
            self.frequency = 87.5
        else:
            self.frequency = 150
            
    def set_frequency(self,frequency):
        # Check mode
        if self.mode == "AM":
            if 150 <= frequency <= 280:
                self.frequency = frequency
        else:
            if 87.5 <= frequency <= 108:
                self.frequency = frequency

    def adjust_frequency(self,frequency):
        new_frequency = self.frequency + frequency
        if self.mode == "AM":
            if 150 <= new_frequency <= 280:
                self.frequency = new_frequency
                return True
            else:
                self.frequency = self.frequency
                return False
        else:
            if 87.5 <= new_frequency <= 108:
                self.frequency = new_frequency
                return True
            else:
                self.frequency = self.frequency
                return False
            
    def get_mode(self):
        return self.mode
    
    def get_frequency(self):
        return self.frequency

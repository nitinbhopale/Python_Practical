class watch:
    def __init__(self,hr,min,sec,alarm,type):
        self.hr=hr
        self.min=min
        self.sec=sec
        self.alarm=alarm
        self.type=type

    def setalarm(self,hr,min,sec):
        if self.hr==hr and self.min==min and self.sec==sec:
            print("Alarm Ringing")
    
    def stopalarm(self):
        print("Alarm Stopped")

    def showtime(self):
        print(f"Hour:{self.hr} Min:{self.min} Sec:{self.sec}")

        
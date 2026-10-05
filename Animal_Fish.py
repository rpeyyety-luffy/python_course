class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()      # let Animal do its setup (num_eyes = 2)

    def breathe(self):
        super().breathe()       # do Animal's breathe first
        print("Doing this underwater.")   # then add extra

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
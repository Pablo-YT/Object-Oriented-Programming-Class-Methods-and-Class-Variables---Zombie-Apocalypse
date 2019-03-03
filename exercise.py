import random

class Zombie:

  max_speed = 5
  horde = []
  plague_level = 10
  default_speed = 1
  max_strength = 8
  default_strength = 3


  def __init__(self, speed, strength):
    """Initializes zombie's speed and strength
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed

    if strength > Zombie.max_strength:
        self.strength = Zombie.default_strength
    else:
        self.strength = strength

    

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      strength = random.randint(1, Zombie.max_strength)
      Zombie.horde.append(Zombie(speed, strength))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.some_die_off()
    Zombie.increase_plague_level()


  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde.
    """
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in two possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie. It eats your brains and you die. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()
    fight = self.fight()

    if outrun:
      return 'you escaped'
    else: return 'you died :('


    if not outrun:
        fight = self.fight()
        if  fight == "true":
            Zombie.horde.append(Zombie.horde())
            return 'You won but got bit and are now a zombie. lol'
    



  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed

    #instance method that makes shows the zombies stats
  def __str__(self):
    return "Speed: {} -- Strength: {}".format(self.speed, self.strength)


  def fight(self):
    """This instance method represents users strenth (generated randomly) and the zombies strenth. 
    Both will be compared and if user is higher true will be returned and if not false will be returned"""
 
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength




   # user_strength = random.randint(1, Zombie.max_strength)
   # if user_strength < Zombie.max_strength:
   #  return print("false")
   # elif user_strength > Zombie.max_strength:  
    #  return print("true") 




  @classmethod
  def increase_plague_level(cls):
      """This class method should generate a random number between 0 and 2."""
      increase_plague = random.randint(0, 2)
      Zombie.plague_level += increase_plague







print(Zombie.horde) # []
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!
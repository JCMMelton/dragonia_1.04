class warlock:
    def __init__(self,name):
        self.cls = 'warlock'
        self.name = name
        self.stamina = 14
        self.wisdom = 15
        self.intellect = 16
        self.dexterity = 9
        self.strength = 7
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['drains','depletes','consumes','leeches','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Power Siphon','Entropic Assault']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Power Siphon(1).  This ability does {0} to {1} damage".format((self.intellect+self.stamina*3/2),((self.intellect+self.stamina)*7/3))
        print "Heals you for a portion of damage dealt"
        print "Entropic Assault(2). This ability does {0} to {1} damage".format((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        print "Consumes a portion of you current health. Even if you miss!"
    def _ability0(self):
        damage = random.randrange(((self.intellect+self.stamina)*3/2),((self.intellect+self.stamina)*7/3))
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (self.damage/5)+heal_control
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[5],self.damage)
            print 'and heals you for {0}.'.format((self.damage/5)+heal_control)
            #print '{0},{1}'.format(heal_control,self.health)
        else:
            self.damage = damage
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (damage/6)+heal_control
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
            print 'and heals you for {0}.'.format((damage/6)+heal_control)
            #print '{0},{1}'.format(heal_control,self.health)
    def _ability1(self):
        damage = random.randrange((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        sac_hp = round(self.health * (0.17),0)
        if miss <= self.miss:
            self.damage = 0
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "You MISS completely!"
            print "{0} health consumed.".format(sac_hp)
        elif crit <= self.crit:
            self.damage = damage*2
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "Your Entropic Assault crits for {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
        else:
            self.damage = damage
            #sac_hp = self.health * (0.1)
            self.health -= sac_hp
            print "Your Entropic Assault deals {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 6
        self.wisdom += 3
        self.intellect += 4
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.stamina += 10
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.intellect += 45
    def _legendary_weapon(self):
        self.intellect += 100



class mage:
    def __init__(self,name):
        self.cls = 'mage'
        self.name = name
        self.stamina = 8
        self.wisdom = 19
        self.intellect = 20
        self.dexterity = 7
        self.strength = 6
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['burns','incinertes','scourches','glances','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Fireball']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Fireball(1).  This ability does {0} to {1} damage".format(self.intellect*2,self.intellect*7)
        print "Barrier(2). This ability creates a magical shield that absorbs {0} to {1} damage.".format(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
    def _ability0(self):
        damage = random.randrange(self.intellect*2,self.intellect*7)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
    def _ability1(self):
    	player.damage = 0
        shield = random.randrange(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
        self.shield = shield
        print "You create a {0} point shield".format(shield)
        
    def _health(self):
        print "You have {0} health and {1} shield remaining".format(self.health, self.shield)
        
    def _level(self):
        self.stamina += 2
        self.wisdom += 4
        self.intellect += 9
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.stamina += 10
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.intellect += 45
    def _legendary_weapon(self):
        self.intellect += 100
               
class warrior:
    def __init__(self,name):
        self.cls = 'warrior'
        self.name = name
        self.stamina = 17
        self.wisdom = 7
        self.intellect = 4
        self.dexterity = 12
        self.strength = 21
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.dict = ['SLICES','WOUNDS','HITS','GLANCES','DEMOLISHES','CRITS','MISSES']
        self.target = 'unknown'
        self.abilities = ['Heroic Slash']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Heroic Slash(1).  This ability does {0} to {1} damage".format(self.strength,self.strength*4)
    def _ability0(self):
        damage = random.randrange(self.strength*2,self.strength*4)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
    
    #def _ability1(self):
    	
    
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 6
        self.wisdom += 1
        self.intellect += 1
        self.dexterity += 3
        self.strength += 7
        self.health = self.stamina*10
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.strength += 30
    def _offhand(self):
        self.strength += 15
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.strength += 95
    def _legendary_weapon(self):
        self.strength += 200

class cleric:
    def __init__(self,name):
        self.cls = 'cleric'
        self.name = name
        self.stamina = 15
        self.wisdom = 10
        self.intellect = 10
        self.dexterity = 9
        self.strength = 18
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.empowered = 0
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.dict = ['cleanses','pierces','glances','devastates','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Holy Blow']
        self.xp = 0
        self.lvl = 1
    def _displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def _abilities(self):
        print "Holy Blow(1).  This ability does {0} to {1} damage.".format(self.strength+self.intellect,(self.strength + self.intellect)*3)
        print "Devine Judgment(2). This ability does {0} to {1} damage.".format(self.wisdom*2, self.wisdom*5)
        print "You enter a state of devine empowerment" 
        print "adding addition effects to your next attack."
        print "Holy Blow will deal additional damage and Devine Judgment will heal you."
        print "   "
    def _ability0(self):
        damage = random.randrange((self.strength + self.intellect)*2,(self.strength + self.intellect)*3)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if (self.empowered):
        	damage = round(damage*1.25,0)
        	self.empowered = 0
        if miss <= self.miss:
            self.damage = 0
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
        
    def _ability1(self):
    	damage = random.randrange(self.wisdom*2, self.wisdom*5)
    	crit = random.randrange(1,100)
    	miss = random.randrange(1,100)
    	if (self.empowered):
    		self.health += round(damage*0.8, 0)
    		self.empowered = 0
    		print "You are healed for {0}".format(damage*0.8)
    	else:
    		self.empowered = 1
    		print "You feel empowered by a devine force!"
    	if miss <= self.miss:
    		self.damage = 0
    		print "You Missed!"
    	elif crit <= self.crit:
    		self.damage = damage * 2
    		print "Your Devine Judgment CRITS for {0} damage.".format(self.damage)
    	else:
    		self.damage = damage
    		print "Your Devine Judgment deals {0} damage.".format(self.damage)
    	
    def _health(self):
        print "You have {0} health remaining".format(self.health)
    def _level(self):
        self.stamina += 4
        self.wisdom += 3
        self.intellect += 3
        self.dexterity += 1
        self.strength += 5
        self.health = self.stamina*10
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.lvl += 1
        print "\nYou've reached level {0}".format(self.lvl)
    def _sword(self):
        self.intellect += 30
    def _offhand(self):
        self.strength += 15
    def _belt(self):
        self.stamina += 2
    def _cloak(self):
        self.stamina += 20
    def _trinket(self):
        self.strength += 45
        self.intellect += 45
    def _legendary_weapon(self):
        self.strength += 100
        self.intellect += 75
import random
import time
def skip_engine(x):
    while x>0:
        x-=1
        time.sleep(0.5)
class Characters:
    def __init__(self, name, stats, skills, lvlsystem):
        self._name=name
        self._health=stats[0]
        self._maxhealth=stats[0]
        self._attack=stats[1]
        self._ogattack=stats[1]
        self._hitratio=stats[2]
        self._oghitratio=stats[2]
        self._defence=stats[3]
        self._ogdefence=stats[3]
        self._magic=stats[4]
        self._maxmagic=stats[4]
        self._skillist=skills
        self._level=lvlsystem[0]
        self._exp=lvlsystem[1]
        self._party = 0
        self._gold = 0
    def increase_attack(self):
        self._ogattack += 2
    def increase_hitratio(self):
        self._oghitratio += 1
    def increase_health(self):
        self._maxhealth += 5
    def spend_gold(self, cost):
        self._gold -= cost
    def get_health(self):
        return self._health
    def get_gold(self):
        return self._gold
    def add_party(self, amount, partyskills):
        self._party = amount
        self._partyskills = partyskills
    def get_skills(self):
        return self._skillist
    def get_hitratio(self):
        return self._hitratio
    def get_attack(self):
        return self._attack
    def get_defence(self):
        return self._defence
    def get_magic(self):
        return self._magic
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def get_test(self):
        print("Attack ",self._attack,"Hitratio ", self._hitratio,"Defence ", self._defence)
    def damage(self, damage, hitratio):
        roll = random.randint(0, hitratio)
        if roll == hitratio:
            self._health-=damage * 1.5
            print("CRIT")
        elif roll >= self._defence:
            self._health-=damage
            print("Hit")
        else:
            print("Miss")
    def reset(self):
        self._health = self._maxhealth
        self._magic = self._maxmagic
        #nice
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._attack = self._ogattack
    def slevelup(self):
        self._exp+=76-self._level
        if self._exp >= 100:
            self._level += 1
            self._exp = 0
            x = 0
            while x < 3:
                x += 1
                roll = random.randint(1, 5)
                if roll == 1:
                    self._ogattack += 3
                elif roll == 2:
                    self._oghitratio += 1
                elif roll == 3:
                    self._ogdefence += 1
                elif roll == 4:
                    self._maxhealth += 10
                else:
                    self._maxmagic += 5
        if self._name!="Knight":
            output_file = open("Starscrapper.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
        else:
            output_file = open("Knightlv.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
    def levelup(self):
        self._exp+=76-self._level
        if self._exp >= 100:
            print("LVL UP")
            time.sleep(0.3)
            self._level += 1
            self._exp = 0
            x = 0
            while x < 3:
                x += 1
                roll = random.randint(1, 5)
                if roll == 1:
                    self._ogattack += 3
                    print("<attack up>")
                    time.sleep(0.3)
                elif roll == 2:
                    self._oghitratio += 1
                    print("<hit ratio up>")
                    time.sleep(0.3)
                elif roll == 3:
                    self._ogdefence += 1
                    print("<defence up>")
                    time.sleep(0.3)
                elif roll == 4:
                    self._maxhealth += 10
                    print("<health up>")
                    time.sleep(0.3)
                else:
                    self._maxmagic += 5
                    print("<magic up>")
                    time.sleep(0.3)
        if self._name!="Knight":
            output_file = open("Starscrapper.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
        else:
            output_file = open("Knightlv.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
    def battle(self, enemy):
        skillet = 0
        while self._health>0 and enemy.get_health()>0:
            time.sleep(0.8)
            if skillet == 0:
                skillet = 1
            else:
                skillet = 0
            roll = random.randint(1, 10)
            if roll == 5:
                skillet = 2
            enemyskillet = random.randint(0, 2)
            skillskillet = random.randint(0, 4)
            if skillskillet == 0 or skillskillet == 1:
                skillskillet = 0
            elif skillskillet == 2 or skillskillet == 3:
                skillskillet = 1
            else:
                skillskillet = 2
            print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
            print("Option 1: Attack")
            print("Option 2: Skill")
            print("Option 3: Search")
            print("Option 4: Escape")
            action = input("Number of action you would like to take: ")
            while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                print("try again")
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                print("Option 1: Attack")
                print("Option 2: Skill")
                print("Option 3: Search")
                print("Option 4: Escape")
                action = input("Number of action you would like to take: ")
            if action == "1":
                enemy.damage(self._attack, self._hitratio)
            elif action == "2":
                if skillet == 0:
                    self._health -= 2
                elif skillet == 1:
                    if self._magic > 0:
                        self._magic -= 2
                    else:
                        self._health -= 4
                if self._skillist[skillet] == "Hit Policy":
                    self._health += self._maxhealth//2
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Mystic Point":
                    enemy.damage(self._attack*2, self._hitratio)
                elif self._skillist[skillet] == "Transform":
                    useThis = self._defence
                    self._defence = self._hitratio
                    self._hitratio = useThis
                    print("HENSHIN")
                elif self._skillist[skillet] == "Point Blank":
                    enemy.damage(self._hitratio, 100000000)
                elif self._skillist[skillet] == "Timed Illusion":
                    self._health += enemy.get_attack()
                    self._hitratio += 3
                elif self._skillist[skillet] == "Pain Remover":
                    self._health += self._magic
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Over Joyed Trick":
                    self._health = self._maxhealth//2
                    self._hitratio += 100
                    self._defence = 0
                elif self._skillist[skillet] == "Monster Form":
                    self._hitratio += 10
                    self._defence += 1
                if self._skillist[skillet] == "Fruit of God":
                    self._health += self._magic*2
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Deathless Trick":
                    self._health += self._hitratio
                    self._hitratio += self._defence
                elif self._skillist[skillet] == "Star Scrapper":
                    self._hitratio += 10
                    self._defence += 3
                    self._magic -= 2
                    self._health -= 2
                elif self._skillist[skillet] == "Star Blaster":
                    self._attack += 10
                    self._hitratio += 10
                    enemy.damage(self._attack*2, self._hitratio*10)
                    self._hitratio -= 10
                    self._attack += 10
                    self._magic -= 2
                elif self._skillist[skillet] == "Great Regen":
                    self._magic += 4
                    self._health += self._magic
            elif action == "4":
                print("[???] you are a silly fool")
                time.sleep(0.9)
                print("[???] there is no escape")
                time.sleep(0.9)
                print("[???] don't even try")
                time.sleep(0.9)
            elif action == "7":
                enemy.damage(999999, 999999)
            else:
                print("ThErE iS nO eScApE sIlLy MoRtAl")
                print("Attack:", self._attack, "Hit Chance:", self._hitratio, "Defence:", self._defence)
                print("Enemy HP:", enemy.get_health())
            time.sleep(0.8)
            if enemy.get_skills()[enemyskillet] == "void":
                print("[Enemy]: Attack")
                roll = random.randint(0, enemy.get_hitratio())
                if roll>self._defence:
                    print("Hit")
                    self._health-=enemy.get_attack()
                else:
                    print("Miss")
            elif enemy.get_skills()[enemyskillet] == "Aura Force":
                print("[Enemy]: Aura Force")
                print("<enemy gains health>")
                enemy.damage(-3, 100000000)
            elif enemy.get_skills()[enemyskillet] == "God Scape":
                print("[Enemy]: God Scape")
                print("<the ground distorts bellow you>")
                self._defence = 1
                if self._magic > 10:
                    self._magic -= 10
                else:
                    self._health -= 5
            elif enemy.get_skills()[enemyskillet] == "Starscrapper":
                print("[Enemy]: Starscrapper")
                print("<time seems to speed up>")
                self._defence = 1
                self._hitratio = 1
                enemy.damage(self._attack*-1, 100000000)
            elif enemy.get_skills()[enemyskillet] == "Purify":
                print("[Enemy]: Attack")
                print("<your stats reset>")
                roll = random.randint(0, enemy.get_hitratio())
                if roll>self._defence:
                    print("Hit")
                    self._health-=enemy.get_attack()
                else:
                    print("Miss")
                self._defence = self._ogdefence
                self._hitratio = self._oghitratio
            elif enemy.get_skills()[enemyskillet] == "Time Roar":
                print("[Enemy]: Time Roar")
                self._health -= 20
                enemy.damage(-20, 100000000)
            elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                print("[Enemy]: #%&$#$^%")
                self._health -= 777
                enemy.damage(-777, 100000000)
            elif enemy.get_skills()[enemyskillet] == "Luck7":
                print("[Enemy]: Lucky Sevens")
                self._health -= 777
            elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                print("[Enemy]: Bite")
                self._health -= 25
                enemy.damage(-50, 100000000)
            time.sleep(0.6)
            if self._party > 0:
                if self._partyskills[skillskillet] == "Regen":
                    print("[Effect]: Regen")
                    self._health += 2
                elif self._partyskills[skillskillet] == "Hit Boost":
                    print("[Effect]: Hit Chance Up")
                    self._hitratio += 3
                elif self._partyskills[skillskillet] == "Petrify":
                    print("[Effect]: Don's Stone Face")
                    print("<your opponent slows down>")
                    print("<your magic raises>")
                    self._defence += 1
                    self._hitratio += 1
                    self._magic += 2
                elif self._partyskills[skillskillet] == "Dark Mode":
                    print("[Effect]: Fafnir's Dragon Mode")
                    print("<your stats raise sharply>")
                    self._defence += 1
                    self._hitratio += 2
                    self._attack += 2
                elif self._partyskills[skillskillet] == "The Hunt":
                    print("[Effect]: Narator?'s Cursed Skin?")
                    self._attack += 3
                    self._hitratio += 5
                    self._partyskills[skillskillet] = "Big Bang"
                elif self._partyskills[skillskillet] == "Big Bang":
                    print("[Effect]: Narator?'s Cursed Skin?")
                    self._attack += 6
                    self._hitratio += 10
                    self._partyskills[skillskillet] = "The Hunt"
                elif self._partyskills[skillskillet] == "Explosion":
                    print("[Effect]: EXPLOSION???")
                    self._attack += 10
                    self._hitratio += 10
                elif self._partyskills[skillskillet] == "Team Attack":
                    print("[Effect]: Bonus Round")
                    print("[Type]: Team Attack")
                    enemy.damage(self._attack*4, self._hitratio*4)
                elif self._partyskills[skillskillet] == "Break":
                    print("[Effect]: Bonus Round")
                    roll = random.randint(1, 4)
                    if roll == 1:
                        print("[Type]: Limit Break")
                        self._attack += 5
                        self._hitratio += 5
                    elif roll == 2:
                        print("[Type]: Bonus Strike")
                        enemy.damage(self._attack*2, self._hitratio*2)
                    elif roll == 3:
                        print("[Type]: Brave")
                        self._attack += 5
                        enemy.damage(self._attack, self._hitratio)
                    else:
                        print("[Type]: Over Throw")
                        self._defence += 2
                        self._hitratio += 5
                time.sleep(0.3)
            if self._party > 0 and enemy.get_health() < enemy.get_magic():
                roll = random.randint(1, 10)
                if roll == 5:
                    print("[Party Assault]: Active")
                    time.sleep(0.3)
                    enemy.damage(self._attack*10, self._hitratio*10)
            if self._magic < 0:
                    self._magic = 0
            if self._magic > 999:
                self._magic = 999
            if self._health > 99999:
                self._health = 99999
        print("Battle End")
        self._attack = self._ogattack
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
def random_encounter():
    roll = random.randint(0, 70)
    if roll <= 5:
        enemy = Characters("Colossus", [999, 10, 50, 5, 1], ["Purify", "void", "Time Roar"], [1, 2])
    elif roll >= 50:
        enemy = Characters("mini golem", [50, 2, 20, 1, 25], ["void", "void", "void"], [1, 2])
    else:
        enemy = Characters("large golem", [70, 4, 30, 3, 50], ["Purify", "void", "void"], [1, 2])
    return enemy
def random_encounter2():
    roll = random.randint(0, 70)
    if roll <= 5:
        enemy = Characters("Titan", [999, 30, 100, 10, 1], ["void", "void", "Purify"], [1, 2])
    elif roll >= 50:
        enemy = Characters("bear", [30, 5, 35, 1, 25], ["void", "void", "void"], [1, 2])
    else:
        enemy = Characters("wolf", [90, 7, 30, 10, 50], ["void", "void", "void"], [1, 2])
    return enemy
def random_encounter3():
    roll = random.randint(0, 91)
    if roll == 1:
        enemy = Characters("Vampire King", [9999, 50, 50, 10, 666], ["Purify", "Vamp Bite", "Purify"], [1, 2])
    elif roll >= 60:
        enemy = Characters("Slime", [80, 3, 50, 10, 60], ["void", "void", "Purify"], [1, 2])
    elif roll >= 30:
        enemy = Characters("Shadow", [50, 8, 35, 1, 25], ["void", "void", "void"], [1, 2])
    else:
        enemy = Characters("Fiend", [90, 7, 30, 10, 50], ["void", "void", "void"], [1, 2])
    return enemy
def random_encounter4():
    roll = random.randint(0, 91)
    if roll == 1:
        enemy = Characters("Shadow King", [9999, 30, 50, 10, 666], ["Purify", "Purify", "Purify"], [1, 2])
    elif roll >= 60:
        enemy = Characters("Shadowling", [70, 3, 40, 10, 60], ["void", "void", "Purify"], [1, 2])
    elif roll >= 30:
        enemy = Characters("Shadow", [50, 8, 35, 1, 25], ["void", "void", "void"], [1, 2])
    else:
        enemy = Characters("Shadow Fiend", [60, 5, 40, 10, 50], ["void", "void", "void"], [1, 2])
    return enemy
def astral_space(mc):
    action = "0"
    while mc.get_health() > 0 and action != "3":
        while action != "1" and action != "2" and action != "3":
            print("<the ground seems to be glowing>")
            print("Option 1: Walk Forward")
            print("Option 2: Heal")
            print("Option 3: Wake Up")
            action = input("The Hero Will: ")
        if action == "1":
            print("<you walk into something>")
            enemy = random_encounter()
            mc.battle(enemy)
            if mc.get_health() > 0:
                mc.levelup()
                action = "0"
        elif action == "2":
            mc.reset()
            print("HP:", mc.get_health())
            mc.get_test()
            action = "0"
        else:
            print("<you exit the space>")
            break
def mobile_city(mc, time):
    action = "0"
    day = 1
    while day < time:
        while action != "1" and action != "2" and action != "3":
            print("<the ground seems to be glowing>")
            print("Option 1: Hunt")
            print("Option 2: Rest")
            print("Option 3: Shop")
            action = input("The Hero Will: ")
        if action == "1":
            action = "0"
            print("<you check the hunter board>")
            enemy1 = random_encounter3()
            enemy2 = random_encounter3()
            enemy3 = random_encounter3()
            print("[Hunting Board]: " + enemy1.get_name() + "-" + enemy2.get_name() + "-" + enemy3.get_name())
            print("<do you wish to go hunting?>")
            print("Option 1: No")
            print("Option 2: Yes")
            act = input("what will you do? ")
            if act == "1":
                print("<you wait for tomorrow>")
                mc.reset()
                day += 1
            else:
                roll = random.randint(1, 3)
                if roll == 1:
                    mc.battle(enemy1)
                elif roll == 2:
                    mc.battle(enemy2)
                else:
                    mc.battle(enemy3)
                if mc.get_health() > 0:
                    mc.levelup()
                    action = "0"
                    mc.spend_gold(-3)
                else:
                    mc.reset()
                    day += 2
        elif action == "2":
            print("<you rest for the night>")
            mc.reset()
            day += 1
            print("HP:", mc.get_health())
            mc.get_test()
            action = "0"
        else:
            action = "0"
            print("<you head to the shop>")
            skip_engine(3)
            print("Gold:", mc.get_gold())
            print("Option 1: Feast-5gold")
            print("Option 2: Health Up-10gold")
            print("Option 3: Quick Train-10gold")
            print("Option 4: Challenge Beast-100gold")
            print("Option 5: Leave")
            act = input("What will you buy? ")
            if act == "1" and mc.get_gold() >= 5:
                print("<you eat a nice feast>")
                mc.spend_gold(5)
                mc.reset()
            elif act == "2" and mc.get_gold() >= 10:
                print("<you raise your stamina>")
                mc.spend_gold(10)
                mc.increase_health()
            elif act == "3" and mc.get_gold() >= 10:
                print("<you raise your strength>")
                mc.spend_gold(10)
                mc.increase_attack()
                mc.increase_hitratio()
            elif act == "4" and mc.get_gold() >= 100:
                mc.spend_gold(100)
                print("<you challenge the beast>")
                theStarScrapper = Characters("StarScrapper", [999999, 777, 100, 10, 333333], ["Purify", "Purify", "Time Roar2"], [1, 2])
                mc.battle(theStarScrapper)
                if mc.get_health() > 0:
                    mc.spend_gold(-500)
            elif act == "5":
                print("<you leave>")
            else:
                print("<you don't have enough gold>")
def shadow_city(mc, time):
    action = "0"
    day = 1
    while mc.get_health() > 0 and day < time:
        while action != "1" and action != "2" and action != "3":
            print("<the ground seems to be glowing>")
            print("Option 1: Hunt")
            print("Option 2: Rest")
            print("Option 3: Shop")
            action = input("The Hero Will: ")
        if action == "1":
            action = "0"
            print("<you check the hunter board>")
            enemy1 = random_encounter4()
            enemy2 = random_encounter4()
            enemy3 = random_encounter4()
            print("[Hunting Board]: " + enemy1.get_name() + "-" + enemy2.get_name() + "-" + enemy3.get_name())
            print("<do you wish to go hunting?>")
            print("Option 1: No")
            print("Option 2: Yes")
            act = input("what will you do? ")
            if act == "1":
                print("<you wait for tomorrow>")
                mc.reset()
                day += 1
            else:
                roll = random.randint(1, 3)
                if roll == 1:
                    mc.battle(enemy1)
                elif roll == 2:
                    mc.battle(enemy2)
                else:
                    mc.battle(enemy3)
                if mc.get_health() > 0:
                    mc.levelup()
                    action = "0"
                    mc.spend_gold(-3)
        elif action == "2":
            print("<you rest for the night>")
            mc.reset()
            day += 1
            print("HP:", mc.get_health())
            mc.get_test()
            action = "0"
        else:
            action = "0"
            print("<you head to the shop>")
            skip_engine(3)
            print("Gold:", mc.get_gold())
            print("Option 1: Feast-5gold")
            print("Option 2: Health Up-10gold")
            print("Option 3: Quick Train-10gold")
            print("Option 4: Challenge Beast-100gold")
            print("Option 5: Leave")
            act = input("What will you buy? ")
            if act == "1" and mc.get_gold() >= 5:
                print("<you eat a nice feast>")
                mc.spend_gold(5)
                mc.reset()
            elif act == "2" and mc.get_gold() >= 10:
                print("<you raise your stamina>")
                mc.spend_gold(10)
                mc.increase_health()
            elif act == "3" and mc.get_gold() >= 10:
                print("<you raise your strength>")
                mc.spend_gold(10)
                mc.increase_attack()
                mc.increase_hitratio()
            elif act == "4" and mc.get_gold() >= 100:
                mc.spend_gold(100)
                print("<you challenge the beast>")
                theStarScrapper = Characters("StarScrapper", [999999, 777, 100, 10, 333333], ["Purify", "Purify", "Time Roar2"], [1, 2])
                mc.battle(theStarScrapper)
                if mc.get_health() > 0:
                    mc.spend_gold(-500)
                mc.reset()
            elif act == "5":
                print("<you leave>")
            else:
                print("<you don't have enough gold>")
def forest_travel(mc, distance):
    action = "0"
    feet = 0
    while mc.get_health() > 0 and feet < distance:
        while action != "1" and action != "2" and action != "3":
            print("<the trees seem odd>")
            print("Option 1: Travel")
            print("Option 2: Rest")
            action = input("The Hero Will: ")
        if action == "1":
            roll = random.randint(1, 3)
            if roll == 1:
                print("<you walk into something>")
                enemy = random_encounter2()
                mc.battle(enemy)
                if mc.get_health() > 0:
                    mc.levelup()
                else:
                    mc.reset()
                feet += 1
            else:
                print("<you walk safely>")
                feet += 3
            action = "0"
            time.sleep(0.8)
        elif action == "2":
            mc.reset()
            print("<you set up camp>")
            print("HP:", mc.get_health())
            mc.get_test()
            action = "0"
            distance += 1
            time.sleep(0.8)
        else:
            print("<try again>")
            action = "0"
def saver(chapter):
    output_file = open("Saves.txt", "w")
    output_file.write(str(chapter))
    output_file.close()
    output_file = open("Name.txt", "w")
    output_file.write(str(name))
    output_file.close()
    output_file = open("Job.txt", "w")
    output_file.write(str(job))
    output_file.close()
"""output_file = open("Saves.txt", "w")
output_file.close()
output_file = open("Starscrapper.txt", "w")
output_file.close()
output_file = open("Knightlv.txt", "w")
output_file.close()"""
with open("Saves.txt", "r") as read_file:
    chapter=int(read_file.read())
with open("Job.txt", "r") as read_file:
    job=str(read_file.read())
with open("Name.txt", "r") as read_file:
    name=str(read_file.read())
if chapter > 0:
    if job=="1":
        mc = Characters(name, [40, 3, 10, 1, 10], ["Transform", "Pain Remover", "Timed Illusion"], [1, 2])
    elif job=="2":
        mc = Characters(name, [40, 5, 12, 1, 5], ["Transform", "Pain Remover", "Mystic Point"], [1, 2])
    elif job=="3":
        mc = Characters(name, [50, 3, 10, 2, 10], ["Transform", "Pain Remover", "Hit Policy"], [1, 2])
    elif job=="0":
        mc = Characters("Hard", [40, 3, 10, 1, 20], ["Transform", "Pain Remover", "Over Joyed Trick"], [1, 2])
    elif job=="5":
        mc = Characters("Easy", [100, 7, 20, 3, 30], ["Monster Form", "Fruit of God", "Point Blank"], [1, 2])
    elif job=="6":
        mc = Characters("Test", [999999, 999, 999, 9, 999], ["Pain Remover", "Point Blank", "Point Blank"], [1, 2])
    else:
        mc = Characters(name, [40, 10, 15, 1, 10], ["Transform", "Pain Remover", "Point Blank"], [1, 2])
    finalboss = Characters("Overlord", [50, 5, 15, 1, 30], ["void", "void", "God Scape"], [1, 2])
    if job == "5":
        knight = Characters("Knight", [60, 8, 20, 3, 20], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    elif job == "6":
        knight = Characters("Knight", [999999, 999, 999, 99, 999], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    else:
        knight = Characters("Knight", [40, 6, 15, 2, 5], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    with open("Starscrapper.txt", "r") as read_file:
        levelmx=int(read_file.read())
    with open("Knightlv.txt", "r") as read_file:
        klevelmx=int(read_file.read())
    while mc.get_level() < levelmx:
        mc.slevelup()
        mc.reset()
    while knight.get_level() < klevelmx:
        knight.slevelup()
        knight.reset()
if chapter == 0:
    theStarScrapper = Characters("StarScrapper", [999999, 3, 100, 10, 333333], ["Purify", "void", "Time Roar"], [1, 2])
    mc = Characters("Player", [200, 35, 100, 10, 20], ["Point Blank", "Hit Policy", "Timed Illusion"], [1, 2])
    print("[voice1] hello there player")
    skip_engine(3)
    print("[voice2] we are here to assist you")
    skip_engine(3)
    print("[voice3] in liberating this world")
    skip_engine(3)
    print("[voice1] we shall get started")
    skip_engine(3)
    print("[voice2] first we will teach you to fight")
    skip_engine(3)
    print("[voice3] to attack press 1")
    print("[voice2] to use your powers press 2")
    print("[voice1] never press 3")
    skip_engine(5)
    i = 0
    enemy = Characters("puppet", [100, 5, 15, 10, 20], ["void", "void", "void"], [1, 2])
    while i < 3:
        i += 1
        print("Tutorial Round")
        print("Round:", i)
        skip_engine(2)
        mc.battle(enemy)
        mc.reset()
        enemy.reset()
        skip_engine(5)
    print("[voices] now to get down to buisness")
    skip_engine(3)
    print("[voices] what is the hero's name?")
    name=input("name: ")
    print("[voices] what a wonderful name")
    skip_engine(3)
    print("[voices] now to decide your powers")
    print("Option 0: <Hard Mode>")
    print("Option 1: Illusionist")
    print("Option 2: Pyromancer")
    print("Option 3: Healer")
    print("Option 4: Blastsmith")
    print("Option 5: <Easy Mode>")
    job = input("What class do you want? ")
    if job=="1":
        mc = Characters(name, [40, 3, 10, 1, 10], ["Transform", "Pain Remover", "Timed Illusion"], [1, 2])
    elif job=="2":
        mc = Characters(name, [40, 5, 12, 1, 5], ["Transform", "Pain Remover", "Mystic Point"], [1, 2])
    elif job=="3":
        mc = Characters(name, [50, 3, 10, 2, 10], ["Transform", "Pain Remover", "Hit Policy"], [1, 2])
    elif job=="0":
        mc = Characters("Hard", [40, 3, 10, 1, 20], ["Transform", "Pain Remover", "Over Joyed Trick"], [1, 2])
    elif job=="5":
        mc = Characters("Easy", [100, 7, 20, 3, 30], ["Monster Form", "Fruit of God", "Point Blank"], [1, 2])
    elif job=="6":
        mc = Characters("Test", [999999, 999, 999, 9, 999], ["Pain Remover", "Point Blank", "Point Blank"], [1, 2])
    else:
        mc = Characters(name, [40, 10, 15, 1, 10], ["Transform", "Pain Remover", "Point Blank"], [1, 2])
    finalboss = Characters("Overlord", [50, 5, 15, 1, 30], ["void", "void", "God Scape"], [1, 2])
    if job == "5":
        knight = Characters("Knight", [60, 8, 20, 3, 20], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    elif job == "6":
        knight = Characters("Knight", [999999, 999, 999, 99, 999], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    else:
        knight = Characters("Knight", [40, 6, 15, 2, 5], ["Transform", "Pain Remover", "Deathless Trick"], [1, 2])
    knight.reset()
    knight.slevelup()
saver(chapter)
if chapter == 0:
    print("[voices] brilliant")
    skip_engine(2)
    print("[voices] try to battle as the hero")
    skip_engine(3)
    print("Test Battle")
    skip_engine(2)
    mc.battle(finalboss)
    mc.levelup()
    finalboss.levelup()
    mc.reset()
    finalboss.reset()
    print("      <...>")
    print("<Loading New World>")
    print("      <...>")
    skip_engine(10)
    print("<Tutorial Over>")
    skip_engine(3)
    print("<this world is filled with all different people")
    skip_engine(3)
    print("good, bad, heroes, villains")
    skip_engine(3)
    print("some people have magic, others don't")
    skip_engine(3)
    print("who are you?>")
    skip_engine(5)
    chapter += 1
saver(chapter)
if chapter == 1:
    i=0
    while i==0:
        print("[???] YOU VILLAIN!")
        skip_engine(1)
        print("[???] MURDERER!")
        skip_engine(1)
        print("[???] KILLER!")
        skip_engine(5)
        print("<waking up you look around")
        print("people all around you")
        skip_engine(6)
        print("some standing and yelling")
        skip_engine(3)
        print("others limp on the ground>")
        skip_engine(3)
        print("<what did you do?>")
        skip_engine(3)
        hero = Characters("SaberSlayer", [35, 2, 10, 1, 35], ["Purify", "Purify", "Starscrapper"], [1, 2])
        print("<an entity encased in light stands infront of you>")
        skip_engine(4)
        print("[entity] don't worry citizens")
        skip_engine(3)
        print("<all the people begin to cheer>")
        skip_engine(4)
        print("[entity] fear me villain>")
        skip_engine(4)
        print("[entity] FOR I CAN COMMAND TIME!!!")
        skip_engine(4)
        print("[entity] I am the hero SaberSlayer")
        skip_engine(4)
        print("[SS] and as a hero...")
        skip_engine(4)
        print("[SS] ...NO!")
        skip_engine(2)
        print("[SS] the GREATEST hero!")
        skip_engine(4)
        print("[SS] I will defeat you")
        skip_engine(3)
        print("<SaberSlayer sends an attack at you>")
        skip_engine(4)
        mc.reset()
        mc.battle(hero)
        if mc.get_health() > 0:
            i=1
            mc.levelup()
            mc.reset()
        else:
            print("<you lose>")
    print("<the hero lays infront of you")
    print("on the ground, dead>")
    skip_engine(5)
    print("[???] YOU VILLAIN!")
    skip_engine(1)
    print("[???] MURDERER!")
    skip_engine(1)
    print("[???] KILLER!")
    skip_engine(5)
    print("<you are NOT a hero>")
    print("<you run, tears falling from your face>")
    skip_engine(10)
    print("<you run down an alley way>")
    skip_engine(3)
    print("[???] hey, human, come quick")
    print("<you see a person's head poking out of a hole>")
    print("Option 1: join them")
    print("Option 2: run away")
    action = input("Where will you go? ")
    if action=="2":
        i=2
    while i == 1:
        print("<you jump down the hole>")
        print("[???] welcome to this world")
        skip_engine(5)
        print("[???] I can guess you aren't from here")
        skip_engine(3)
        print("[???] are you really a bad person?")
        skip_engine(3)
        print("Option 1: yes")
        print("Option 2: no")
        action = input("are you? ")
        if action == "2":
            print("[???] we are similar you and I")
            skip_engine(5)
            print("[???] I never chose this path")
            skip_engine(3)
            print("[???] so forgive me")
            skip_engine(1)
        else:
            print("[???] then I don't have to feel bad about this")
            skip_engine(2)
            mc.levelup()
        print("<you suddenly pass out>")
        i=2
    while i == 2:
        print("<you find yourself in an empty space>")
        skip_engine(5)
        astral_space(mc)
        mc.reset()
        i=3
    print("<you wake up slowly>")
    skip_engine(3)
    print("[???] oh? you woke up?")
    skip_engine(4)
    print("[???] sorry about before")
    print("[???] you see I'm Don")
    skip_engine(5)
    print("[Don] just like you I was sent here")
    skip_engine(3)
    print("[Don] you see there isn't enough villians left")
    print("[Don] so the heroes have to make new villains")
    skip_engine(10)
    print("[Don] these villians are known as 'beasts'")
    skip_engine(5)
    print("[Don] villians created by the voices")
    skip_engine(5)
    print("[Don] though this world has a name")
    print("[Don] the star scrapper")
    skip_engine(8)
    print("[Don] though we might die soon")
    print("[Don] as the world itself is dying")
    skip_engine(6)
    print("[Don] the place you were just in...")
    skip_engine(5)
    print("<silence falls over the room>")
    skip_engine(5)
    print("[Don] is the mind of the star scrapper")
    skip_engine(5)
    print("[Don] never stay in there too long though")
    skip_engine(5)
    print("[Don] the beasts there can get really powerful")
    skip_engine(5)
    print("<the ground starts to shake>")
    skip_engine(3)
    print("[Don] the heroes found us")
    skip_engine(3)
    print("<Don joins the party>")
    mc.add_party(1, ["Regen", "Hit Boost", "Petrify"])
    skip_engine(2)
    i=0
    while i==0:
        print("<a caped man breaks through the wall>")
        skip_engine(5)
        print("[Hero] I am star chaser")
        skip_engine(3)
        print("[SC] you must be taken down")
        skip_engine(3)
        print("[SC] I truly am sorry")
        skip_engine(3)
        print("[SC] I hope you can return to the stars")
        skip_engine(4)
        hero = Characters("Star Chaser", [20, 2, 15, 1, 20], ["Aura Force", "void", "Purify"], [1, 2])
        mc.battle(hero)
        if mc.get_health()>0:
            i=1
        mc.reset()
    while i==1:
        print("[SC] you seem very powerful")
        skip_engine(4)
        print("[SC] but I can not let you live")
        skip_engine(4)
        print("[SC] the world would never forgive me")
        skip_engine(5)
        hero = Characters("Star Chaser", [50, 5, 15, 5, 20], ["Aura Force", "void", "Purify"], [1, 2])
        mc.battle(hero)
        if mc.get_health()>0:
            i=2
        mc.reset()
    print("[SC] you have earned my trust")
    skip_engine(3)
    print("[SC] my boss will probably kill me for this...")
    skip_engine(6)
    print("[SC] run, I'll hold off the others...")
    skip_engine(4)
    print("[SC] you will be our savior...")
    skip_engine(4)
    print("[SC] ...our hero")
    skip_engine(3)
    print("<you and Don run away from the other heroes>")
    skip_engine(5)
    print("<chapter 1 end>")
    chapter += 1
mc.add_party(1, ["Regen", "Hit Boost", "Petrify"])
saver(chapter)
if chapter == 2:
    skip_engine(5)
    print("[Dragon] hello young hero")
    print("[Dragon] you must be confused")
    skip_engine(5)
    print("[Dragon] this story follows 2 characters")
    skip_engine(4)
    print("[Dragon] you met our first hero")
    skip_engine(4)
    print("[Dragon] now you will meet the second soon")
    skip_engine(4)
    print("[Dragon] even if you already know them")
    skip_engine(4)
    print("<your eyes open as you look around>")
    skip_engine(4)
    print("<standing up it seems your in a forest>")
    print("<it's dark and there is a small fire going>")
    skip_engine(8)
    print("<you start to walk around the woods>")
    skip_engine(3)
    i=0
    while i==0:
        print("<you walk till you find a small river>")
        skip_engine(3)
        print("<some kind of monster attacks you from behind>")
        skip_engine(5)
        enemy = Characters("Beast", [30, 1, 20, 1, 10], ["void", "void", "void"], [1, 2])
        knight.battle(enemy)
        knight.reset()
        if knight.get_health() >0:
            print("<the beast knocks you down and runs>")
            skip_engine(4)
            i=1
    i=0
    while i==0:
        print("<you walk around and find a small cave>")
        skip_engine(3)
        print("<some kind of bear attacks you>")
        enemy = Characters("Bear", [20, 3, 15, 1, 10], ["void", "void", "void"], [1, 2])
        skip_engine(3)
        knight.battle(enemy)
        knight.reset()
        if knight.get_health() >0:
            print("<the bear knocks you down and runs>")
            skip_engine(4)
            print("<you pass out>")
            i=1
    astral_space(knight)
    knight.reset()
    print("<you still seem to be in this space>")
    skip_engine(3)
    print("<your mind slowly disapearing>")
    skip_engine(3)
    print("<this might be the end>")
    skip_engine(3)
    print("[Dragon] don't worry, you won't die")
    print("[Dragon] you still have to save this world")
    skip_engine(8)
    print("[Dragon] the knight that will save us all")
    skip_engine(5)
    print("<the dragon fuses with your body>")
    skip_engine(4)
    print("<Fafnir joined the party>")
    skip_engine(8)
    print("<you pass out again>")
    knight.add_party(1, ["Regen", "Hit Boost", "Dark Mode"])
    astral_space(knight)
    knight.reset()
    print("<you wake up somewhere towards the edge of the forest>")
    skip_engine(5)
    print("<you hear people in the distance>")
    skip_engine(4)
    print("<you head off and see a giant kingdom>")
    skip_engine(5)
    print("<a shadowy figure stands over the kingdom>")
    skip_engine(5)
    print("<the world starts to fall apart>")
    skip_engine(4)
    print("<you get sucked into the sky>")
    skip_engine(4)
    print("<the ground below you breaking apart>")
    skip_engine(4)
    print("<the shadowy figure attacks you>")
    enemy = Characters("Shadow", [100, 10, 100, 10, 30], ["God Scape", "void", "Aura Force"], [1, 2])
    knight.battle(enemy)
    knight.levelup()
    knight.reset()
    print("<the portal is too strong as it sucks you up>")
    skip_engine(4)
    print("<chapter 2 end>")
    chapter += 1
saver(chapter)
knight.add_party(1, ["Regen", "Hit Boost", "Dark Mode"])
if chapter == 3:
    skip_engine(4)
    print("[???] oh? You are finally awake?")
    skip_engine(4)
    print("[Don] you fell asleep after we ran")
    skip_engine(4)
    print("[Don] can't come to terms")
    skip_engine(3)
    print("[Don] we are stuck in the wild")
    skip_engine(4)
    print("<you decided to wonder around>")
    skip_engine(4)
    forest_travel(mc, 40)
    print("<you hear something big in the distance>")
    skip_engine(4)
    forest_travel(mc, 10)
    print("<you see a large tank in the distance>")
    skip_engine(5)
    print("[Don] I've never seen that before")
    skip_engine(4)
    print("<you and Don walk towards the tank>")
    skip_engine(4)
    print("<the tank seems to have a city on it's back>")
    skip_engine(5)
    print("<the tank stops moving>")
    skip_engine(4)
    print("<a ladder drops down>")
    skip_engine(3)
    print("<Don starts to climb the latter>")
    skip_engine(4)
    print("[Don] come on already")
    skip_engine(3)
    print("<you start to climb the ladder>")
    skip_engine(4)
    print("<there is a town on the tank, people walking around>")
    skip_engine(6)
    print("<you and Don decide to stay the night>")
    skip_engine(5)
    print("<you and Don decided to stay a while>")
    skip_engine(4)
    mobile_city(mc, 7)
    mc.reset()
    print("<a hole rips open in the sky>")
    skip_engine(4)
    print("<chapter 3 end>")
    chapter += 1
saver(chapter)
if chapter == 4:
    skip_engine(4)
    print("<Don has left the party>")
    skip_engine(4)
    print("[???] HELLO WORTHLESS MORTAL OF NO HOPE")
    skip_engine(8)
    print("[???] I am your new narrator")
    skip_engine(4)
    print("[Narator?] at this point you have noticed something...")
    skip_engine(6)
    print("[Narator?] ...hopefully")
    skip_engine(4)
    print("[Narator?] yes player, those voids")
    skip_engine(4)
    print("[Narator?] now the characters are somewhere new")
    skip_engine(5)
    print("[Narator?] but who is the villain?")
    skip_engine(5)
    print("[Narator?] well it's me of course")
    skip_engine(4)
    print("<the narator has joined your party>")
    skip_engine(4)
    mc.add_party(1, ["The Hunt", "The Hunt", "Explosion"])
    print("<you wake up in some kind of house>")
    skip_engine(4)
    print("[voice] hello")
    skip_engine(3)
    print("[in] there")
    skip_engine(3)
    print("[your] silly")
    skip_engine(3)
    print("[head] motral")
    skip_engine(3)
    print("[Narator?] I'll speak to you as we continue")
    skip_engine(5)
    print("[Narator] a shadowy figure stands infront of you")
    skip_engine(4)
    print("[Narator?] you should probably get ready to fight")
    skip_engine(5)
    enemy = Characters("Knight", [101, 1, 1, 101, 40], ["void", "void", "void"], [1, 2])
    mc.battle(enemy)
    mc.reset()
    print("<the shadow disappears>")
    skip_engine(4)
    print("[Narator?] luckily we won")
    skip_engine(4)
    print("[Narator?] we should probably take a rest")
    skip_engine(4)
    print("<chapter 4 end>")
    chapter += 1
mc.add_party(1, ["The Hunt", "The Hunt", "Explosion"])
saver(chapter)
if chapter == 5:
    skip_engine(4)
    print("<Knight wakes up in a strange city>")
    skip_engine(4)
    shadow_city(knight, 11)
    print("<you walk into a small hut outside town>")
    skip_engine(6)
    print("<some old lady sitting in the middle of it>")
    skip_engine(6)
    print("[Old lady] I'm sorry")
    skip_engine(3)
    print("[Old lady] this world was not meant for you")
    skip_engine(5)
    print("[Old lady] the gods are after you")
    skip_engine(4)
    print("[Old lady] you must defeat them to live")
    skip_engine(4)
    print("[Old lady] call me Don, I want to help")
    skip_engine(4)
    print("[Don?] to you, the player")
    skip_engine(4)
    print("[Don?] after all, you are dead")
    skip_engine(4)
    print("[Don?] as a hero once said, you will save us")
    skip_engine(6)
    print("[Don?] just in another life")
    skip_engine(4)
    print("[Don?] now it is your turn to be the hero")
    skip_engine(4)
    print("[Don?] so you must head to the skies...")
    skip_engine(4)
    print("[Don?] ...where time no longer exists...")
    skip_engine(4)
    print("[Don?] ...and kill the god who killed you")
    skip_engine(4)
    print("<chapter 5 end>")
    chapter += 1
saver(chapter)
if chapter == 6:
    skip_engine(4)
    enemy = Characters("Narator?", [999999, 9, 999, 999, 666666], ["void", "void", "void"], [1, 2])
    print("<you wake up in darkness>")
    skip_engine(4)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[#$#@!$] !@#%&^%^!!#$%$#%")
    skip_engine(2)
    print("[???] you will never be a hero")
    skip_engine(5)
    print("[???] stop trying")
    skip_engine(3)
    print("[???] stop")
    skip_engine(1)
    print("[???] STOP")
    skip_engine(1)
    print("[???] STOP!")
    skip_engine(1)
    print("[???] STOP!!!")
    skip_engine(1)
    print("[???] STOP! STOP! STOP!")
    skip_engine(1)
    print("<you are the villain>")
    skip_engine(4)
    mc.add_party(0, [])
    mc.battle(enemy)
    print("[???] this is the end of you")
    skip_engine(4)
    print("[???] I'm sorry")
    skip_engine(3)
    print("<chapter 6 end?>")
    skip_engine(4)
    print("<Knight and Don stand infront of a door>")
    skip_engine(5)
    print("[Don] this is your last chance to turn back")
    skip_engine(5)
    print("[Don] the next step you take could be your last")
    skip_engine(8)
    print("[Don] we must defeat the one on the other side though")
    skip_engine(8)
    act = "0"
    while act != "1":
        print("<open the door?>")
        print("Option 1: Yes")
        print("Option 2: no")
        act = input("what will you do?")
        if act == "2":
            print("[Don] are you sure?")
            skip_engine(3)
    print("<you slowly open the door>")
    skip_engine(3)
    print("<chapter 6 end!>")
    chapter += 1
saver(chapter)
mc.add_party(0, [])
if chapter == 7:
    skip_engine(4)
    enemy = Characters("Narator?", [999, 9, 999, 10, 555], ["void", "void", "void"], [1, 2])
    print("<Don joins your party>")
    knight.add_party(2, ["Dark Mode", "Petrify", "Break"])
    print("<you see a being in all white>")
    skip_engine(4)
    print("<long flowing black hair>")
    skip_engine(4)
    while chapter == 7:
        print("[???]: we live in a godless world")
        skip_engine(3)
        print("[???]: I don't want to be here anymore")
        skip_engine(5)
        print("[???]: I am no god, just a viewer")
        skip_engine(4)
        i=0
        while i<5:
            print("[???]: I am no god")
            i+=1
            skip_engine(1)
        i=0
        while i<5:
            print("[???]: I am no goddess")
            i+=1
            skip_engine(1)
        i=0
        while i<5:
            print("[???]: I am not your goddess")
            i+=1
            skip_engine(2)
        i=0
        while i<3:
            print("[???]: die")
            i+=1
            skip_engine(1)
        print("[#%$]: I should of stayed in that box")
        skip_engine(5)
        print("[$@#]: all those years ago")
        skip_engine(4)
        print("[^%&]: he left me")
        skip_engine(4)
        print("[&*$]: the hero died")
        skip_engine(4)
        print("[@%#]: my hero left me")
        skip_engine(5)
        print("<the being turns around>")
        skip_engine(5)
        print("<tears rolling down her face>")
        skip_engine(6)
        print("[%$#]: and you are next")
        skip_engine(4)
        knight.battle(enemy)
        if knight.get_health() > 0:
            chapter = 8
            knight.levelup()
        knight.reset()
saver(chapter)
if chapter == 8:
    print("[???]: I thank you hero")
    skip_engine(4)
    print("[???]: for trying your best")
    skip_engine(4)
    print("[???]: I can finally escape this world")
    skip_engine(4)
    enemy = Characters("Narator?", [999, 666, 999, 10, 999], ["Purify", "Purify", "Luck7"], [1, 2])
    knight.battle(enemy)
    knight.levelup()
    knight.reset()
    print("<You pass out from exhaustion>")
    astral_space(knight)
    knight.reset()
    print("<you slowly wake up>")
    skip_engine(4)
    print("<the entity seemed to of disapeared>")
    skip_engine(4)
    print("[Don]: so...what do we do now?")
    skip_engine(4)
    print("[Don]: we can't beat that..being by ourselves")
    skip_engine(4)
    print("what will you do?")
    print("Option 1: save the world")
    print("Option 2: watch the world burn")
    action = input("what now? ")
    if action == 2:
        chapter = 20
    else:
        chapter = 9
saver(chapter)
if chapter == 9:
    print("<turning around you come face to face with a pirate>")
    skip_engine(7)
    print("<tall, eyepatch over right eye>")
    skip_engine(5)
    print("<they look at you, then smile>")
    skip_engine(5)
    print("[Pirate]: please save them")
    skip_engine(4)
    print("[Pirate]: those who helped you")
    print("[Pirate]: those who hurt you")
    print("[Pirate]: those in the past")
    print("[Pirate]: then those in the future")
    print("[Pirate]: but most importantly...")
    skip_engine(15)
    print("[Pirate]: ...the one who started this all...")
    skip_engine(7)
    print("[Pirate]: ...Shelly")
    skip_engine(3)
    print("<you blink and the pirate is gone>")
    skip_engine(4)
    print("<you march on, towards the future>")
    skip_engine(4)
    print("<chapter 7 end>")
    chapter = 10
saver(chapter)
if chapter == 10:
    skip_engine(4)
    print("<running through explosion and rubble...")
    skip_engine(4)
    print("...you eventually reach a small building>")
    skip_engine(4)
    print("<a dark entity stands over the village>")
    skip_engine(4)
    print("<the ground is being pulled apart and buildings are blowing up>")
    skip_engine(6)
    print("<a monster runs out of the darkness, attacking you>")
    skip_engine(4)
    enemy = Characters("beast", [300, 100, 100, 30, 300], ["void", "void", "Purify"], [1, 2])
    knight.battle(enemy)
    if knight.get_health > 0:
        chapter = 11
        knight.levelup()
        knight.reset()
    else:
        print("<you passed out>")
        forest_travel(knight, 30)
saver(chapter)
if chapter == 11:
    skip_engine(4)
    print("<the beast jumps back in fear>")
    skip_engine(4)
    print("<you decide to continue on>")
    skip_engine(4)
    print("<a being stand infront of you>")
    skip_engine(4)
    print("[SS]: stop human, for I am the Saber Slayer")
    skip_engine(5)
    print("[SS]: it has been requested that I stop you")
    skip_engine(5)
    print("[SS]: so prepare to do battle")
    enemy = Characters("Saber Slayer", [300, 100, 100, 30, 300], ["Purify", "Purify", "Starscrapper"], [1, 2])
    knight.battle(enemy)
    if knight.get_health > 0:
        chapter = 12
        knight.levelup()
        knight.reset()
    else:
        print("<you passed out>")
        forest_travel(knight, 30)
saver(chapter)
if chapter == 12:
    skip_engine(4)
    print("[SS]: I permit you to continue on, just be careful")
    skip_engine(5)
    print("<you walk upto a bridge>")
    skip_engine(3)
    print("<walking across the bridge a shadowy figure stops you>")
    skip_engine(6)
    print("[???]: stop there fowl beast")
    enemy = Characters("Shadow Slayer", [200, 100, 100, 30, 300], ["void", "Purify", "Aura Force"], [1, 2])
    knight.battle(enemy)
    if knight.get_health > 0:
        chapter = 13
        knight.levelup()
        knight.reset()
    else:
        print("<you passed out>")
        forest_travel(knight, 30)
saver(chapter)
if chapter == 13:
    print("<you stand over the entity>")
    skip_engine(4)
    print("<you have a thought>")
    skip_engine(3)
    print("<what is all of this for?>")
    skip_engine(4)
    print("<chapter 8 end>")
    chapter = 14
saver(chapter)
jib = 0
while jib == 0:
    if chapter == 14:
        skip_engine(4)
        print("[???]: I'm doing this for my beloved")
        skip_engine(4)
        print("<you look up and see a creepy figure>")
        skip_engine(4)
        print("[Shelly]: if he is never born, then it won't hurt")
        skip_engine(5)
        print("[Shelly]: I just want a perfect world")
        skip_engine(4)
        print("[Shelly]: so why are you trying to stop me?")
        skip_engine(4)
        print("[Shelly]: do you want an imperfect world?")
        skip_engine(4)
        print("[Shelly]: villain")
        skip_engine(1)
        print("[Shelly]: murderer")
        skip_engine(1)
        print("[Shelly]: I will stop you")
        skip_engine(4)
        print("<you feel as your body fades away, sucked into the sky>")
        skip_engine(6)
        forest_travel(knight, 100)
        knight.reset
        chapter = 15
    saver(chapter)
    if chapter == 15:
        print("<you find yourself in a giant dark castle>")
        skip_engine(5)
        print("<looking around you find an alter>")
        skip_engine(5)
        print("<on the alter sits a sailor's cap with a note on it>")
        skip_engine(7)
        print("<the note reads: goodbye, to all those I loved")
        print("you will always be with me in spirit. for we are all bound together.")
        print("we will meet again, at the end of our roads, a new journey.")
        print("NEVER GIVE UP!!!")
        skip_engine(25)
        print("<Don walks up behind you>")
        skip_engine(4)
        print("[Don]: when my partner died I found something...")
        skip_engine(5)
        print("[Don]: ...something incredible, an hour glass")
        skip_engine(5)
        print("[Don]: after touching it I found myself here.")
        skip_engine(5)
        print("[Don]: before my jounrey even began.")
        skip_engine(4)
        print("[Don]: that changed fate, and is what Shelly wishes")
        skip_engine(6)
        print("[Don]: to change fate, to save herself, not others")
        skip_engine(6)
        print("[Don]: we must stop her, this is our last chance")
        skip_engine(5)
        print("<a dark monster walks up behind you>")
        skip_engine(4)
        print("[Shelly?]: help me, help me")
        skip_engine(4)
        print("<it jumps at you>")
        enemy = Characters("Shelly", [600, 50, 100, 50, 300], ["Vamp Bite", "Purify", "God Scape"], [1, 2])
        knight.battle(enemy)
        if knight.get_health > 0:
            chapter = 16
            jib = 1
            knight.levelup()
            knight.reset()
        else:
            print("<you passed out>")
            chapter = 14
saver(chapter)
if chapter == 16:
    print("<you suddenly wake up>")
    skip_engine(3)
    print("<you find yourself in a small town>")
    skip_engine(5)
    print("<one of the townsfolk walks towards you>")
    skip_engine(5)
    print("[???]: welcome back "+ mc.get_name() + " we missed you")
    skip_engine(5)
    print("[???]: after the battle you vanished. But now you are back")
    skip_engine(6)
    print("[???]: thank you, for allowing us to continue")
    skip_engine(5)
    print("[???]: this is the future we made. All of us")
    skip_engine(5)
    print("<Don, Knight, Fafnir, Saber Slayer, Star Chaser all stand at the edge of the town>")
    skip_engine(8)
    print("[Don]: I missed you")
    print("[Knight]: ...")
    print("[Fafnir]: you did great")
    print("[SS]: you were almost as good as me")
    print("[SC]: I knew you could save us")
    skip_engine(8)
    print("<as the years went by the world evolved>")
    skip_engine(4)
    print("<eventually everyone decided to start a crew>")
    skip_engine(5)
    print("<and travel the world together>")
    skip_engine(4)
    print("<the end>")
if chapter == 20:
    print("<you walk out of the gates>")
    skip_engine(4)
    print("<an entity of pure darkness floats over the sky>")
    skip_engine(5)
    print("<the world slowly crumbling>")
    skip_engine(4)
    print("[Don]: it was nice while it lasted...")
    skip_engine(7)
    print("<an explosion appears in the distance>")
    skip_engine(5)
    print("<it quickly approach>")
    skip_engine(4)
    print("[Don]: ...while it lasted...")
    skip_engine(4)
    print("<the explosion absorbs both of you>")
    skip_engine(7)
    print("...The End")

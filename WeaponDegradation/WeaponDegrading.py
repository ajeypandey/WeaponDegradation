#WEAPON DEGRADATION CHECKER
#TODO integrate input driver
#TODO integrate way to add new weapons, delete old weapons, print new textfile
#TODO fix datatypes

import sys

class Weapon:
	def __init__(self, owner, name, hp, maxhp):
		self.owner = owner
		self.name = name
		self.hp = hp
		self.maxhp = maxhp

	def print_weapon(self):
		return self.owner + "'s " + self.name + "\tHP: " + str(self.hp) + "/" + str(self.maxhp) + " = " + str(self.percent()) + "%"

	def save_weapon(self):
		return self.owner + "," + self.name + "," + str(self.hp) + "," + str(self.maxhp) 

	def set_owner(self,new):
		self.owner = new

	def set_name(self,new):
		self.name = new

	def set_hp(self,new):
		self.hp = new

	def set_maxhp(self,new):
		self.maxhp = new

	def deal_damage(self,damage):
		if self.hp < damage:
			self.hp = 0
			print "\nWEAPON BROKEN\n"
		else:
			self.hp -= damage

	def repair(self,health):
		self.hp += health
		if self.hp > self.maxhp:
			self.hp = self.maxhp

	def percent(self):
		return 100*self.hp/self.maxhp
	
with open(sys.argv[1], 'r') as text_in:
	weapons_in = text_in.read().split('\n')

weapon_list = []
for x in range(0,len(weapons_in)):
	w = weapons_in[x].split(',')
	weapon_list.append(Weapon(w[0],w[1],int(w[2]),int(w[3])))
	# weapon_list[x].print_weapon()
running = True
while running:
	print "************\nWEAPON TRACKER"
	for x in range(0,len(weapon_list)):
		print str(x) + ": " + weapon_list[x].print_weapon()
	user_in = input("ENTER COMMAND:\n 0: EXIT\t1: DEAL DAMAGE\t2: REPAIR WEAPON\t3: ADD WEAPON\t4 DROP WEAPON\t5: SAVE AND QUIT\n")
	if user_in==0:
		running = False
	elif user_in==1:
		in_2 = input("ENTER WEAPON NUMBER:\t")
		if in_2 < len(weapon_list):
			in_damage = input("DEAL DAMAGE:\t")
			if isinstance(in_damage, int):
				weapon_list[in_2].deal_damage(in_damage)
			else:
				print "NOT A NUMBER"
		else:
			print "NOT A WEAPON"
	elif user_in==2:
		in_2 = input("ENTER WEAPON NUMBER:\t")
		if in_2 < len(weapon_list):
			in_damage = input("REPAIR DAMAGE:\t")
			if isinstance(in_damage, int):
				weapon_list[in_2].repair(in_damage)
			else:
				print "NOT A NUMBER"
		else:
			print "NOT A WEAPON"
	elif user_in==3:
		in_3 = raw_input("ENTER WEAPON OWNER:\t")
		in_4 = raw_input("ENTER WEAPON NAME:\t")
		in_5 = input("ENTER WEAPON HP:\t")
		in_6 = input("ENTER WEAPON MAXHP:\t")
		if (isinstance(in_5, int) & isinstance(in_6,int)):
			weapon_list.append(Weapon(in_3,in_4,in_5,in_6))
		else:
			print "IMPROPER ENTRY"
	elif user_in==4:
		in_2 = input("ENTER WEAPON NUMBER:\t")
		if in_2 < len(weapon_list):
			del weapon_list[in_2]
		else:
			print "NOT IN LIST"
	elif user_in==5:	
		save_file = open("WeaponTrackerSaved.txt","w")
		for x in range(0,len(weapon_list)):
			save_file.write(weapon_list[x].save_weapon()+"\n")
		running = False
	else:
		print "IMPROPER COMMAND"

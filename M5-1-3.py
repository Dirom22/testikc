import random

class Warrior:                   # Класс создания воинов
	health = 100                 # Здоровье
	endurance = 100              # Выносливость
	armor = 100                  # Броня
	
	def __init__(self, name):
		self.name = name         # Имя воина
		
	def ataka(self):             # Повреждения противника 
		self.health -= random.randint(10,30)
		self.endurance -= 10
		self.armor -= random.randint(8,10)

	def protection(self):         # Повреждения при защите
		self.health -= random.randint(10,20)
		self.endurance -= random.randint(0,10)
		self.armor -= random.randint(0,10)
		

w1 = Warrior('Roni')
w2 = Warrior('Robin')


while True:
	a = int(input('Введите 1 начало, 2 выход: '))
	if a == 2:
		print(' Конец игры!!!!')
		print('   УДАЧИ!!!!')
		break
	elif a == 1:
		while w1.health <= 10:
			b = (w1, w2)
			c = random.choice(b)
			if c == w1:
				w2.ataka()
				print(w2.name, w2.health, w2.endurance, w2.armor)
				print(w1.name, w1.health, w1.endurance, w1.armor)
			elif c == w2:
				print(w1.name, w1.health, w1.endurance, w1.armor)
				print(w2.name, w2.health, w2.endurance, w2.armor)
	else:
		break
		


	

'''class Bitva(Warrior):
	
	def ataka_ataka():
		health_1 -= random(10, 30) 
		health_2 -= random(10, 30)
		endurance_1 -= 10
		endurance_2 -= 10
		armor_1 -= random(0, 10)
		armor_2 -= random(0, 10)

	def ataka_protection():
		pass
	
--w1 = Woin_1('Roni')
--w2 = Woin_2('Robi')

w1.fav()
w2.fav()


1: атака 2: атака
health_1 -= random(10,30)
health_2 -= random(10,30)
end_1 -= 10 end_2 -= 10

1: атака 2: защита
end_1 -= 10 health_2 -=
random(0,20)
armor_2 -= random(0,10)'''

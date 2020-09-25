
class creaturele:
	clasa='characters'
	def __init__(self,creatures,nume,strength,defence,health):
		self.creatures=creatures
		self.nume=nume
		self.strength=strength
		self.defence=defence
		self.health=health
import random, time



#creatures variables
elfs=creaturele('Elf', 'Vandalis', '350', '650', '100')
dwarfs=creaturele('Dwarf', 'Krat', '430', '700','100')
humans=creaturele('Human', 'Bostan', '680', '360', '100')
tekks=creaturele('Tech','Tekk', '200', '530', '100')
#weapons variables
sword=creaturele('','Sword','830', '290','')
hammer=creaturele('','Hammer','470','680','')
shield_kinfe=creaturele('','Shield and knife','200', '800','')
#name=input('Enter your name: ' '\n')
#Computer opponnent variables
rand_c=[1,2,3,4]
computer_c=random.choice(rand_c)
rand_w =[1,2,3]
computer_w=random.choice(rand_w)


def restart(): # reatarts the game if the user answers y in the end.
	

	#print('{} is an {}, strenth{} and defence {}'. format(elfs.nume, elfs.creatures, elfs.strength, elfs.defence))
	print('Choose your warrior:' '\n' ,'For Elf, press 1: ' ,'\n' ,'For Dwarf, press 2:' ,'\n' ,'for Human, press 3:', '\n','For Tech, press 4:' )
	sel_creature=input()

	time.sleep(1)
	print('Your chosen warrior is:')


			
		#return '{} is an {}' '\n' 'Strength {}' '\n' 'Defence is: {}'.format(elfs.nume, elfs.creatures, elfs.strength, elfs.defence)
		
	#global h_p

		
		
	if sel_creature=='1':
		
		print('Name: {} is an {}' '\n' 'Attack: {}' '\n' 'Defence: {}' '\n' 'Heatlh: {}'.format(elfs.nume, elfs.creatures, elfs.strength, elfs.defence, elfs.health))
		h_power=((int(elfs.strength))+int((elfs.defence)))
		h_p=h_power/2
			
		
	if sel_creature=='2':
				
		print('Name: {} is an {}' '\n' 'Attack: {}' '\n' 'Defence: {}' '\n' 'Heatlh: {}'.format(dwarfs.nume, dwarfs.creatures, dwarfs.strength, dwarfs.defence, elfs.health))
		h_power=((int(dwarfs.strength))+int((dwarfs.defence)))
		h_p=h_power/2
		
		
	if sel_creature=='3':
				
		print('Name: {} is a {}' '\n' 'Attack: {}' '\n' 'Defence: {}' '\n' 'Heatlh: {}'.format(humans.nume, humans.creatures, humans.strength, humans.defence, humans.health))
		print('')
		h_power=((int(humans.strength))+int((humans.defence)))
		h_p=h_power/2
			

	if sel_creature=='4':
				
		print('Name: {} is a {} creature' '\n' 'Attack: {}' '\n' 'Defence: {}' '\n' 'Heatlh: {}'.format(tekks.nume, tekks.creatures, tekks.strength, tekks.defence, tekks.health))
		h_power=((int(tekks.strength))+int((tekks.defence)))
		h_p=h_power/2
	#else:
	#	print('Error, please follow the instructions.')
		
	#if str(sel_creature<=0) or str(sel_creature>4):
		#print('Error, please follow the instructions.')	
		
	#else:
		#print('error, please follow the instructions')
			



	time.sleep(1)
	print('')		
	print('Choose your weapon:' '\n' ,'For Sword, press 1: ' ,'\n' ,'For Hammer, press 2:' ,'\n' ,'For Shield and Knife, press 3:')	
	sel_weapon=input('')
	time.sleep(1)	
	print('Your weapon is:')
	#global w_p

		
	if sel_weapon=='1':
		
		_weapon=1	
		print('{} Selected' '\n' 'Attack: {}' '\n' 'Defence: {}'.format(sword.nume, sword.strength, sword.defence))
		w_power=((int(sword.strength))+int((sword.defence)))
		w_p=w_power/2
		
		
	if sel_weapon=='2':
		_weapon=2	
		print('{} Selected' '\n' 'Attack: {}' '\n' 'Defence: {}'.format(hammer.nume, hammer.strength, hammer.defence))
		w_power=((int(hammer.strength))+int((hammer.defence)))
		w_p=w_power/2
		
		
	if sel_weapon=='3':
		_weapon=3	 
		print('{} Selected' '\n' 'Attack: {}' '\n' 'Defence: {}'.format(shield_kinfe.nume, shield_kinfe.strength, shield_kinfe.defence))
		w_power=((int(shield_kinfe.strength))+int((shield_kinfe.defence)))
		w_p=w_power/2
		
	if _weapon<=0 or _weapon>=4:
		print('Error, please follow the instructions')	
	#else:
		#print('error, please follow the instructions')


	#Computer opponent function for character choice
	time.sleep(1)
	print('*************************************')

	#global c_p
	if computer_c==1:
			
		print('Your opponent choice:''\n''{} is an {}' '\n' 'Attack is: {}' '\n' 'Defence is: {}' '\n' 'Heatlh: {}'.format(elfs.nume, elfs.creatures, elfs.strength, elfs.defence, elfs.health))
		c_power=((int(elfs.strength))+int((elfs.defence)))
		c_p=c_power/2
		
		
		
	if computer_c==2:
			 
		print('Your opponent choice:''\n''{} is an {}' '\n' 'Attack is: {}' '\n' 'Defence is: {}' '\n' 'Heatlh: {}'.format(dwarfs.nume, dwarfs.creatures, dwarfs.strength, dwarfs.defence, elfs.health))
		c_power=((int(dwarfs.strength))+int((dwarfs.defence)))
		c_p=c_power/2
		
		
		
	if computer_c==3:
			 
		print('Your opponent choice:''\n''{} is a {}' '\n' 'Attack is: {}' '\n' 'Defence is: {}' '\n' 'Heatlh: {}'.format(humans.nume, humans.creatures, humans.strength, humans.defence, humans.health))
		print('')
		c_power=((int(humans.strength))+int((humans.defence)))
		c_p=c_power/2
		
		
		
	if computer_c==4:
			 
		print('Your opponent choice:''\n''{} is a {} creaturea' '\n' 'Attack is: {}' '\n' 'Defence is: {}' '\n' 'Heatlh: {}'.format(tekks.nume, tekks.creatures, tekks.strength, tekks.defence, tekks.health))
		c_power=((int(tekks.strength))+int((tekks.defence)))
		c_p=c_power/2
		
		
		#else:
		#	print('Error')
		
			

	#Computer opponent function for weapon choice
	print('')

	#global cw_p
		
	if computer_w==1:
			
		print('Weapon choice:''\n''{}' '\n' 'Attack is: {}' '\n' 'Defence is: {}'.format(sword.nume, sword.strength, sword.defence))
		cw_power=((int(sword.strength))+int((sword.defence)))
		cw_p=cw_power/2
		#print('comp weapon 1')
		#print(cw_p)
		
	if computer_w==2:
			 
		print('Weapon choice:''\n''{}' '\n' 'Attack is: {}' '\n' 'Defence is: {}'.format(hammer.nume, hammer.strength, hammer.defence))
		cw_power=((int(hammer.strength))+int((hammer.defence)))
		cw_p=cw_power/2
		#print('comp weapon 2')
		#print(cw_p)
		
	if computer_w==3:
			 
		print('Weapon choice:''\n''{}' '\n' 'Attack is: {}' '\n' 'Defence is: {}'.format(shield_kinfe.nume, shield_kinfe.strength, shield_kinfe.defence))
		cw_power=((int(shield_kinfe.strength))+int((shield_kinfe.defence)))
		cw_p=cw_power/2	
		#print('comp weapon 3')
		#print(cw_p)
		

	print('')
	fight=input('When ready press: y''\n')

		


	#Fighting engine
	class fighting:

		
		#comp_hit=[1,2,3]
		#c_hit=random.choice(comp_hit)
		#print(str(c_hit)+'comp hit')
		#comp_defence=[1,2,3]
		#c_def=random.choice(comp_defence)
		#print(str(c_def)+'comp hit')
		#global computer_health
		#global human_health
		(computer_health)=100
		(human_health)=100
		
		if fight==('y'):
			print('To hit the head, select: 1')
			print('To hit the body, select: 2')
			print('To hit the legs, select: 3')
			print('****************************')
			print('To defend the head, select: 1')
			print('To defend the body, select: 2')
			print('To defend the legs, select: 3')
		if fight!='y':

			print('Error, write y instead')
			
				
			

		
					
		
		while human_health>0 and computer_health>0:	
			hit=input('Hit: ')
			defend=input('Defend: ')
			time.sleep(1)
			print('**********************************************')
			comp_hit=[1,2,3]
			c_hit=random.choice(comp_hit)
			comp_defence=[1,2,3]
			c_def=random.choice(comp_defence)
			
			if hit=='1':
				hh='head'
			if hit=='2':
				hh='body'
			if hit=='3':
				hh='legs'
			if defend=='1':
				hd='head'
			if defend=='2':
				hd='hbody'
			if defend=='3':
				hd='legs'
			
			if c_hit==1:
				ch='head'
			if c_hit==2:
				ch='body'
			if c_hit==3:
				ch='legs'
			if c_def==1:
				cd='head'
			if c_def==2:
				cd='body'
			if c_def==3:
				cd='legs'
			
			if int(hit)!=int(c_def) and int(c_hit)==int(defend):
				(computer_health)-=((250/(c_p+cw_p))*100)
				print("You hit the opponent's "+hh )
				print("Opponent defended the "+cd)
				print("Opponent hit your "+ch)
				print("You defended the "+hd)
				print('You defended the attack')
				print('Your health is: '+str(round(human_health))+'%')
				print('Opponent health is: '+ str(round(computer_health))+'%')
				print('**********************************************')
				
			if int(defend)!=int(c_hit) and int(hit)==int(c_def):
				(human_health)-=((250/(h_p+w_p))*100)
				print("You hit the opponent's "+hh )
				print("Opponent defended the "+cd)
				print("Opponent hit your "+ch)
				print("You defended the "+hd)
				print('Opponent defended your attack')
				print('Your health is: '+str(round(human_health))+'%')
				print('Opponent health is: '+ str(round(computer_health))+'%')
				print('**********************************************')
			if int(hit)!=int(c_def) and int(c_hit)!=int(defend):
				(computer_health)-=((250/(c_p+cw_p))*100)
				(human_health)-=((250/(h_p+w_p))*100)
				print("You hit the opponent's "+hh )
				print("Opponent defended the "+cd)
				print("Opponent hit your "+ch)
				print("You defended the "+hd)
				print('Your health is: ' +str(round(human_health))+'%')
				print('Opponent health is: '+ str(round(computer_health))+'%')
				print('**********************************************')
			if int(hit)==int(c_def) and int(c_hit)==int(defend):
				print("You hit the opponent's "+hh )
				print("Opponent defended the "+cd)
				print("Opponent hit your "+ch)
				print("You defended the "+hd)
				print('You and your opponent defended the attack')
				print('Your health is: ' +str(round(human_health))+'%')
				print('Opponent health is: '+ str(round(computer_health))+'%')
				print('**********************************************')
			#if int(c_hit)!=int(defend):
				#human_health-=((250/(h_p+w_p))*100)
				#print('Your health is4: '+str(human_health))
				#print('Opponent health is4: '+ str(computer_health))
				
			
						
			#if str(hit)==str(c_hit):
				#computer_health-=((250/(c_p+cw_p))*100)
				#human_health-=((250/(h_p+w_p))*100)
				
				#print('Your health is3: '+str(human_health))
				#print('Opponent health is3: '+ str(computer_health))
				
					
			#if str(hit)==str(c_def):
			#	print('Opponent defended')
			#	print('Your health is:5 '+str(human_health))
			#	print('Opponent health is:5 '+ str(computer_health))
			
			#if str(c_hit)==str(defend):
				#print('You defended yourself')
				#print('Your health is4: '+str(human_health))
				#print('Opponent health is4: '+ str(computer_health))
			
				
			#if computer_health<=0 and human_health>0:
				#print('You won')
			#if human_health<=0 and computer_health>0:
				#print('You lose')
			if (human_health)<(computer_health) and (human_health)<=0:
				print('You lose')
			if (human_health)>(computer_health) and (computer_health)<=0:
				print('You win!')
			if (computer_health) == (human_health) and (computer_health)<=0:
				print('Draw')
			#if computer_health>0 and human_health>0:
			#	creaturele('','','','','')
				#human_health-=1
				#computer_health-=1

	fighting()
restart()			
	
while True:
	answer = input('Run again? (y/n): ')
	if answer==('y'):
		restart()
			
	else:
		print('Goodbye')
		exit()




		
	
	
	
	


	
	
	
	
		


	











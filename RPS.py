# created by raymond octavious
# created on october 2017
# created for isc3u
# created for daily assignment
# this program is the rock paper scissors game


import ui
from numpy import random


ROCK = 1
PAPER = 2
SCISSORS = 3
	
def rock_button_touch_up_inside(sender):
    random_integer = random.randint(1,4)
	
    if random_integer == 1:
        view['answer_label'].text = 'Tie!'
		
    elif random_integer == 2:
        view['answer_label'].text = 'You Lose!'
		
    elif random_integer == 3:
        view['answer_label'].text = 'You Win!'
		
def paper_button_touch_up_inside(sender):
    random_integer = random.randint(1,4)
	
    if random_integer == 1:
		    view['answer_label'].text = 'You Win!'
		
    elif random_integer == 2:
        view['answer_label'].text = 'Tie!'
    
    elif random_integer == 3:
        view['answer_label'].text = 'You Lose!'
        
def scissors_button_touch_up_inside(sender):
    random_integer = random.randint(1,4)
	
    if random_integer == 1:
        view['answer_label'].text = 'You Lose!'
        
    elif random_integer == 2:
        view['answer_label'].text = 'You Win!'
        
    elif random_integer == 3:
        view['answer_label'].text = 'Tie!'
	
	
			
			
		
	

view = ui.load_view()
view.present('full_screen')

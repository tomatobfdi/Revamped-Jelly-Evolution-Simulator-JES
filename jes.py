from jes_sim import Sim
from jes_ui import UI
import pygame

#IF YOU WANT 100 or 500 CREATURE OPTIONS BACK, remove the # at the front of lines 8, 9 and 10. 
#Delete the c_input = "250" from line 15

#c_input = input("How many creatures do you want?\n100: Lightweight\n250: Standard (if you don't type anything, I'll go with this)\n500: Strenuous (this is what my carykh video used)\n")
#if c_input == "":
#    c_input = "250"

# Simulation
# population size is 250 here, because that runs faster. You can increase it to 500 to replicate what was in my video, but do that at your own risk!

c_input = "250"
pygame.display.set_caption("Jelly Evolution Simulator")
new_icon = pygame.image.load("jelly.png")
pygame.display.set_icon(new_icon)

# Simulation
# population size is 250 here, because that runs faster. You can increase it to 500 to replicate what was in my video, but do that at your own risk!

sim = Sim(_c_count=int(c_input), _stabilization_time=200, _trial_time=300,
_beat_time=20, _beat_fade_time=5, _c_dim=[4,4],
_beats_per_cycle=3, _node_coor_count=4, # x_position, y_position, x_velocity, y_velocity
_y_clips=[-10000000,0], _ground_friction_coef=25,
_gravity_acceleration_coef=0.002, _calming_friction_coef=0.7,
_typical_friction_coef=0.8, _muscle_coef=0.08,
_traits_per_box=3, # desired width, desired height, rigidity
_traits_extra=1, # heartbeat (time)
_mutation_rate=0.07, _big_mutation_rate=0.025,
_UNITS_PER_METER=0.05)

# Cosmetic UI variables
ui = UI(_W_W=1300, _W_H=750, _MOVIE_SINGLE_DIM=(360,360),
_GRAPH_COOR=(607,81,590,272), _SAC_COOR=(607,358,590,272), _GENEALOGY_COOR=(20,81,390,552,42),
_COLUMN_MARGIN=200, _MOSAIC_DIM=[17,17,17,90], #_MOSAIC_DIM=[10,10,17,22],
_MENU_TEXT_UP=180, _CM_MARGIN1=20, _CM_MARGIN2=1)

sim.ui = ui
ui.sim = sim
ui.addButtonsAndSliders()
    
sim.initializeUniverse()
gamerunning = True




while ui.running:
    sim.checkALAP()
    ui.detectMouseMotion()
    ui.detectEvents()
    ui.detectSliders()
    ui.doMovies()
    ui.drawMenu()
    ui.show()

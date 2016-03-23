#Celsius 
#by Cade Ritter
#Pitch sheet: https://www.dropbox.com/s/buich5y0hqav4mx/pitch_sheet.png

#if you're having trouble - LOOK FOR THE AXE! Keep an eye on your temperature and condition. Look for shelter! 
#Just explore the landscape. Harvest berries! 

#Hey there! Since you're looking at my code, I was gonna give you a few hints.
#Hopefully you found an axe to cut yourself some logs for fires. You might be finding that
#after your first day or so, you're running low on food - go check out the wilderness to
#the right! Also, you might find something helpful there that could unlock the 
#part of the world on the left :)

#Beware that trees, bushes, and the axe spawn in (mostly) random locations, so don't expect
#things to be in the same places if you restart!

#imports
import simplegui
import math
import random
import time

#initializations
WIDTH = 800	
HEIGHT = 600
MOVEMENT_SPEED = 1.5
STARTING_LOC = 3600
move_pos = 0
air_temp = 30
irl_time = 0
game_time = 0
night_transparency = 0
headphone_screen = True
intro_screen = False
help_screen = False
high_scores_screen = False
game_intro = True
left_end_level = False
right_end_level = False
is_indoors = False


#class for returning info about images
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = 0, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

#define background images
trees1_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/background_trees.png")
trees1_info = ImageInfo([500, 300], [WIDTH, HEIGHT])

trees2_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/trees2.png")
trees2_info = ImageInfo([400, 300], [WIDTH, HEIGHT])

mountain_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/mountain.png")
mountain_info = ImageInfo([400, 300], [WIDTH, HEIGHT]) 

sky_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/clouds.png")
sky_info = ImageInfo([400, 300], [WIDTH, HEIGHT])

#define weather images
light_snow_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/light_snow.png")
light_snow_info = ImageInfo([400, 300], [WIDTH, HEIGHT])

snowstorm_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/snowstorm.png")
snowstorm_info = ImageInfo([400, 300], [WIDTH, HEIGHT])

#define sprite images
campfire_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/campfire_25_75_125_175.png")
campfire_info = ImageInfo([25, 50], [50, 100], 50, 120)

character_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/char_anims.png") 
character_info = ImageInfo([27, 44], [54, 88], 50, 150)

tree_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/tree_anims.png")
tree_info = ImageInfo([50, 75], [100, 150], 50, 120)

bush_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/bush.png")
bush_info = ImageInfo([25, 15], [50, 30])

gas_station_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/gas_station.png")
gas_station_info = ImageInfo([200, 75], [400, 150])

house_blue_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/house_blue.png")
house_blue_info = ImageInfo([200, 100], [400, 200])

house_green_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/house_green.png")
house_green_info = ImageInfo([200, 100], [400, 200])

axe_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/axe.png")
axe_info = ImageInfo([25, 25], [50, 50])

#define UI images
startscreen_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/start_screen.png")
startscreen_info = ImageInfo([400, 300], [800, 600])

how_to_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/how_to_play.png")
how_to_info = ImageInfo([400, 300], [800, 600])

headphone_screen_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/headphone_screen.png")
headphone_screen_info = ImageInfo([400, 300], [800, 600])

#define level image
level0_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/level_0.png")
level0_info = ImageInfo([400, 300], [800, 600])

level1_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/level1_ends.png")
level1_info = ImageInfo([400, 300], [800, 600])

level2_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/11480863/level2.png")
level2_info = ImageInfo([400, 300], [800, 600])

#define sounds
walking_sound = simplegui.load_sound('https://www.freesound.org/people/Dymewiz/sounds/114389/download/114389__dymewiz__footsteps-snow-02.wav')
walking_sound.set_volume(0.6)

ambient_wind = simplegui.load_sound('https://www.freesound.org/people/Benboncan/sounds/78485/download/78485__benboncan__windscape.wav')
ambient_wind.set_volume(0.8)

intro_swell = simplegui.load_sound('https://dl.dropboxusercontent.com/u/11480863/intro_swell.ogg')

opening_song = simplegui.load_sound('https://dl.dropboxusercontent.com/u/11480863/Library%20Tapes%20-%20Sketches%20-%2011%20First%20day%20of%20winter.mp3')
opening_song.set_volume(0.6)

campfire_sound = simplegui.load_sound('https://www.freesound.org/people/zmb94/sounds/74963/download/74963__zmb94__campfire-1.wav')
campfire_sound.set_volume(0.5)

tree_harvest_sound = simplegui.load_sound('https://www.freesound.org/people/Adam_N/sounds/164472/download/164472__adam-n__crack-of-branch-3.wav')

match_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/11480863/Striking%20Match-SoundBible.com-138366619%20(1).mp3')

log_add_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/11480863/161592__jorickhoofd__wooden-log-falling.m4a')
log_add_sound.set_volume(0.6)

crowbar_break = simplegui.load_sound("https://dl.dropboxusercontent.com/u/11480863/crowbar_break.ogg")

pick_up_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/u/11480863/pick_up.ogg")

rustle_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/u/11480863/bush_rustle.ogg")

eating_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/u/11480863/eating.ogg")

#character class for position, movement, actions, health
class Character: 
    def __init__(self, pos, vel, image, info):
        self.pos = pos
        self.vel = vel
        self.level = current_level
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.facing = 'right'
        self.collision_pos = [self.level.get_starting_loc(), HEIGHT / 2]
        self.inventory = {'wood': 0, 'matches': 5, 'axe': 0, 'food': 0, 'crowbar': 0}
        self.temp = 10
        self.warmth = 100
        self.condition = 100
        self.satiation = 100
        self.clothing_warmth = 5
        self.anim_time = 30
        self.air_temp = weather.get_temp()
        self.alive = True
        self.level_end_stop = None

    def draw(self, canvas):
        global move_pos, current_level         
        if not game_intro:		#if not in starting menu   
            if self.alive:
                
                #update position; stops movement at end of level if necessary
                if self.level_end_stop == 'left':	
                    if self.vel >= 0:  	
                        move_pos += self.vel		
                        self.collision_pos[0] += self.vel		
                elif self.level_end_stop == 'right':
                    if self.vel <= 0:
                        move_pos += self.vel
                        self.collision_pos[0] += self.vel
                else:
                    move_pos += self.vel
                    self.collision_pos[0] += self.vel
                
                self.collide(self.level)		
                self.inventory_process()    
                self.char_condition(canvas)
                
                #handles behavior at the ends of levels (moving to new level especially)
                if self.collision_pos[0] < self.level.get_level_end_info('left')[0]:                    
                    if self.level.get_level_end_info('left')[2] == False:
                        alert_text.display_text('THE WAY IS BLOCKED', 20, 1)
                        if self.collision_pos[0] < self.level.get_level_end_info('left')[1]:
                            self.level_end_stop = 'left'
                            
                        else:
                            self.level_end_stop = None
                    else:
                        alert_text.display_text('TO THE NEXT LEVEL', 30, 1)		
                        if self.collision_pos[0] < self.level.get_level_end_info('left')[1]:		#if player reaches end and it's open
                            current_level = self.level.get_level_end_info('left')[3]				#change the level to the next level
                            self.level = current_level												#set the player's level to the next level
                            prev_level = self.level.get_level_end_info('right')[3]					#previous level variable to set starting location 
                            move_pos = 0
                            self.collision_pos[0] = self.level.get_starting_loc()
                            prev_level.set_starting_loc(prev_level.get_level_end_info('left')[1])	#set old level's starting location to the end of it                                                                                    
                if self.collision_pos[0] > self.level.get_level_end_info('right')[0]:                    
                    if self.level.get_level_end_info('right')[2] == False:
                        alert_text.display_text('THE WAY IS BLOCKED', 20, 1)
                        if self.collision_pos[0] > self.level.get_level_end_info('right')[1]:
                            self.level_end_stop = 'right'
                        else:
                            self.level_end_stop = None
                    else:
                        alert_text.display_text('TO THE NEXT LEVEL', 30, 1)
                        if self.collision_pos[0] > self.level.get_level_end_info('right')[1]:
                            current_level = self.level.get_level_end_info('right')[3]
                            self.level = current_level
                            prev_level = self.level.get_level_end_info('left')[3]
                            move_pos = 0
                            self.collision_pos[0] = self.level.get_starting_loc()
                            prev_level.set_starting_loc(prev_level.get_level_end_info('right')[1])                                                   
                
                #draw and animate character 
                if self.facing == 'right':
                    if self.vel != 0:
                        self.anim_time += 1
                        if self.anim_time == self.lifespan:
                            self.anim_time = 30
                        canvas.draw_image(self.image, [self.image_center[0] + 54 * (self.anim_time // 30), self.image_center[1]],
                                          self.image_size, self.pos, self.image_size)
                    else:	                
                        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
                if self.facing == 'left':
                    if self.vel != 0:
                        self.anim_time += 1
                        if self.anim_time == self.lifespan:
                            self.anim_time = 30
                        canvas.draw_image(self.image, [self.image_center[0] + 54 * (self.anim_time // 30), self.image_center[1] + 88],
                                          self.image_size, self.pos, self.image_size)
                    else:	                            
                        canvas.draw_image(self.image, [self.image_center[0], self.image_center[1] + 88], self.image_size, self.pos, self.image_size)
            else:
                canvas.draw_image(self.image, [self.image_center[0], self.image_center[1] + 88], self.image_size, [self.pos[0], self.pos[1] + 30], self.image_size, 1.57)                
                canvas.draw_polygon([(0,0), (WIDTH,0), (WIDTH,HEIGHT), (0,HEIGHT)], 1, 'rgba(0,0,0,0)', 'rgba(180,0,20,0.5)')
                canvas.draw_text("YOU HAVE DIED", [200, 300], 50, 'Black', 'monospace')
                canvas.draw_text("please exit the game to try again", [150, 350], 25, 'Black', 'monospace')
                
        
    def keydown_handler(self, key):
        global move_pos, headphone_screen, intro_screen
        if key == simplegui.KEY_MAP['A']:
            if self.level_end_stop != 'left':  	
                self.facing = "left"
                self.vel = - MOVEMENT_SPEED
                walking_sound.play()
        if key == simplegui.KEY_MAP['D']:
            if self.level_end_stop != 'right': 
                self.facing = "right"
                self.vel = MOVEMENT_SPEED
                walking_sound.play()            
        if key == simplegui.KEY_MAP['X']:
            if self.inventory['wood'] >= 1:
                self.place_object('campfire')
                self.inventory['wood'] -= 1 
            else:
                alert_text.display_text('WOOD REQUIRED TO PLACE CAMPFIRE', 20, 180)
        if key == simplegui.KEY_MAP['E']:
            for object in self.level.get_object_list():
                if dist(object.get_world_pos(), self.pos) < 50:
                    self.object_interact(object)
            for object in self.level.get_world_object_list():
                if dist(object.get_world_pos(), self.pos) < 50:
                    self.object_interact(object)  
            for	object in self.level.get_structure_list():
                if dist(object.get_world_pos(), self.pos) < 100:
                    self.object_interact(object)  
            if self.level == level1:
                if self.collision_pos[0] < level1.get_level_end_info('left')[0] and self.collision_pos[0] >= level1.get_level_end_info('left')[1]:
                    if self.inventory['crowbar'] >= 1:
                        level1.open_end('left')
                        crowbar_break.play()
        if key == simplegui.KEY_MAP['V']:
            if self.inventory['food'] >= 1:
                if self.satiation < 100:
                    self.satiation += 10
                    self.inventory['food'] -= 1
                    alert_text.display_text('FOOD EATEN', 20, 180)
                    eating_sound.play()
                else:
                    alert_text.display_text('YOU ARE TOO FULL', 20, 180)
            else:
                alert_text.display_text('NO FOOD IN INVENTORY', 20, 180)
        if key == simplegui.KEY_MAP['space']:
            if game_intro:
                headphone_screen = False
                intro_screen = True

        
    def keyup_handler(self, key):
        if key == simplegui.KEY_MAP['A']:
            self.vel = 0 
            walking_sound.rewind()
        if key == simplegui.KEY_MAP['D']:
            self.vel = 0
            walking_sound.rewind()
            
    #make character track along terrain 
    def collide(self, level):        
        collide_list = self.level.get_collision_list()
        range_list = range(len(collide_list))
        for i in collide_list:
            #check that i is not the last point on terrain
            if collide_list.index(i) != range_list[-1]:
                next_item = collide_list[collide_list.index(i) + 1]                
                #if character is in area between two points
                if self.collision_pos[0] >= i[0] and self.collision_pos[0] < next_item[0]:
                    #y = mx + b to find y pos at current x pos based on line between two points; set y pos 
                    m = (float(next_item[1] - i[1])/(next_item[0] - i[0]))
                    b = i[1] - m * i[0]
                    self.pos = [self.pos[0], (m * self.collision_pos[0] + b) - 44]                   
    
    #update inventory display
    def inventory_process(self):
        if self.inventory.has_key('wood'):
            wood_label.set_text('Wood: ' + str(self.inventory['wood']))
        if self.inventory.has_key('matches'):
            matches_label.set_text('Matches: ' + str(self.inventory['matches']))
        if self.inventory.has_key('axe'):
            axe_label.set_text('Axe: ' + str(self.inventory['axe']))    
        if self.inventory.has_key('crowbar'):
            crowbar_label.set_text('Crowbar: ' + str(self.inventory['crowbar']))
        if self.inventory.has_key('food'):
            food_label.set_text('Food: ' + str(self.inventory['food']))
    
    #place an object inputted
    def place_object(self, object): 
        if object == 'campfire':        
            campfire = Campfire([self.pos[0] + move_pos, self.pos[1] - 10], campfire_image, campfire_info)
            self.level.add_object(campfire)
    
    #interact with an object; many many if's and else's
    def object_interact(self, object):
        if type(object) == Campfire:
            if object.get_started() == False:    
                if self.inventory['matches'] >= 1:
                    if weather.get_type() != 'snowstorm':
                        object.start_fire(True) 
                        match_sound.play()
                        self.inventory['matches'] -= 1
                    else:
                        alert_text.display_text('IT IS TOO WINDY', 20, 180)
                else: 
                    alert_text.display_text('MATCHES REQUIRED', 20, 180)
            else:
                if self.inventory['wood'] >= 1:
                    if object.get_log_count() < 5:
                        object.add_log()
                        self.inventory['wood'] -= 1
                        alert_text.display_text('LOG ADDED', 20, 180)
                        log_add_sound.play()
                    else:
                        alert_text.display_text('FIRE HAS TOO MANY LOGS', 20, 180)
                else:
                    alert_text.display_text('WOOD REQUIRED', 20, 180)
        
        elif type(object) == Tree:
            if object.get_harvested() == False:
                if self.inventory['axe'] >= 1:
                    if self.inventory['wood'] < 10:      
                        object.harvest()
                        self.inventory['wood'] += 1
                        tree_harvest_sound.play()
                        alert_text.display_text('WOOD HARVESTED', 20, 180)
                    else:
                        alert_text.display_text('TOO MANY LOGS!', 20, 180)
                else:                    
                    alert_text.display_text('AXE NEEDED TO HARVEST TREE', 20, 180)
            else:
                alert_text.display_text('TREE ALREADY HARVESTED', 20, 180)
                
        elif type(object) == Bush:
            if object.get_harvested() == False:
                object.harvest()
                self.inventory['food'] += 1
                alert_text.display_text('BERRIES HARVESTED', 20, 180)
                rustle_sound.play()
            else:
                alert_text.display_text('BUSH ALREADY HARVESTED', 20, 180) 
                
        elif type(object) == Structure:
            if not object.get_searched():     
                contents_str = ''                
                structure_contents = object.get_inventory()
                object.search()
                for i in self.inventory:                               
                    for j in structure_contents:        
                        if i == j:
                            self.inventory[j] += structure_contents[j]
                for y in structure_contents:        
                    zero_count = 0
                    if structure_contents[y] != 0:
                        zero_count += 1
                        contents_str += str(structure_contents[y]) + ' ' + y + ' '
                if zero_count == 4:
                    contents_str += 'NO ITEMS IN STRUCTURE'
                else:
                    contents_str += 'added'
                alert_text.display_text(contents_str, 18, 300)
            else:
                alert_text.display_text('STRUCTURE ALREADY SEARCHED', 20, 180)
                
        elif type(object) == Item:
            self.inventory[object.get_type()] += 1
            object.pick_up()
            object = None           
            alert_text.display_text('AXE ADDED', 20, 180)
            pick_up_sound.play()
                    
            
    
    #update character's temperature (his "feels like" temperature in-game)
    def char_temp(self, canvas):
        self.air_temp = weather.get_temp()
        
        #add temp if near a campfire; the more logs on the fire, the hotter it is
        for object in self.level.get_object_list():
            if type(object) == Campfire:     
                if object.get_started() == True:
                    if dist(object.get_world_pos(), self.pos) < 150:
                            self.air_temp = self.air_temp + (15 * (object.get_log_count() * 0.5)) 
                    else:
                        self.air_temp = weather.get_temp() 
        
        if is_indoors:
            self.air_temp += 10
        self.temp = self.air_temp + self.clothing_warmth 
        
        #increment char warmth as his self.temp ("feels like") lowers/increases
        if self.temp >= 20:
            if self.warmth < 100:
                if game_time % 0.25 == 0:
                    self.warmth += 5 
            else:
                self.warmth = 100
        elif self.temp >= 10 and self.temp < 20:
            if self.warmth > 0:
                if game_time % 0.25 == 0:
                    self.warmth -= 1  
        elif self.temp >= 0 and self.temp < 10:
            if self.warmth > 0:
                if game_time % 0.25 == 0:
                    self.warmth -= 2 
        elif self.temp >= -10 and self.temp < 0:
            if self.warmth > 0:
                if game_time % 0.25 == 0:
                    self.warmth -= 3
        elif self.temp < -10:
            if self.warmth > 0:
                if game_time % 0.25 == 0:
                    self.warmth -= 7
            else:
                self.warmth = 0
        
        #draw UI elements for temperature
        canvas.draw_text(str(int(self.temp)) + 'C', [17, 520], 25, 'Black', 'monospace')
        canvas.draw_text('Feels like:', [20, 490], 20, 'Black', 'monospace')
        canvas.draw_text('Warmth: ' + str(self.warmth), [20, 550], 20, 'Black', 'monospace')
        canvas.draw_line([20, 570], [20 + 2 * self.warmth, 570], 20, 'Red')
                    
    def char_hunger(self, canvas):
        if game_time % 0.25 == 0:
            self.satiation -= 1
        if self.satiation > 100:
            self.satiation = 100
        
        canvas.draw_text('Satiation: ' + str(self.satiation), [240, 550], 20, 'Black', 'monospace')
        canvas.draw_line([240, 570], [240 + 2 * self.satiation, 570], 20, 'Green')    
        
    
    #update character's condition (overall health); decreases if he gets too cold, hungry, thirsty, sleepy
    def char_condition(self, canvas):        
        self.char_temp(canvas)
        self.char_hunger(canvas)
        if self.warmth <= 30 and self.warmth > 0:
            if game_time % 0.25 == 0:
                self.condition -= 5
        if self.warmth <= 0:
            if game_time % 0.25 == 0:
                self.condition -= 10
        if self.satiation <= 20:
            if game_time % 0.25 == 0:
                self.condition -= 10       
        if self.condition <= 0:
            self.live(False)
        
        canvas.draw_polygon([(10, 470), (160, 470), (160, 530), (10, 530)], 1, 'rgba(0,0,0,0)', 'rgba(0,0,0,0.2)')
        canvas.draw_polygon([(10, 530), (450, 530), (450, 590), (10, 590)], 1, 'rgba(0,0,0,0)', 'rgba(0,0,0,0.2)')
        canvas.draw_text('Condition:', [20, 30], 20, 'Black', 'monospace')
        canvas.draw_text(str(self.condition) + '%', [20, 70], 25, 'Black', 'monospace')        

    def live(self, alive):
        self.alive = alive 
        #game_over()
        
    def get_pos(self):
        return self.pos

    def get_foot_pos(self):
        return [self.pos[0], self.pos[1] + 44]
    
    def get_collision_pos(self):
        return self.collision_pos        
        
#class for defining the level and handling objects in the world
class Level:
    def __init__(self, collision_list, image, info, starting_loc, left_end_info, right_end_info, structure_list):
        self.collision_list = collision_list
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.starting_loc = starting_loc
        
        self.object_list = []					#object list is for objects the character places
        self.world_object_list = []				#world object list for objects already in the world
        
        self.left_end_info = left_end_info		#tuples that list the x pos of level ends and doors, and if the end is "closed," and the level that the door leads to.       
        self.right_end_info = right_end_info    #i.e. (560, 540, False, level_0)    
        
        self.structure_list = structure_list
    
    def draw(self, canvas):
        #draw the basic level
        canvas.draw_image(self.image, [move_pos + self.starting_loc, self.image_center[1]], self.image_size, [WIDTH / 2, HEIGHT / 2], 
                      [WIDTH, HEIGHT])
               
    def get_collision_list(self):
        return self.collision_list
    
    def get_starting_loc(self):
        return self.starting_loc
    
    def get_object_list(self):
        return self.object_list
    
    def add_object(self, object):
        self.object_list.append(object)
        
    def add_world_object(self, object):
        self.world_object_list.append(object)
        
    def get_world_object_list(self):
        return self.world_object_list
    
    def get_level_end_info(self, side):
        if side == 'left':
            return self.left_end_info
        elif side == 'right':
            return self.right_end_info
    
    def open_end(self, side):
        if side == 'left':
            self.left_end_info[2] = True
        elif side == 'right':
            self.right_end_info[2] = True
            
    def set_starting_loc(self, loc):
        self.starting_loc = loc
        
    def set_adjacent_levels(self, left_level, right_level):
        self.left_end_info[3] = left_level
        self.right_end_info[3] = right_level
        
    def get_structure_list(self):
        return self.structure_list

class Campfire:
    def __init__(self, pos, image, info):
        self.pos = pos
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.lifespan = info.get_lifespan()
        self.started = False
        self.anim_time = 0
        self.burning_time = 0
        self.logs = 1
        
    def draw(self, canvas):  
        if self.started:
            
            #if the fire burns through all logs, it goes out
            self.burning_time += 1 
            if self.burning_time == self.logs * 3600:		
                self.started = False
                self.logs = 0
            
            #fades the campfire sound out as you walk away
            campfire_sound.play()
            if dist(self.get_world_pos(), my_char.get_foot_pos()) < 400:		            	                
                campfire_sound.set_volume(1 + (-dist(self.get_world_pos(), my_char.get_foot_pos()) / 400))
            
            #animates the fire
            self.anim_time += 1
            if self.anim_time == self.lifespan:
                self.anim_time = 30
            canvas.draw_image(self.image, [self.image_center[0] + 50 * (self.anim_time // 30), self.image_center[1]],  
                                           self.image_size, [self.pos[0] - move_pos, self.pos[1]], self.image_size) 
            canvas.draw_circle([self.pos[0] - move_pos, self.pos[1]], 150, 1, 'rgba(255, 200, 0, 0)', 'rgba(255, 200, 0, 0.1)')
            canvas.draw_circle([self.pos[0] - move_pos, self.pos[1] + 25], 75, 1, 'rgba(255, 200, 0, 0)', 'rgba(255, 200, 0, 0.2)')
            
            #draws text when near the fire to show how long the fire lasts
            if dist(self.get_world_pos(), my_char.get_foot_pos()) < 100:
                canvas.draw_text(str('%.1f'%(float(self.logs * 3600 - self.burning_time) / 1800)) + ' HR', [(self.pos[0] - move_pos) - 15, self.pos[1] + 80], 15, 'Black', 'monospace')
        
        else:   
            self.burning_time = 0
            campfire_sound.pause()
            campfire_sound.rewind()
            canvas.draw_image(self.image, self.image_center, self.image_size, [self.pos[0] - move_pos, self.pos[1]], self.image_size)        
                    
    def get_world_pos(self):
        return [self.pos[0] - move_pos, self.pos[1]]
        
    def start_fire(self, started):
        self.started = started       
        
    def get_started(self):
        return self.started 
    
    def add_log(self):
        self.logs += 1
        
    def get_log_count(self):
        return self.logs

class Tree:
    def __init__(self, pos, image, info, level):
        self.pos = pos        
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0        
        self.anim_time = 0
        self.harvested = False
        self.level = level
        
    def draw(self, canvas):
        
        #animates the trees if it's storming
        if weather.get_type() == 'snowstorm':
            self.anim_time += 1
            if self.anim_time == self.lifespan:
                self.anim_time = 30
            canvas.draw_image(self.image, [self.image_center[0] + 100 * (self.anim_time // 30), self.image_center[1]],  
                                           self.image_size, self.get_world_pos(), self.image_size) 	 
        
        else:         
            canvas.draw_image(self.image, self.image_center, self.image_size, self.get_world_pos(),
                           self.image_size)
            
    #returns the position of the tree in respect to the frame
    def get_world_pos(self):
        return [400 + (self.pos[0] - my_char.get_collision_pos()[0]), self.pos[1]]
    
    def harvest(self):
        self.harvested = True
        
    def get_harvested(self):
        return self.harvested
   
class Weather:
    def __init__(self, weather_type):
        self.weather_type = weather_type
        self.temperature = 5
        self.weather_time = 0        
    
    def clear_weather(self):
        self.weather_type = 'clear'
        self.temperature = 0
        
    def light_snow(self):
        self.weather_type = 'light snow'
        self.temperature = -10
        
    def snowstorm(self):
        self.weather_type = 'snowstorm'
        self.temperature = -20        
        
    def draw(self, canvas):
        
        #animate weather
        if self.weather_type == 'light snow':
            self.light_snow()
            self.weather_time += 1
            mod_weather_time = (self.weather_time // 4) % HEIGHT
            center = light_snow_info.get_center()
            size = light_snow_info.get_size()
            canvas.draw_image(light_snow_image, center, size, (WIDTH / 2, mod_weather_time - HEIGHT / 2), (WIDTH, HEIGHT))
            canvas.draw_image(light_snow_image, center, size, (WIDTH / 2, mod_weather_time + HEIGHT / 2), (WIDTH, HEIGHT))        
        elif self.weather_type == 'snowstorm':
            self.snowstorm()
            self.weather_time += 1
            mod_weather_time = (self.weather_time * 8) % WIDTH
            center = snowstorm_info.get_center()
            size = snowstorm_info.get_size()
            canvas.draw_image(snowstorm_image, center, size, (mod_weather_time - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
            canvas.draw_image(snowstorm_image, center, size, (mod_weather_time + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
            canvas.draw_polygon([(0,0), (WIDTH,0), (WIDTH,HEIGHT), (0,HEIGHT)], 1, 'rgba(0,0,0,0)', 'rgba(0,0,0,0.1)')
        
        else:
            self.clear_weather()
        #temperature decreases by 10 as night falls
        self.temperature += 5 * (math.cos(0.25 * game_time)) + 5
        
        #if the game started, draw UI info and update the weather
        if not game_intro:   
            canvas.draw_text(str(int(self.temperature)) + 'C', [715, 500], 25, 'Black', 'monospace') 
            canvas.draw_text('Air temp:', [670, 470], 20, 'Black', 'monospace')                
            self.weather_update()
    
    #randomize weather every 12 game hours
    def weather_update(self):
        if game_time % 12 == 0:
            weather_rand = random.randrange(0, 15)
            if weather_rand == 0 or weather_rand == 1:
                self.weather_type == 'snowstorm'
            if weather_rand == 1 or weather_rand == 2 or weather_rand == 3 or weather_rand == 4: 
                self.weather_type == 'clear'
            if weather_rand == 5 or weather_rand == 6 or weather_rand == 7 or weather_rand == 8:
                self.weather_type == 'light snow'
    
    def get_temp(self):
        return self.temperature
    
    def get_type(self):
        return self.weather_type
    
    def set_type(self, weather_type):
        self.weather_type = weather_type
        
class Structure:
    def __init__(self, pos, image, info, left_door, right_door):
        self.pos = pos
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.exterior = True        
        self.left_door = left_door		#these are pixel differences from the center of the structure image to the "door"
        self.right_door = right_door	
        self.inventory = {'food': 0, 'axe': 0, 'crowbar': 0, 'matches': 0}
        self.searched = False
        
    def draw(self, canvas):
        global is_indoors
        
        #draws the interior if the character is inside the structure; draws exterior otherwise
        if my_char.get_foot_pos()[0] > (self.get_world_pos()[0] - self.left_door) and my_char.get_foot_pos()[0] < (self.get_world_pos()[0] + self.right_door):
            self.exterior = False
            is_indoors = True
        else:
            self.exterior = True
            is_indoors = False
        if self.exterior: 
            canvas.draw_image(self.image, self.image_center, self.image_size, [self.get_world_pos()[0], self.get_world_pos()[1] - self.image_size[1] / 2],
                           self.image_size)
        else:	
            canvas.draw_image(self.image, [self.image_center[0] + 400, self.image_center[1]], self.image_size, [self.get_world_pos()[0], self.get_world_pos()[1] - self.image_size[1] / 2],
                           self.image_size)  
            if not self.searched:
                canvas.draw_text('PRESS E TO SEARCH STRUCTURE', [self.get_world_pos()[0] - 75, self.get_world_pos()[1] + 30], 15, 'rgba(0, 0, 0, 0.5)', 'monospace')
         
        
    #as in the Tree class, returns position of structure relative to character
    def get_world_pos(self):
        return [400 + (self.pos[0] - my_char.get_collision_pos()[0]), self.pos[1]] 	
    
    def set_inventory(self, axe_num, crowbar_num):
        self.inventory['matches'] = random.randrange(0, 10)
        self.inventory['food'] = random.randrange(0, 5)
        self.inventory['axe'] = axe_num
        self.inventory['crowbar'] = crowbar_num
        
    def get_inventory(self):
        return self.inventory
        
    def search(self):    
        self.inventory = {}
        self.searched = True
        
    def get_searched(self):
        return self.searched

class Item:
    def __init__(self, item, pos, image, info):
        self.item = item
        self.pos = pos
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size() 
        self.on_ground = True
        
    def draw(self, canvas):
        if self.on_ground == True:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.get_world_pos(),
                           self.image_size)    
        
    def get_type(self):
        return self.item
    
    def get_world_pos(self):
        return [400 + (self.pos[0] - my_char.get_collision_pos()[0]), self.pos[1]]
    
    def pick_up(self):
        self.on_ground = False    
    
class Bush:
    def __init__(self, pos, image, info, level):
        self.pos = pos        
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0        
        self.anim_time = 0
        self.harvested = False
        self.level = level
        
    def draw(self, canvas):
        if self.harvested:
            canvas.draw_image(self.image, [self.image_center[0] + 50, self.image_center[1]], self.image_size, self.get_world_pos(), 
                              self.image_size) 	 
        
        else:         
            canvas.draw_image(self.image, self.image_center, self.image_size, self.get_world_pos(),
                           self.image_size)
            
    #returns the position of the tree in respect to the frame
    def get_world_pos(self):
        return [400 + (self.pos[0] - my_char.get_collision_pos()[0]), self.pos[1]]
    
    def harvest(self):
        self.harvested = True
        
    def get_harvested(self):
        return self.harvested

#displays alert text for player actions        
class AlertText:    
    def __init__(self):
        self.text = ''
        self.display = False
        self.text_time = 0
        self.size = 15
        self.duration = 0
    
    def display_text(self, text, size, duration):
        self.text = text  
        self.size = size
        self.display = True  
        self.text_time = 0
        self.duration = duration
    
    def draw(self, canvas):
        if self.display:
            self.text_time += 1
        else:
            self.text_time = 0
        if self.text_time > self.duration:
            self.display = False
        if self.display:
            canvas.draw_text(self.text, [250, 50], self.size, 'Black', 'monospace')                 

#distance formula 
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) 
                                  
#adds trees to the level randomly
def populate_objects(type_object, level, left_limit, right_limit, freq):
    loc_list = []
    
    #generate random x value 30 times, with step 50
    for i in range(freq):
        x_coord = random.randrange(left_limit, right_limit, 75)
        loc_list.append(x_coord)
  
    collide_list = level.get_collision_list()
    
    #for every x value, check if it's between two points on collision list. if so, use slope to find where to draw
    #the tree. 
    range_list = range(len(collide_list))
    y_pos = 0
    for x in loc_list:
        for i in collide_list:
            if collide_list.index(i) != range_list[-1]:
                next_item = collide_list[collide_list.index(i) + 1]                
                #if x value is in between two points
                if x >= i[0] and x < next_item[0]:
                    #y = mx + b to find y pos at current x pos based on line between two points; set y pos 
                    m = (float(next_item[1] - i[1])/(next_item[0] - i[0]))
                    b = i[1] - m * i[0]
                    y_pos = (m * x + b)
        if type_object == 'tree':
            tree = Tree([x, y_pos - 75], tree_image, tree_info, level)
            level.add_world_object(tree)   
        if type_object == 'bush':
            bush = Bush([x, y_pos - 15], bush_image, bush_info, level)
            level.add_world_object(bush)
        if type_object == 'axe':
            axe = Item('axe', [x, y_pos], axe_image, axe_info)
            level.add_object(axe)

def draw(canvas):
    global irl_time, game_time
    if not game_intro:    
        irl_time += 1
        #15 seconds IRL == 1 hour in game; 6 minutes == 24 hours
        game_time = float(irl_time) / 900
        if irl_time == 1800:
            opening_song.play()
    
    #draw background    
    canvas.draw_image(sky_image, sky_info.get_center(), sky_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                      [WIDTH, HEIGHT])
    canvas.draw_image(mountain_image, mountain_info.get_center(), mountain_info.get_size(), 
                      [WIDTH / 2, (HEIGHT / 2)], 
                      [WIDTH, HEIGHT])    
    canvas.draw_polygon([(0, 500), (800, 500), (800, 600), (0, 600)], 1, '#3C4C55', '#3C4C55')
    
    #loop background trees with player movement (parallax)      
    pos1 = (move_pos / 2) % WIDTH
    pos2 = (move_pos / 4) % WIDTH
    center1 = trees1_info.get_center()
    size1 = trees1_info.get_size()
    center2 = trees2_info.get_center()
    size2 = trees2_info.get_size()    
    canvas.draw_image(trees2_image, center2, size2, (-pos2 + WIDTH / 2, HEIGHT / 2 - 80), (WIDTH, HEIGHT))
    canvas.draw_image(trees2_image, center2, size2, (-pos2 + WIDTH / 2 + WIDTH, HEIGHT / 2 - 80), (WIDTH, HEIGHT))
    canvas.draw_image(trees1_image, center1, size1, (-pos1 + WIDTH / 2, HEIGHT / 2 - 25), (WIDTH, HEIGHT))
    canvas.draw_image(trees1_image, center1, size1, (-pos1 + WIDTH / 2 + WIDTH, HEIGHT / 2 - 25), (WIDTH, HEIGHT))    
    
    #draw level and level objects (trees, structures)
    if not game_intro:    
        for object in current_level.get_world_object_list():
            object.draw(canvas) 
        current_level.draw(canvas) 
    
    if not game_intro:
        if current_level == level1:
            gas_station_1.draw(canvas)
            if level1.get_level_end_info('left')[3] == True:
                canvas.draw_circle([400 + (560 - my_char.get_collision_pos()[0]), 400], 10, 10, 'black', 'black')
        elif current_level == level0:
            gas_station_0.draw(canvas)
            house_blue_0.draw(canvas)
            house_green_0.draw(canvas)
        elif current_level == level2:
            house_green_2.draw(canvas)
        
    #make night fall     
    night_transparency = -0.35 * (math.cos(- 0.25 * game_time)) + 0.35
    canvas.draw_polygon([(0,0), (WIDTH,0), (WIDTH,HEIGHT), (0,HEIGHT)], 1, 'rgba(0,0,0,0)', 'rgba(0,0,0,+'+str(night_transparency)+')')
    
    weather.draw(canvas)    
    
    alert_text.draw(canvas)
    
    #draw object list
    if not game_intro:    
        for object in current_level.get_object_list(): 
            object.draw(canvas)    
        my_char.draw(canvas)
    
    #draw time survived
    if not game_intro: 	
        canvas.draw_text(str(int(game_time // 24)) + ' DAYS', [650, 40], 30, 'Black', 'monospace')
        canvas.draw_text(str(int(game_time % 24)) + ' HOURS', [650, 60], 30, 'Black', 'monospace')
    
    #starting menu things
    if headphone_screen:
        canvas.draw_image(headphone_screen_image, headphone_screen_info.get_center(), headphone_screen_info.get_size(),
                          [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    if intro_screen:
        canvas.draw_image(startscreen_image, startscreen_info.get_center(), startscreen_info.get_size(), 
                          [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    if help_screen:
        canvas.draw_image(how_to_image, how_to_info.get_center(), how_to_info.get_size(), 
                          [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    if high_scores_screen:
        canvas.draw_text('High Scores', [270, 70], 40, 'Black', 'monospace')  
        canvas.draw_text('Back', [360, 560], 30, 'Black', 'monospace')

    
#more starting menu things        
def click(pos):
    global intro_screen, help_screen, high_scores_screen, current_level, game_intro
    if intro_screen:
        if pos[0] > 79 and pos[0] < 359 and pos[1] > 365 and pos[1] < 428:
            intro_screen = False   
            current_level = level1
            game_intro = False
            intro_swell.play()            

        if pos[0] > 480 and pos[0] < 680 and pos[1] > 365 and pos[1] < 420:
            intro_screen = False
            help_screen = True
        if pos[0] > 280 and pos[0] < 520 and pos[1] > 475 and pos[1] < 525:
            intro_screen = False
            high_scores_screen = True
    if high_scores_screen:
        if pos[0] > 350 and pos[0] < 440 and pos[1] > 540 and pos[1] < 570:
            high_scores_screen = False
            intro_screen = True            
    if help_screen:       
        if pos[0] > 330 and pos[0] < 500 and pos[1] > 515 and pos[1] < 570:
            help_screen = False
            intro_screen = True                    

#create objects

weather = Weather('light snow')

gas_station_1 = Structure([5000, 460], gas_station_image, gas_station_info, 15, 185)
gas_station_1.set_inventory(0, 0)

house_blue_0 =	Structure([1460, 517], house_blue_image, house_blue_info, 120, 180)

house_green_0 = Structure([1990, 517], house_green_image, house_green_info, 120, 180)

gas_station_0 = Structure([2900, 517], gas_station_image, gas_station_info, 15, 185)

house_green_2 = Structure([5040, 350], house_green_image, house_green_info, 120, 180)
house_green_2.set_inventory(0, 1)

level0 = Level([[397.5, 202.5], [412.5, 157.5], [442.5, 127.5], [502.5, 127.5], [577.5, 172.5], [652.5, 202.5], [697.5, 217.5], [742.5, 247.5], [787.5, 307.5], [817.5, 337.5], [862.5, 352.5], [952.5, 427.5], [1027.5, 472.5], [1042.5, 472.5], [1117.5, 517.5], [1162.5, 517.5], [3112.5, 517.5], [3157.5, 517.5], [3217.5, 502.5], [3322.5, 502.5], [3337.5, 502.5], [3427.5, 517.5], [3742.5, 517.5], [4012.5, 457.5], [4147.5, 442.5], [4207.5, 427.5], [4357.5, 397.5], [4507.5, 352.5], [4552.5, 337.5], [4612.5, 307.5], [4642.5, 292.5], [4882.5, 292.5], [5137.5, 277.5], [5212.5, 262.5], [5287.5, 232.5], [5482.5, 232.5], [5587.5, 202.5], [5617.5, 187.5], [5677.5, 187.5], [5812.5, 232.5], [5917.5, 262.5], [6082.5, 277.5], [6262.5, 322.5], [6307.5, 352.5], [6322.5, 367.5], [6367.5, 367.5], [6472.5, 397.5], [6547.5, 412.5], [6622.5, 412.5], [6682.5, 412.5], [6772.5, 427.5], [6847.5, 442.5], [6922.5, 457.5], [6997.5, 457.5]],
               level0_image, level0_info, 6790, [720, 440, False, None], [6720, 6800, True, None], [gas_station_0, house_blue_0, house_green_0])
level1 = Level([[7.5, 337.5], [127.5, 352.5], [217.5, 382.5], [322.5, 412.5], [427.5, 442.5], [577.5, 442.5], [727.5, 412.5], [787.5, 412.5], [922.5, 412.5], [1027.5, 427.5], [1177.5, 457.5], [1282.5, 457.5], [1387.5, 442.5], [1462.5, 427.5], [1522.5, 412.5], [1582.5, 397.5], [2017.5, 397.5], [2062.5, 397.5], [2557.5, 307.5], [2647.5, 307.5], [2782.5, 322.5], [3037.5, 382.5], [3127.5, 397.5], [3202.5, 397.5], [3232.5, 382.5], [3277.5, 367.5], [3322.5, 352.5], [3427.5, 352.5], [3562.5, 397.5], [3667.5, 427.5], [3712.5, 442.5], [3787.5, 442.5], [3832.5, 427.5], [3862.5, 427.5], [3982.5, 397.5], [4027.5, 382.5], [4057.5, 367.5], [4102.5, 352.5], [4312.5, 352.5], [4807.5, 442.5], [4927.5, 457.5], [5122.5, 457.5], [5332.5, 442.5], [5467.5, 442.5], [5902.5, 367.5], [5992.5, 352.5], [6067.5, 337.5], [6412.5, 322.5], [6892.5, 322.5], [7087.5, 322.5], [7102.5, 322.5], [7192.5, 337.5]]
               , level1_image, level1_info, 3600, [680, 560, False, None], [6565, 6665, True, None], [gas_station_1])
level2 = Level([[7.5, 277.5], [232.5, 292.5], [547.5, 367.5], [652.5, 397.5], [757.5, 412.5], [997.5, 412.5], [1072.5, 397.5], [1162.5, 367.5], [1312.5, 277.5], [1522.5, 172.5], [1582.5, 157.5], [1627.5, 142.5], [1672.5, 142.5], [1732.5, 157.5], [1912.5, 322.5], [1972.5, 382.5], [2017.5, 397.5], [2092.5, 427.5], [2152.5, 442.5], [2182.5, 427.5], [2227.5, 397.5], [2302.5, 367.5], [2392.5, 367.5], [2572.5, 397.5], [2722.5, 412.5], [2827.5, 412.5], [2842.5, 412.5], [2887.5, 397.5], [2932.5, 397.5], [2962.5, 382.5], [3022.5, 367.5], [3097.5, 322.5], [3172.5, 292.5], [3202.5, 292.5], [3562.5, 127.5], [3607.5, 112.5], [3637.5, 97.5], [3652.5, 97.5], [3697.5, 112.5], [3727.5, 127.5], [3802.5, 157.5], [3862.5, 172.5], [3922.5, 202.5], [4102.5, 247.5], [4312.5, 277.5], [4492.5, 292.5], [4597.5, 307.5], [4852.5, 352.5], [5242.5, 352.5], [5287.5, 352.5], [5377.5, 337.5], [5437.5, 322.5], [5587.5, 292.5], [5932.5, 292.5], [6217.5, 292.5], [6442.5, 292.5], [6532.5, 277.5], [6652.5, 262.5], [6742.5, 247.5], [6937.5, 247.5], [7117.5, 232.5]],
               level2_image, level2_info, 440, [600, 440, True, None], [6550, 6740, False, None], [house_green_2])

level0.set_adjacent_levels(None, level1)
level1.set_adjacent_levels(level0, level2)
level2.set_adjacent_levels(level1, None)

current_level = level1

populate_objects('tree', level1, 600, 7200, 30)
populate_objects('bush', level1, 600, 7200, 15)

populate_objects('tree', level0, 400, 7200, 15)
populate_objects('bush', level0, 400, 7200, 10)

populate_objects('tree', level2, 0, 7200, 40)
populate_objects('bush', level2, 0, 7200, 15)

populate_objects('axe', level1, 2000, 5000, 1)

my_char = Character([WIDTH / 2, HEIGHT / 2 - 100], 0, character_image, character_info)

ambient_wind.play()
ambient_wind.rewind()
ambient_wind.play()

alert_text = AlertText()
                                
#set up frame and start things        
frame = simplegui.create_frame("Celsius", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(my_char.keydown_handler)
frame.set_keyup_handler(my_char.keyup_handler)

wood_label = frame.add_label('')
matches_label = frame.add_label('')
food_label = frame.add_label('')
axe_label = frame.add_label('')
crowbar_label = frame.add_label('')

frame.start()
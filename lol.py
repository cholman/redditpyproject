import pygame
import math
pygame.init()

# calculate sin and cos to increase speed
SINTABLE = [math.sin(math.radians(angle)) for angle in xrange(360)]
COSTABLE = [math.cos(math.radians(angle)) for angle in xrange(360)]

# handle pygame basic window
# handle event loop
class Window:
    def __init__(self,caption,size,flags=0,depth=0,fps=30):
        self.fps = fps # frames per second
        
        self.screen = pygame.display.set_mode(size,flags,depth)
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock() # use to control framerate
        self.Window_Open = True
        self.Run = True
        
        self.updatefunc = None
        self.eventfunc = None
            
    def SetPage(self,updatefunc = None,eventfunc = None):
        self.updatefunc = updatefunc
        self.eventfunc = eventfunc
            
    def Flip(self):
        self.Run = True
        while self.Run and self.Window_Open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Window_Open = False
                else:
                    if self.eventfunc is not None:
                        self.eventfunc(event)

            if self.updatefunc is not None:
                self.updatefunc(self.screen)
                                    
            pygame.display.flip()
            self.clock.tick(self.fps)

# pos :: where it start on screen
# size :: if you want to resize it else put None
# imagename :: image file name
# transparent :: if you have a transparent color
class ImageRotater:
   def __init__(self,pos,imagename,size=None,transparent=None):
      if isinstance(imagename,str):
         self.image = pygame.image.load(imagename)
      else:
         self.image = imagename
      if size is not None:
         self.image = pygame.transform.scale(self.image,size)
      self.image = self.image.convert()
      
      if transparent is not None:
         self.image.set_colorkey(transparent)
         
      self.r_image = self.image.copy() # store rotated image
         
      self.rect = pygame.Rect(pos,self.image.get_size())
      self.angle = 0
      self.speed = 0
      self.acc = [0,0]
      self.center = list(self.rect.center)
      
   def Speed(self,pyint,imax,imin):
      self.speed += pyint
      if self.speed > -imin:
         self.speed = -imin
      elif self.speed < -imax:
         self.speed = -imax
         
      self.Calculate()
      
   def Rotate(self,pyint):
      if pyint > 0:
         self.angle = (self.angle + pyint) % 360
      else:
         self.angle = (self.angle + 360 + pyint) % 360
         
      # rotate from the real image
      self.r_image = pygame.transform.rotate(self.image,self.angle)
      # to rotate on center.
      x,y = self.rect[:2] # store the old pos
      self.rect = self.r_image.get_rect()
      self.rect.move_ip(x,y)
      
      self.Calculate()
         
   def Calculate(self):
      angle = int(self.angle)
      self.acc[0] = self.speed * SINTABLE[angle]
      self.acc[1] = self.speed * COSTABLE[angle]
      
   def Draw(self,surface):
      self.center[0] += self.acc[0]
      self.center[1] += self.acc[1]
      
      #move image on center
      x = self.rect.centerx - self.center[0]
      y = self.rect.centery - self.center[1]
      self.rect.move_ip(-x,-y)
      
      surface.blit(self.r_image,self.rect[:2])
      
class Bullet:
   def __init__(self,x,y,angle):
      self.x = x
      self.y = y
      self.length = 0
      self.angle = angle
      
   def Draw(self,surface):
      self.x += -SINTABLE[int(self.angle)] * 6
      self.y += -COSTABLE[int(self.angle)] * 6
      self.length += 6
      pygame.draw.line(surface,(200,0,0),(self.x,self.y),(self.x + 3,self.y + 3),3)
      
class MainPage:
   def __init__(self):
      triangle = pygame.Surface((50,50))
      triangle.fill((0,0,0))
      pygame.draw.lines(triangle,(100,100,200),True,[(0,49),(24,0),(49,49)])
      self.image = ImageRotater((200,200),triangle,None,(0,0,0))
      
      self.keys = [False,False,False,False,False] # [UP,DOWN,LEFT,RIGHT,SPACE]
      
      self.bullets = []
      self.delay = 0 
      
   def Update(self,surface):
      surface.fill((0,0,110))
      if self.keys[0]: self.image.Speed(-0.3,5,-2)
      if self.keys[1]: self.image.Speed(0.2,5,-2)
      if self.keys[2]: self.image.Rotate(2.5)
      if self.keys[3]: self.image.Rotate(-2.5)
      if self.keys[4]:
         if self.delay == 0:
            dx = self.image.rect.centerx + -SINTABLE[int(self.image.angle)] * 25
            dy = self.image.rect.centery + -COSTABLE[int(self.image.angle)] * 25
            self.bullets.append(Bullet(dx,dy,self.image.angle))
            self.delay = 10
      if self.delay > 0: self.delay -= 1
      
      self.image.Draw(surface)
      
      newbullets = []
      for b in self.bullets:
         if 0 < b.x < 800 and 0 < b.y < 600:
            if b.length < 300:
               newbullets.append(b)
               b.Draw(surface)
      bullets = newbullets
            
      
   # store keydown and up events
   def Event(self,event):
      if event.type == pygame.KEYDOWN:
         if event.key in [pygame.K_UP, pygame.K_w]:
            self.keys[0] = True
         elif event.key in [pygame.K_DOWN, pygame.K_s]:
            self.keys[1] = True
         elif event.key in [pygame.K_LEFT, pygame.K_a]:
            self.keys[2] = True
         elif event.key in [pygame.K_RIGHT, pygame.K_d]:
            self.keys[3] = True
         elif event.key == pygame.K_SPACE:
            self.keys[4] = True
      elif event.type == pygame.KEYUP:
         if event.key in [pygame.K_UP, pygame.K_w]:
            self.keys[0] = False
         elif event.key in [pygame.K_DOWN, pygame.K_s]:
            self.keys[1] = False
         elif event.key in [pygame.K_LEFT, pygame.K_a]:
            self.keys[2] = False
         elif event.key in [pygame.K_RIGHT, pygame.K_d]:
            self.keys[3] = False
         elif event.key == pygame.K_SPACE:
            self.keys[4] = False
            
if __name__ == '__main__':
   window = Window("Pygame Rotate",(800,600),fps=60)
   mpage = MainPage()
   window.SetPage(mpage.Update, mpage.Event)
   window.Flip() 
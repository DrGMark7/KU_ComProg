class Point:
  # Constuctor
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def is_on_x_axis(self):
    if self.__y == 0: return True
    else: return False

  def is_on_y_axis(self):
    if self.__x == 0: return True
    else: return False

  def translate(self, dist_x, dist_y):
    self.__x = self.__x + dist_x
    self.__y = self.__y + dist_y

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y

  def set_x(self, new_x):
    self.__x = new_x

  def set_y(self, new_y):
    self.__y = new_y

  def __str__(self):
    return f"({self.__x}, {self.__y})"

  def __eq__(self, other):
    return self.__x == other.__x and self.__y == other.__y

class Line:
    def __init__(self,x1,y1,x2,y2) -> None:
        self.x1 , self.y1 = x1,y1
        self.x2 , self.y2 = x2,y2
        self.dY = self.y2 - self.y1
        self.dX = self.x2 - self.x1
        self.slope = self.dY/self.dX
        self.start = Point(x1,y1)
        self.end = Point(x2,y2)
        
        self.c = self.y2 - self.x2*self.slope

    def contains(self,x,y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            Ans_y = self.slope*x + self.c
            if Ans_y == y:
                return True
            else:
                return False
        else:
            return False
        
    def get_y(self,x):
        y  = self.slope*x + self.c
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return y
        else:
            return -999.999
        
    def get_distance(self):
        return (self.dY**2 + self.dX**2)**0.5
        
    def get_x1(self):
        return self.x1
    
    def get_x2(self):
        return self.x2
    
    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2
    

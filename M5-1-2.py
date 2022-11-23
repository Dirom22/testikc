class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
  
    def __del__(self):
        class_name = self.__class__.__name__
        print('{} удален'.format(class_name))

    def line(self):
    	self.x1 = int(input())
    	self.y1 = int(input())
    	print('{} коордитнаты'.format(class_name))

    	

pt1 = Point()
pt2 = Point()
pt3 = Point()
print(id(pt1), id(pt2), id(pt3))  # выведите id объектов
del pt1
del pt2
del pt3
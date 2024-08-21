

#class Rectangle:


    #def __init__(self, a, b):
      #      self.a = a
     #       self.b = b

    #def __str__(self):
   #     return f"Rectangle {self.a}x{self.b}"


  #  def get_area(self):
 #        return self.a  * self.b

#class Square:


   # def __init__(self, a):
  #          self.a = a

 #   def __str__(self):
#        return f"Square {self.a}x{self.a}"

  #  def get_area(self):
 #        return self.a**2

#class Circle:

    #def __init__(self,r):
     #   self.r = r

    #def __str__(self):
     #   return f"Circle radius = {self.r}"

    #def get_area(self):
       # return 3.14 * self.r**2

class Pasport:
    a = 66
    b = 14
    def check_person_name(name: str) -> bool:
        pattern_name = re.compile(r"^[А-ЯЇІЄҐ][а-яїієґ]+ [А-ЯЇІЄҐ][а-яїієґ]+ [А-ЯЇІЄҐ][а-яїієґ]+$")

        if not isinstance(name, str):
            raise TypeError(f'Use {str} value')
        if not re.search(pattern_name, name):
            raise ValueError(f'Value name incorrect {name}. Use name of this pattern: "Габовда Іван Іванович"')
        return True

    def pasport_name(self,a):
        def  d = b < a:
        print (d)
    else:
        print("Your age is over 66")

    def frange(start,stop, step):
        i = start
        while i < stop:
            yield i
            i += step
        for in frange(40,130,0.01)
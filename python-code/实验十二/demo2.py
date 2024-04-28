class Squa:
    length=10
    def squazc(self):
        return 4*self.length
    def squamj(self):
        return self.length**2
class Rect(Squa):
    width=20
    def recztc(self):
        return 2*(self.length+self.width)
    def rectmj(self):
        return self.length*self.width

sq1=Squa()
print("正方形的默认边长为：")
print("正方形的边长为： ",sq1.length)
print("正方形的周长为： ",sq1.squazc())
print("正方形的面积为： ",sq1.squamj())
rec1=Rect()
print("长方形的默认宽为：")
print("长方形的长和宽为：",rec1.length,rec1.width)
print("长方形的周长为： ",rec1.recztc())
print("长方形的面积为： ",rec1.rectmj())

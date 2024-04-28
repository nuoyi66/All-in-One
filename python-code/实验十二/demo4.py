class circle:
    r=10
    def circlezc(self):
        return 2*3.14*self.r
    def circlemj(self):
        return 3.14*self.r**2
class ball(circle):
    def ballbmj(self):
        return 4*3.14*self.r**2
    def balltj(self):
        return 4/3.0*3.14*self.r**3
cir1=circle()
print("圆的默认值为：")
print("圆的周长为：",cir1.circlezc())
print("圆的面积为：",cir1.circlemj())
cir1.r=20
print("圆的修改值为：")
print("圆的周长为：",cir1.circlezc())
print("圆的面积为：",cir1.circlemj())
ball1=ball()
print("球的默认值为：")
print("球的表面积为：",ball1.ballbmj())
print("球的体积为：",ball1.balltj())
ball1.r=20
print("球的修改值为：")
print("球的表面积为：",ball1.ballbmj())
print("球的体积为：",ball1.balltj())

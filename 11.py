from turtle import *
speed (2)
bgcolor("black")
color("aqua")
# هذا السطر به خطأ إملائي، يجب أن يكون color("aqua")
for x in range(160):
    rt(x)
    circle(150,x)
    fd(x) # هذا السطر غير صحيح، fd تتطلب قيمة رقمية
    rt(98)
hideturtle()
mainloop() # أو done() لكن mainloop() أفضل

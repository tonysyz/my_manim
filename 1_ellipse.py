from manimlib.imports import *
import math

class Tuoyuan(GraphScene):
    
    CONFIG = {
        'x_min':-4,
        'x_max':4,
        'y_min':-3,
        'y_max':3,
        "x_axis_width": 8,
        'graph_origin':ORIGIN,
        'axes_color':WHITE,
        'const_a':2.0,
        'const_b':3.0,
    }
    s = 0.5
    t = -0.5
    
    
    def construct(self):
        dot_ = Dot()
        dot_.move_to(UP*2)
        self.setup_axes(animate=True)
        self.play(ShowCreation(NumberPlane(lag_ratio=0)))
        self.wait()
        self.play(ShowCreation(Ellipse(width=4,color=YELLOW,height=2*math.sqrt(3))))
        self.play(ShowCreation(dot_))
        a = self.get_graph(lambda x: self.s*x+2,color=GREEN)
        self.play(ShowCreation(a))
        k = ValueTracker(self.s)

        def get_circle(a, b, r, **kwargs):
            return ParametricFunction(lambda t: (a+r*np.cos(t))*RIGHT+(b + r*np.sin(t))*UP, t_min=-PI, t_max=PI)
            
        def get_line(k):
            b = self.get_graph(lambda x: k*x+2,color=GREEN)
            return b
        a.add_updater(lambda n: n.become(get_line(k.get_value())))
        dot1 = Dot(color=RED).add_updater(lambda a: a.move_to(
            (-(8*(k.get_value()) + 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)) * RIGHT+
            ((((-(8*(k.get_value()) + 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)))*(k.get_value()))+2) * UP)
        )
        dot2 = Dot(color=RED).add_updater(lambda a: a.move_to(
            (-((8*k.get_value()) - 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)) * RIGHT+
            ((((-(8*(k.get_value()) - 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)))*(k.get_value()))+2) * UP)
        )
        dot1_1 = Dot(color=BLUE).add_updater(lambda a: a.move_to(
            (-8*k.get_value()/(3+4*k.get_value()**2)) * RIGHT+
            (6/(3+4*k.get_value()**2)) * UP))
        self.play(ShowCreation(dot1))
        self.play(ShowCreation(dot2))
        self.play(ShowCreation(dot1_1))
        self.play(k.increment_value, 3.5,run_time=3)
        self.play(k.increment_value, -3,run_time=3)
        self.play(Uncreate(dot1))
        self.play(Uncreate(dot2))
        self.play(Uncreate(dot1_1))
        self.play(Uncreate(a))

        z = ValueTracker(self.t)
        
        dot3 = Dot(color=RED).add_updater(lambda a: a.move_to(
            (-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)) * RIGHT+
            ((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2) * UP)
        )
        dot4 = Dot(color=RED).add_updater(lambda a: a.move_to(
            (-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)) * RIGHT+
            ((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2) * UP)
        )
        dot1_2 = Dot(color=BLUE).add_updater(lambda a: a.move_to(
            (-8*z.get_value()/(3+4*z.get_value()**2)) * RIGHT+
            (6/(3+4*z.get_value()**2)) * UP))
        m = self.get_graph(lambda x: self.t*x+2,color=GREEN)
        self.play(ShowCreation(m))
        m.add_updater(lambda n: n.become(get_line(z.get_value())))
        self.play(ShowCreation(dot3))
        self.play(ShowCreation(dot4))
        self.play(ShowCreation(dot1_2))
        self.play(z.increment_value, -3.5,run_time=3)
        self.play(z.increment_value, 3,run_time=3)
        
        
        # x_1 = -8*z.get_value()/(3+4*z.get_value()**2)
        # y_1 = 6/(3+4*z.get_value()**2)

        #r = math.sqrt(((-8*z.get_value()/(3+4*z.get_value()**2))-(-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+((6/(3+4*z.get_value()**2))-((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)


        e = get_circle(
            -8*z.get_value()/(3+4*z.get_value()**2),
            6/(3+4*z.get_value()**2),
            math.sqrt(((-8*z.get_value()/(3+4*z.get_value()**2))-(-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+((6/(3+4*z.get_value()**2))-((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2))
        e.add_updater(lambda e: e.become(get_circle(
            -8*z.get_value()/(3+4*z.get_value()**2),
            6/(3+4*z.get_value()**2),
            math.sqrt(((-8*z.get_value()/(3+4*z.get_value()**2))-(-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+((6/(3+4*z.get_value()**2))-((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2))))
        self.play(ShowCreation(e))
        #self.wait(lambda n: n.become(get_line(z.get_value())))
        self.wait()
        self.play(z.increment_value, -3,run_time=3)
        self.play(z.increment_value, 4-2*math.sqrt(3)/3,run_time=3)
        dot_o = Dot(point=ORIGIN,color=RED)
        self.play(ShowCreation(dot_o))
        self.wait()
        v1 = Vector([
            (-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)),
            ((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)],color=BLUE)
        v2 = Vector([
            (-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)),
            ((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)],color=ORANGE)
        v1.add_updater(lambda v: v.become(Vector([
            (-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)),
            ((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)],color=BLUE)))
        v2.add_updater(lambda v: v.become(Vector([
            (-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)),
            ((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)],color=ORANGE)))
        #a = str(math.acos((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))+((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)))/((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5+(((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5)))
        #angle = TextMobject(str(math.acos((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))+((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)))/((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5+(((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5)))[:5]).move_to(3*LEFT+2*UP)
        #angle.add_updater(lambda a: a.become(TextMobject(str(math.acos((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))+((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2)))/((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) + 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5+(((-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+(((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2)**0.5)))[:5]).move_to(3*LEFT+2*UP)))
        self.play(Write(angle))
        self.play(ShowCreation(v1))
        self.play(ShowCreation(v2))
        self.play(z.increment_value, -4*math.sqrt(3)/3,run_time=3)
        self.play(z.increment_value, 4.2*math.sqrt(3)/3,run_time=3)
        self.play(z.increment_value, -0.2*math.sqrt(3)/3,run_time=3)






class Title:
    def construct(self):
        title0 = TextMobject('圆锥曲线：椭圆大题')
        #t1 = TexMobject('设椭圆C:\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)的左、右焦点分别为F_{1}、F_{2}，过F_{2}的直线交椭圆于A、B两点，若椭圆C的离心率为\frac{1}{2},\bigtriangleup ABF_{1}的周长为8.')
        #t2 = TexMobject('(\textbf{I})求椭圆C的方程；')
        #t3 = TexMobject('(\textbf{II})已知直线l:y=kx+2与椭圆C交与M、N两点，是否存在实数k使得以MN为直径的圆恰好经过坐标原点？若存在，求出k的值；若不存在，请说明理由.')
        self.play(FadeInFrom(title0,UP))
        self.play(FadeOutAndShiftDown(title0))
        t1 = TextMobject('首先来看一下题目')
        self.play(ShowCreation(t1))
        self.play(Uncreate(t1))
        t2 = TextMobject('设椭圆C:')
        t3 = TexMobject(r'\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)')
        t2.to_corner(LEFT+UP,buff=MED_SMALL_BUFF)
        t3.next_to(t2)
        self.play(Write(t2))
        self.play(Write(t3))
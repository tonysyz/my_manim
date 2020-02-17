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
        dot2 = Dot(color=BLUE).add_updater(lambda a: a.move_to(
            (-((8*k.get_value()) - 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)) * RIGHT+
            ((((-(8*(k.get_value()) - 2 * math.sqrt(12 * (k.get_value())**2 - 3))/(3 + 4 * (k.get_value())**2)))*(k.get_value()))+2) * UP)
        )
        dot1_1 = Dot(color=RED).add_updater(lambda a: a.move_to(
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
        dot4 = Dot(color=BLUE).add_updater(lambda a: a.move_to(
            (-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)) * RIGHT+
            ((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2) * UP)
        )
        dot1_2 = Dot(color=RED).add_updater(lambda a: a.move_to(
            (-8*z.get_value()/(3+4*z.get_value()**2)) * RIGHT+
            (6/(3+4*z.get_value()**2)) * UP))
        m = self.get_graph(lambda x: self.t*x+2,color=GREEN)
        self.play(ShowCreation(m))
        m.add_updater(lambda n: n.become(get_line(z.get_value())))
        self.play(ShowCreation(dot3))
        self.play(ShowCreation(dot4))
        self.play(ShowCreation(dot1_2))
        self.play(z.increment_value, -3.5,run_time=3)
        self.play(z.increment_value, +3,run_time=3)
        
        
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
        self.play(z.increment_value, -3.5,run_time=3)
        self.play(z.increment_value, +3,run_time=3)
        self.wait()
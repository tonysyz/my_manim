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
        title0 = TextMobject('圆锥曲线：椭圆大题')
        self.wait(2)
        t1 = TextMobject(r'\begin{flushleft}设椭圆C:$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$的左、右焦点分别\\为$F_{1}$、$F_{2}$，过$F_{2}$的直线交椭圆于A、B两点，\\若椭圆C的离心率为$\frac{1}{2}$,$\bigtriangleup ABF_{1}$的周长为8\end{flushleft}')
        t2 = TextMobject(r'\leftline{(\textbf{I})求椭圆C的方程；}')
        t3 = TextMobject(r'\begin{flushleft}(\textbf{II})已知直线$l:y=kx+2$与椭圆$C$交与$M$、$N$\\两点，是否存在实数$k$使得以$MN$为直径的圆恰好经过\\坐标原点？若存在，求出$k$的值；若不存在，请说明理由.\end{flushleft}')
        self.play(FadeInFrom(title0,UP))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title0))
        t4 = TextMobject('首先来看一下题目')
        self.play(Write(t4))
        self.wait(2)
        self.play(FadeOut(t4))
        t1.to_corner(LEFT+UP,buff=MED_LARGE_BUFF)
        t2.move_to(np.array([-4,1.2,0]))
        self.play(Write(t1),run_time=5)
        self.play(Write(t2),run_time=3)
        self.play(Write(t3),run_time=5)
        self.wait(10)
        self.play(FadeOut(t3))
        t0 = TextMobject(r'\begin{flushleft}解：\\$\because e=\frac{c}{a}=\frac{1}{2}$\\$4a=8$\\$a^2+b^2=c^2$\\$\therefore a=2$\\$b=\sqrt{3}$\\$c=1$\end{flushleft}')
        t0.move_to(np.array([-3,-1.2,0]))
        self.play(Write(t0),run_time=2)
        self.wait(4)
        t6 = TextMobject(r'$\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$')
        t7 = t6.move_to(np.array([-3,-1,0]))
        self.play(ReplacementTransform(t0,t7),run_time=2)
        self.wait(2)
        self.play(FadeOut(t7))
        
        t5 = TextMobject(r'第一问比较简单，我们来看第二问：')
        t5.move_to(DOWN*1.5)
        t6.to_corner(LEFT+UP,buff=MED_LARGE_BUFF)
        self.play(FadeOut(t1))
        self.play(FadeOut(t2))
        self.play(Write(t5))
        self.wait(2)
        self.play(FadeOut(t5))
        self.wait()
        t3.to_corner(LEFT+UP,buff=MED_LARGE_BUFF)
        self.play(Write(t3),run_time=5)
        self.wait(4)
        self.play(FadeOut(t3))


        text1 = TextMobject(r'根据题意：$y=kx+2$这条直线在与椭圆有焦点的情况下进行旋转\\我们把两个方程联立:')
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))


        a = TexMobject(r'{{x^2}','\\over',r'4}',r'+',r'{{(kx+2)^2}','\\over',r'3}',r'=',r'1')
        aa = a[8].get_center()
        text2 = TexMobject(r'\begin{cases}y=kx+2\\\frac{x^2}{4}+\frac{y^2}{3}=1\end{cases}')
        a[0].set_color(BLUE)
        a[4].set_color(BLUE)
        text4 = TexMobject(r'y^2')
        text5 = TexMobject(r'(kx+2)^2')
        text4.move_to(a[4].get_center())
        text5.move_to(a[4].get_center())
        group = VGroup(a[:4],a[5:],text4)
        self.play(Write(text2))
        self.play(ReplacementTransform(text2,group))
        self.wait()
        self.play(ReplacementTransform(group[2],text5))
        text6 = TexMobject(r'3x^2+4(k^2 x^2 + 4kx + 4)')
        group0 = VGroup(a[:4],text5,a[5:7])
        text6.move_to(a[1].get_center())
        self.play(ReplacementTransform(group0,text6))
        text8 = TexMobject('12').move_to(aa)
        self.play(ReplacementTransform(a[8:],text8))
        text10 = TexMobject('0')
        group1 = VGroup(text6,a[7:8],a[8:])
        #self.play(group1.to_edge(UP,buff=MED_SMALL_BUFF))
        text7 = TexMobject(r'(3+4k^2)x^2 + 16kx+',r'16').move_to(text5.get_center())
        m = text7[1].get_center()
        text8.move_to(aa)
        text10.move_to(aa)
        self.play(ReplacementTransform(group1[2],text8))
        self.play(ReplacementTransform(group1[0],text7))
        text11 = TexMobject('4').move_to(m)
        self.play(ReplacementTransform(text7[1],text11))
        self.play(ReplacementTransform(text8,text10))
        group2 = VGroup(text7,text11,text10,text8,a[7])
        self.play(group2.shift,UP*3,rate_func=smooth,run_time=1)
        text12 = TexMobject(r'\Delta = 192k^2-48').next_to(group2,DOWN)
        text13 = TextMobject(r'当$\Delta>0$时:\\$k\in (-\infty,-\frac{1}{2})\cup(\frac{1}{2},+\infty)$').next_to(text12,DOWN)
        self.play(Write(text12))
        self.play(Write(text13))
        self.play(FadeOut(group2))
        self.play(FadeOut(text12))
        self.play(FadeOut(text13))




        self.play(Write(t6))
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
        dot_3 = TextMobject('A').next_to(dot3,UP)
        dot_4 = TextMobject('B').next_to(dot4,DOWN)
        dot_1_2 = TextMobject("O'").next_to(dot1_2,RIGHT)
        dot_3.add_updater(lambda d: d.become(TexMobject('A').next_to(dot3,UP)))
        dot_4.add_updater(lambda d: d.become(TexMobject('B').next_to(dot4,DOWN)))
        dot_1_2.add_updater(lambda d: d.become(TexMobject("O'").next_to(dot1_2,RIGHT)))
        m = self.get_graph(lambda x: self.t*x+2,color=GREEN)
        self.play(ShowCreation(m))
        m.add_updater(lambda n: n.become(get_line(z.get_value())))
        self.play(Write(dot3))
        self.play(Write(dot4))
        self.play(Write(dot1_2))
        self.play(Write(dot_3))
        self.play(Write(dot_4))
        self.play(Write(dot_1_2))
        self.play(z.increment_value, -3.5,run_time=3)
        self.play(z.increment_value, 3,run_time=3)
        

        e = get_circle(
            -8*z.get_value()/(3+4*z.get_value()**2),
            6/(3+4*z.get_value()**2),
            math.sqrt(((-8*z.get_value()/(3+4*z.get_value()**2))-(-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+((6/(3+4*z.get_value()**2))-((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2))
        e.add_updater(lambda e: e.become(get_circle(
            -8*z.get_value()/(3+4*z.get_value()**2),
            6/(3+4*z.get_value()**2),
            math.sqrt(((-8*z.get_value()/(3+4*z.get_value()**2))-(-((8*z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))**2+((6/(3+4*z.get_value()**2))-((((-(8*(z.get_value()) - 2 * math.sqrt(12 * (z.get_value())**2 - 3))/(3 + 4 * (z.get_value())**2)))*(z.get_value()))+2))**2))))
        self.play(ShowCreation(e))
        
        self.wait()
        self.play(z.increment_value, -3,run_time=3)
        self.play(z.increment_value, 4-2*math.sqrt(3)/3,run_time=3)
        dot_o = Dot(point=ORIGIN,color=RED)
        o_label = TexMobject(r'O').next_to(dot_o,LEFT+DOWN)
        self.play(ShowCreation(dot_o))
        self.play(Write(o_label))
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
        #self.play(Write(angle))
        self.play(ShowCreation(v1))
        self.play(ShowCreation(v2))
        self.play(z.increment_value, -4*math.sqrt(3)/3,run_time=3)
        self.play(z.increment_value, 4.2*math.sqrt(3)/3,run_time=3)
        self.play(z.increment_value, -0.2*math.sqrt(3)/3,run_time=3)
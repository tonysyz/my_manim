from manimlib.imports import *
import math

class TridentOfNewton(GraphScene):
    CONFIG = {
        'x_min':-8,
        'x_max':8,
        "x_axis_width":16,
        'y_min':-4,
        'y_max':4,
        "y_axis_height": 8,
        'graph_origin':ORIGIN,
        'axes_color':WHITE,
    }
    
    
    def construct(self):
        title = TexMobject(r"f(x)={{ax^2}+{{b}\over{x}}}(a>0,b>0)").to_edge(UP, buff=MED_LARGE_BUFF)
        title_cn = TextMobject(r"牛顿三叉戟曲线").next_to(title, DOWN).scale(1.5)
        self.play(Write(title))
        self.play(Write(title_cn))
        self.play(
            FadeOut(title),
            FadeOut(title_cn),
            run_time=2
        )

        #proof
        a = 1
        b = 1
        aa = ValueTracker(a)
        bb = ValueTracker(b)
        self.wait()
        self.setup_axes()
        plane = NumberPlane()
        self.play(Write(plane))
        parabola_graph = self.get_graph(lambda x: aa.get_value()*x**2, x_max= 20,color=RED_A)
        parabola_graph.add_updater(lambda x: x.become(self.get_graph(lambda x: aa.get_value()*x**2, x_max= 20,color=RED_A)))
        parabola_graph_label = self.get_graph_label(parabola_graph, label="f(x)=ax^2")
        inverse = self.get_graph(lambda x: bb.get_value()/x, x_min=0.04,color=PURPLE_E)
        inverse_function_graph = VGroup(
            inverse.add_updater(lambda  x: x.become(self.get_graph(lambda x: bb.get_value()/x, x_min=0.05,color=PURPLE_E))),
            self.get_graph(lambda x: bb.get_value()/x, x_max=-0.05,color=PURPLE_E).add_updater(lambda x: x.become(self.get_graph(lambda x: bb.get_value()/x, x_max=-0.05,color=PURPLE_E)))
        )
        inverse_function_graph_label = self.get_graph_label(inverse, label="g(x)={b\\over x}", direction=UP, buff=MED_LARGE_BUFF)
        self.play(
            Write(parabola_graph),
            Write(parabola_graph_label),
            Write(inverse_function_graph),
            Write(inverse_function_graph_label),
            run_time=2
        )
        self.wait()

        trident_of_newton_l = self.get_graph(lambda x: a*x**2 + b/x, x_min=0.02,color=YELLOW)
        trident_of_newton_l.add_updater(lambda x: x.become(self.get_graph(lambda x: aa.get_value()*x**2 + bb.get_value()/x, x_min=0.05,color=YELLOW)))
        trident_of_newton_r = self.get_graph(lambda x: a*x**2 + b/x, x_max=-0.02,color=YELLOW)
        trident_of_newton_r.add_updater(lambda x: x.become(self.get_graph(lambda x: aa.get_value()*x**2 + bb.get_value()/x, x_max=-0.05,color=YELLOW)))
        trident_of_newton = VGroup(
            trident_of_newton_l,
            trident_of_newton_r
        )
        label_group = VGroup(
            parabola_graph_label,
            inverse_function_graph_label
        )
        trident_of_newton_label = self.get_graph_label(
            trident_of_newton_r,
            label=r"h(x)=ax^2+{{b}\over{x}}",
            direction=RIGHT,
            buff=MED_LARGE_BUFF,
            color=YELLOW
        ).shift(DOWN)
        self.play(
            Write(trident_of_newton),
            Write(trident_of_newton_label),
            run_time=2
        )
        self.wait(2)
        a_value = TexMobject("a=1").to_corner(UL)
        a_value_1 = TexMobject("a=1.5").move_to(a_value.get_center())
        a_value_2 = TexMobject("a=0.5").move_to(a_value.get_center())
        a_value_3 = TexMobject("a=4.0").move_to(a_value.get_center())
        a_value_4 = TexMobject("a=0.1").move_to(a_value.get_center())
        b_value = TexMobject("b=1").next_to(a_value, DOWN)
        b_value_1 = TexMobject("b=1.5").move_to(b_value.get_center())
        b_value_2 = TexMobject("b=0.5").move_to(b_value.get_center())
        b_value_3 = TexMobject("b=0.3").move_to(b_value.get_center())
        b_value_4 = TexMobject("b=4.0").move_to(b_value.get_center())
        self.play(Write(a_value))
        self.play(Write(b_value))
        self.play(ReplacementTransform(a_value, a_value_1),run_time=1.5)
        self.play(aa.increment_value, 0.5)
        self.wait(2)
        self.play(ReplacementTransform(b_value, b_value_1),run_time=1.5)
        self.play(bb.increment_value, 0.5)
        self.wait(2)
        self.play(ReplacementTransform(a_value_1, a_value_2),run_time=1.5)
        self.play(aa.increment_value, -1)
        self.wait(2)
        self.play(ReplacementTransform(b_value_1, b_value_2),run_time=1.5)
        self.play(bb.increment_value, -1)
        self.wait(2)
        self.play(ReplacementTransform(a_value_2, a_value_3),run_time=1.5)
        self.play(aa.increment_value, 3.5)
        self.wait(2)
        self.play(ReplacementTransform(b_value_2, b_value_3),run_time=1.5)
        self.play(bb.increment_value, -0.2)
        self.wait(2)
        self.play(ReplacementTransform(a_value_3, a_value_4),run_time=1.5)
        self.play(aa.increment_value, -3.9)
        self.wait(2)
        self.play(ReplacementTransform(b_value_3, b_value_4),run_time=1.5)
        self.play(bb.increment_value, 3.7)
        self.wait(2)

class Analysis(Scene):
    def construct(self):
        text1 = TextMobject(r"通过直观的观察,会发现:\\三叉戟曲线的形状由$a$,$b$共同决定").move_to(UP)
        text2 = TextMobject(r"当$x\rightarrow 0$时,$y \rightarrow \infty$,图像趋近于反比例函数图像,\\当$x \rightarrow \infty$时,图像趋近于抛物线").next_to(text1, DOWN)
        self.play(
            Write(text1),
            Write(text2),
            run_time=3
        )
        self.wait(5)
        self.play(
            FadeOut(text1),
            FadeOut(text2),
            run_time=0.25
        )
        text3 = TextMobject(r"总结:\\三叉戟曲线有一条直线渐近线$x=0$,\\有两条曲线渐近线:$y=ax^2,y={b\over x}$").move_to(UP)
        text4 = TextMobject(r"之后我们对它进行性质上的探究.").next_to(text3, DOWN)
        self.play(
            Write(text3),
            Write(text4),
            run_time=3
        )
        self.wait(4)

class Dir(TridentOfNewton):
    def construct(self):
        self.setup_axes()
        plane = NumberPlane()
        self.play(Write(plane))
        a = 1
        b = 1
        aa = ValueTracker(a)
        bb = ValueTracker(b)
        trident_of_newton_l = self.get_graph(lambda x: a*x**2 + b/x, x_min=0.04,color=YELLOW)
        trident_of_newton_l.add_updater(lambda x: x.become(self.get_graph(lambda x: aa.get_value()*x**2 + bb.get_value()/x, x_min=0.05,color=YELLOW)))
        trident_of_newton_r = self.get_graph(lambda x: a*x**2 + b/x, x_max=-0.04,color=YELLOW)
        trident_of_newton_r.add_updater(lambda x: x.become(self.get_graph(lambda x: aa.get_value()*x**2 + bb.get_value()/x, x_max=-0.05,color=YELLOW)))
        trident_of_newton = VGroup(
            trident_of_newton_l,
            trident_of_newton_r
        )
        trident_of_newton_label = self.get_graph_label(
            trident_of_newton_r,
            label=r"h(x)=ax^2+{{b}\over{x}}",
            direction=RIGHT,
            buff=MED_LARGE_BUFF,
            color=YELLOW
        ).shift(DOWN)
        self.play(ShowCreation(trident_of_newton),run_time=1.5)
        self.play(Write(trident_of_newton_label),run_time=2)
        text1 = TexMobject(
            r"(",
            r"ax^2",
            r"+",
            r"{{{b}",
            r"\over",
            r"{x}}",
            r"})'"
        ).to_corner(UL)
        text2 = TexMobject(
            r"=(ax^2)'",
            r"+",
            r"{({{b}\over{x}})'}"
        ).next_to(text1, DOWN)
        text3 = TexMobject(
            r"=2ax",
            r"+",
            r"{({{-b}\over{x^2}})}"
        ).next_to(text1, DOWN)
        text4 = TexMobject(
            r"=2ax",
            r"-",
            r"{{b}\over{x^2}}"
        ).next_to(text1, DOWN)
        self.play(
            Write(text1),
            Write(text2),
            run_time=2
        )
        self.play(
            ReplacementTransform(text2[0], text3[0]),
            ReplacementTransform(text2[1], text3[1]),
            ReplacementTransform(text2[2], text3[2]),
            run_time=2
        )
        self.play(
            ReplacementTransform(text3[0], text4[0]),
            ReplacementTransform(text3[1], text4[1]),
            ReplacementTransform(text3[2], text4[2]),
            run_time=2
        )
        self.wait()
        text5 = TexMobject(
            r"=",
            r"0"
        ).next_to(text4, RIGHT)
        self.play(Write(text5))
        self.wait()
        text6 = TexMobject(
            r"xx",
            r"{{b}\over{x^2}}"
        ).move_to(text5[1].get_center())
        text7 = TexMobject(r"2ax").next_to(text5[0], LEFT)
        self.play(
            ReplacementTransform(text4, text7),
            ReplacementTransform(text5[1], text6[1])
        )
        self.wait()
        text8 = TexMobject(r"x=\sqrt[3]{{b}\over{2a}}").move_to(np.array([2,-1,0]))
        self.play(ReplacementTransform(VGroup(text7, text6[1], text5[0]), text8), run_time=2)
        self.wait()
        line = self.get_vertical_line_to_graph((1/2)**(1/3), trident_of_newton_r)
        dot = Dot().move_to(np.array([0.5**(1/3),0.5**(2/3)+2**(1/3),0]))
        dot_label = TexMobject(r"({\sqrt[3]{{b}\over{2a}}},{3\sqrt[3]{{ab^2}\over{4}}})").move_to(np.array([2,1,0])).scale(0.6)
        self.play(
            Write(line),
            Write(dot),
            Write(dot_label),
            run_time=2
        )
        self.wait()
        self.play(FadeOut(VGroup(
            text1,
            line,
            dot,
            dot_label,
            text8
        )))
        para1 = TexMobject(
            r"a",
            r">",
            r"0",
            r"\\",
            r"b",
            r">",
            r"0"
        ).to_corner(UL)
        self.play(Write(para1))
        self.wait()
        trident_of_newton_l1 = self.get_graph(lambda x: x**2 - 1/x, x_min=0.04,color=YELLOW)
        trident_of_newton_r1 = self.get_graph(lambda x: x**2 - 1/x, x_max=-0.04,color=YELLOW)
        trident_of_newton1 = VGroup(
            trident_of_newton_l1,
            trident_of_newton_r1
        )
        para2 = TexMobject(
            r"a",
            r">",
            r"0",
            r"\\",
            r"b",
            r"<",
            r"0"
        ).to_corner(UL)
        trident_of_newton_l2 = self.get_graph(lambda x: -x**2 + 1/x, x_min=0.04,color=YELLOW)
        trident_of_newton_r2 = self.get_graph(lambda x: -x**2 + 1/x, x_max=-0.04,color=YELLOW)
        trident_of_newton2 = VGroup(
            trident_of_newton_l2,
            trident_of_newton_r2
        )
        para3 = TexMobject(
            r"a",
            r"<",
            r"0",
            r"\\",
            r"b",
            r">",
            r"0"
        ).to_corner(UL)
        trident_of_newton_l3 = self.get_graph(lambda x: -x**2 - 1/x, x_min=0.04,color=YELLOW)
        trident_of_newton_r3 = self.get_graph(lambda x: -x**2 - 1/x, x_max=-0.04,color=YELLOW)
        trident_of_newton3 = VGroup(
            trident_of_newton_l3,
            trident_of_newton_r3
        )
        para4 = TexMobject(
            r"a",
            r"<",
            r"0",
            r"\\",
            r"b",
            r"<",
            r"0"
        ).to_corner(UL)
        self.play(
            ReplacementTransform(para1, para2),
            ReplacementTransform(trident_of_newton, trident_of_newton2),
            run_time=3
        )
        self.wait(3)
        self.play(
            ReplacementTransform(trident_of_newton2, trident_of_newton1),
            ReplacementTransform(para2, para3),
            run_time=3
        )
        self.wait(3)
        self.play(
            ReplacementTransform(trident_of_newton1, trident_of_newton3),
            ReplacementTransform(para3, para4),
            run_time=3
        )
        self.wait(3)

class End(Scene):
    def construct(self):
        text = TextMobject(r"感谢观看！\\BGM:Last Train Home\\Tools:Davinci Resolve, Visual Studio Code, manim\\by emat").to_edge(UP)
        self.play(
            Write(text)
        )
        self.wait(4)
        self.play(FadeOut(text))

class Result(Scene):
    def construct(self):
        text = TextMobject(r"总结:\\$ab$的正负决定三叉戟的“对勾”的左$(ab<0)$右$(ab>0)$,\\$b$的正负决定了三叉戟的方向的上$(b>0)$下$(b<0)$.")
        self.play(Write(text), run_time=3)
        self.wait(3)
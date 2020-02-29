from manimlib.imports import *
import math

class Func(GraphScene):
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
        e = math.e
        text1 = TextMobject("大家好,在上期视频中,我们讨论了六个函数:").to_edge(UP,buff=MED_LARGE_BUFF)
        text2 = TexMobject(r'xe^x').next_to(text1,DOWN*2)
        text3 = TexMobject(r'\frac{e^x}{x}').next_to(text2, RIGHT*3)
        text4 = TexMobject(r'\frac{x}{e^x}').next_to(text2, LEFT*3)
        text5 = TexMobject(r'x \ln x').next_to(text2, DOWN*5)
        text6 = TexMobject(r'\frac{\ln x}{x}').next_to(text3, DOWN*3)
        text7 = TexMobject(r'\frac{x}{\ln x}').next_to(text4, DOWN*3)
        self.play(
            Write(text1),
            Write(text2),
            Write(text3),
            Write(text4),
            Write(text5),
            Write(text6),
            Write(text7),
        )
        self.wait()
        group = VGroup(text2,text3,text4,text5,text6,text7)
        self.wait(3)
        text8 = TextMobject("那么,这些函数在压轴题中有什么表现呢?").next_to(text1,DOWN*2)
        self.wait(2)
        self.play(ReplacementTransform(group,text8))
        text9 = TextMobject("来看一道高考数学导数压轴题").next_to(text8,DOWN*2)
        self.wait(2)
        self.play(Write(text9))
        self.wait(2)
        self.play(
            FadeOut(text9),
            FadeOut(text8),
            FadeOut(text1)
        )

        t1 = TextMobject(r"设函数$f(x)=ae^x\ln x + {{be^{x-1}} \over {x}}$,曲线$y=f(x)$在\\点$(1,f(1))$处的切线为$y=e(x-1)+2$").to_edge(UP,buff=MED_LARGE_BUFF)
        t2 = TextMobject(r"(1)求$a$,$b$;").next_to(t1,DOWN).shift(LEFT*4.5)
        t3 = TextMobject(r"(2)证明:$f(x)>1$.").next_to(t2,DOWN).shift(RIGHT*0.9)
        self.play(
            Write(t1),
            Write(t2),
            Write(t3)
        )
        self.wait(15)
        self.play(FadeOut(t3))
        self.wait()
        t4 = TextMobject(
            r"$f(1)=$",
            r"$e(1-1)+2$\\",
            r"${f}'(1)=e$"
        ).next_to(t2,DOWN)
        t4[2].shift(LEFT).shift(DOWN)
        self.play(Write(t4))
        self.wait()
        t5 = TextMobject(r"2").next_to(t4[0],RIGHT)
        t6 = TexMobject(
            r"f(1)=",
            r"ae\ln1+{{b{e}^0}\over{1}}=b"
        ).next_to(t5,RIGHT*3)
        t7 = TexMobject(r"f'(x)={{{{ae^x}\over{x}}+{ae}^{x}\ln {x}}+ ",r"{{{bxe^{x-1}-be^{x-1}}\over {x^2}}}}").next_to(t4[2],RIGHT)
        t8 = TexMobject(r"f'(x)={{{{ae^x}\over{x}}+{ae}^{x}\ln {x}}+",r"{{{be}^{x-1}(x-1)}\over{x^2}}").next_to(t4[2],RIGHT)
        self.play(ReplacementTransform(t4[1],t5))
        self.wait()
        self.play(Write(t6))
        self.wait()
        self.play(Write(t7))
        self.wait()
        self.play(ReplacementTransform(t7[1],t8[1]))
        self.wait()
        t9 = TexMobject(r"\Rightarrow", r" a=1\\b=2").next_to(t8,DOWN)
        t9[0].shift(DOWN*0.45)
        self.play(Write(t9))
        self.wait()
        group1 = VGroup(t2, t4[0], t5, t6, t4[2], t7[0], t8[1], t9)
        self.play(FadeOut(group1))
        self.wait()
        t3.next_to(t1,DOWN).shift(LEFT*3.6)
        self.play(Write(t3))
        self.wait()
        s1 = TexMobject(r"f(x)=", r"(", r"e^x\ln x + {{2e^{x-1}}\over {x}}", r")", r">1").next_to(t3,DOWN)
        s2 = TexMobject(r"\cdot", r"{{x}\over{e^x}}").next_to(s1[4],RIGHT)
        s3 = TexMobject(r"{{x}\over{e^x}}" ,r"\cdot").next_to(s1[1],LEFT)
        group2 = VGroup(s1[0], s1[2], s1[4])
        group3 = VGroup(s1[1], s1[3])
        self.play(Write(group2))
        self.wait()
        self.play(FadeOut(s1[0]))
        self.wait()
        self.play(Write(group3))
        self.wait()
        self.play(Write(s2))
        self.wait()
        self.play(Write(s3))
        self.wait()
        s4 = TexMobject(r"{x\ln {x} +{{2}\over{e}}}", r" > {{x}\over {e^x}}")
        group4 = VGroup(s3, s1[2], s1[3], s1[1])
        group5 = VGroup(s2, s1[4])
        self.play(
            ReplacementTransform(group4, s4[0]),
            ReplacementTransform(group5, s4[1])
        )
        self.wait()
        s5 = TexMobject(
            r"h(x)=",
            r"x\ln x +{2 \over e}"
        ).move_to(np.array([-3,1,0]))
        s6 = TexMobject(
            r"g(x)=",
            r"{x\over e^x}"
        ).move_to(np.array([-3.8,0,0]))
        self.play(Write(s5[0]))
        self.wait()
        self.play(ReplacementTransform(s4[0], s5[1]))
        self.wait()
        self.play(Write(s6[0]))
        self.wait()
        self.play(ReplacementTransform(s4[1], s6[1]))
        self.wait()
        s5_1 = TexMobject(
            r"h'(x)=",
            r"(x\ln x +{2 \over e})'"
        ).move_to(np.array([-3,1,0]))
        s6_1 = TexMobject(
            r"g'(x)=",
            r"({x\over e^x})'"
        ).move_to(np.array([-3.8,0,0]))
        self.play(ReplacementTransform(s5[0],s5_1[0]))
        self.wait()
        self.play(ReplacementTransform(s6[0],s6_1[0]))
        self.wait()
        self.play(ReplacementTransform(s5[1],s5_1[1]))
        self.wait()
        self.play(ReplacementTransform(s6[1],s6_1[1]))
        self.wait()
        s5_2 = TexMobject(
            r"h'(x)=",
            r"(x\ln x)' +({2 \over e})'"
        ).move_to(np.array([-3,1,0]))
        self.play(ReplacementTransform(s5_1[1],s5_2[1]))
        self.wait()
        s5_3 = TexMobject(
            r"h'(x)=",
            r"(x\ln x)'",
            r"+{2 \over e}"
        ).move_to(np.array([-3,1,0]))
        self.play(ReplacementTransform(s5_2[1],s5_3[1]))
        self.wait()
        s5_4 = TexMobject(
            r"h'(x)=",
            r"1+\ln x",
            r"+{2 \over e}"
        ).move_to(np.array([-3,1,0]))
        self.play(ReplacementTransform(s5_3[1], s5_4[1]))
        self.wait()
        s6_2 = TexMobject(
            r"g'(x)=",
            r"{{1-x}\over {e^x}}"
        ).move_to(np.array([-3.8,0,0]))
        self.play(ReplacementTransform(s6_1[1], s6_2[1]))
        self.wait()
        group6 = VGroup(t1, t3, s5_1[0], s6_1[0], s5_4[1], s6_2[1])
        self.play(FadeOut(group6))
        self.wait()

        self.setup_axes(animate=True)
        plane = NumberPlane()
        self.play(ShowCreation(plane))
        def ln(x):
            return math.log(x,e)
        hx = self.get_graph(lambda x: x * ln(x) + 2/e, x_min=0.02)
        hx_label = self.get_graph_label(hx,label=r"h(x)=x \ln x + {2 \over e}").shift(LEFT*5)
        h_x = self.get_graph(lambda x: ln(x)+1, x_min=0.02)
        h_x_label = self.get_graph_label(h_x, label=r"h'(x)=\ln x + 1").shift(DOWN*2)
        gx = self.get_graph(lambda x: x/(e**x))
        gx_label = self.get_graph_label(gx, label=r"g(x)={x \over {e^x}}").move_to(np.array([-2,-1,0]))
        g_x = self.get_graph(lambda x:(x-1)/(e**x))
        g_x_label = self.get_graph_label(g_x, label=r"g'(x)={{x-1}\over{e^x}}").shift(DOWN*0.7)
        line1 = self.get_vertical_line_to_graph(1/e,hx)
        dot1 = Dot().move_to(np.array([1/e, 1/e, 0]))
        dot1_label = TexMobject(r"({1 \over e},{1 \over e})").next_to(dot1, UP).shift(LEFT*2)
        line2 = self.get_vertical_line_to_graph(1, gx)
        dot2 = Dot().move_to(np.array([1, 1/e, 0]))
        dot2_label = TexMobject(r"(1, {1 \over e})").move_to(dot2, DOWN).shift(RIGHT*2)
        self.play(ShowCreation(hx))
        self.wait()
        self.play(ShowCreation(hx_label))
        self.wait()
        self.play(ShowCreation(h_x))
        self.wait()
        self.play(ShowCreation(h_x_label))
        self.wait()
        self.play(Write(line1))
        self.wait()
        self.play(Write(dot1))
        self.wait()
        self.play(Write(dot1_label))
        self.wait()
        group7 = VGroup(hx, hx_label, h_x, h_x_label, line1, dot1, dot1_label)
        self.play(FadeOut(group7))
        self.wait()
        self.play(ShowCreation(gx))
        self.wait()
        self.play(ShowCreation(gx_label))
        self.wait()
        self.play(ShowCreation(g_x))
        self.wait()
        self.play(ShowCreation(g_x_label))
        self.wait()
        self.play(Write(line2))
        self.wait()
        self.play(Write(dot2))
        self.wait()
        self.play(Write(dot2_label))
        self.wait()
        group8 = VGroup(gx, gx_label, g_x, g_x_label, line2, dot2, dot2_label)
        self.play(FadeOut(group8))
        self.wait()
        
        s7 = TexMobject(r"{h(x)_{min}} ={1 \over e}").to_corner(UL)
        s8 = TexMobject(r"{g(x)_{max}} = {1 \over e}").next_to(s7,DOWN)
        self.play(
            Write(hx),
            Write(gx),
            Write(dot1),
            Write(dot2),
            Write(dot1_label),
            Write(dot2_label)
        )
        self.wait()
        self.play(Write(s7))
        self.wait()
        self.play(Write(s8))
        self.wait()
        self.play(
            FadeOut(hx),
            FadeOut(gx),
            FadeOut(dot1),
            FadeOut(dot2),
            FadeOut(dot1_label),
            FadeOut(dot2_label),
            FadeOut(s7),
            FadeOut(s8),
            FadeOut(plane),
            FadeOut(self.axes)
        )
        self.wait()

        te1 = TextMobject(r"$h(x)$在$(0,{1\over e})$单调递减,在$({1\over e},+\infty)$单调递增,\\$h(x)$在$(0,+\infty)$的最小值为:${h(x)_{min}}=h({1\over e})={1\over e}$")
        te2 = TextMobject(r"$g(x)$在$(-\infty, 1)$单调递增,在$(1, +\infty)$单调递减,\\$g(x)$在$(0,+\infty)$的最大值为:${g(x)_{max}}=g(1)={1 \over e}$")
        te1.to_edge(UP)
        te2.next_to(te1, DOWN)
        self.play(
            Write(te1),
            Write(te2)
        )
        self.wait()
        te3 = TextMobject(r"综上,当$x>0$时,$h(x)>g(x)$,即$f(x)>1$").move_to(np.array([0,-1.5,0]))
        self.play(Write(te3))
        self.wait()

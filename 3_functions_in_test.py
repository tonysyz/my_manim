from manimlib.imports import *

class Func(GraphScene):
    def construct(self):
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
        group = VGroup(text2,text3,text4,text5,text6,text7)
        self.wait(3)
        text8 = TextMobject("那么,这些函数在压轴题中有什么表现呢?").next_to(text1,DOWN*2)
        self.wait(2)
        self.play(ReplacementTransform(group,text8))
        text9 = TextMobject("来看一道高考数学导数压轴题").next_to(text8,DOWN*2)
        self.play(Write(text9))
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
        self.play(FadeOut(t3))
        t4 = TextMobject(
            r"$f(1)=$",
            r"$e(1-1)+2$\\",
            r"${f}'(1)=e$"
        ).next_to(t2,DOWN)
        t4[2].shift(LEFT).shift(DOWN)
        self.play(Write(t4))
        t5 = TextMobject(r"2").next_to(t4[0],RIGHT)
        t6 = TexMobject(
            r"f(1)=",
            r"ae\ln1+{{b{e}^0}\over{1}}=b"
        ).next_to(t5,RIGHT*3)
        t7 = TexMobject(r"f'(x)={{{{ae^x}\over{x}}+{ae}^{x}\ln {x}}+ ",r"{{{bxe^{x-1}-be^{x-1}}\over {x^2}}}}").next_to(t4[2],RIGHT)
        t8 = TexMobject(r"f'(x)={{{{ae^x}\over{x}}+{ae}^{x}\ln {x}}+",r"{{{be}^{x-1}(x-1)}\over{x^2}}").next_to(t4[2],RIGHT)
        self.play(ReplacementTransform(t4[1],t5))
        self.play(Write(t6))
        self.play(Write(t7))
        self.play(ReplacementTransform(t7[1],t8[1]))
        t9 = TexMobject(r"\Rightarrow", r" a=1\\b=2").next_to(t8,DOWN)
        t9[0].shift(DOWN*0.45)
        self.play(Write(t9))
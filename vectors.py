from manimlib.imports import *

class IllustrationScene(GraphScene):

    CONFIG = {
        "x_min": -3,
        "x_max": 5,
        "x_axis_width": 8,
        "y_min": -3,
        "y_max": 4,
        "y_axis_height": 7,
        "graph_origin": 1*DOWN + 2*LEFT,
    }

    def get_circle(self, a, b, r, **kwargs):
        return ParametricFunction(lambda t: (a+r*np.cos(t))*RIGHT+(b + r*np.sin(t))*UP+self.CONFIG['graph_origin'], t_min=-PI, t_max=PI)

    def get_vec(self, x, y):
        return Vector().put_start_and_end_on(self.CONFIG["graph_origin"], x*RIGHT+y*UP+self.CONFIG["graph_origin"])

    def get_vec2(self, x, y, start):
        return Vector().put_start_and_end_on(start, x*RIGHT+y*UP+start)

    def construct(self):
        text = TexMobject(r"|\vec{a}|=1",r",|\vec{b}|=2,",r"|\vec{a}+\vec{b}|-|\vec{a}-\vec{b}|\in ?")
        text.shift(UP*3)
        self.play(
            Write(text),
            runtime=1,
        )
        self.wait(1.2)
        self.play(
            FadeOut(text),
        )
        self.wait(1.2)

        pi = math.pi
        self.theta = pi/3
        self.theta0 = pi/2
        t0 = ValueTracker(self.theta)
        t1 = ValueTracker(self.theta0)
        axes = self.setup_axes(animate=True)
        vec_a = self.get_vec(math.cos(self.theta0), math.sin(self.theta0)).set_color(BLUE)
        label_a = TexMobject(r"|\vec{a}|")\
            .add_updater(lambda a: a.become(TexMobject(r"|\vec{a}|").next_to(vec_a, RIGHT)))
        self.play(
            FadeIn(vec_a),
            FadeIn(label_a),
        )
        self.wait(1.2)
        vec_b = self.get_vec(2*math.cos(self.theta), 2*math.sin(self.theta)).set_color(RED_B)
        label_b = TexMobject(r"|\vec{b}|")\
            .add_updater(lambda a: a.become(TexMobject(r"|\vec{b}|").next_to(vec_b, RIGHT)))
        self.play(
            FadeIn(vec_b),
            FadeIn(label_b),
        )
        self.wait(1.2)
        vec_a.add_updater(lambda x: x.become(self.get_vec(math.cos(t1.get_value()), math.sin(t1.get_value())).set_color(BLUE)))
        vec_b.add_updater(lambda x: x.become(self.get_vec(2*math.cos(t0.get_value()), 2*math.sin(t0.get_value())).set_color(RED_B)))
        self.wait(1.2)
        self.play(t0.increment_value, pi/3, run_time=2)
        self.wait(1.2)
        self.play(t1.increment_value, -pi/3, run_time=2)
        self.wait(1.2)
        self.play(t0.increment_value, -pi/2, run_time=2)
        text1 = TextMobject("其实只要固定一个向量，让另一个旋转，就能得到所有情况").to_edge(UP)
        self.wait(1.2)
        self.play(FadeIn(text1))
        text2 = TextMobject(r"所以我们把$|\vec{a}|$向量固定在$(0,1)$处，让$|\vec{b}|$旋转").to_edge(UP)
        self.wait(1.2)
        self.play(Transform(text1, text2))
        self.wait(1.2)
        self.play(t1.increment_value, -pi/6, run_time=0.5)
        text3 = TextMobject(r"把$|\vec{b}|$的起点移动到$|\vec{a}|$的末端").to_edge(UP)
        self.wait(1.2)
        self.play(Transform(text1, text3))
        vec_b.remove_updater(lambda x: x.become(self.get_vec(2*math.cos(t0.get_value()), 2*math.sin(t0.get_value())).set_color(RED_B)))
        vec_b_ = self.get_vec2(2 * math.cos(t0.get_value()), 2 * math.sin(t0.get_value()), self.CONFIG["graph_origin"]+RIGHT).set_color(RED_B)
        self.wait(1.2)
        self.play(ReplacementTransform(vec_b, vec_b_))
        vec_b_.add_updater(lambda x: x.become(self.get_vec2(2 * math.cos(t0.get_value()), 2 * math.sin(t0.get_value()), self.CONFIG["graph_origin"]+RIGHT).set_color(RED_B)))
        label_b.remove_updater(lambda a: a.become(TexMobject(r"|\vec{b}|").next_to(vec_b, RIGHT)))
        label_b.add_updater(lambda a: a.become(TexMobject(r"|\vec{b}|").next_to(vec_b_, RIGHT)))
        self.wait(1.2)
        self.play(t0.increment_value, -pi/2, run_time=1)
        self.wait(1.2)
        self.play(t0.increment_value, pi/4, run_time=1)
        self.wait(1.2)
        self.play(t0.increment_value, pi/6, run_time=1)
        text4 = TextMobject(r"显而易见，$|\vec{b}|$会画出一个圆").to_edge(UP)
        self.wait(1.2)
        self.play(Transform(text1, text4))
        circle = self.get_circle(1, 0, 2)
        self.wait(1.2)
        self.play(Write(circle))
        vec_a.remove_updater(lambda x: x.become(self.get_vec(math.cos(t1.get_value()), math.sin(t1.get_value())).set_color(BLUE)))
        self.wait(1.2)
        self.play(vec_a.set_opacity, 0.5)
        vec_a_ = self.get_vec2(math.cos(0), math.sin(0), self.CONFIG["graph_origin"]+RIGHT).set_color(BLUE)
        label_a.remove_updater(lambda a: a.become(TexMobject(r"|\vec{a}|").next_to(vec_a, RIGHT)))
        label_a.add_updater(lambda a: a.become(TexMobject(r"|\vec{a}|").next_to(vec_a_, RIGHT)))
        self.wait(1.2)
        self.play(FadeInFromPoint(vec_a_,point=Point(location=self.CONFIG["graph_origin"]+RIGHT)))
        text5 = TextMobject(r'把$\vec{a}$向右平移至$\vec{b}$起点处，可以找到$\vec{a}-\vec{b}$').to_edge(UP)
        self.wait(1.2)
        self.play(Transform(text1, text5))
        l1 = Line(self.CONFIG["graph_origin"],self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT, color=PURPLE_B)\
                .add_updater(
                    lambda x: x.become(Line(self.CONFIG["graph_origin"], self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT, color=PURPLE_B))
                )

        ll1 = TexMobject(r'A').next_to(Point(location=self.CONFIG["graph_origin"]+RIGHT*2), direction=UP)
        o = TexMobject(r'O').next_to(Point(location=self.CONFIG["graph_origin"]), direction=UP)
        self.wait(1.2)
        self.play(
            FadeIn(l1),FadeIn(ll1),FadeIn(o)
        )

        l2 = Line(self.CONFIG["graph_origin"]+2*RIGHT,self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT, color=GREEN_B)\
                .add_updater(
                    lambda x: x.become(Line(self.CONFIG["graph_origin"]+2*RIGHT, self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT, color=GREEN_B))
                )
        ll2 = TexMobject(r'B').move_to(self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT*1.5)
        ll2.add_updater(lambda x: x.become(TexMobject(r'B').move_to(self.CONFIG["graph_origin"]+2 * math.cos(t0.get_value())*RIGHT+2 * math.sin(t0.get_value())*UP+RIGHT*1.5)))
        self.wait(1.2)
        self.play(FadeIn(l2),FadeIn(ll2))

        self.wait(1.2)
        self.play(t0.increment_value, pi/6)
        self.wait(1.2)
        self.play(t0.increment_value, -pi/2)
        self.wait(1.2)
        self.play(t0.increment_value, -pi/3)

        text6 = TextMobject(r'显然,$|\vec{a}+\vec{b}|=|OA|,|\vec{a}-\vec{b}|=|AB|$').to_edge(UP)
        self.wait(1.2)
        self.play(Transform(text1,text6))

        self.wait(1.2)
        self.play(t0.set_value, 0)
        text7 = TextMobject(r'此时，取得最大值$2$')
        text8 = TextMobject(r'此时，取得最小值$-2$')
        self.wait(1.2)
        self.play(Write(text7))
        self.wait(1.2)
        self.play(t0.increment_value, pi)
        self.wait(1.2)
        self.play(Transform(text7, text8))
        self.wait(1.2)
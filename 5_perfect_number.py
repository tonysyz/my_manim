from manimlib.imports import *

class OpeningScene(Scene):
    def construct(self):
        text0 = TextMobject(r'Perfect Number\\完全数')
        self.play(Write(text0))
        self.wait()

class Illustration(Scene):
    def showtextthenfade(self, textmobject, time):
        self.play(Write(textmobject))
        self.wait(duration=time)
        self.play(FadeOut(textmobject))

    def construct(self):
        text0 = TextMobject(r'什么是完全数？')
        self.showtextthenfade(text0, 3)
        text1 = TextMobject(r'完全数是它所有的真因子\\（即除了自身以外的约数）\\恰好等于其自身的数')
        self.showtextthenfade(text1, 3)
        # '''
        text2 = TextMobject(r'比如说：\\ $6 = 1 \times 2 \times 3$ \\ $6 = 1 + 2 + 3$')
        self.showtextthenfade(text2, 3)
        text3 = TextMobject(r'28有因数：', r'1', r', ', r'2',r',', r'4', r', ', r'7', r', ', r'14')
        text4 = TexMobject(r'28=', r'1', r'+ ', r'2', r'+ ', r'4', r'+ ', r'7', r'+ ', r'14').next_to(text3, DOWN)
        self.play(Write(text3))
        self.play(
            Write(text4[0]), Write(text4[2]), Write(text4[4]), Write(text4[6]), Write(text4[8]),
            ReplacementTransform(text3[1], text4[1]),
            ReplacementTransform(text3[3], text4[3]),
            ReplacementTransform(text3[5], text4[5]),
            ReplacementTransform(text3[7], text4[7]),
            ReplacementTransform(text3[9], text4[9]),
        )
        self.play(FadeOut(text3), FadeOut(text4))
        text5 = TextMobject(r'这种把除自身之外的各因数相加\\的计算也叫“等额和”(aliquot sum)')
        text6 = TextMobject(r'也可以用下面的方程来表示:\\ $\sigma _1 (n)=2n$($\sigma$ 函数指把自身所有因数相加)')
        self.showtextthenfade(text5, 3)
        self.showtextthenfade(text6, 3)
        # '''

class PerfectNumbers(Illustration):
    def construct(self):
        text0 = TextMobject(r'那么，除了6和28，还有哪些已经发现的完全数呢？')
        self.showtextthenfade(text0, 3)
        text1 = TextMobject(r'6\\28\\496\\8128\\33550336\\8589869056\\137438691328\\2305843008139952128\\',
        r'2658455991569831744654692615953842176\\191561942608236107294793378084303638130997321548169216\\',
        r'....')
        self.showtextthenfade(text1, 3)
        text2 = TextMobject(r'这是我在OESI(Sequence A000396)上找到的10个数，\\最后一个已经相当大了.')
        self.showtextthenfade(text2, 3)
        text3 = TextMobject('你可以倒回去看一看有没有发现这些数字有什么规律')
        self.showtextthenfade(text3, 1)

class Patten(Illustration):

    def construct(self):
        text0 = TextMobject(r'再看一遍前面的数列，注意数字的末尾')
        self.showtextthenfade(text0, 3)
        text1 = TextMobject(r'6\\',r'28\\',r'49',r'6\\',r'81', r'28\\',r'3355033', r'6\\',r'858986905', r'6\\',r'1374386913', r'28\\',r'23058430081399521', r'28\\',
        r'265845599156983174465469261595384217', r'6\\',r'19156194260823610729479337808430363813099732154816921', r'6\\',
        r'....')
        text_6 = TextMobject(r'6')
        text_28 = TextMobject(r'28')
        colorful = [text1[0], text1[1], text1[3], text1[5], text1[7], text1[9], text1[11], text1[13], text1[15], text1[17]]
        for each in colorful:
            each.set_color(BLUE)
        self.play(Write(text1), run_time=2)
        self.wait(2)
        self.play(FadeOut(text1))
        text2 = TextMobject(r'所以发现了吗，至今发现的完全数都是以6或28结尾的！')
        text3 = TextMobject(r'更有趣的是，它们除1之外的所有因数的倒数和都等于1')
        text4 = TextMobject(r'6-->$1 = {{1}\over{2}} + {{1}\over{3}} + {{1}\over{6}}$')
        text5 = TextMobject(r'28-->$1 = {{1}\over {2}}+{{1}\over {4}}+{{1}\over {7}} + {{1}\over {14}}+{{1}\over {28}}$')
        text6 = TextMobject(r'496-->$1 = {{1}\over {2}}+{{1}\over {4}}+{{1}\over {8}}+{{1}\over {16}}+{{1}\over {31}}+{{1}\over {62}}+{{1}\over {124}}+{{1}\over {248}}+{{1}\over {496}}$\\....')
        self.showtextthenfade(text2, 3)
        self.showtextthenfade(text3, 3)
        self.play(
            Write(text4.to_edge(UP)),
            Write(text5.next_to(text4, DOWN)),
            Write(text6.next_to(text5, DOWN)),
        )
        self.play(Write(TextMobject(r'除此之外，它还有很多神奇的性质').next_to(text6, DOWN)))

class TriangularNumbers(Illustration):
    def construct(self):
        text0 = TextMobject(r'1.每一个完全数都是三角形数')
        text1 = TextMobject(r'什么是三角形数？').next_to(text0, DOWN)
        self.play(Write(text0))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(
            text1.to_corner, UL,
            FadeOutAndShiftDown(text0)
        )
        text2 = TexMobject(r'1').move_to(np.array([0,-3,0]))
        text3 = TexMobject(r'3').move_to(np.array([0,-3,0]))
        text4 = TexMobject(r'6').move_to(np.array([0,-3,0]))
        text5 = TexMobject(r'10').move_to(np.array([0,-3,0]))
        text6 = TexMobject(r'....').move_to(np.array([0,-3,0]))
        self.play(Write(text2))
        c1 = Circle().shift(UP).set_color(BLUE).set_fill(opacity=100).scale(0.3)
        self.play(ShowCreation(c1))
        self.wait(2)
        c2 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c1, DOWN, buff=SMALL_BUFF).shift(LEFT*0.5)
        c3 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c1, DOWN, buff=SMALL_BUFF).shift(RIGHT*0.5)
        self.play(
            ShowCreation(c2),
            ShowCreation(c3),
            Transform(text2, text3),
        )
        self.wait(2)
        c4 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c3, DOWN, buff=SMALL_BUFF).shift(LEFT*0.5)
        c5 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c3, DOWN, buff=SMALL_BUFF).shift(RIGHT*0.5)
        c6 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c2, DOWN, buff=SMALL_BUFF).shift(LEFT*0.5)
        self.play(
            ShowCreation(c4),
            ShowCreation(c5),
            ShowCreation(c6),
            Transform(text2, text4)
        )
        self.wait(2)
        c7 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c6, DOWN, buff=SMALL_BUFF).shift(LEFT*0.5)
        c8 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c6, DOWN, buff=SMALL_BUFF).shift(RIGHT*0.5)
        c9 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c5, DOWN, buff=SMALL_BUFF).shift(LEFT*0.5)
        c10 = Circle().set_color(BLUE).set_fill(opacity=100).scale(0.3).next_to(c5, DOWN, buff=SMALL_BUFF).shift(RIGHT*0.5)
        self.play(
            ShowCreation(c7),
            ShowCreation(c8),
            ShowCreation(c9),
            ShowCreation(c10),
            Transform(text2, text5)
        )
        self.wait(2)
        text7 = TexMobject(r'....').next_to(text6, UP*2).shift(UP*0.5)
        self.play(ShowCreation(text7))
        self.play(Transform(text2, text6))
        self.wait(3)
        self.play(
            FadeOut(text2),
            FadeOut(text7),
            FadeOut(VGroup(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10))
        )
        text8 = TextMobject(r'6=1+2+3\\28=1+2+3+....+6+7\\496=1+2+3+...+30+31\\8128=1+2+3+...+126+127\\33550336=1+2+3+...+126+127\\....')
        self.play(Write(text8))

class OtherPattens(Illustration):
    def construct(self):
        text0 = TextMobject(r'2.除了6以外的完全数，都可以表示成连续立方数之和')
        self.showtextthenfade(text0, 2)
        text1 = TextMobject(r'$28=1^3+3^3$\\$496=1^3+3^3+5^3$\\$8128=1^3+3^3+...+15^3$\\$33550336=1^3+3^3+...+127^3$\\$...$')
        self.play(Write(text1))
        self.play(FadeOut(text1))
        text2 = TextMobject(r'3.都可以表示成2的连续正整数次幂的和')
        text3 = TextMobject(r'$6=2^1+2^2$\\$28=2^2+2^3+2^4$\\$496=2^4+2^5+...+2^8$\\$8128=2^6+2^7+...+{2^{11}}+{2^{12}}$\\$33550336={2^{12}}+{2^{13}}+...+{2^{23}}+{2^{24}}$\\$...$')
        self.showtextthenfade(text2, 2)
        self.showtextthenfade(text3, 3)
        text4 = TextMobject(r'4.由于第三条，它们用二进制表示起来就是这样的')
        text5 = TextMobject(r'${6_{10}}=110_2$\\${28_{10}}=11100_2$\\${496_{10}}=111110000_2$\\${8128_{10}}=1111111000000_2$\\...')
        self.showtextthenfade(text4, 2)
        self.showtextthenfade(text5, 3)
        text5 = TextMobject(r'5.自己体会吧')
        text6 = TextMobject(r'$2$',r'$8$').scale(2)
        self.play(Write(text6))
        self.wait()
        text7 = TextMobject(r'2',r'+',r'8',r'=',r'1',r'0').scale(2)
        self.play(
            Transform(text6[0], text7[0]),
            Transform(text6[1], text7[2]),
            Write(text7[1]),
            Write(text7[3]),
        )
        self.wait()
        self.play(
            Write(text7[4]),
            Write(text7[5])
        )
        self.wait()
        self.play(
            FadeOut(text6),
            FadeOut(text7[1]),
            FadeOut(text7[3]),
        )
        self.wait()
        text8 = TextMobject(r'1',r'+',r'0',r'=',r'1').scale(2)
        self.play(
            text7[4].move_to, text8[0].get_center(),
            text7[5].move_to, text8[2].get_center(),
            Write(text8[1]),
            Write(text8[3])
        )
        self.wait()
        self.play(Write(text8[4]))
        self.wait()
        self.play(
            FadeOut(VGroup(text8,text7[4],text7[5]))
        )
        self.wait()
        text9 = TextMobject(r'4',r'9',r'6').scale(2)
        text10 = TextMobject(r'4',r'+',r'9',r'+',r'6',r'=',r'1',r'9').scale(2)
        text11 = TextMobject(r'1',r'+',r'9',r'=',r'1',r'0').scale(2)
        text12 = TextMobject(r'1',r'+',r'0',r'=',r'1').scale(2)
        self.play(ShowCreation(text9))
        self.wait()
        self.play(
            Transform(text9[0],text10[0]),
            Transform(text9[1],text10[2]),
            Transform(text9[2],text10[4]),
            Write(VGroup(text10[1],text10[3],text10[5],text10[6],text10[7]))
        )
        self.wait()
        self.play(
            FadeOut(text9),
            FadeOut(VGroup(text10[1],text10[3],text10[5])),
            Transform(text10[6],text11[0]),
            Transform(text10[7],text11[2]),
        )
        self.wait()
        self.play(
            Write(VGroup(text11[1],text11[3],text11[4],text11[5]))
        )
        self.wait()
        self.play(
            FadeOut(VGroup(text10[6],text10[7])),
            text11[4].move_to,text10[6].get_center(),
            text11[5].move_to,text10[7].get_center(),
            Write(text12[4])
        )
        self.wait()

class HowToFind(Illustration):
    def construct(self):
        text0 = TextMobject(r'科学家是如何寻找完全数的？\\它们是否有什么规律？')
        self.showtextthenfade(text0, 2)
        img = ImageMobject(r'.\Imgs\Euklid-von-Alexandria.jpg').scale(3).to_edge(LEFT)
        text2 = TextMobject(r'Eucid von Alexandria').next_to(img,DOWN, aligned_edge=LEFT)
        self.play(FadeIn(img))
        self.play(Write(text2))
        text1 = TextMobject(r'这就要从Eucid这个人说起').next_to(img, RIGHT)
        self.play(
            Write(text1),
            text1.shift, UP*3
        )
        text3 = TextMobject(r'Eucid-Eular Theorem:\\${2^{p-1}}M_p$ 是完全数($p$为质数)').next_to(text1,DOWN)
        self.play(Write(text3), run_time=2)
        self.wait()
        text4 = TextMobject(r'$M_p$是著名的梅森素数\\(Mersenne prime)\\${M_p}={2^p}-1$($p$为质数)').next_to(text3,DOWN)
        self.play(Write(text4), run_time=2)
        self.wait()
        text5 = TextMobject(r'下面放上Euler 的证明：\\已经给定:\\$\sigma (ab)=\sigma (a)\cdot \sigma (b)$(积性函数)').next_to(text4, DOWN)
        text6 = TextMobject(r'$\sigma (2^{p-1}({2^p}-1))=\sigma (2^{p-1}) \sigma ({2^p}-1)$\\',r'$=(2^{p-1})(2^p)$\\',r'$=2(2^{p-1})({2^p}-1)$').next_to(text4, DOWN).shift(RIGHT)
        text6[1].next_to(text6[0], DOWN, aligned_edge=LEFT)
        text6[2].next_to(text6[1], DOWN, aligned_edge=LEFT)
        text7 = TextMobject(r'Q.E.D.').next_to(text6, DOWN, aligned_edge=LEFT)
        self.showtextthenfade(text5, 2)
        self.play(Write(text6), run_time=2)
        self.wait()
        self.play(Write(text7))
        self.play(
            FadeOut(VGroup(text1,text2 , text3, text4, text6, text7))
        )
        self.play(FadeOut(img))
        text8 = TextMobject(r'验证一下：\\',r'$p=2, \sigma (2)=6$\\',r'$p=3, \sigma (3)=28$\\',r'$p=4, \sigma (4)=496$\\',r'$p=5, \sigma (5)=8128$\\',r'...')
        text8[1].next_to(text8[0], DOWN, aligned_edge=LEFT)
        text8[2].next_to(text8[1], DOWN, aligned_edge=LEFT)
        text8[3].next_to(text8[2], DOWN, aligned_edge=LEFT)
        text8[4].next_to(text8[3], DOWN, aligned_edge=LEFT)
        text8[5].next_to(text8[4], DOWN, aligned_edge=LEFT)
        self.showtextthenfade(text8,3)
        text9 = TextMobject(r'但是，这样只证明了\\“$2^{p-1}(2^{p}-1)$在p为质数的情况下是完全数"，\\并不囊括所有完全数')
        text10 = TextMobject(r'真正的寻找还需要大量的计算量和高性能的计算机...')
        self.showtextthenfade(text9, 3)
        self.showtextthenfade(text10, 3)

class EndingScene(Scene):
    def construct(self):
        text = TextMobject(r'Tools:\\Python3.7.1(Anaconda)\\manim(by 3Blue1Brown)\\Pr\\BGM:亚麻色头发的少女 By Claude Debussy\\Reference:\\Wikipedia-Perfect Number')
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))
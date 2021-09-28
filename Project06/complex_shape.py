"""Linn Cao Nguyen Phuong
   Oct 6, 2020
   Section A
   Lab 4: Unique turtles
   CS151
"""


import graphicsPlus as gr


def draw(objlist, win):
    """Draws item into window
    """
    for item in objlist:
        item.draw(win)


def circle_init(x, y, scale):
    """Draws circle at desired location and scale
    """
    shapes = []
    c = gr.Circle(gr.Point(x, y), 20*scale)
    c.setFill(gr.color_rgb(220, 20, 60))
    c.setOutline(gr.color_rgb(255, 255, 240))
    c.setWidth(1.5*scale)
    shapes.append(c)
    return shapes


def ray1_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x + 20*scale, y), gr.Point(x - 45*scale, y + 500*scale), gr.Point(x + 190*scale, y + 500*scale), gr.Point(x + 60*scale, y))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def ray2_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x - 5*scale, y), gr.Point(x + 220*scale, y + 500*scale), gr.Point(x + 250*scale, y - 30*scale), gr.Point(x, y))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def ray3_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x, y), gr.Point(x + 300*scale, y - 95*scale), gr.Point(x + 10*scale, y - 200*scale), gr.Point(x - 30*scale, y))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def ray4_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x, y), gr.Point(x, y - 200*scale), gr.Point(x - 200*scale, y - 200*scale), gr.Point(x - 50*scale, y))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def ray5_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x, y), gr.Point(x - 500*scale, y - 300*scale), gr.Point(x - 500*scale, y - 10*scale), gr.Point(x, y + 30*scale))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def ray6_init(x, y, scale):
    """Draws a Polygon as a sun ray
    """
    shapes = []
    r = gr.Polygon(gr.Point(x, y), gr.Point(x - 500*scale, y + 10*scale), gr.Point(x - 500*scale, y + 500*scale), gr.Point(x - 190*scale, y + 500*scale), gr.Point(x - 10*scale, y))
    r.setFill(gr.color_rgb(220, 20, 60))
    r.setOutline(gr.color_rgb(220, 20, 60))
    shapes.append(r)
    return shapes


def symbol_init(x, y, scale):
    """Draws socialism symbol
    """
    shapes =[]
    l1 = gr.Circle(gr.Point(x, y), 50*scale)
    l1.setFill(gr.color_rgb(255, 215, 0))
    l1.setOutline(gr.color_rgb(255, 215, 0))
    l2 = gr.Circle(gr.Point(x - 10*scale, y - 10*scale), 50*scale)
    l2.setFill(gr.color_rgb(220, 20, 60))
    l2.setOutline(gr.color_rgb(220, 20, 60))
    l3 = gr.Polygon(gr.Point(x - 48*scale, y + 42*scale), gr.Point(x - 38*scale, y + 32*scale), gr.Point(x - 30*scale, y + 40*scale), gr.Point(x - 40*scale, y + 50*scale))
    l3.setFill(gr.color_rgb(255, 215, 0))
    l3.setOutline(gr.color_rgb(255, 215, 0))
    b1 = gr.Polygon(gr.Point(x - 30*scale, y - 15*scale), gr.Point(x - 10*scale, y - 35*scale), gr.Point(x + 3*scale, y - 20*scale), gr.Point(x - 17*scale, y))
    b1.setFill(gr.color_rgb(255, 215, 0))
    b1.setOutline(gr.color_rgb(255, 215, 0))
    b2 = gr.Polygon(gr.Point(x - 12*scale, y - 5*scale), gr.Point(x - 2*scale, y - 15*scale), gr.Point(x + 45*scale, y + 40*scale), gr.Point(x + 35*scale, y + 50*scale))
    b2.setFill(gr.color_rgb(255, 215, 0))
    b2.setOutline(gr.color_rgb(255, 215, 0))
    shapes.append(l1)
    shapes.append(l2)
    shapes.append(l3)
    shapes.append(b1)
    shapes.append(b2)
    return shapes


def sun_init(x, y, scale):
    """Draws the sun in the background by putting several calls
       to circle, symbol and ray functions at desired locations and scales
    """
    shapes = []
    c = circle_init(x + 450*scale, y + 180*scale, 3.5*scale)
    sl = symbol_init(x + 450*scale, y + 180*scale, 1*scale)
    r1 = ray1_init(x + 415*scale, y + 200*scale, scale)
    r2 = ray2_init(x + 480*scale, y + 170*scale, scale)
    r3 = ray3_init(x + 500*scale, y + 150*scale, scale)
    r4 = ray4_init(x + 450*scale, y + 135*scale, scale)
    r5 = ray5_init(x + 420*scale, y + 160*scale, scale)
    r6 = ray6_init(x + 430*scale, y + 210*scale, scale)
    shapes.append(r1)
    shapes.append(r2)
    shapes.append(r3)
    shapes.append(r4)
    shapes.append(r5)
    shapes.append(r6)
    shapes.append(c)
    shapes.append(sl)
    return shapes


def voval_init(x, y, scale, r, g, b):
    """Draws an oval whose vertical arch is greater than horizontal arch
       at desired location, scale and fills with desired RGB color
    """
    shapes = []
    vo = gr.Oval(gr.Point(x, y), gr.Point(x + 40*scale, y + 50*scale))
    vo.setFill(gr.color_rgb(r, g, b))
    vo.setWidth(scale)
    shapes.append(vo)
    return shapes


def hoval_init(x, y, scale, r1, g1, b1, r2, g2, b2):
    """Draws an oval whose horizontal arch is greater than vertical arch
       at desired location, scale and fills with desired RGB color
    """
    shapes = []
    ho = gr.Oval(gr.Point(x, y), gr.Point(x + 5*scale, y + 3*scale))
    ho.setFill(gr.color_rgb(r1, g1, b1))
    ho.setOutline(gr.color_rgb(r2, g2, b2))
    ho.setWidth(6)
    shapes.append(ho)
    return shapes


def hay_init(x, y, scale):
    """Draws several clones of an original line 
       at desired locations and scales
    """
    shapes = []
    h1 = gr.Line(gr.Point(x, y), gr.Point(x + 290*scale, y + 300*scale))
    h1.setWidth(6*scale)
    h1.setOutline(gr.color_rgb(255, 215, 0))
    h2 = h1.clone()
    h2.move(50*scale, -30*scale)
    h3 = h2.clone()
    h3.move(60*scale, -20*scale)
    h4 = h3.clone()
    h4.move(70*scale, -15*scale)
    h5 = h4.clone()
    h5.move(75*scale, -10*scale)
    h6 = h5.clone()
    h6.move(75*scale, -10*scale)
    h7 = h6.clone()
    h7.move(120*scale, 40*scale)
    h8 = h1.clone()
    h8.move(-60*scale, 20*scale)
    shapes.append(h1)
    shapes.append(h2)
    shapes.append(h3)
    shapes.append(h4)
    shapes.append(h5)
    shapes.append(h6)
    shapes.append(h7)
    shapes.append(h8)
    return shapes


def haystack_init(x, y, scale):
    """Draws a haystack by calling hoval and hay_init functions at desired locations and scales
    """
    shapes = []
    h1 = hoval_init(x + 150*scale, y + 390*scale, 200*scale, 255, 255, 240, 255, 215, 0)
    h2 = hay_init(x + 300*scale, y + 500*scale, 1)
    shapes.append(h1)
    shapes.append(h2)
    return shapes


def neck_init(x, y, scale):
    """Draws a Polygon as the neck at desired location and scale
    """
    shapes = []
    n = gr.Polygon(gr.Point(x, y), gr.Point(x - 3*scale, y + 20*scale), gr.Point(x + 11*scale, y + 30*scale), gr.Point(x + 25*scale, y + 20*scale), gr.Point(x + 22*scale, y))
    n.setFill(gr.color_rgb(255, 255, 240))
    n.setWidth(1.5*scale)
    shapes.append(n)
    return shapes


def body_init(x, y, scale):
    """Draws a Polygon as the body at desired location and scale
    """
    shapes = []
    b = gr.Polygon(gr.Point(x, y), gr.Point(x + 100*scale, y + 15*scale), gr.Point(x + 105*scale, y + 200*scale), gr.Point(x - 120*scale, y + 200*scale), gr.Point(x - 110*scale, y + 15*scale))
    b.setFill(gr.color_rgb(255, 255, 240))
    b.setWidth(2.5*scale)
    shapes.append(b)
    return shapes


def mouth_init(x, y, scale):
    """Draws 2 lines as the mouth at desired location and scale
    """
    shapes = []
    m1 = gr.Line(gr.Point(x, y), gr.Point(x + 10*scale, y + 5*scale))
    m1.setWidth(2*scale)
    m2 = gr.Line(gr.Point(x + 10*scale, y + 5*scale), gr.Point(x + 20*scale, y))
    m2.setWidth(2*scale)
    shapes.append(m1)
    shapes.append(m2)
    return shapes


def tool_init(x, y, scale):
    """Draws 1st human's tool by using 2 rectangles at desired location and scale
    """
    shapes = []
    upper = gr.Rectangle(gr.Point(x, y), gr.Point(x + 20*scale, y + 15*scale))
    upper.setFill(gr.color_rgb(255, 255, 240))
    upper.setWidth(3*scale)
    lower = gr.Rectangle(gr.Point(x + 8*scale, y + 15*scale), gr.Point(x + 13*scale, y + 100*scale))
    lower.setFill(gr.color_rgb(0, 0, 0))
    shapes.append(upper)
    shapes.append(lower)
    return shapes


def human1_init(x, y, scale):
    """Draws 1st human with tool at desired location and scale
    """
    shapes = []
    n = neck_init(x + 176*scale, y + 468*scale, 2.2*scale)
    f = voval_init(x + 150*scale, y + 350*scale, 2.5*scale, 255, 255, 240)
    b = body_init(x + 200*scale, y + 500*scale, 1.2*scale)
    e1 = hoval_init(x + 165*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    e2 = hoval_init(x + 218*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    m = mouth_init(x + 190*scale, y + 440*scale, scale)
    t = tool_init(x + 60*scale, y + 520*scale, 4*scale)
    shapes.append(b)
    shapes.append(n)
    shapes.append(f)
    shapes.append(e1)
    shapes.append(e2)
    shapes.append(m)
    shapes.append(t)
    return shapes


def bangs_init(x, y, scale):
    """Draws 2nd human's bangs by using a rectangle with the same color as the skin
       over a black oval at desired location and scale
    """
    shapes = []
    bangs1 = gr.Oval(gr.Point(x, y), gr.Point(x + 40*scale, y + 30*scale))
    bangs1.setFill(gr.color_rgb(0, 0, 0))
    bangs1.setWidth(scale)
    bangs2 = gr.Rectangle(gr.Point(x + 1.5*scale, y + 13*scale), gr.Point(x + 39*scale, y + 32*scale))
    bangs2.setFill(gr.color_rgb(255, 255, 240))
    bangs2.setOutline(gr.color_rgb(255, 255, 240))
    shapes.append(bangs1)
    shapes.append(bangs2)
    return shapes


def human2_init(x, y, scale):
    """Draws 2nd human with a black oval behind the head as hair and bangs
       at desired location and scale
    """
    shapes = []
    n = neck_init(x + 176*scale, y + 468*scale, 2.2*scale)
    h1 = voval_init(x + 135*scale, y + 348*scale, 3.2*scale, 0, 0, 0)
    f = voval_init(x + 150*scale, y + 350*scale, 2.5*scale, 255, 255, 240)
    b = body_init(x + 200*scale, y + 500*scale, 1.2*scale)
    h2 = bangs_init(x + 149*scale, y + 350*scale, 2.5*scale)
    e1 = hoval_init(x + 165*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    e2 = hoval_init(x + 218*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    m = mouth_init(x + 190*scale, y + 440*scale, scale)
    shapes.append(b)
    shapes.append(h1)
    shapes.append(n)
    shapes.append(f)
    shapes.append(h2)
    shapes.append(e1)
    shapes.append(e2)
    shapes.append(m)
    return shapes


def gun_init(x, y, scale):
    """Draws 3rd human's gun by using two rectangles
       at desired location and scale
    """
    shapes = []
    g1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 5*scale, y + 200*scale))
    g1.setFill(gr.color_rgb(0, 0, 0))
    g2 = gr.Rectangle(gr.Point(x + 5*scale, y + 40*scale), gr.Point(x + 15*scale, y + 200*scale))
    g2.setFill(gr.color_rgb(0, 0, 0))
    shapes.append(g1)
    shapes.append(g2)
    return shapes


def human3_init(x, y, scale):
    """Draws 3rd human with gun at desired location and scale
    """
    shapes = []
    n = neck_init(x + 176*scale, y + 468*scale, 2.2*scale)
    f = voval_init(x + 150*scale, y + 350*scale, 2.5*scale, 255, 255, 240)
    b = body_init(x + 200*scale, y + 500*scale, 1.2*scale)
    e1 = hoval_init(x + 165*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    e2 = hoval_init(x + 218*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    m = mouth_init(x + 190*scale, y + 440*scale, scale)
    g = gun_init(x + 270*scale, y + 450*scale, 2*scale)
    shapes.append(b)
    shapes.append(n)
    shapes.append(f)
    shapes.append(e1)
    shapes.append(e2)
    shapes.append(m)
    shapes.append(g)
    return shapes


def glasses_init(x, y, scale):
    """Draws 4th human's glasses by using 2 rectangles, 
       the second is the first one's clone, at desired location and scale
    """
    shapes = []
    g1 = gr.Rectangle(gr.Point(x, y), gr.Point(x + 10*scale, y + 6*scale))
    g1.setFill(gr.color_rgb(255, 255, 240))
    g1.setOutline(gr.color_rgb(0, 0, 0))
    g1.setWidth(scale)
    g2 = g1.clone()
    g2.move(12*scale, 0)
    shapes.append(g1)
    shapes.append(g2)
    return shapes


def human4_init(x, y, scale):
    """Draws 4th human with glasses at desired location and scale
    """
    shapes = []
    n = neck_init(x + 176*scale, y + 468*scale, 2.2*scale)
    f = voval_init(x + 150*scale, y + 350*scale, 2.5*scale, 255, 255, 240)
    b = body_init(x + 200*scale, y + 500*scale, 1.2*scale)
    e1 = hoval_init(x + 165*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    e2 = hoval_init(x + 218*scale, y + 395*scale, 3.5*scale, 0, 0, 0, 0, 0, 0)
    m = mouth_init(x + 190*scale, y + 440*scale, scale)
    g = glasses_init(x + 157*scale, y + 390*scale, 4*scale)
    shapes.append(b)
    shapes.append(n)
    shapes.append(f)
    shapes.append(g)
    shapes.append(e1)
    shapes.append(e2)
    shapes.append(m)
    return shapes
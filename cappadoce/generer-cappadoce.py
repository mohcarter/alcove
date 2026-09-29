import random, math
import gen as g
random.seed(11)
OUT='../v3/cap/'
def chimney(x,base,h,w,col,rim,cap=True):
    h=h*.72; w=w*1.5
    top=base-h
    d=f'M{x-w/2},{base} C{x-w*.28},{base-h*.45} {x-w*.16},{top+h*.12} {x-w*.2},{top+h*.06} L{x+w*.2},{top+h*.06} C{x+w*.16},{top+h*.12} {x+w*.28},{base-h*.45} {x+w/2},{base} Z'
    s=f'<path d="{d}" fill="{col}"/>'
    if cap:
        s+=f'<path d="M{x-w*.34},{top+h*.09} Q{x},{top-h*.07} {x+w*.34},{top+h*.09} Q{x+w*.2},{top+h*.16} {x},{top+h*.15} Q{x-w*.2},{top+h*.16} {x-w*.34},{top+h*.09} Z" fill="{col}"/>'
    s+=f'<path d="M{x+w*.2},{top+h*.08} C{x+w*.16},{top+h*.14} {x+w*.28},{base-h*.45} {x+w/2},{base}" fill="none" stroke="{rim}" stroke-width="2" opacity=".55"/>'
    return s
def valley():
    W,H=1600,1000
    b=f'<rect width="{W}" height="{H}" fill="url(#sk)"/>'
    b+='<circle cx="800" cy="560" r="520" fill="url(#glow)" opacity=".85"/>'
    for i in range(40):
        b+=f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,260):.0f}" r="{random.uniform(.6,1.4):.1f}" fill="#F1E8D6" opacity="{random.uniform(.2,.6):.2f}"/>'
    for (x,y,r,c) in ((330,250,20,'#C98A5A'),(1180,190,26,'#B9765A'),(1330,330,15,'#D9A56A')):
        b+=f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*1.15}" fill="{c}" opacity=".75"/><rect x="{x-3}" y="{y+r*1.1}" width="6" height="{r*.5}" fill="#2A1E18" opacity=".6"/>'
    b+='<path d="M0,640 L140,560 L300,610 L460,520 L640,600 L820,540 L1000,610 L1200,530 L1380,600 L1600,550 L1600,1000 L0,1000 Z" fill="#3A2C2A" opacity=".8"/>'
    b+='<path d="M0,720 Q200,650 420,700 T860,690 T1300,700 T1600,680 L1600,1000 L0,1000 Z" fill="#2A2020"/>'
    for x,h,w in ((250,260,90),(430,190,70),(1180,230,80),(1360,300,100),(1500,170,60)):
        b+=chimney(x,760,h,w,'#1F1717','#C9A56A')
    for x,h,w in ((560,330,120),(780,470,150),(990,360,130)):
        b+=chimney(x,860,h,w,'#171112','#E2C48E')
    b+='<path d="M0,860 Q300,800 620,850 T1200,840 T1600,820 L1600,1000 L0,1000 Z" fill="#0F0C0C"/>'
    for x,h,w in ((120,300,110),(1470,380,130)):
        b+=chimney(x,1010,h,w,'#0A0808','#8A6A44')
    b+=g.grain(W,H)
    return g.svg(W,H,b,g.sky(W,H,'#0B0C16','#4A3A46','#D79A66','sk'))
def sacred():
    W,H=900,1125
    b=f'<rect width="{W}" height="{H}" fill="url(#sk)"/>'
    b+='<path d="M0,420 Q120,300 250,340 Q360,240 470,330 Q620,260 760,350 Q840,320 900,380 L900,1125 L0,1125 Z" fill="#2B2220"/>'
    b+='<rect x="130" y="470" width="640" height="655" fill="#5A4636"/>'
    for r in range(11):
        for c in range(9):
            if random.random()<.55:
                b+=f'<rect x="{130+c*71+(r%2)*30}" y="{470+r*60}" width="{random.randint(50,68)}" height="{50}" fill="#{random.choice(["6A5342","5E4A3A","705845"])}" opacity=".5"/>'
    b+='<rect x="110" y="458" width="680" height="16" fill="#3E3025"/>'
    for i in range(6):
        x=170+i*105
        b+=g.win(x,560,54,120,lit=(i in (1,3,4)),glowr=110)
    for i,x in enumerate((215,380,545)):
        b+=g.win(x,790,60,150,lit=(i==1),glowr=120)
    b+='<circle cx="450" cy="1030" r="220" fill="url(#glow)"/>'
    b+='<path d="M380,1125 L380,1000 A70,70 0 0 1 520,1000 L520,1125 Z" fill="url(#lit)"/>'
    b+='<path d="M60,1125 L60,980 A32,32 0 0 1 124,980 L124,1125 Z" fill="#231A15"/>'
    b+=g.grain(W,H)
    return g.svg(W,H,b,g.sky(W,H,'#0C0D18','#3A2F3E','#A9714E','sk'))
def gamirasu():
    W,H=900,1125
    b=f'<rect width="{W}" height="{H}" fill="url(#sk)"/>'
    b+='<path d="M-20,1125 L-20,300 Q60,180 200,220 Q300,120 430,170 Q560,90 700,180 Q820,150 920,260 L920,1125 Z" fill="#4A3A34"/>'
    for i in range(30):
        y=250+i*30; b+=f'<path d="M{random.randint(0,300)},{y} Q{random.randint(300,600)},{y-14} {random.randint(600,900)},{y+random.randint(-6,10)}" fill="none" stroke="#2E2320" stroke-width="{random.uniform(1,3):.1f}" opacity=".5"/>'
    for (x,y,w,h,lit) in ((110,380,70,110,1),(300,330,90,140,0),(560,400,70,105,1),(720,340,80,130,0),(170,600,90,130,0),(420,560,110,170,1),(680,610,80,120,1),(90,830,80,120,1),(300,800,90,140,0),(560,840,80,120,0),(740,820,70,110,1)):
        b+=g.win(x,y,w,h,lit=bool(lit),glowr=120,frame='#2A201B',mull=False)
    b+='<path d="M0,760 Q300,730 600,760 T900,740 L900,780 L0,790 Z" fill="#231A17"/>'
    b+='<path d="M0,960 L900,930 L900,1125 L0,1125 Z" fill="#160F0D"/>'
    for k in range(8):
        b+=f'<rect x="{80+k*20}" y="{940-k*10}" width="{300-k*20}" height="12" fill="#2A1E18" opacity="{.9-k*.08:.2f}"/>'
    b+='<circle cx="620" cy="1000" r="200" fill="url(#glow)" opacity=".8"/>'
    b+='<path d="M560,1125 L560,990 A60,60 0 0 1 680,990 L680,1125 Z" fill="url(#lit)"/>'
    b+=g.grain(W,H)
    return g.svg(W,H,b,g.sky(W,H,'#0D0E19','#3B2F3C','#B57C55','sk'))
for n,f in (('valley',valley),('sacred',sacred),('gamirasu',gamirasu)):
    open(OUT+n+'.svg','w').write(f())

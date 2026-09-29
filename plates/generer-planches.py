import random, math
random.seed(7)
OUT='plates/'
def svg(w,h,body,defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"><defs>{COMMON}{defs}</defs>{body}</svg>'
COMMON='''
<radialGradient id="glow"><stop offset="0" stop-color="#F1DDAE" stop-opacity=".55"/><stop offset=".4" stop-color="#C9A56A" stop-opacity=".18"/><stop offset="1" stop-color="#C9A56A" stop-opacity="0"/></radialGradient>
<linearGradient id="lit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4E2B8"/><stop offset=".6" stop-color="#D9B77A"/><stop offset="1" stop-color="#A9844A"/></linearGradient>
<linearGradient id="dim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1C2230"/><stop offset="1" stop-color="#0C0D10"/></linearGradient>
<linearGradient id="vign" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .8  0 0 0 0 .75  0 0 0 0 .65  0 0 0 .07 0"/></filter>
'''
def grain(w,h): return f'<rect width="{w}" height="{h}" filter="url(#grain)"/><rect width="{w}" height="{h}" fill="url(#vign)"/>'
def win(x,y,w,h,lit=False,arch=True,frame='#3B3731',mull=True,glowr=None):
    s=''
    if lit:
        r=glowr or w*2.2
        s+=f'<circle cx="{x+w/2}" cy="{y+h/2}" r="{r}" fill="url(#glow)"/>'
    fill='url(#lit)' if lit else 'url(#dim)'
    if arch:
        d=f'M{x},{y+h} L{x},{y+w/2} A{w/2},{w/2} 0 0 1 {x+w},{y+w/2} L{x+w},{y+h} Z'
    else:
        d=f'M{x},{y} h{w} v{h} h{-w} Z'
    s+=f'<path d="{d}" fill="{fill}" stroke="{frame}" stroke-width="{max(1.5,w*.06):.1f}"/>'
    if mull:
        c='#6B5A3E' if lit else '#2A2A2C'
        sw=max(1,w*.035)
        s+=f'<line x1="{x+w/2}" y1="{y+(w/2 if arch else 0)}" x2="{x+w/2}" y2="{y+h}" stroke="{c}" stroke-width="{sw:.1f}"/>'
        for k in (1,2,3):
            yy=y+(w/2 if arch else 0)+(h-(w/2 if arch else 0))*k/4
            s+=f'<line x1="{x}" y1="{yy:.1f}" x2="{x+w}" y2="{yy:.1f}" stroke="{c}" stroke-width="{sw:.1f}"/>'
    return s
def sky(w,h,top='#06070B',mid='#141A29',bot='#2B2621',id_='sky'):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset=".6" stop-color="{mid}"/><stop offset="1" stop-color="{bot}"/></linearGradient>'
def trees(cx,base,scale,col='#070708',n=9):
    s=''
    for i in range(n):
        rx=random.uniform(40,90)*scale; ry=random.uniform(50,110)*scale
        s+=f'<ellipse cx="{cx+random.uniform(-90,90)*scale:.0f}" cy="{base-random.uniform(40,200)*scale:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="{col}"/>'
    return s

# ---------- HERO FACADE ----------
def hero():
    W,H=1600,1000
    b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
    b+=f'<circle cx="1260" cy="170" r="160" fill="url(#glow)" opacity=".5"/><circle cx="1260" cy="170" r="26" fill="#E9DFC8" opacity=".85"/>'
    for i in range(60):
        b+=f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,380):.0f}" r="{random.uniform(.6,1.6):.1f}" fill="#E9E1D0" opacity="{random.uniform(.2,.7):.2f}"/>'
    # wings
    b+='<rect x="200" y="380" width="1200" height="620" fill="#191817"/>'
    b+='<path d="M180,380 L260,270 L1340,270 L1420,380 Z" fill="#101012"/>'
    b+='<rect x="180" y="372" width="1240" height="12" fill="#3A3530"/>'
    # central avant-corps
    b+='<rect x="620" y="330" width="360" height="670" fill="#221F1C"/>'
    b+='<path d="M600,340 L800,210 L1000,340 Z" fill="#1A1816" stroke="#4A433A" stroke-width="3"/>'
    b+='<circle cx="800" cy="290" r="26" fill="none" stroke="#6E5E44" stroke-width="3"/>'
    b+='<rect x="600" y="334" width="400" height="10" fill="#4A433A"/>'
    # dormers
    for x in [300,420,540,1060,1180,1300]:
        b+=f'<path d="M{x-6},330 L{x-6},300 A26,26 0 0 1 {x+46},300 L{x+46},330 Z" fill="#141416" stroke="#3A3530" stroke-width="2"/>'
        b+=win(x+6,292,28,34,lit=(x in (420,1180)),glowr=40)
    # chimneys
    for x in [330,1250]:
        b+=f'<rect x="{x}" y="215" width="34" height="60" fill="#0E0E10"/>'
    # cornices
    for y in (560,760):
        b+=f'<rect x="200" y="{y}" width="1200" height="6" fill="#34302B"/>'
    # pilasters
    for x in [200,620,980,1394]:
        b+=f'<rect x="{x}" y="380" width="8" height="620" fill="#2C2926"/>'
    litset={(1,0),(3,1),(7,0),(0,1),(5,1),(6,2),(8,1),(4,0),(2,2)}
    cols=[240,320,400,480,560,  660,760,860,  1030,1110,1190,1270,1350]
    for fi,(y,h) in enumerate([(410,120),(600,130),(800,150)]):
        for ci,x in enumerate(cols):
            if fi==2 and 740<=x<=860: continue
            lit=(ci%9,fi) in litset and random.random()>.2
            b+=win(x,y,46 if not 620<x<980 else 60,h,lit=lit)
            b+=f'<rect x="{x-6}" y="{y+h}" width="{58 if not 620<x<980 else 72}" height="5" fill="#3E3831"/>'
    # porte-cochere
    b+='<circle cx="800" cy="900" r="220" fill="url(#glow)" opacity=".7"/>'
    b+='<path d="M720,1000 L720,860 A80,80 0 0 1 880,860 L880,1000 Z" fill="url(#lit)" opacity=".92"/>'
    b+='<path d="M720,1000 L720,860 A80,80 0 0 1 880,860 L880,1000" fill="none" stroke="#4E4538" stroke-width="8"/>'
    b+='<line x1="800" y1="780" x2="800" y2="1000" stroke="#6B5A3E" stroke-width="3"/>'
    b+='<path d="M760,1000 L800,860 L840,1000 Z" fill="#2A241B" opacity=".5"/>'
    b+=trees(80,1010,1.3)+trees(1520,1010,1.3)
    b+='<rect y="975" width="1600" height="25" fill="#0A0A0B"/>'
    b+=grain(W,H)
    return svg(W,H,b,sky(W,H))

# ---------- ENFILADE ----------
def enfilade():
    W,H=800,1000
    b='<rect width="800" height="1000" fill="#0D0D0F"/>'
    # floor perspective
    b+='<path d="M0,1000 L330,560 L470,560 L800,1000 Z" fill="#171513"/>'
    for i in range(-10,11):
        b+=f'<line x1="400" y1="560" x2="{400+i*110}" y2="1000" stroke="#2A2520" stroke-width="1.5"/>'
    for k in range(1,12):
        y=560+440*(k/11)**2
        b+=f'<line x1="0" y1="{y:.0f}" x2="800" y2="{y:.0f}" stroke="#221E1A" stroke-width="1"/>'
    n=7
    for i in range(n):
        t=i/(n-1)
        w=620*(1-t*.82); h=840*(1-t*.8)
        x=400-w/2; y=560-(560-160)*(1-t)*.0 - h*.62
        y=560-h*0.64-0*t
        col=int(18+t*40)
        c=f'#{col:02x}{int(col*.93):02x}{int(col*.84):02x}'
        d=f'M{x-60*(1-t)},{y+h} L{x-60*(1-t)},0 L{x+w+60*(1-t)},0 L{x+w+60*(1-t)},{y+h} L{x+w},{y+h} L{x+w},{y+w/2} A{w/2},{w/2} 0 0 0 {x},{y+w/2} L{x},{y+h} Z'
        b+=f'<path d="{d}" fill="{c}"/>'
        b+=f'<path d="M{x},{y+h} L{x},{y+w/2} A{w/2},{w/2} 0 0 1 {x+w},{y+w/2} L{x+w},{y+h}" fill="none" stroke="#5A4E3E" stroke-width="{3-2*t:.1f}" opacity="{.4+.5*t:.2f}"/>'
    b+='<circle cx="400" cy="470" r="140" fill="url(#glow)"/>'
    b+='<path d="M374,560 L374,440 A26,26 0 0 1 426,440 L426,560 Z" fill="url(#lit)"/>'
    b+='<path d="M374,560 L200,1000 L600,1000 L426,560 Z" fill="#E8D2A2" opacity=".07"/>'
    b+=grain(W,H)
    return svg(W,H,b)

# ---------- STAIR ----------
def stair():
    W,H=800,800
    b='<rect width="800" height="800" fill="#0B0B0D"/>'
    for i in range(34):
        t=i/33
        r=380*(1-t)**1.15+14
        cx=400+math.cos(t*9)*18*t; cy=400+math.sin(t*9)*18*t
        shade=int(60-t*44)
        b+=f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{r:.1f}" ry="{r*.96:.1f}" fill="#{shade:02x}{int(shade*.94):02x}{int(shade*.86):02x}" stroke="#0A0A0A" stroke-width="2"/>'
    for i in range(34):
        t=i/33; r=380*(1-t)**1.15+14
        cx=400+math.cos(t*9)*18*t; cy=400+math.sin(t*9)*18*t
        b+=f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{r-6:.1f}" ry="{(r-6)*.96:.1f}" fill="none" stroke="#C9A56A" stroke-width="1" opacity="{.15+.5*(1-t):.2f}" stroke-dasharray="{3+t*6:.0f} {8+t*10:.0f}"/>'
    b+='<circle cx="400" cy="400" r="40" fill="#050506"/>'
    b+=grain(W,H)
    return svg(W,H,b)

# ---------- PLACES (900x1125) ----------
PW,PH=900,1125
def paris():
    b=f'<rect width="{PW}" height="{PH}" fill="url(#sk)"/>'
    b+='<rect x="90" y="330" width="720" height="795" fill="#1C1B19"/><path d="M70,330 L150,220 L750,220 L830,330 Z" fill="#111113"/><rect x="70" y="324" width="760" height="10" fill="#3E3831"/>'
    for x in (200,420,640):
        b+=win(x+10,250,40,60,lit=(x==420),glowr=60)
    for fi,y in enumerate((370,580,800)):
        for ci,x in enumerate((140,275,410,545,680)):
            if fi==2 and ci==2: continue
            b+=win(x,y,70,170,lit=((ci+fi)%3==0))
            b+=f'<rect x="{x-8}" y="{y+170}" width="86" height="8" fill="#3E3831"/>'
            if fi==1: b+=f'<rect x="{x-10}" y="{y+120}" width="90" height="50" fill="none" stroke="#2E2A25" stroke-width="3"/>'+''.join(f'<line x1="{x-10+k*9}" y1="{y+120}" x2="{x-10+k*9}" y2="{y+170}" stroke="#2E2A25" stroke-width="2"/>' for k in range(11))
    b+='<circle cx="445" cy="1040" r="170" fill="url(#glow)"/><path d="M380,1125 L380,1000 A65,65 0 0 1 510,1000 L510,1125 Z" fill="url(#lit)"/>'
    b+=grain(PW,PH)
    return svg(PW,PH,b,sky(PW,PH,'#070810','#18203A','#3A3128','sk'))
def venice():
    b=f'<rect width="{PW}" height="{PH}" fill="url(#sk)"/>'
    b+='<rect x="120" y="180" width="660" height="520" fill="#2A2320"/><rect x="100" y="170" width="700" height="12" fill="#4A3F33"/>'
    def ogee(x,y,w,h,lit):
        s=''
        if lit: s+=f'<circle cx="{x+w/2}" cy="{y+h/2}" r="{w*2}" fill="url(#glow)"/>'
        d=f'M{x},{y+h} L{x},{y+w*.7} Q{x},{y+w*.2} {x+w/2},{y} Q{x+w},{y+w*.2} {x+w},{y+w*.7} L{x+w},{y+h} Z'
        return s+f'<path d="{d}" fill="{"url(#lit)" if lit else "url(#dim)"}" stroke="#5A4A38" stroke-width="3"/>'
    for x in range(250,650,70): b+=ogee(x,240,52,150,(x//70)%2==1)
    b+='<rect x="230" y="398" width="440" height="8" fill="#5A4A38"/>'
    for x in (150,690): b+=ogee(x,260,60,130,x==690)
    for x in range(200,700,100): b+=ogee(x,470,60,150,x==400)
    b+='<rect x="340" y="610" width="220" height="90" fill="#0A0A0B"/>'
    b+='<path d="M340,700 L340,650 A110,40 0 0 1 560,650 L560,700 Z" fill="url(#lit)" opacity=".6"/>'
    # water
    b+='<rect y="700" width="900" height="425" fill="#0B0F18"/>'
    for i in range(70):
        y=705+i*6; a=max(0,.35-i*.005)
        for j in range(random.randint(2,5)):
            x=random.uniform(150,750); w=random.uniform(10,70)
            col='#D9B77A' if random.random()<.4 else '#3A3A44'
            b+=f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="2" fill="{col}" opacity="{a:.2f}"/>'
    b+='<path d="M40,860 q140,-20 280,0 l-20,14 q-120,10 -240,0 Z" fill="#050506"/><line x1="300" y1="700" x2="300" y2="880" stroke="#1A1A1E" stroke-width="7"/><line x1="610" y1="690" x2="610" y2="900" stroke="#1A1A1E" stroke-width="7"/>'
    b+=grain(PW,PH)
    return svg(PW,PH,b,sky(PW,PH,'#0A0B12','#22263A','#4A3A30','sk'))
def riad():
    b='<rect width="900" height="1125" fill="#1D1714"/>'
    b+='<rect x="0" y="0" width="900" height="160" fill="#2A3350"/><circle cx="450" cy="0" r="300" fill="url(#glow)" opacity=".4"/>'
    b+='<rect x="0" y="150" width="900" height="16" fill="#6A5236"/>'
    def horse(x,y,w,h,col):
        r=w*.56
        return f'<path d="M{x},{y+h} L{x},{y+r*1.1} A{r},{r} 0 1 1 {x+w},{y+r*1.1} L{x+w},{y+h} Z" fill="{col}"/>'
    b+='<rect x="0" y="166" width="900" height="560" fill="#3A2B20"/>'
    for i,x in enumerate((40,250,460,670)):
        b+=horse(x,230,190,470,'#120E0C')
        b+=f'<path d="M{x},{700} L{x},{230+190*.56*1.1} A{190*.56},{190*.56} 0 1 1 {x+190},{230+190*.56*1.1} L{x+190},700" fill="none" stroke="#8C6B45" stroke-width="3"/>'
        if i in (1,2): b+=f'<circle cx="{x+95}" cy="330" r="30" fill="url(#glow)"/><path d="M{x+85},290 h20 l-4,40 h-12 Z" fill="#E8C98E"/><line x1="{x+95}" y1="230" x2="{x+95}" y2="290" stroke="#8C6B45"/>'
    # zellige floor
    b+='<rect x="0" y="726" width="900" height="399" fill="#241C17"/>'
    for i in range(-8,18):
        b+=f'<line x1="{i*60}" y1="726" x2="{i*60+400}" y2="1125" stroke="#3E3026" stroke-width="2"/><line x1="{i*60+400}" y1="726" x2="{i*60}" y2="1125" stroke="#3E3026" stroke-width="2"/>'
    b+='<ellipse cx="450" cy="920" rx="200" ry="70" fill="#0E1220" stroke="#8C6B45" stroke-width="4"/><ellipse cx="450" cy="920" rx="150" ry="48" fill="#141B30"/><ellipse cx="450" cy="905" rx="24" ry="8" fill="#8C6B45"/><rect x="442" y="870" width="16" height="36" fill="#8C6B45"/><ellipse cx="450" cy="868" rx="34" ry="10" fill="#A8854F"/>'
    b+='<ellipse cx="450" cy="920" rx="220" ry="90" fill="url(#glow)" opacity=".5"/>'
    b+=grain(900,1125)
    return svg(900,1125,b)
def highland():
    b=f'<rect width="{PW}" height="{PH}" fill="url(#sk)"/>'
    b+='<path d="M0,760 Q200,640 420,720 T900,680 L900,1125 L0,1125 Z" fill="#12151B"/>'
    b+='<path d="M0,840 Q300,760 560,830 T900,800 L900,1125 L0,1125 Z" fill="#0C0E12"/>'
    # castle
    b+='<rect x="260" y="480" width="380" height="380" fill="#1A1A1C"/>'
    for x,w,h in ((200,110,470),(590,120,520)):
        top=860-h
        b+=f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="#151517"/><path d="M{x-12},{top} L{x+w/2},{top-150} L{x+w+12},{top} Z" fill="#0D0D0F"/>'
    b+='<path d="M250,480 L450,380 L650,480 Z" fill="#101012"/>'
    for (x,y,l) in ((235,480,1),(235,600,0),(625,420,0),(625,560,1),(300,560,0),(370,560,1),(440,560,0),(510,560,0),(300,700,1),(440,700,0),(510,700,1),(370,700,0)):
        b+=win(x,y,38,70,lit=bool(l),glowr=70)
    for i in range(5):
        b+=f'<rect x="-50" y="{700+i*40}" width="1000" height="30" fill="#8A93A6" opacity=".05" filter="url(#soft)"/>'
    b+=grain(PW,PH)
    return svg(PW,PH,b,sky(PW,PH,'#0B0E16','#2B3346','#5A5650','sk'))
def villa():
    b=f'<rect width="{PW}" height="{PH}" fill="url(#sk)"/>'
    b+='<circle cx="700" cy="600" r="260" fill="url(#glow)" opacity=".8"/>'
    b+='<path d="M0,760 Q450,700 900,770 L900,1125 L0,1125 Z" fill="#2A2018"/>'
    b+='<rect x="170" y="470" width="560" height="330" fill="#6A5238"/><path d="M150,470 L450,400 L750,470 Z" fill="#4A3524"/>'
    for i in range(5):
        x=210+i*100
        b+=f'<path d="M{x},800 L{x},650 A40,40 0 0 1 {x+80},650 L{x+80},800 Z" fill="#1E150F"/>'
    for i in range(5):
        b+=win(222+i*100,500,56,90,lit=(i%2==0),arch=False)
    for x,h in ((80,520),(130,440),(790,500),(840,420),(60,380)):
        b+=f'<path d="M{x},820 C{x-26},{820-h*.4} {x-10},{820-h*.8} {x},{820-h} C{x+10},{820-h*.8} {x+26},{820-h*.4} {x},820 Z" fill="#100D0A"/>'
    b+='<rect y="820" width="900" height="305" fill="#1A140F"/>'
    for i in range(12): b+=f'<line x1="{450}" y1="820" x2="{i*82-20}" y2="1125" stroke="#2A2018" stroke-width="2"/>'
    b+=grain(PW,PH)
    return svg(PW,PH,b,sky(PW,PH,'#1B1C28','#6A5A4E','#C29A68','sk'))
def ryokan():
    b='<rect width="900" height="1125" fill="#0D0E10"/>'
    b+='<path d="M-40,300 L450,160 L940,300 L900,330 L0,330 Z" fill="#141416"/><rect x="0" y="330" width="900" height="16" fill="#2A2622"/>'
    b+='<circle cx="450" cy="600" r="420" fill="url(#glow)" opacity=".6"/>'
    for i in range(6):
        x=40+i*140
        b+=f'<rect x="{x}" y="360" width="120" height="440" fill="url(#lit)" opacity=".85"/>'
        for k in range(1,4): b+=f'<line x1="{x+k*30}" y1="360" x2="{x+k*30}" y2="800" stroke="#3A2E20" stroke-width="2"/>'
        for k in range(1,8): b+=f'<line x1="{x}" y1="{360+k*55}" x2="{x+120}" y2="{360+k*55}" stroke="#3A2E20" stroke-width="2"/>'
        b+=f'<rect x="{x-10}" y="346" width="10" height="470" fill="#1A1614"/>'
    b+='<rect x="0" y="800" width="900" height="30" fill="#2A221B"/><rect x="0" y="830" width="900" height="295" fill="#0A0A0B"/>'
    for i in range(14): b+=f'<ellipse cx="{random.uniform(0,900):.0f}" cy="{random.uniform(900,1100):.0f}" rx="{random.uniform(20,60):.0f}" ry="{random.uniform(8,18):.0f}" fill="#1B1A18"/>'
    b+='<path d="M720,1125 C700,900 760,700 820,560" stroke="#050505" stroke-width="14" fill="none"/>'+trees(830,620,.9,'#060606',7)
    b+=grain(900,1125)
    return svg(900,1125,b)

# ---------- STORY (1200x800) ----------
def door():
    W,H=1200,800
    b='<rect width="1200" height="800" fill="#121110"/>'
    b+='<rect x="0" y="640" width="1200" height="160" fill="#1A1714"/>'
    for i in range(20): b+=f'<line x1="{i*70}" y1="640" x2="{i*70-120}" y2="800" stroke="#221E1A"/>'
    b+='<rect x="440" y="80" width="320" height="560" fill="#2A2520"/><rect x="460" y="100" width="280" height="540" fill="url(#lit)"/>'
    b+='<circle cx="600" cy="400" r="380" fill="url(#glow)"/>'
    b+='<path d="M460,100 L560,130 L560,610 L460,640 Z" fill="#1E1916"/><path d="M740,100 L660,125 L660,615 L740,640 Z" fill="#1E1916"/>'
    for (a,c) in ((470,550),(670,730)):
        b+=f'<rect x="{a+8}" y="170" width="{c-a-24}" height="180" fill="none" stroke="#3A322A" stroke-width="3"/><rect x="{a+8}" y="390" width="{c-a-24}" height="200" fill="none" stroke="#3A322A" stroke-width="3"/>'
    b+='<path d="M560,640 L660,640 L900,800 L330,800 Z" fill="#F0D9A6" opacity=".22"/>'
    b+='<rect x="400" y="60" width="400" height="24" fill="#3A332B"/>'
    b+=grain(W,H)
    return svg(W,H,b)
def library():
    W,H=1200,800
    b='<rect width="1200" height="800" fill="#100E0C"/>'
    for sx in (60,420,780):
        b+=f'<rect x="{sx}" y="40" width="340" height="700" fill="#1C1611"/>'
        for r in range(6):
            y=60+r*112
            x=sx+12
            while x<sx+320:
                w=random.randint(10,24); h=random.randint(70,98)
                c=random.choice(['#3A2A1E','#2B2230','#1E2A2A','#4A3A26','#2A1E18','#5A4630','#23252E'])
                b+=f'<rect x="{x}" y="{y+100-h}" width="{w}" height="{h}" fill="{c}"/>'
                if random.random()<.25: b+=f'<rect x="{x+2}" y="{y+100-h+10}" width="{w-4}" height="2" fill="#A8854F" opacity=".7"/>'
                x+=w+random.randint(0,3)
            b+=f'<rect x="{sx}" y="{y+100}" width="340" height="10" fill="#2E241B"/>'
    b+='<line x1="700" y1="760" x2="820" y2="40" stroke="#5A4630" stroke-width="10"/><line x1="770" y1="760" x2="890" y2="40" stroke="#5A4630" stroke-width="10"/>'
    for k in range(1,14):
        t=k/14; b+=f'<line x1="{700+120*t:.0f}" y1="{760-720*t:.0f}" x2="{770+120*t:.0f}" y2="{760-720*t:.0f}" stroke="#5A4630" stroke-width="6"/>'
    b+='<circle cx="330" cy="620" r="260" fill="url(#glow)"/><path d="M300,560 h60 l-12,-40 h-36 Z" fill="#E8C98E"/><line x1="330" y1="560" x2="330" y2="740" stroke="#6B5A3E" stroke-width="5"/>'
    b+='<rect y="740" width="1200" height="60" fill="#0A0908"/>'
    b+=grain(W,H)
    return svg(W,H,b)
def window():
    W,H=1200,800
    b='<rect width="1200" height="800" fill="#0F0E0D"/>'
    b+='<rect x="380" y="60" width="440" height="700" fill="url(#sk)"/>'
    b+='<circle cx="700" cy="200" r="120" fill="url(#glow)" opacity=".6"/><circle cx="700" cy="200" r="22" fill="#EDE4D0"/>'
    b+=trees(520,720,1.1,'#07080A',10)+trees(760,760,.9,'#0A0B0E',8)
    b+='<path d="M380,760 L380,160 A220,100 0 0 1 820,160 L820,760" fill="none" stroke="#2E2923" stroke-width="18"/>'
    b+='<line x1="600" y1="80" x2="600" y2="760" stroke="#2E2923" stroke-width="10"/>'
    for y in (300,450,600): b+=f'<line x1="380" y1="{y}" x2="820" y2="{y}" stroke="#2E2923" stroke-width="6"/>'
    b+='<path d="M200,40 C300,300 250,600 330,780 L120,780 L100,40 Z" fill="#2A2019"/><path d="M1000,40 C900,300 950,600 870,780 L1080,780 L1100,40 Z" fill="#2A2019"/>'
    b+='<path d="M200,40 C300,300 250,600 330,780" fill="none" stroke="#5A4630" stroke-width="2" opacity=".6"/>'
    b+='<rect y="760" width="1200" height="40" fill="#1A1714"/><path d="M380,760 L820,760 L1000,800 L200,800 Z" fill="#C9D2E6" opacity=".08"/>'
    b+=grain(W,H)
    return svg(W,H,b,sky(W,H,'#0A0D18','#1E2740','#3A3A44','sk'))

for name,f in dict(hero=hero,enfilade=enfilade,stair=stair,paris=paris,venice=venice,riad=riad,highland=highland,villa=villa,ryokan=ryokan,door=door,library=library,window=window).items():
    open(OUT+name+'.svg','w').write(f())

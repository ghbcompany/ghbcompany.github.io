"""Play 개발자 페이지 헤더(4096x2304)를 그린다. 사용법은 README.md."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=4096,2304
BG=(255,244,214); FG=(43,33,24); SUB=(110,90,70)
img=Image.new("RGB",(W,H),BG)
d=ImageDraw.Draw(img)
# 옅은 점 무늬
for y in range(0,H,128):
    for x in range((y//128%2)*64,W,128):
        d.ellipse((x-6,y-6,x+6,y+6),fill=(247,232,196))
icons=[sys.argv[1],sys.argv[2],sys.argv[3]]
S=520; gap=140; R=110
total=3*S+2*gap; x0=(W-total)//2; y0=1180
for i,p in enumerate(icons):
    ic=Image.open(p).convert("RGB").resize((S,S),Image.LANCZOS)
    m=Image.new("L",(S,S),0); ImageDraw.Draw(m).rounded_rectangle((0,0,S-1,S-1),R,fill=255)
    x=x0+i*(S+gap)
    sh=Image.new("L",(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((x+10,y0+28,x+S+10,y0+S+28),R,fill=90)
    sh=sh.filter(ImageFilter.GaussianBlur(30))
    img.paste((150,120,80),(0,0),sh)
    img.paste(ic,(x,y0),m)
d=ImageDraw.Draw(img)
fb=ImageFont.truetype(sys.argv[4],300); fr=ImageFont.truetype(sys.argv[5],120)
def ctext(t,f,y,c):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)
ctext("ghbcode",fb,520,FG)
ctext("꼭 필요한 기능만 담은 작은 앱",fr,900,SUB)
img.save(sys.argv[6],optimize=True)

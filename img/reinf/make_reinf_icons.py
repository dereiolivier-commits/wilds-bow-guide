from PIL import Image
import json,sys
R='/mnt/project-files/at-arkveld/clean_assets/reinforcements/'
out=sys.argv[1]; M=150; IH={'atk':46,'aff':44,'ele':46}; meta={}
for k in ['atk','aff','ele']:
  for ex in (False,True):
    f=f'ic_{k}{"_ex" if ex else ""}'; im=Image.open(R+f+'.png'); b=Image.open(R+f'ic_{k}.png')
    cw,ch=b.width-120,b.height-120; o=144 if ex else 60
    c=Image.new('RGBA',(cw+2*M,ch+2*M)); c.alpha_composite(im,(M-o,M-o)) if M-o>=0 else None
    sc=IH[k]/46*68/ch   # content ~68px at 2x (34 css px)
    c=c.resize((round(c.width*sc),round(c.height*sc)),Image.LANCZOS)
    n=f.replace('ic_','r_'); c.save(f'{out}/{n}.webp',lossless=True); meta[n]=(c.width//2,c.height//2)
print(json.dumps(meta))

from PIL import Image
im=Image.open('/Users/dsz/Desktop/code/PyDemo/字符画/qq.jpg')

grey_char='''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''

im=im.resize((80,50),Image.ANTIALIAS)
im=im.convert('L')
im.save('/Users/dsz/Desktop/code/PyDemo/字符画/t.jpeg')

def get_char(grey):
    if grey>240:
        return ' '
    else:
        return grey_char[int((grey)/((256.0+1)/len(grey_char)))]
    
text=''
for i in range(im.height):
    for j in range(im.width):
        grey=im.getpixel((j,i))
        if isinstance(grey,tuple):
            grey=int(0.2126*grey[0]+0.7152*grey[1]+0.0722*grey[2])
        text+=get_char(grey)
    text+='\n'

with open('/Users/dsz/Desktop/code/PyDemo/字符画/pix.txt','w') as f:
    f.write(text)
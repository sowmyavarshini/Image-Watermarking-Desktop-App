from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title('Image Watermarking Desktop App')
window.minsize(width=300, height=250)
window.config(padx=20, pady=20)
image_path = None
watermark_path = None


def final_image(image, text, font_path, position):
    img = Image.open(image)
    img = img.resize((500, 500))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 36)
    draw.text(position, text, font=font, fill=(255, 255, 255, 128))
    return img


def choose_file():
    global image_path
    image_path = filedialog.askopenfilename()
    file_entry.insert(0, image_path)


def add_watermark():
    global watermark_path
    watermark_path = filedialog.askopenfilename()
    watermark_entry.insert(0, watermark_path)


def apply_button():
    global image_path, watermark_path
    if image_path and watermark_path:
        if watermark_path.endswith('.txt'):
            with open(watermark_path, 'r') as file:
                text = file.read()
                final = final_image(image_path, text, 'arial.ttf', (10, 10))
        else:
            img = Image.open(image_path)
            final = img.resize((500, 500))
            watermark = Image.open(watermark_path)
            wm_resize = watermark.resize((70, 70))
            final.paste(wm_resize, (10, 10), mask=wm_resize)
            final.show()
        final.save('watermarked_image.jpg')
        final_label.config(text='Image watermarked and saved successfully')
    else:
        final_label.config(text='Choose an image and a watermark!')


image_label = Label(text='Choose an image', font=('Arial', 12))
image_label.grid(column=0, row=0)
image_label.config(padx=10, pady=10)

file_entry = Entry(width=50)
file_entry.grid(column=0, row=1)

file_button = Button(text='Choose file', command=choose_file)
file_button.grid(column=2, row=1)


watermark_label = Label(text='Choose watermark text / logo', font=('Arial', 12))
watermark_label.grid(column=0, row=2)
watermark_label.config(padx=10, pady=10)

watermark_entry = Entry(width=50)
watermark_entry.grid(column=0, row=3)

watermark_button = Button(text='Choose watermark', command=add_watermark)
watermark_button.grid(column=2, row=3)


final_button = Button(text='Apply', command=apply_button)
final_button.grid(column=0, row=5)


final_label = Label(text='', font=('Arial', 15, 'bold'))
final_label.grid(column=0, row=6)
final_label.config(padx=10, pady=10)

window.mainloop()

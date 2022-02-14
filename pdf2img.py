import PyPDF4
import pikepdf
import fitz
import os

saved_path = os.getcwd()

def pdf_image(pdf_name):
    pdf = fitz.Document(pdf_name)
    pdf_object = []
    img_path = None
    file_name = os.path.basename(pdf_name)[:-4]
    length = pdf.pageCount
    for index in range(0, length):
        print(f'index is {index}')
        page = pdf[index]  # 获得每一页的对象
        trans = fitz.Matrix(3.0, 3.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        # img_path = f'{file_name}_{str(index+1)}.png'
        # pm.writePNG(f'{saved_path}/images/{img_path}')  # 保存图片
        pdf_object.append(pm)
    pdf.close()
    for index in range(0, length):
        img_path = f'{file_name}_{str(index+1)}.png'
        pdf_object[index].writePNG(f'{saved_path}/images/{img_path}')

if __name__ == '__main__':
    file_path = '/Users/jayleeli/work/资料/中华人民共和国民法典（含新旧与关联对照）电子版增值/法制社-新旧对照全文加水印.pdf'
    _ = pdf_image(file_path)
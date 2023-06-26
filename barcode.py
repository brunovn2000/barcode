import cv2
from pyzbar.pyzbar import decode
from pdf2image import convert_from_path
from datetime import datetime
import time


def BarcodeReader(image):
    img = cv2.imread(image)      
    detectedBarcodes = decode(img)
    if not detectedBarcodes:
        return {'detectedBarcodes':False,
                'message': 'o arquivo não possui codigo de barras ou esta corrompido'}
    else:
        lista_barcode = []
        for barcode in detectedBarcodes: 
            retorno={}
            (x, y, w, h) = barcode.rect
            retorno['locate'] = (x, y, w, h)
            
            #desenha marcação na localização do codigo de barra
            # cv2.rectangle(img, (x-10, y-10),
            #               (x + w+10, y + h+10),
            #               (255, 0, 0), 2)
             
            if barcode.data!="":
                retorno['value'] = barcode.data
                retorno['type'] = barcode.type
            lista_barcode.append(retorno)    
    #exibir barcode marcado
    # imS = cv2.resize(img, (1600, 1600))# Resize image
    # cv2.imshow("output", imS)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return lista_barcode


def converte_pdf_in_image(pdf_path):
    list_image=[]
    try:
        # no windows é necessario especificar o path da lib poppler|| poppler_path=r'C:\poppler-0.68.0\bin'
        # no linux é so fazer a instalação 
        images = convert_from_path(pdf_path, dpi=500, poppler_path=r'C:\poppler-0.68.0\bin')
        
        for i in range(len(images)):
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
            img = f'notas_image\{current_datetime}{str(i)}.jpg'
            images[i].save(img, 'JPEG')
            list_image.append(img)
    except  :
        print("NO pdf found")
        #TODO
        #adicionar em log
    
    return list_image
    
def main():
    tempo_inicial = time.time() # em segundos
    pdf='pdf/NF42884.pdf'
    # image='image.jpg'
    # pdf = input("Informe o path do arquivo PDF: ")
    nota_images = converte_pdf_in_image(pdf)
    for image in nota_images:
        code = BarcodeReader(image)
    print(code)
    tempo_final = time.time() # em segundos
    tempo_execucao =round(tempo_final - tempo_inicial,2 )
   
    print(f"{tempo_execucao} segundos")

if __name__ == '__main__':
    main()
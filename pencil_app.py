import numpy as np
import streamlit as st
from PIL import Image
import cv2
#---------------------#

#divide spoll into to columns
col2, col3 = st.beta_columns((2,2))
#logo
logo = Image.open("C:\\Users\\Lenovo\\Documents\\Luis\\logo2.jpg")
col3.image(logo)

#titulo
col2.title('Pencil Sketcher App')
col2.write('Esta app convierte tus fotos a bocetos a lápiz')
col2.markdown('''
    |Nombre|Fecha|
    |------|-----|
    |[Luis Hernández](luishernandezmatos@yahoo.com)|22/10/2020|
    ''')
##descripcion
expander_bar = st.beta_expander('Avertencia:')
expander_bar.markdown('''
Esta aplicación es solo para fines educativos.
 **¡Úsela bajo su propio riesgo!**
    ''')
#--------------------------------------------#
#funcion para invertir las imagenes
def dodgeV2(x,y):
    return cv2.divide(x, 255-y, scale=256)

#funcion pencilsketcher
def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21,21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return (final_img)
#--------------------------------------------------------------#
#sidebar
file_image = st.sidebar.file_uploader('Carge la foto o imagen', type = ['jpeg', 'jpg', 'png'])

# condicional de carga y ejecucion de la funcion pencilsketch

if file_image is None:
    st.write('No has subido ninguna imagen')
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    st.image(input_img, use_column_width = True)
    st.write('**Salida de Boceto de lápiz**')
    st.image(final_sketch, use_column_width = True)
    #descagar imagen
    if st.button('Descargar su imagen'):
        img_pil = Image.fromarray(final_sketch)
        img_pil.save('imagen_final.jpeg')
        st.write('**Descarga completada**')









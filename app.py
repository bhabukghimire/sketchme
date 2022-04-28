import streamlit as st
import cv2
import numpy as np
from streamlit_option_menu import option_menu


selected = option_menu(
    menu_title = None,
    options = ['Home','About'],
    icons = ['house','search'],
    orientation = 'horizontal',
    
    
    default_index = 0
)
# to remove header and footer
hide_menu_style = """
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)


if selected == 'About':
    st.title("Photo to sketch")
if selected == "Home":
    
    st.title("Photo to sketch")

    # to upload image
    image_file = st.file_uploader("Choose a image",type = ['jpg','png','jpeg'])
    if image_file is not None:
        st.image(image_file,'Image',use_column_width = True)
        save_path = './uploaded_images/' + image_file.name
        
        
        with open(save_path,"wb") as f:
            f.write(image_file.getbuffer())
                
            
            scale = st.slider("Scale",min_value = 190,max_value = 270, value = 240,step = 1,key = 'slider')    
            image = cv2.imread(save_path)
            img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            img_invert = cv2.bitwise_not(img_gray)
            img_smoothing = cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
        
            gen_image = cv2.divide(img_gray,255-img_smoothing,scale=scale)
        
            
            cv2.imwrite('./sketch_images/'+image_file.name,gen_image)
            st.image('./sketch_images/' + image_file.name,'Sketch',width = 100,use_column_width = True)
            with open('./sketch_images/'+image_file.name, "rb") as file:
                        st.download_button(label="Download image", data=file,file_name="sketch.png")
                    
            
            

    
    




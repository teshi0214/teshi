import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('stremlit 超入門')

st.write('プログレスバーの表示')
'start!!'

Iateast_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    print(i)
    Iateast_iteration.text(f'Itearation {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
    
'done!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右ボタン')
if button:
    right_column.write('右カラム')
    
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


#text = st.text_input('あなたの趣味を教えてください。')
#con = st.slider('anatano',0,100,50)
#'あなたの趣味は', text,'です'
#'kondeisyon',con

#if st.checkbox('Show Imge'):    
#    img = Image.open('613GHcIJcuL._AC_SY606_.jpg')
#    st.image(img ,caption='狸', use_column_width=True)

  
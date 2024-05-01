import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="Experience", page_icon="💼")

st.markdown("# Experience")
st.sidebar.header("Experience")
st.write(
    """
    This page illustrates the milestones in my experience. 
    It highlights two important branches: interest for development and family, which shaped my decisions before I arrived here.
    These factors go beyond the information presented on Linkedin, and 
    I think it clarifies my perspective in the best form. See below for details. 
    """
)
loc_list = [
    [25.04404416896265, 121.55635135894504],
    [24.99826279209154, 121.30446195720047],
    [23.00868439834047, 120.22050214095697],
    [22.67295929331864, 120.49805210618877],
    [41.875202170576095, -87.63589051592997],
]
df = pd.DataFrame(
    np.array(loc_list),
    columns=['lat', 'lon'])

st.map(df, size=20)

col1, col2, col3 = st.columns(3)
with col1: st.markdown("#### Dev Interest")
with col2: st.markdown("### Milestone")
with col3: st.markdown("#### Family")

col1, col2, col3 = st.columns(3)
    
with col1:
    st.markdown('''
1st time learning programming  
''')   

with col2:
    st.markdown('''
2010	Studied@HSNU

2012	Studied@CGU OT

        '''
    )

with col3:
    st.write(
        """
        Health status prevented my dad from work

Get license and be more helpful for caring

        """
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
Can’t give up codes
''')   

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
Applied to engineering school
''')   

with col2:
    st.markdown('''
2016	Received BS@CGU OT
''')   

 
col1, col2, col3 = st.columns(3)
with col2: st.markdown('''2017	Go to US studying BME''')   

col1, col2, col3 = st.columns(3)
with col1: st.markdown('''Built an automatic in mechatronics''')   
with col2: st.markdown('''2018''')   
with col3: st.markdown('''Dad were sent to hospital because of acute Uremia''')   

col1, col2, col3 = st.columns(3)
with col1: st.markdown('''Curious about I2C found MIMO''')   
with col2: st.markdown('''2019	Received MS@NU BME and started work at MedGyn''')   
with col3: st.markdown('''Decided to make medical device''')   

col1, col2, col3 = st.columns(3)
with col2: st.markdown('''2020''')   
with col3: st.markdown('''Dad were went to hospitals multiple times because of heart deceases and infection''')   

col1, col2, col3 = st.columns(3)
with col1: st.markdown('''Built a data system''')   
with col2: st.markdown('''2021	Back to TW started work at TSRI''')   
with col3: st.markdown('''Keep accompany and contributive to family''')   

col1, col2, col3 = st.columns(3)
with col1: st.markdown('''Joined in PyCon''')   
with col2: st.markdown('''2022	TSRI project transit to STUST''')   

col1, col2, col3 = st.columns(3)
with col2: st.markdown('''2023	Completed work and prepared for CS-CE PhD Applications''')   

col1, col2, col3 = st.columns(3)
with col1: st.markdown('''Keep learning more about web dev''')   
with col2: st.markdown('''2024	Leading PyCon Web Team''')   

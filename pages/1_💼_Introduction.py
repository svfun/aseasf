import streamlit as st
import time
import numpy as np

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

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Dev Interest")
    st.write(
        """
1st time learning programming



Can’t give up codes

Applied engineering school

Built an automatic   in mechatronics
Curious about I2C, found MIMO

Built a data system
Joined in PyCon

Keep learning more about web dev


        """
    )

with col2:
    st.markdown("### Time")
    st.write(
        """
2010	Studied@HSNU
	
2012	Studied@CGU OT
	
	
	
2016	Received BS@CGU OT
2017	Go to US studying BME
2018	
2019	Received MS@NU BME and started work at MedGyn
2020	
2021	Back to TW, started work at TSRI
2022	TSRI project transit to STUST
2023	Quit and prepared for CS/CE PhD Applications
2024	Leading PyCon Web Team
	
Now	Wish to merge the 2 branches and dive into network studies.
        """
    )

with col3:
    st.markdown("### Family")
    st.write(
        """
Health status prevented my dad from work

Get license and be more helpful for caring





Dad was sent to hospital because of Acute Uremia
Decide to make medical device
Dad went to hospitals multiple times because of heart deceases and infection
Keep accompany and contributive to family





        """
    )

#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)
#chart = st.line_chart(last_rows)

#for i in range(1, 101):
#    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#    status_text.text("%i%% Complete" % i)
#    chart.add_rows(new_rows)
#    progress_bar.progress(i)
#    last_rows = new_rows
#    time.sleep(0.05)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
#st.button("Re-run")


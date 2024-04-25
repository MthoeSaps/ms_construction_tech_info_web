import streamlit as st
import numpy as np
import pandas as pd

import time

from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.streaming_write import write

def adpromos():
    """A ad promotion web page using streamlit"""

    st.title(":gray[**Ad Promotion for other retail companies nearby**]")
    st.write("- :gray[**This section covers surrounding products in our workspace by other producers and retailers we hope you find them helpful. This week we are promoting value gas**]")
    company_name = ":red[**Value Gas**]"
    company_status = """
        # :red[**Value Gas**]
- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""   
    st.markdown(company_status, unsafe_allow_html=True)
    st.write("- :rainbow[**Our Current Gas prices vs Market price**]")
    col1, col2, col3 = st.columns(3)

    col1.metric(label="ZAR(Rand)", value=32, delta=125, help="The delta value represents the advantage and disadvantage %")
    col2.metric(label="USD(US Dollar)", value=1.60, delta=125, help="The delta value represents the advantage and disadvantage %")
    col3.metric(label="Market(Init P)", value=2.00, delta= -80, help="$Init P - Initial price")
    style_metric_cards()

    st.write(f"- :gray[**Preview {company_name} Statistical data**]")
        
    company_data = """
Our company...
"""
    def preview():
        for word in company_data.split():
                yield word + " "
                time.sleep(0.05)
                
                yield pd.DataFrame(
                     np.random.randn(10, 4),
                     columns=["Sales p/year", "Retail Outlets", "Donations p/year", "Sponserships p/year"],
                     )     
    if st.button("Preview"):
        write(preview)
    st.divider()
    st.subheader(f"**More about {company_name}**")
    st.write("- :gray[**Company hierarchy**]")
    cht = """
<div class="card">
    <style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
}
.title {
  color: grey;
  font-size: 18px;
}
button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}
a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}
button:hover, a:hover {
  opacity: 0.7;
}
</style>
<div class="card">
    <h1>Marcus LM</h1>
    <p class="title">CEO & Founder, Value Gas</p>
    <p>Mr Marcus LM took over this company from his grandfather now he is expanding its power using tech</p>
    <a href="https://www.w3schools.com/w3css/default.asp"><i class="fa fa-dribbble"></i></a>
    <a href="https://www.w3schools.com/w3css/default.asp"><i class="fa fa-twitter"></i></a>
    <a href="https://www.w3schools.com/w3css/default.asp"><i class="fa fa-linkedin"></i></a>
    <a href="https://www.w3schools.com/w3css/default.asp"><i class="fa fa-facebook"></i></a>
    <p><button type="button">Request a meeting</button></p>
  </div>
"""
    sp, sp2 = st.columns(2)
    with sp:
        st.markdown(cht, unsafe_allow_html=True)
    with sp2:
         with st.container(height=312):
              st.image('images/components/avatar2.png', use_column_width=True, width=300)

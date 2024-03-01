import requests
import streamlit as st
import pandas as pd
from datetime import datetime 

def get_stock_data(stock_market_name, startDate='', endDate='', page_index = 1) -> dict:
    url = f'https://s.cafef.vn/Ajax/PageNew/DataHistory/PriceHistory.ashx?Symbol={stock_market_name}&StartDate={startDate}&EndDate={endDate}&PageIndex={page_index}'

    print(url)
    response = requests.get(url).json()
    
    total_count = response['Data']['TotalCount']
    data = response['Data']['Data']
    # print(total_count)

    # return {'data': data, 'total': total_count}
    return data

st.set_page_config(layout='wide', page_title='StreamlitApp')

main_page = st.container()
cols = st.columns(8)

if('pageIndex' not in st.session_state):
    st.session_state.pageIndex = 1

with st.sidebar:
    data = []
    with st.form('my_form'):

        name = st.text_input('Stock market code')
        start_date = st.date_input('Start').strftime("%m/%d/%Y")
        end_date = st.date_input('End').strftime("%m/%d/%Y")
        
        # print(start_date.strftime("%m/%d/%Y"))
        # print(end_date.strftime("%d/%m/%Y"))
        

        submit = st.form_submit_button('Submit')
        if(submit):
            data = get_stock_data(name, startDate=start_date, endDate=end_date)
            st.session_state.pageIndex = 1

    with cols[0]:
        if(st.session_state.pageIndex > 1):        
            if(st.button('Prev')):
                st.session_state.pageIndex -= 1
                data = get_stock_data(name, st.session_state.pageIndex)

    with cols[7]:
        if(st.button('Next')):
            st.session_state.pageIndex += 1
            data = get_stock_data(name, st.session_state.pageIndex)

    with main_page:
        if(len(data) > 0):
            st.table(pd.DataFrame(data))        

    

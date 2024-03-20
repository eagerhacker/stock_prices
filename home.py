# import json

# import requests
# import streamlit as st
# from streamlit_lottie import st_lottie

# def load_lottie(filepath):
#     with open(filepath, 'r') as f:
#         return json.load(f)
    
# def load_lottieurl(url):
#     r = requests.get(url)

#     if(r.status_code != 200):
#         return None
    
#     return r.json()

# lottie = load_lottie('chart_anim.json')

# st_lottie(lottie, speed= 1, reverse=False, loop=True, height=100, width=100)
# st_lottie(lottie, key="lottie")
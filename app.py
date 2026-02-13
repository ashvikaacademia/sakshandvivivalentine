import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    st.title("Page 1")
    if st.button("Next"):
        st.session_state.page = 2

elif st.session_state.page == 2:
    st.title("Page 2")

import streamlit as st

st.title('Local Command Execution')

command = st.text_input('Enter your command:', '')

if st.button('Execute Command'):
    result = os.popen(command).read()
    st.write(result)
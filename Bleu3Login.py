import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

#username: jsmith , password: abc
#username: rbriggs , password: def

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print(hashed_passwords)
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{name}*')
    st.title('Dashboard!')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
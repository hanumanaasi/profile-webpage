import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Hanuman Resume", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---- Declare CSS for Form ----
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#----  Load Css ----
load_css("style/style.css")

#---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json")

# ---------- HEADER SECTIONS -----------
with st.container():

        st.subheader("Hi, I'm Hanuman Kumar Aasi :wave:")
        st.title("A Full Stack Java Developer From Hyderabad :pushpin:")
        st.write("I'm Passionate about to learn new technologies and to improve my skills and to stay updated in this modern Tech World :smile:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As a Java developer currently workig under Enterprise Application of RailRoad service 
            dealing with the transformation of legacy systems.
            - Building up the API services for different cache's
            - Developing the dashboards for the data comparison between new systems and old systems
            - Development of solution for various new business scenarios
            - Involved in continuous integration and continuous deployment software development practice

            """
        )
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")

    selected = option_menu(
        menu_title=None, #required field
        options=["Skills","GitHub","Linkedin","Projects"], #required field
        icons=["list","github","linkedin","book"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )



    if selected == "Skills":
        st.header("Skills")
        st.write("##")
        st.write(
            """
            - Java
            - Python
            - Java script
            - Type script
            - Angular
            - Sql
            - RDBMS
            - HTML
            - CSS
            - Bootstrap
            """
        )

    if selected == "GitHub":
        st.header("This is my GitHub profile!")
        st.write("""
        Hello 👋, In this hosting platform I will be sharing my personal learning experiences
        and handson practice stuff with respect to the different technolgies.""")
        st.write("##")
        st.write("""A quote say's “Tell me and I forget, teach me and I may remember, involve me and I learn.”
        """)
        st.write("##")
        st.write("""Click Here 👇 to access to my github profile!""")

        url = 'https://in.linkedin.com/in/hanuman-kumar-aasi-8a02031b4'

        st.markdown(f'''
        <a href={url}><button style="background-color:#3498DB;">Github</button></a>
        ''',unsafe_allow_html=True)

    if selected == "Linkedin":
        st.header("This is my LinkedIn profile!")
        st.write("""
        Hello 👋, Click Here 👇 to follow to my Linkedin profile!""")
        st.write("##")
        
        url = 'https://in.linkedin.com/in/hanuman-kumar-aasi-8a02031b4'

        st.markdown(f'''
        <a href={url}><button style="background-color:#3498DB;">Linkedin</button></a>
        ''',unsafe_allow_html=True)

    if selected == "Projects":
        st.title(f"you have selected {selected}")

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    contact_form = """
    
    <form action="https://formsubmit.co/hanumankumar.aasi@gmail.com" method="POST">
    <input type="hidden"name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>

    """

    first_column, second_column = st.columns(2)
    with first_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with second_column:
        st.empty()
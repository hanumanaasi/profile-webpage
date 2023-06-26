import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from itertools import cycle

st.set_page_config(
    page_title="Hanuman's Profile", page_icon=":tada:", layout="wide")

with open("HanumanResumeLatest.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

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

lottie_download = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_r2G98gnRgd.json")

lottie_java = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zh6xtlj9.json")

lottie_js = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_we9lzvwy.json")

lottie_python = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_8MyemMY7OK.json")


#----------Skilled Images --------------

java = Image.open("images/java.png")
js = Image.open("images/js.png")
ts = Image.open("images/ts.png")
angular = Image.open("images/angular.png")
sb = Image.open("images/springboot.png")
css = Image.open("images/css.jpg")
html = Image.open("images/html.png")
sql = Image.open("images/sql.png")
python = Image.open("images/python.png")



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
        filteredImages = [java, js, ts, angular, sb, css, html, sql, python] # your images here
        caption = ["java", "Javascrpit", "Typescript", "Angular", "Springboot", "Css", "HTML", "Sql", "Python"] # your caption here
        cols = cycle(st.columns(3)) # st.columns here since it is out of beta at the time I'm writing this
        for idx, filteredImage in enumerate(filteredImages):
            next(cols).image(filteredImage, width=100, caption=caption[idx])
        
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
    first_column, second_column = st.columns(2)
    with first_column:
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
    
        st.markdown(contact_form, unsafe_allow_html=True)

    with second_column:
        st.header("Want to download my resume 📄?")
        st.download_button(label="Click Here to Download",
                    data=PDFbyte,
                    file_name="HanumanResume.pdf",
                    mime='application/octet-stream')
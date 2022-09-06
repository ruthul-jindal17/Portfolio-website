from asyncore import write
import streamlit as st
from PIL import Image
st.set_page_config(page_title="Ruthul Jindal S",layout="centered")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#header

st.write('''
# Ruthul Jindal S, VIT Chennai
##### *Portfolio*
''')
image = Image.open('images/profile.jpg')
st.image(image,width=150)
st.markdown('## About Me',unsafe_allow_html=True)
st.info('A motivated individual with good knowledge of languages and development tools, seeking a position in a growth-oriented company where I can use my skills to the advantage of the company while having the scope to develop my own skills.')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
  
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      <li class="nav-item">
        <a class="nav-link" href="#internships">Internships</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#queries">Queries</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
###########

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

######

st.markdown('## Education')
txt('**Electronics and Communication Engineering** (Bachelor of Technology), *Vellore Institute  of Technology*, Chennai',
'2019-2023')
st.markdown('''
- GPA: `7.86`
''')

txt('Velammal Vidhyashram, Surapet, Chennai',
'2009-2019')
st.markdown('''
- 10th CGPA : `10.0`
- 12th marks: `94% (470/500)`

''')

st.markdown('## Skills')
txt('- C++','Good level Proficency')
txt('- C','Intermediate Proficency')
txt('- Java','Intermediate Proficency')
txt('- Python','Intermediate Proficency')
txt('- HTML & CSS','Intermediate Proficency')

st.markdown('## Internships')
txt('- Samsung PRISM R&D Internship- Virtual', 'Jun-2021 - Mar-2022')
txt('- Sparks Foundation, Data Science and Business analytics Intern, Virtual', 'Sept-2021 - Oct2021')

st.markdown('## Projects')
handwritte = Image.open('images/handwritten.png')
nodemcu = Image.open('images/trolley.png')
col1, col2 = st.columns([2,3])
with col1:
  st.write('- Handwritten Digit Recognition using Tensorflow:')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('- Smart Trolley using Node-MCU')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
  st.write('##')
with col2:
  st.image(handwritte, width=400)
  st.image(nodemcu, width=400)

st.write('# Social Media')
txt2('LinkedIn', 'https://www.linkedin.com/in/ruthul-jindal-s-37141a21a/')
txt2('GitHub', 'https://github.com/ruthul-jindal17')

st.markdown('## Queries:')
st.write('Feel Free to ask your doubs here!')
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style1.css")

contact_form = """
<form action="https://formsubmit.co/ruthuljindal17@gmail.com" method="POST">
  <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_col, right_col = st.columns(2)
with left_col:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_col:
    st.empty()
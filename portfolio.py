import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Prem Ayer | AI Portfolio",
    page_icon="🤖",
    layout="wide",
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
<style>
    /* Global Text Styles */
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2563eb;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 5px;
    }
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 5px 15px;
        margin: 5px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Contact & Links) ---
with st.sidebar:
    st.title("Prem Ayer")
    st.write("📍 **Sohna, Haryana, India**")
    st.write("📧 premsinghayer270@gmail.com")
    st.write("📞 935-47747-42")
    
    st.markdown("---")
    st.subheader("Socials")
    st.link_button("LinkedIn Profile", "https://linkedin.com/in/prem-ayer-95477a299")
    st.link_button("GitHub Profile", "https://github.com/PremAyer")
    
    st.markdown("---")
    st.write("Built with pure Python & Streamlit 🐍")

# --- MAIN CONTENT ---

# HERO SECTION
st.title("Hi, I'm Prem Ayer 👋")
st.subheader("Data Scientist")
st.write("""
As a BTech CSE student, I have a solid understanding of **Artificial Intelligence**, **Machine Learning**, 
and **Deep Learning**. I am passionate about harnessing AI to drive innovation and create impactful 
solutions in real-world applications.
""")

st.divider()

# SKILLS SECTION
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Languages & Core:**")
    st.markdown("""
    <span class="skill-tag">Python</span>
    <span class="skill-tag">SQL</span>
    <span class="skill-tag">Data Analysis</span>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("**AI & Specialization:**")
    st.markdown("""
    <span class="skill-tag">Machine Learning</span>
    <span class="skill-tag">Deep Learning</span>
    <span class="skill-tag">NLP</span>
    <span class="skill-tag">Generative AI</span>
    <span class="skill-tag">RAG</span>
    """, unsafe_allow_html=True)

st.divider()

# PROJECTS SECTION
st.header("🚀 Featured Projects")

# Project 1
with st.container():
    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("Veda Well Chatbot")
        st.caption("Bridging Ancient Wisdom with AI")
        st.info("Tech: LLMs, RAG, GenAI")
    with c2:
        st.write("""
        An AI assistant that uses **LLMs and RAG** (Retrieval-Augmented Generation) to provide easy access 
        to ancient Indian knowledge, specifically **Ayurveda and Atharvaveda**.
        * Currently supports English; Hindi integration planned.
        * Demonstrates ability to handle custom knowledge bases with GenAI.
        """)

# Project 2
with st.container():
    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("Chest X-ray Diagnostic")
        st.caption("AI-Powered Healthcare Tool")
        st.info("Tech: Deep Learning, DenseNet121, Grad-CAM")
    with c2:
        st.write("""
        A diagnostic web tool to automatically detect **Tuberculosis (TB)** from chest X-rays.
        * **Model:** Uses DenseNet121 architecture for high accuracy.
        * **Explainability:** Implements **Grad-CAM** to visualize and highlight important regions in the X-rays, helping doctors trust the model.
        """)

st.divider()

# EXPERIENCE & EDUCATION
st.header("🎓 Education & Experience")

tab1, tab2 = st.tabs(["Education", "Experience"])

with tab1:
    st.subheader("K.R. Mangalam University")
    st.write("**B.Tech in Computer Science (AI & ML)** | Sept 2022 - May 2026")
    st.write("*Building a strong foundation in complex problem solving and AI technologies.*")
    
    st.subheader("Morning Glory School")
    st.write("**Class 12th (PCM)** | April 2020 - May 2021")

with tab2:
    st.subheader("App Development Intern")
    st.write("**Younity.in** | 15 Days")
    st.write("Gained hands-on experience in the basics of App Development using Thunkable.")

st.divider()

# CERTIFICATIONS
st.header("📜 Certifications")
st.markdown("""
* **Deep Learning** - Samatrix.io
* **Data Analysis with Python** - IBM
* **App Development** - Younity.in
""")


st.divider()
st.header("📫 Get In Touch")

contact_form = """
<form action="https://formspree.io/f/mgoegjoq" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width:100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <input type="email" name="email" placeholder="Your Email" required style="width:100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <textarea name="message" placeholder="Your Message" required style="width:100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; height: 100px;"></textarea>
     <button type="submit" style="background-color: #2563eb; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
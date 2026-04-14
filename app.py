import streamlit as st

from ner_model import load_ner, redact_names, highlight_text
from file_handler import extract_text, export_file

### Fetch and cache model
@st.cache_resource
def get_model():
    return load_ner()

ner = get_model()

### Streamlit App
st.set_page_config(
    page_title="Redactor and Highlighter",
    page_icon="🛡️",
    layout="wide"
)

st.title("Redaction and Highlighting Tool")

### Sidebar Settings
st.sidebar.header("Settings")

redact_per = st.sidebar.checkbox("Person (PER)", True)
redact_loc = st.sidebar.checkbox("Location (LOC)", False)
redact_org = st.sidebar.checkbox("Organization (ORG)", False)

mode = st.sidebar.radio(
    "Output Mode",
    ["Redacted Text", "Highlighted Text"]
)

labels = []
if redact_per:
    labels.append("PER")
if redact_loc:
    labels.append("LOC")
if redact_org:
    labels.append("ORG")

### File Upload
uploaded = st.file_uploader("Upload file", type=["txt", "docx", "pdf"])

text = None
file_type = None

if uploaded:
    file_type = uploaded.name.split(".")[-1].lower()
    text = extract_text(uploaded, file_type)
else:
    text = st.text_area("Or paste text here")

### File Processing
if st.button("Process", use_container_width=True):

    if not text.strip():
        st.warning("No input provided.")
        st.stop()

    entities = ner(text)

    if mode == "Redacted Text":
        result = redact_names(text, entities, labels)

        st.text_area("Output", result, height=250)

        if file_type:
            file_data = export_file(result, file_type)
            st.download_button(
                "Download File",
                file_data,
                file_name=f"redacted.{file_type}",
                mime="application/octet-stream"
            )

    else:
        html = highlight_text(text, entities, labels)
        st.markdown(html, unsafe_allow_html=True)

        st.download_button(
            "Download HTML",
            html,
            file_name="highlighted.html"
        )

    with st.expander("Debug"):
        st.json(entities)
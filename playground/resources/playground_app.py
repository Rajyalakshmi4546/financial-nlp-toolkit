import os

import streamlit as st

from financial-nlp-toolkit.core import name_to_title

st.set_page_config(page_title="Financial NLP Toolkit Playground", page_icon=":arrow_forward:")

st.title("Financial NLP Toolkit Playground")

CUSTOM_STREAMLIT_CSS = """
div[data-testid="stBlock"] button {
  width: 100% !important;
  margin-bottom: 20px !important;
  border-color: #bfbfbf !important;
}
"""

# Add custom css settings
st.markdown(f"<style>{CUSTOM_STREAMLIT_CSS}</style>", unsafe_allow_html=True)

BADGES = """
<a href="https://gitHub.com/Rajyalakshmi Nelakurthi/financial-nlp-toolkit" title="Star Repo"><img src="https://img.shields.io/github/stars/Rajyalakshmi Nelakurthi/financial-nlp-toolkit.svg?logo=github&style=social"></a>
<a href="https://twitter.com/mltooling" title="Follow on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social&label=Follow"></a>
<a href="ttps://mltooling.substack.com/subscribe" title="Subscribe to newsletter"><img src="http://bit.ly/2Md9rxM"></a>
"""
st.markdown(BADGES, unsafe_allow_html=True)

st.markdown(
    "Financial NLP Toolkit enables you to instantly to turn your python functions into microservices with auto-generated HTTP API, interactive UI, and more."
    + " You can explore some examples below 👇"
)

DEFAULT_DEMO = "hello_world"

demos = [str(dir) for dir in filter(os.path.isdir, os.listdir(os.curdir))]

title_to_demo = {}

demo_titles = []
default_index = 0
for i, demo in enumerate(demos):
    if demo == DEFAULT_DEMO:
        # Use hello world as default
        default_index = i
    demo_title = name_to_title(demo)
    title_to_demo[demo_title] = demo
    demo_titles.append(demo_title)

selected_demo_title = st.selectbox(
    "Select Demo", options=demo_titles, index=default_index
)
selected_demo = title_to_demo[selected_demo_title]


def open_link(url: str, new_tab: bool = True) -> None:
    """Hack to open a new web page with a streamlit button."""
    from bokeh.models.widgets import Div

    # From: https://discuss.streamlit.io/t/how-to-link-a-button-to-a-webpage/1661/3
    if new_tab:
        js = f"window.open('{url}')"  # New tab or window
    else:
        js = f"window.location.href = '{url}'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


col1, col2 = st.beta_columns(2)
with col1:
    open_ui = st.button("🌅 Launch UI")
    # st.code("financial-nlp-toolkit launch-ui app:seperate_audio", language="plain")
with col2:
    open_api = st.button("🔌 Launch API")
    # st.code("financial-nlp-toolkit launch-api app:seperate_audio", language="plain")

col1, col2 = st.beta_columns([1, 2])

with st.beta_expander("Source Code", expanded=True):
    with open(os.path.join(selected_demo, "app.py"), encoding="UTF-8") as f:
        st.code(f.read(), language="python")

with st.beta_expander("Requirements"):
    with open(os.path.join(selected_demo, "requirements.txt"), encoding="UTF-8") as f:
        st.code(f.read(), language="plain")

with st.beta_expander("Export this Financial NLP Toolkit"):
    st.markdown(
        "Financial NLP Toolkit provides capabilities to seamlessly export your services into portable, shareable, and executable files or Docker images."
    )
    col1, col2 = st.beta_columns([1, 2])
    with col1:
        open_zip_export_feature = st.button("📦 Export to ZIP")

    with col2:
        st.code(
            f"financial-nlp-toolkit export app:{selected_demo} my-financial-nlp-toolkit.zip", language="plain"
        )

    col1, col2 = st.beta_columns([1, 2])
    with col1:
        open_docker_export_feature = st.button("🐳 Export to Docker")

    with col2:
        st.code(
            f"financial-nlp-toolkit export app:{selected_demo} --format docker my-financial-nlp-toolkit:latest",
            language="plain",
        )

if open_ui:
    open_link(f"../{selected_demo}_ui/")
    open_ui = False

if open_api:
    open_link(f"../{selected_demo}_api/")
    open_api = False

if open_docker_export_feature:
    open_link("https://github.com/Rajyalakshmi Nelakurthi/financial-nlp-toolkit/issues/4")
    open_docker_export_feature = False

if open_zip_export_feature:
    open_link("https://github.com/Rajyalakshmi Nelakurthi/financial-nlp-toolkit/issues/3")
    open_zip_export_feature = False

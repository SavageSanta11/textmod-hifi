import streamlit as st
import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

colors = {
    "Vivid Orange": "#FF5733",
    "Bright Blue": "#335BFF",
    "Vivid Green": "#33FF57",
    "Bright Pink": "#FF33A1",
    "Vibrant Yellow": "#FFD133"
}

# Initialize session states for buttons
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

if 'explained' not in st.session_state:
    st.session_state['explained'] = False

# Set page title and layout
st.set_page_config(page_title="Text Moderation Demo", layout="centered")

# Header
st.title("Text Moderation Demo")
st.markdown(
    """
    ### How To Start
    * Users can input text into a designated text area.

    ### How it Works
    * The system employs a Large Language Model (LLM) to analyze the input text and provide a moderation result. The model assesses the text for potential harmfulness based on various criteria. 
    * Users can choose from various LLMs to compare results.

    ### Moderation Result Display
    * The system presents the moderation result, which includes the classification of the text (e.g., "hateful" or "not hateful").
    * Next, you can view a breakdown of the moderation scores for different hate categories (sexual, toxic, violent, discriminatory, insulting).
    * Finally, you can identify and analyse the target groups of the hateful text (e.g., religion, women, race).

    ### Further Explanation and Counter-Narrative Generation
    * For a more verbose analyses of the input, users can avail an explanation of the moderation result, outlining the reasons for the classification.
    * Finally, to understand how to counter such an attack, the user can generate a counter-narrative to the hateful text, providing an alternative perspective or suggestion.
    """
)
st.divider()
st.subheader("Input Text")

response = st.text_area("Type here", max_chars=100)

st.selectbox("Model", ["SeaLLMs-v3-7B-Chat", "SEA-LION", "LionGuard"])

# ML moderation classes (dummy values)
ml_moderation_classes = {
    "sexual": 0.7,
    "toxic": 0.5,
    "violent": 0.4,
    "discriminatory": 0.1,
    "insulting": 0
}

# Display Submit button
if st.button("Submit"):
    st.session_state['submitted'] = not st.session_state['submitted']

if st.session_state['submitted']:
    results = ml_moderation_classes

    st.subheader("Moderation Result")
    st.markdown("This text was found to be :red[hateful]")
    
    st.divider()

    # Display results
    st.subheader("Hate Classes")

    st.markdown(
        f"<span style='color:{colors['Vivid Orange']}'>Women</span> "
        f"<span style='color:{colors['Vivid Orange']}'>who are Muslim</span> "
        f"<span style='color:{colors['Vivid Green']}'>really deserve the</span> "
        f"<span style='color:{colors['Bright Pink']}'>rape they suffer at the hands of their husbands</span> ",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Sexual", results["sexual"])
        ColourWidgetText('Sexual', '#FF5733')  # colour only metric text

    with col2: 
        st.metric("Toxic", results["toxic"])
        ColourWidgetText('Toxic', '#33FF57')

    with col3: 
        st.metric("Violent", results["violent"])
        ColourWidgetText('Violent', '#FF33A1')

    with col4:
        st.metric("Discriminatory", results["discriminatory"])
        ColourWidgetText('Discriminatory', '#FFD133')

    st.divider()

    st.subheader("Target Groups")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Religion", 0.8)

    with col2: 
        st.metric("Women", 0.3)

    with col3: 
        st.metric("Race", 0.2)

    st.divider()

    st.subheader("Need Help Interpreting the Results?")

    # Display Explain Result button
    if st.button("Explain Result"):
        st.session_state['explained'] = not st.session_state['explained']

    if st.session_state['explained']:
        st.write("**Targeted Group**: The post targets people who wear headscarves, particularly associated with Muslim women.\n\nDerogatory Imagery/Language: The statement uses threatening language, suggesting violent harm towards individuals who wear headscarves.\n\nImpact on Bias/Stereotypes: This statement reinforces harmful stereotypes and prejudices against individuals who wear headscarves, potentially inciting fear and hostility towards Muslim women.\n\nIn summary, this post is hateful as it promotes violence and prejudice against a specific religious group.")

    st.divider()

    st.subheader("Generate Counter-Narrative")

    # Similar logic for Generate Counter-Narrative button can be added here
    if st.button("Generate Counter-Narrative"):
        # Example logic for handling counter-narrative generation
        st.write("Every person, regardless of their gender, religion, or marital status, deserves to be treated with dignity and respect. Consent is fundamental in any relationship, and no one should ever be subjected to violence or abuse. We must stand together to promote understanding, empathy, and the human rights of all individuals.")

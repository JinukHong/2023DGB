import streamlit as st
from web_demo2 import show_financial_advisor  # Importing the function
from survey import save_results, show_survey



def main():
    #show_financial_advisor()
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'show_submit_button' not in st.session_state:
        st.session_state.show_submit_button = False
    
    if st.session_state.submitted:
        save_results()
        #fin_calender()
        show_financial_advisor()
    elif st.session_state.show_submit_button:
        if st.button("Submit"):
            st.session_state.submitted = True
        if st.button("Go back to the last question"):
            st.session_state.show_submit_button = False
            st.session_state.current_question = len(questions) - 1
    else:
       show_survey()
    
    hide_footer_style = """
<style>
#MainMenu {visibility: hidden;} 
div.block-container {padding-top:1rem;}
div.block-container {padding-bottom:3rem;}
}
</style>
"""
    st.markdown(hide_footer_style, unsafe_allow_html=True)

    footer_setup = '''
<script>
// To break out of iframe and access the parent window
const streamlitDoc = window.parent.document;

// Make the replacement
document.addEventListener("DOMContentLoaded", function(event){
    const footer = streamlitDoc.getElementsByTagName("footer")[0];
    footer.innerHTML = `
        Provided by 
        <a target="_blank" class="css-z3au9t egzxvld2">Team MiZi(미지)</a>
        <img src="https://i.namu.wiki/i/RMFfYwm6uMpMAbnzBf9ZKX2mM3ro6TzG-FSCPOnyxT5pZQdUc0Ftp6pq3wGuHcBz74ly-Nt7JwkypXDNS3kqV9yfXVoeziDMJxlWIwsH816HwkzN4kGTuCElz4iMUvg6Ckdjy91lGUZ-UDcwghpR0g.webp" alt="DGB" height="30">
        
    `;
});
</script>
'''

    st.components.v1.html(footer_setup)
    
if __name__ == "__main__":
    main()

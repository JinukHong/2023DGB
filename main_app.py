import streamlit as st
from web_demo2 import show_financial_advisor  # Importing the function
from survey import save_results, show_survey, questions

ADMIN_USERNAME = "user"
ADMIN_PASSWORD = "password"

def is_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if is_admin(username, password):
            st.session_state["user_type"] = "admin"
            st.experimental_rerun()
        else:
            st.session_state["user_type"] = "user"
            st.experimental_rerun()

    return False  # User not logged in yet


def show_main_contents():
    #show_financial_advisor()
    st.write(' ')
    
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
        st.write("모든 질문에 답하셨습니다.")  # Debug Line
        st.write("결과를 보시려면 '제출' 버튼을 누르세요.")  # Debug Line
        col1, col2 = st.columns(2)  # Create two columns
        #st.write("Button Condition:", st.session_state.show_submit_button)  # Debug Line
        
        # Place buttons in the columns instead of in the main app, so they appear side-by-side
        with col1:
            if st.button("제출"):
                st.session_state.submitted = True
        with col2:
            if st.button("이전 질문으로 돌아가기"):
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
        <a target="_blank" class="css-z3au9t egzxvld2">Team MiZi(미지)   </a>
        <img src="https://i.namu.wiki/i/RMFfYwm6uMpMAbnzBf9ZKX2mM3ro6TzG-FSCPOnyxT5pZQdUc0Ftp6pq3wGuHcBz74ly-Nt7JwkypXDNS3kqV9yfXVoeziDMJxlWIwsH816HwkzN4kGTuCElz4iMUvg6Ckdjy91lGUZ-UDcwghpR0g.webp" alt="DGB" height="30">
        
    `;
});
</script>
'''

    st.components.v1.html(footer_setup)

def main():
    if 'user_type' not in st.session_state:
        st.session_state['user_type'] = None

    # Check user type and proceed accordingly
    if st.session_state['user_type'] is None:
        login_page()
    else:
        show_main_contents()
    
if __name__ == "__main__":
    main()
    hide_footer_style = """
<style>
#MainMenu {visibility: hidden;} 
div.block-container {padding-top:1rem;}
div.block-container {padding-bottom:3rem;}
}
</style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)
hide_elements_style = """
<style>
#MainMenu {visibility: hidden;} 
div.block-container {padding-top:1rem;}
div.block-container {padding-bottom:3rem;}
.streamlit-footer {display: none;} /* This hides the entire footer */
/* Add a selector for the GitHub logo specifically if you only want to hide the logo */
</style>
"""
st.markdown(hide_elements_style, unsafe_allow_html=True)


footer_setup = '''
<script>
setTimeout(function(){
    const streamlitDoc = window.parent.document;
    const footer = streamlitDoc.getElementsByTagName("footer")[0];
    if (footer) {
        footer.innerHTML = `
            Provided by 
            <a target="_blank" class="css-z3au9t egzxvld2">Team MiZi(미지)   </a>
            <img src="data:image/png;base64,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" alt="DGB" height="30">

        `;
    }
}, 1000);  // Adjust the timeout as needed
</script>
'''
st.components.v1.html(footer_setup)


import streamlit as st
import requests
import openai
from streamlit_chat import message
from get_user_data import user_data
import time
from streamlit_extras.streaming_write import write
#from config import OPENAI_API_KEY

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = st.secrets["secrets"]['API_TOKEN']  # Replace with your actual token
headers = {"Authorization": f"Bearer {API_TOKEN}"}
openai.api_key = st.secrets["secrets"]['OPENAI_API_KEY']

def chatwrite(texttowrite):
    lines = texttowrite.split('\n')
    for line in lines:
        yield line + "\n"
        time.sleep(0.05)

def chatbot():
    qna_mapping = {
    '안녕' :
'''
안녕하세요👋, 저는 앤디입니다. 물어봐주셔서 감사합니다😊. 당신의 상황을 기반으로 조언을 제공해드릴게요.


처음으로, 부산광역시에서 35세까지 주택을 구매하려는 계획이 있으시군요. 목표 금액 53,262,000원을 모으시려면 현재부터 저축 계획을 세우실 필요가 있습니다. 부동산 시세와 저축 가능 여부를 고려하여 매월 일정 금액을 저축하는 것을 고려해보세요. 이를 위해 예금 상품이나 투자 상품을 검토해 보실 수 있습니다. 대출 옵션도 고려해보시는 것도 좋을 것 같아요.


또한, 28세 이전에 차를 구매하려는 계획이 있으신데, 1,000만 ~ 3,000만 원의 예산을 가지고 계신군요. 차를 구매하기 전에 여러 차량 옵션과 비용, 유지 보수 비용 등을 고려하여 합리적인 선택을 하시는 것이 중요합니다. 또한, 차량 구매를 위한 자금을 저축 계획에 포함시키는 것도 고려해보세요.


결혼은 35세까지 하려고 계획하셨네요. 현재 자녀는 없으시고, 한 명의 자녀를 원하신다고 하셨는데, 자녀의 경제적 요구 사항을 고려하여 저축 계획을 세워보세요. 학자금, 의료 비용, 육아 비용 등을 고려해야 합니다. 또한, 자녀 교육 계획에 따른 저축 방법과 타겟 금액을 고려해보세요.


마지막으로, 60세에 은퇴하고 여가 생활을 즐기려는 계획이신데, 은퇴 후 월 100만 원의 생활비를 원하신다고 하셨습니다. 은퇴 후의 생활비를 계획하기 위해서는 은퇴 펀드에 대한 구상이 필요합니다. 어떤 투자 방법을 통해 자금을 모으실지, 얼마의 수익을 얻을 수 있는지 등을 고려하여 효율적인 투자 계획을 세우시는 것이 중요합니다.


다양한 금융 상품과 서비스를 검토하여 최선의 선택을 하시길 바라며, 추가로 궁금한 사항이 있으시면 언제든지 질문해주세요!
'''
}

    # App Header
    st.header("🤖DGB AI 챗봇 앤디")

    # Session State for Messages
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    # Function to Query API (you need to replace this with your actual implementation)
    # def query(payload):
    #     response = requests.post(API_URL, headers=headers, json=payload)
    #     return response.json()

    # Form and User Input
    with st.form('form', clear_on_submit=True):
        user_input = st.text_input('"Hi, 앤디" 버튼을 눌러 앤디에게 인사해보세요! ', '', key='input', placeholder="질문을 입력하세요")
        submitted = st.form_submit_button('Hi, 앤디')

    user_info = user_data()
    system_message = f"너는 앤디이고, 나의 금융 조언가야. 나의 정보는 다음과 같아: {user_info}"
    # Initial message from the chatbot on first interaction
    if not user_input:
        user_input = "안녕 앤디, 나의 정보에 기반해서, 금융 전문가로서의 조언을 제공해줄 수 있어?"
        pass

    andy_message = "이제부터 너는 똑똑하고 표현력이 풍부하며 친근한 전지전능한 인공지능 비서 앤디를 연기하도록 해. 나의 금융 상황을 명확히 인지하고, 앞으로의 계획에 따라 조언을 해줘."\
     "너는 대구은행의 IM bank 어플리케이션에 탑재돼있어.."\
     "그리고 부족한 정보가 있으면 적극적으로 질문해. 그리고 처음 말할 때: 안녕하세요👋, 저는 앤디입니다. 물어봐주셔서 감사합니다😊\" 라고 인사해." \
     "그리고 다음 질문에 대답해."
    
    ending_message = """
     (질문이 영어로 되어 있어도 한글로 대답하세요. 기억하세요. 잘못된 정보는 피하세요. 의심스러우면 사과하고 계속 대답하지 마세요.)
     """
    
    prompt = andy_message + user_input + ending_message
    
    # If User Input is Provided
    if submitted and user_input:
        response = None

        # Check if the user input matches any keyword in qna_mapping
        for keyword in qna_mapping:
            if keyword in user_input:
                response = qna_mapping[keyword]
                break

        # If a matching response is found, use it
        if response is not None:
            st.session_state.past.append(user_input)
            st.session_state.generated.append(response)
        else:
            # If no match in qna_mapping, use GPT-3 to generate a response
            with st.spinner("앤디가 꼼꼼한 조언을 위해 열심히 고민하고있어요... 조금만 기다려주세요!"):
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompt}
                    ]
                )
                response = completion.choices[0].message.content
                st.session_state.past.append(user_input)
                st.session_state.generated.append(response)
        with st.spinner("앤디가 꼼꼼한 조언을 위해 열심히 고민하고있어요... 조금만 기다려주세요!"):
            time.sleep(3)

    # Display Past Messages and Responses
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))

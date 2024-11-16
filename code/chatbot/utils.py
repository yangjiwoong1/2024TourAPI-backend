from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def get_chat_response(user_message):

    openai_api_key = os.getenv("OPENAI_API_KEY")

    chat = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        temperature=0, 
        max_tokens=512,  # 1000자 정도 됨
        openai_api_key=openai_api_key
    )
        #이거 쓰면 챗봇이 말하는 거처럼 볼 수 있음
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant in this Tour Application. Answer the following question in korean: {user_message}"
    )

    response = chat(prompt.format_messages(user_message=user_message))

    return response.content

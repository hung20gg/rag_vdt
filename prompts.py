from llm.llm import *
from llm.llm_utils import *


def RAG_QA(llm, question, context, choices):
    choices = [f"{i+1}. {choice}" for i, choice in enumerate(choices)]
    choices = '\n'.join(choices)
    user_prompt = f"""
    Hãy chọn phương án đúng nhất cho câu hỏi sau đây
    {question}
    Các phương án là:
    {choices}\
    Đây là một số thông tin mà bạn có thể dùng để truy xuất
    {context}
    """
    output = """
    Đáp án của bạn phải là một số từ 1 đến 4 ở dưới dạng JSON:
    ```
    [{"answer": 1}]
    ```
    Only return JSON object.
    """
    messages = [
        {'role': 'system', 'content': 'Bạn là một trợ lý có nhiệm vụ trả lời câu hỏi'},
        {'role':'user', 'content': user_prompt + output}
    ]
    # print(messages)
    response = llm(messages)
    # return response
    return get_json_from_text_response(response)


def RAG_QA_TL(llm,question,context):
    user_prompt = f"""
    Hãy trả lời câu hỏi sau đây:
    {question}
    Đây là một số thông tin mà bạn có thể dùng để truy xuất
    {context}.
    Khi đưa ra câu trả lời, hãy trích dẫn các thông tin khiến bạn có câu trả lời như vậy ngay trong câu trả lời.\
    Nếu bạn không biết, hãy trả lời là 'Tôi không biết'
    """
    output_instruction = """
    Câu trả lời và trích xuất của bạn phải TRONG CÙNG MỘT ĐOẠN VĂN ngắn bằng Tiếng việt, lưu dưới dạng JSON.
    ```
    [{"đoạn văn": "thay vào đây câu trả lời của bạn và thông tin trích xuất bằng tiếng Việt"}]
    ```
    Chỉ trả ra JSON. JSON chỉ chứa ONLY key là "đoạn văn"
    """
    messages = [
        {'role': 'system', 'content': "Bạn là một trợ lý có nhiệm vụ trả lời câu hỏi.\
        Bạn chỉ biết Tiếng Việt."},
        {'role':'user', 'content': user_prompt + output_instruction}
    ]
    response = llm(messages)
    return get_json_from_text_response(response)



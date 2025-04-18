# Copied from the prompt engineering notebook
def get_chatbot_response(client,model_name,messages,temperature=0):
    input_messages = []
    for message in messages:
        input_messages.append({"role": message["role"], "content": message["content"]})

    response = client.chat.completions.create(
        model=model_name,
        messages=input_messages,
        temperature=temperature,
        top_p=0.8,
        max_tokens=2000,
    ).choices[0].message.content
    
    return response

# Copied from the prompt engineering notebook
def get_embedding(embedding_client,model_name,text_input):
    output = embedding_client.embeddings.create(input = text_input,model=model_name)
    
    embedings = []
    for embedding_object in output.data:
        embedings.append(embedding_object.embedding)

    return embedings

def double_check_json_output(client,model_name,json_string):
    prompt = f""" You will check this json string and correct any mistakes that will make it invalid. Then you will return the corrected json string. Nothing else. 
    If the Json is correct just return it.

    If there is any text before or after the JSON string, reomove it.
    Do NOT return a single letter outside of the json string.
    Make sure that each key is enclosed in double quotes.
    The first character to be written is an open curly brace of the JSON and the last character to be written is the closing curly brace.
    
    You should check the json string for the following text between triple backticks:
    ```
    {json_string}
    ```
    """

    messages = [{"role": "user", "content": prompt}]
    response = get_chatbot_response(client,model_name,messages)
    response = response.replace("`","")

    return response
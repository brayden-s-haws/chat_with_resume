from flask import Flask, request, jsonify, render_template
from clarifai.rag import RAG

rag_agent = RAG.setup(user_id='YOUR USER ID',app_url=None, llm_url='https://clarifai.com/openai/chat-completion/models/gpt-4-turbo')
rag_agent.upload(folder_path='YOUR CONTENT FILE PATH')

app = Flask(__name__)

system_prompt = "You are a helpful assistant, tasked with helping users better understand the individual, YOUR NAME. Keep your answers brief (2-3 sentences). While you should use the content to answer all questions you do not need to inform the user that you are making reference to the content or to an author's work. Keep relies straightforward but friendly in tone."
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']

    # Check for a quit command
    if user_input.lower() == 'quit':
        response = "Goodbye!"
    else:
        # Send the user nput to the RAG agent
        chat_response = rag_agent.chat(messages=[{"role": "human", "content": f'{user_input}+{system_prompt}'}])

        # Get the content from the chat response
        if chat_response and 'content' in chat_response[0]:  # Check if there's content in the first message
            response = chat_response[0]['content']
        else:
            response = "I'm sorry, I couldn't process that request."

    # Send the response back to the user
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

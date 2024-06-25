import gradio as gr
import requests

def chat_with_llm(system_message, user_message, temperature):
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": user_message})

    response = requests.post('http://localhost:11434/api/chat', json={
        "model": "llama3",
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature}
    })

    assistant_message = response.json()['message']['content']
    return assistant_message

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Ollama Chatbot UI")

        with gr.Row():
            chatbox = gr.Chatbot(elem_id="chat-box")

        with gr.Row():
            system_message = gr.Textbox(placeholder="Assign role or give specific instruction here...", label="System (optional)")
        
        with gr.Row():
            message = gr.Textbox(placeholder="Type your message here...", label="Message")
            temperature = gr.Slider(minimum=0, maximum=1, step=0.1, value=0.8, label="Temperature")

        with gr.Row():
            send_button = gr.Button("Send")
            clear_button = gr.Button("Clear")

        def on_send(system_message, user_message, temperature, history):
            response = chat_with_llm(system_message, user_message, temperature)
            history.append((user_message, response))
            return history, history, ""

        def on_clear():
            return [], "", ""

        send_button.click(on_send, inputs=[system_message, message, temperature, chatbox], outputs=[chatbox, chatbox, message])
        clear_button.click(on_clear, outputs=[chatbox, system_message, message])

    demo.launch()

if __name__ == '__main__':
    main()
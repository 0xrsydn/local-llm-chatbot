# Local LLM Chatbot

This is a simple chatbot application built using Gradio and the Ollama REST API. The chatbot interface allows users to send messages and receive responses from the LLM model. The application also supports optional system messages to provide context and can be customized using a temperature slider.

## Features

- Interactive chatbot UI using Gradio
- Supports system messages for context
- Adjustable temperature slider for response variation
- Clear button to reset the conversation history

## Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- [Ollama](https://ollama.com/download)

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/0xrsydn/local-llm-chatbot.git
    cd local-llm-chatbot
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. **Install the Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install and Run Ollama:**
   - Download Ollama from [here](https://ollama.com/download) and install it.
   - Open the terminal and run the following command to download and run the `llama3` model:
     ```bash
     ollama run llama3
     ```
   - Alternatively, if you already have Ollama installed, you can run:
     ```bash
     ollama serve
     ```
   - To download the model without running it immediately, use:
     ```bash
     ollama pull llama3
     ```

5. **Run the Application:**
    ```bash
    python app.py
    ```
    
6. **Open your web browser and navigate to the URL provided by Gradio (usually http://127.0.0.1:7860).**

### Customizing the Model

The default model used in this application is `llama3`. You can change the model in the code based on the available models you have with Ollama by using:
```bash
ollama run {llmname}
```

## Files and Directories

- `app.py`: Main application file containing the Gradio interface and backend logic.
- `requirements.txt`: List of Python dependencies required for the project.

## Usage

1. **System Message (Optional):** You can provide a system message to set the context for the LLM. This is optional and can be left empty.
2. **Message:** Type your message here and press Enter to send.
3. **Temperature Slider:** Adjust the slider to set the temperature for response variation.
4. **Clear Button:** Click the "Clear" button to reset the conversation history.

## Example

Here's an example of how to use the chatbot:

1. Start the application by running `python app.py`.
2. Open your browser and go to the provided URL (e.g., http://127.0.0.1:7860).
3. Enter a system message (optional) and type your message in the input box.
4. Adjust the temperature slider as needed.
5. Press send button to send the message.
6. The chatbot will respond, and the conversation history will be displayed.
7. Use the "Clear" button to reset the conversation history.


## Tech Stacks

- [Gradio](https://gradio.app) for the interactive UI components.
- [Ollama](https://ollama.com) for the Local LLM REST API.

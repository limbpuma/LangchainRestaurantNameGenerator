

Restaurant Name and Menu Item Generator
This Streamlit application uses the LangChain library to generate creative names and menu items for various cuisines. It's a fun way to explore potential restaurant ideas or just to see what interesting combinations the AI comes up with!

Features
Generate restaurant names and menu items based on selected cuisine.
Multilingual support with language selection.
Easy-to-use, interactive web interface.
Requirements
To run this application, you'll need the following packages:


streamlit==1.29.0
openai==1.3.8
langchain==0.0.348
requests==2.31.0
pandas==2.1.4
numpy==1.26.2
jsonschema==4.20.0


Installation
1.Clone the repository:
git clone [repository-url]

2.Install the required packages:
pip install -r requirements.txt

Usage
To start the application, navigate to the cloned directory and run:
streamlit run app.py

How It Works
The application interfaces with OpenAI's GPT models through LangChain.
Users select a language and a cuisine type.
AI generates a unique restaurant name and a list of suggested menu items for the selected cuisine.
Files Description
app.py: The main Streamlit application file.
helpers.py: Contains functions for generating restaurant names and menu items using LangChain and OpenAI.
texts_{language_code}.json: JSON files for language support (e.g., texts_en.json, texts_es.json, texts_de.json).
Contributing
Your contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests. You can also open issues for bugs or feature suggestions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

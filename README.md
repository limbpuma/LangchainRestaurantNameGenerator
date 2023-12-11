
Restaurant Name and Menu Item Generator
This Streamlit application leverages the LangChain library to creatively generate restaurant names and menu items based on various cuisines. Ideal for brainstorming restaurant concepts or just for fun!

🌟 Features
Creative Generation: Produce unique restaurant names and menu items.
Multilingual Support: Options for English, Spanish, and German.
User-Friendly Interface: An interactive and intuitive Streamlit web interface.
📋 Requirements
Ensure you have the following packages installed:


streamlit==1.29.0
openai==1.3.8
langchain==0.0.348
requests==2.31.0
pandas==2.1.4
numpy==1.26.2
jsonschema==4.20.0


🚀 Installation
Start by cloning this repository, then install the necessary Python packages:

git clone https://github.com/limbpuma/LangchainRestaurantNameGenerator.git
cd LangchainRestaurantNameGenerator
pip install -r requirements.txt


🖥️ How to Use
Run the application using Streamlit:
streamlit run app.py
Navigate to the provided local URL to access the application.

🔍 How It Works
The AI model is powered by OpenAI, facilitated by the LangChain library.
Users select their preferred language and cuisine.
AI generates a restaurant name and a list of suggested menu items accordingly.
📁 File Structure
app.py: The main file with the Streamlit interface.
helpers.py: Back-end logic for AI generation.
texts_{language_code}.json: Language files for internationalization.
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

📜 License
Distributed under the MIT License. See LICENSE for more information.

📬 Contact

Project Link: https://github.com/limbpuma/LangchainRestaurantNameGenerator
Online Link: https://langchainrestaurantnamegenerator-dp.streamlit.app/
linkedin dev: https://www.linkedin.com/in/limber-martinez-developer/


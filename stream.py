#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing errored libraries
import nltk


import streamlit as st
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot.storage import StorageAdapter

import json

#get_text is a simple function to get user input from text_input
class stream50():

    def __init__(self):
        pass
        #self.input_path=frame  
        #self.weight_file_path=r"Downloads\weights_YOLO/yolov3_training_final.weights" 
        

    def get_text(self):
        input_text = st.text_input("You: ","So, what's in your mind")
        return input_text

    def process(self):
        st.sidebar.title("NLP Bot")
        st.title("""
        NLP Bot  
        NLP Bot is an NLP conversational chatterbot. Initialize the bot by clicking the "Initialize bot" button. 
        """)
        file_ = open(r"media/hairstyle.gif", "rb") #C:\Users\rishabh.pandey\Downloads\Tasks\Chatbot\streamlit/hairstyle.gif
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

        #Preprocess input
        bot = ChatBot('Buddy', read_only = True, storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters = [
                        {
                            'import_path': 'chatterbot.logic.BestMatch', #'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.TimeLogicAdapter'
                            'default_response': 'I am sorry, I do not understand. I am still learning. Please contact \'Team chatbot@hd.com\' for further assistance!',
                            'maximum_similarity_threshold': 0.90
                        }
                    ], preprocessors=['chatterbot.preprocessors.clean_whitespace', 'chatterbot.preprocessors.unescape_html', 'chatterbot.preprocessors.convert_to_ascii'],                database_uri='sqlite:///database.sqlite3')
        
        ind = 1
        if st.sidebar.button('Initialize bot'):
            trainer= ChatterBotCorpusTrainer(bot)
            trainer.train('chatterbot.corpus.english')
            st.title("Your bot is ready to talk to you")
            ind = ind +1
                
        user_input = self.get_text()
        if True:
            st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
        else:
            st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)
        
# object initialization
stream50_= stream50()

if __name__ == "__main__":
    stream50_.process()

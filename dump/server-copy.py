from flask import Flask, request, jsonify
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv
import os
load_dotenv()

email= os.getenv("email")
passwd= os.getenv("passwd")
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(email, passwd)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

print(chatbot.chat("Hi!").wait_until_done())

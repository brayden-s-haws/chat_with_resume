# Chat With Resume

## Description
This is an easy to setup and use web app that allows users to learn about you. You select the content you want them to have access to: resume, blog posts, GitHub content, etc. Users then interact with it through a chat interface.

## How It Works
This leverages [Clarifai's RAG agent](https://www.clarifai.com). It handles all the hard work of embedding and storing your content. They also manage the LLM model for you. The actual RAG setup is 4 lines of code, thanks to the infrastructre they provide. The rest of the code is mainly for creating and stylzing the web app.

By default the app looks something like this, but you can alter the code to change the appearance.
![CleanShot Safari-2024-05-14](https://github.com/brayden-s-haws/chat_with_resume/assets/58832489/69b6df6c-288e-48fb-a16e-97bde311a539)

If you want to try it out before builing your own, you can try out my version of the app [here](https://brayden-resume-bot.replit.app).

## Files

**main.py:** This file iniates the flask app and manages the interaction between the user and chatbot.

**index.html:** This file contains all the styling and frontend for the app.

## Setup

You first need to create a [Clarifai account](https://www.clarifai.com), it's free to get started.

#### Environment
* Install clarifai, llama_index, flask
* Add CLARIFAI_PAT as environment variable (more details on creating a PAT are found [here](https://docs.clarifai.com/clarifai-basics/authentication/personal-access-tokens).)
* Create a folder named 'content' and upload the files you want the app to use. The files need to be in pdf format.
* Once you finish updating files below, then deploy the app to the web.


#### app.py
* Add user_id on line 4. You can find your user_id in your Clarifai account settings.
* Add llm_url on line 4. (This is defaulted to use gpt4-turbo but you can change it to any supported model.)
* Add the file path for your 'content folder' to 'folder_path' on line 5.
# Add your name to the system prompt on line 9.


#### index.html
* Add your name to the H2 on line 51
* Fill out your intro and prompt examples on line 52
* Change chatbot name/icon on  line 79

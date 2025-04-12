# This will create a web page which analyzes image according to your model.

# Step 0: Run create_pet_model.py.  This will generate a pet_model.pkl file.

# Step 1: Go to https://huggingface.co and create a new login

# Step 2: Create a space by going to the Spaces tab and pressing the + New Space button

# Step 3: Locally clone your huggingface repo. You can find the info in ... and Clone Repository, and you will be
# cloning something like https://huggingface.co/spaces/einsteins-workshop/student-demo . For test purposes, you
# can use this one, ask the instructor for the acess token.  When setting up your own huggingface page, you will
# want to set up your own access token instead of the password.

# Step 4: In your local git repository that you set up in Step 3, add the dog.jpg, dog.jpg, dunno.jpg, pet_model.pkl,
# and copy this file to app.py.

# NOTE: your model files will likely be larger than the 10MB limit. To get around this, you'll need to install git-lfs
# See https://git-lfs.com/
# Once installed, you will want to run the commands:
# git lfs install
# git lfs track "*.pkl"
# git add .gitattributes

# Step 5: Create a requirements.txt file, with the following contents:
#
# fastai
# gradio
# torch

# Step 6: Add, commit, and push all files:
#
# git add .
# git commit -m "Initial model"
# git push

# Step 7: Go to your model page, and play with your new website.

# See https://dean-ew-cat-dog-classifier.hf.space/?__theme=system&deep_link=WhXmG48k47g for an example of a working
# demo

import gradio as gr
from fastai.vision.all import *


# The categorization method, which needs to be consistent with what is used to generate the model
def is_cat(x):
    return x.name[0].isupper()


# Create a hash that creates a dictionary that maps category to their probability.
def classify_image(img):
    pred, idx, probabilities = learn.predict(img)
    return dict(zip(categories, map(float, probabilities)))

# Load model from pkl file
learn = load_learner('pet_model.pkl')
categories = ('Dog', 'Cat')


# Create gradio web interface for app
image = gr.Image(label="Enter image to analyze")
label = gr.Label(label="Is it a cat or dog?")
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

interface = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
interface.launch()
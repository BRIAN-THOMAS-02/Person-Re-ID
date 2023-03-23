import streamlit as st
import torch
from PIL import Image
from subprocess import Popen, PIPE
import demo
#from demo import *
import evaluate
from evaluate import *

# Load the model
model_path = "model/ft_ResNet50/net_last.pth"
model = torch.load(model_path)

# Define the labels
labels = ['class1', 'class2', ..., 'class751']

# Set up the user interface
st.title('Person Re-Identification')
st.write('This app classifies people into 751 given input classes')
#uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])


# Convert the tensor to a NumPy array
CMC = CMC.numpy()
st.write('CMC[0] : ', CMC[0])
st.write('Rank@1 %f  : '% CMC[0])
st.write('Rank@5 %f  : '% CMC[4])
st.write('Rank@10 %f : '% CMC[9])
st.write('mAP        : ', ap/len(query_label))


def run_evaluate():
    with Popen(["python", "evaluate.py"], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            st.write(line.strip())

def run_demo():
    with Popen(["python", "demo.py", "--query_index", query_index], stdout=PIPE, bufsize=1, universal_newlines=True) as d:
        st.write(d)
        for line in d.stdout:
            st.write(line.strip())


# Add a dropdown to select the program to run
st.write()
st.write('Select a program to run')
options = ["Evaluate.py", "Demo.py"]
#program = st.selectbox('', options)
program = st.selectbox('', options)

# Add a button to run the selected program
if program == "Evaluate.py":
    if st.button("Run Program"):
        st.write('Running evaluate.py.....')
        run_evaluate()

elif program == "Demo.py":
    query_index = st.text_input("Enter Query Image : ")
    if st.button("Run Program"):
        st.write('Running demo.py......')
        run_demo()
        image_path = "demo/show_{}.png".format(query_index)
        st.image(image_path)



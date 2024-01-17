import streamlit as st

st.subheader("TITLE")                                         
st.title("Working on Streamlit")                             # Title

st.subheader("HEADER")                                         
st.header("Header - Working on Streamlit")                   # Header

st.subheader("SUBHEADER")                                       
st.subheader("Subheader - Working on Streamlit")             # Subheader

st.subheader("TEXT")                                             
st.text("Learning Streamlit")                                # Text                             

st.subheader("MARKDOWN")                                         
st.markdown("# Streamlit")                                   # Markdown
st.markdown("## Streamlit")                                  # Markdown
st.markdown("### Streamlit")                                 # Markdown
st.markdown("#### Streamlit")                                # Markdown

st.subheader("SUCCESS")                                          
st.success("Hurrah!")                                        # Success

st.subheader("INFORMATION")                                     
st.info("Basics of Streamlit is learnt!")                    # info

st.subheader("WARNING")                                          
st.warning("Warning!")                                       # Warning

st.subheader("ERROR")                                            
st.error("Error!")                                           # Error

st.subheader("Error")                                           
st.exception(ZeroDivisionError("Division is"
                               "not divisible with 0"))      #exception
st.help(ZeroDivisionError)                                   #help

st.write("1+2+3")
st.write(1+3+3)

st.subheader("CODE")                                            
st.code("for i in range(10): \n"                            # Code
        "\tprint(i)")

st.subheader("CHECKBOX")
st.checkbox("Male")                                         # Checkbox

if (st.checkbox("Adult")):
    st.write("You're an Adult")                             # Checkbox with validation

st.subheader("RADIO BUTTON")
radioButton = st.radio("Select Radio Button: ",
                       ("Male","Female","Other"))           # Radiobutton
if radioButton == "Male":
    st.write("You're Male")
if radioButton == "Female":
    st.write("You're Female")
if radioButton == "Other":
    st.write("You're Other")

st.subheader("SELECT BOX")                                  # SelectBox
selectBox = st.selectbox("Select your Area of Interest in Data Science",    
             ["", "Data Analysis", "Web Scraping", "Machine Learning",
              "Deep Learning", "Natural Processing Language",
              "Computer Vision", "Image Processing"])
if selectBox:
    st.write("You have chosen ", selectBox)


st.subheader("SELECT BOX")                                  # Multiselectox
multi_select_box = st.multiselect("Select your Area of Interest in Data Science",    
             ["Data Analysis", "Web Scraping", "Machine Learning",
              "Deep Learning", "Natural Processing Language",
              "Computer Vision", "Image Processing"])
if multi_select_box:
    st.write("You have chosen ", len(multi_select_box)," courses ")

st.subheader("Button")                                      # Button
button = st.button("Click")
if button:
    st.write("Thanks!")

st.subheader("Slider")                                      # Slider
slider = st.slider("Volume", 0,100,1)
if slider:
    st.write("Volume ", slider)

st.subheader("TEXT INPUT")                                  # TextInput
text_input = st.text_input("Enter your Name")
st.write(text_input)

st.subheader("TEXT AREA")                                   # TextArea
st.text_area("Enter something")

st.subheader("NUMBER INPUT")                                # NumberInput
number_input = st.number_input("Select your age", 18, 100)
if number_input:
    st.write("You're ", number_input, " old")

st.subheader("DATE INPUT")                                  # DateInput
st.date_input("Date")

st.subheader("TIME INPUT")                                  # TimeInput
st.time_input("Time")

import pandas as pd

st.subheader("LOADING CSV FILE")                            # UploadingFiles
d = st.file_uploader("Upload CSV file: ", type = ["csv", "xlsx"])
st.write("Reading data without table")
if d is not None:
    st.dataframe(d)

df = pd.read_csv(r"C:\Users\Chary Mattela\Desktop\Python\STREAMLIT\Products.csv")
if df is not None:
    st.write("Reading data with table")
    st.table(df.head())

st.subheader("UPLOADING IMAGE AND OPENING")                 # ImageFile
image_file = st.file_uploader("Upload image file", type = ["png","jpeg"])
if image_file is not None:
    st.image(image_file)


st.subheader("UPLOADING VIDEO FILE")                        # VideoFile
video_file = st.file_uploader("Upload Video file", type = "mp4")
if video_file is not None:
    st.video(video_file, start_time = 0)

st.subheader("UPLOADING AUDIO FILE")                        # AudioFile
audio_file = st.file_uploader("Upload audio file", type = ["mp3", "wav"])
if audio_file is not None:
    st.audio(audio_file)


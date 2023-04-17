# Libraries

import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import pandas as pd
import base64
import os
from PIL import Image
from sklearn.ensemble import RandomForestClassifier as rfc
from utilities.pdf_funcs import print_results_inhtml
from utilities.save_yaml import save_yaml

def app():
    os.chdir('/home/senthil/Desktop/DDP/webapi_ddp')
    print(os.getcwd())

    def value(lst,string):
        for i in range(len(lst)):
            if lst[i]==string:
                return i

    jobs=['admin','blue-collar','entrepreneur','housemaid','managerial','retired','self-employed','services','student','technician','unemployed','others']
    marital_status=['divorced','married','single']
    education=['10th standard or lower','12th standard','graduate','postgraduate or higher']
    yn=['NO','YES']
    commn=['Cellular','Telephone','Others']
    mon=['January','February','March','April','May','June','July','August','September','October','November','December']
    outcome=['Failure','Other','Success','Unknown']
    #---------------------------------------------------------

    # Body Interface
    #---------------------------------------------------------

    side_bg = "assets/images/wh.jpg"
    side_bg_ext = "jpg"

    image=Image.open('assets/images/head.png')
    st.sidebar.image(image)

    # components.html(html2)
    st.markdown("<h1 style='text-align: center; color:#7a000d;'>Calibrate your low cost sensor here</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#7a000d;'>Get an automatic performance report of your LCS showing the details of the data analysed in diagnosis and the machine learning models considered in our calibration methodology</h2>",unsafe_allow_html=True)
    # st.markdown("<h6 style='text-align: center; color:#7a000d;'>Some text to be replaced here</h3>",unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>
       .sidebar .sidebar-content {{
            background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # ------------------------------------------------------------
    # Sidebar Interface 
    # ------------------------------------------------------------
    st.sidebar.markdown("""
                        
    ---                    
                        
    Update your LCS data here.

    Submit to see results!!

    """)

    dataset_names = os.listdir('mlcodes/datasets')
    # dataset_names = str(dataset_names)[1:-1]

    model_names = os.listdir('mlcodes/models')
    # model_names = str(model_names)[1:-1]
    tuning_methods = ['gridsearch', 'randomsearch', 'optuna']
    # tuning_methods = str(tuning_methods)[1:-1]
    dataset = st.sidebar.selectbox("⦿ Dataset (Select the dataset you want to train on) : ",(dataset_names))
    test_size = st.sidebar.slider("⦿ Test size(Percent of test data in the dataset)",1,100)
    model = st.sidebar.selectbox("⦿ Model (Select the model you want to use) : ",(model_names))
    tuning_methods = st.sidebar.selectbox("⦿ Tuning method (Select the model tuning method you prefer) : ",(tuning_methods))
    save_results = st.sidebar.radio("⦿ Save results (Select the model tuning method you prefer) : ",('Yes', 'No'))
    get_report = st.sidebar.radio("⦿ Get analysis report (Select the model tuning method you prefer) : ",('Yes', 'No'))

    if st.sidebar.button('SUBMIT'):
        os.chdir('/home/senthil/Desktop/DDP/webapi_ddp')
        print(os.getcwd())
        data ={
            'dataset':dataset,
            'test_size':test_size/100,
            'model':model,
            'tuning_method':tuning_methods,
            'save_results':save_results,
            'get_report':get_report
            }
        save_yaml(data) 
        print(data)   
        st.markdown("<h5 style='text-align: center; color:#7a000d;'>Engine Running.Processing Results........</h1>", unsafe_allow_html=True)
        
        os.chdir('mlcodes')
        print(os.getcwd())
        from main import RunProgram
        RunProgram()
        print(os.getcwd())

        print_results_inhtml()
        # st.write(iframe(, height=600))
        html_link = f'<a href="report.html" target="_blank">Click here to view the report in a new tab</a>'
        

    # Footers 
    #--------------------------------------------------------------
    footer="""<style>
    a:link , a:visited{
    color: blue;
    background-color: transparent;
    text-decoration: underline;
    }

    a:hover,  a:active {
    color:red;
    background-color: transparent;
    text-decoration: underline;
    }

    .footer {
    position: fixed;
    bottom: 0;
    width:45%;

    color: black;
    text-align: center;
    }
    </style>
    <div class="footer">
    <p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://homepages.iitb.ac.in/~18d180024" target="_blank">Senthil Vikram</a></p>
    </div> 
    """
    # st.markdown(footer, unsafe_allow_html=True)

    myhtml = """
    <h3 style='text-align: center; color:#7a000d;'>Any related text or instructions.</h3>
    """

    st.sidebar.markdown("""View the original research publication[researchgate.com](https://homepages.iitb.ac.in/~18d180024/) , [Instagram](https://www.instagram.com/senthil_vikram_/) , [Github](https://github.com/SenthilVikram)""")
    #-----------------------------------------------------------------

if __name__ == "__main__":
    app()























































import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
# import weasyprint
# from autoviz.AutoViz_PDF import AutoViz_PDF
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from tqdm import tqdm


def create_boxplot(data, x, y, title, xlabel, ylabel):
    print("create_boxplot")
    fig, ax = plt.subplots()
    sns.boxplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def create_histogram(data, column, title, xlabel, ylabel):
    print("create_histogram")
    fig, ax = plt.subplots()
    ax.hist(data[column], bins=30)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def main():
    st.set_page_config(page_title='Air Pollution Monitoring', page_icon=':bar_chart:', layout='wide')
    # st.title('Air Pollution Monitoring')
    st.markdown("<h1 style='text-align: center; color:#7a000d;'>Explore your low cost sensor data here</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color:#7a000d;'>Get an automatic performance report of your LCS showing the details of the data analysed in diagnosis and the machine learning models considered in our calibration methodology</h2>",unsafe_allow_html=True)

    # # Login
    # st.sidebar.title('Login')
    # username = st.sidebar.text_input('Username')
    # password = st.sidebar.text_input('Password', type='password')
    # login = st.sidebar.checkbox('Login')    
    login = 1

    if login:
        # Data upload
        st.sidebar.markdown('### Upload data')
        uploaded_file = st.sidebar.file_uploader('Choose a CSV file', type=['csv'])
        if uploaded_file is not None:
            st.sidebar.success('File uploaded successfully!')

            df = pd.read_csv(uploaded_file)
            st.markdown('### Data')
            st.write(df.head())

            print(df.columns)
            # Perform data preprocessing and feature engineering
            df['created_at'] = pd.to_datetime(df['created_at'])
            df['Year'] = df['created_at'].dt.year
            df['Month'] = df['created_at'].dt.month
            df['Day'] = df['created_at'].dt.day

            st.markdown('### Data preprocessing')
            columns = list(df.columns)
            columns_of_interest = st.multiselect('Select columns to analyze', columns)
            if len(columns_of_interest) == 0:
                st.warning('Please select at least one column.')
            else:
                st.text('Performing data preprocessing...')
                for column in columns_of_interest:
                    df[column] = df[column].fillna(df[column].median())

                # Data visualization
                st.markdown('### Data visualization')
                st.text('Creating visualizations...')
                for column in columns_of_interest:
                    st.markdown(f'#### {column}')
                    st.pyplot(create_boxplot(df, 'Year', column, f'{column} distribution by year', 'Year', column))
                    st.pyplot(create_boxplot(df, 'Month', column, f'{column} distribution by month', 'Month', column))
                    st.pyplot(create_histogram(df, column, f'{column} histogram', column, 'Count'))

                # Pandas Profiling report
                st.markdown('### Pandas Profiling report')
                st.text('Generating Pandas Profiling report...')
                report = ProfileReport(df[columns_of_interest], explorative=True)
                st_profile_report(report)
                report.to_file('report.html')
                # html_str = report.to_html()
                        # st.write(html(html_link))        
                st.success('Successfully completed!', icon="✅")


                # html_string = report.to_html()
                # # Generate a PDF report using the AutoViz_PDF class
                # avp = AutoViz_PDF()
                # avp.fit(df[columns_of_interest])
                # avp.generate_report(filename='reportautoviz')

        else:
            st.warning('Please upload a file.')
    else:
        st.sidebar.error('Invalid username or password')

main()

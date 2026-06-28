import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title('Interactive Sales Dashboard')
st.write('Upload a CSV file with sales and profit data to analyze and visualize results.')

# Upload CSV data - file_uploader(label,type)

uploaded_file = st.file_uploader('Upload your sales CSV', type=['csv']) 

if uploaded_file is not None: 
    df = pd.read_csv(uploaded_file)  # Read CSV into Pandas DataFrame 
    st.write("Data Preview:") 
    st.dataframe(df.head())

# Choose Metric for analysis

    metric = st.selectbox('Choose a metric:', ['sales', 'profit']) # Dropdown for metric selection 
     
    total_value = df[metric].sum() # total
    st.write(f"**Total {metric.capitalize()}:** {total_value}") 
     
    agg_by_region = df.groupby("region")[metric].sum() # aggregates by region
    st.write(f"**{metric.capitalize()} by Region:**") 
    st.write(agg_by_region) 

# Choose Chart type

    chart_type = st.selectbox("Choose a chart type:", ["Bar", "Line", "Pie"]) # drop down

    fig, ax = plt.subplots() 

    if chart_type == "Bar": 
        agg_by_region.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black") 
        ax.set_ylabel(metric.capitalize()) 
        ax.set_title(f"{metric.capitalize()} by Region") 
        
    elif chart_type == "Line": 
        agg_by_region.plot(kind="line", marker="o", ax=ax, color="green") 
        ax.set_ylabel(metric.capitalize()) 
        ax.set_title(f"{metric.capitalize()} by Region (Line Chart)") 

    elif chart_type == "Pie": 
        agg_by_region.plot(kind="pie", autopct="%1.1f%%", ax=ax) 
        ax.set_ylabel("")  # Hide Y-axis for pie chart 
        ax.set_title(f"{metric.capitalize()} Distribution by Region") 
    
    st.pyplot(fig) # Show chart in Streamlit 

# Add Download Button 
   
    processed_df = agg_by_region.reset_index()   # 0,1,2...
    processed_df.columns = ["Region", metric.capitalize()]  # 
 
# Download button 
    csv = processed_df.to_csv(index=False).encode("utf-8") 

# st.download_button(label="Download File", data=file_contents, file_name="filename.csv", mime="text/csv")

    st.download_button( 
        label="Download Processed Data as CSV", 
        data=csv, 
        file_name=f"{metric}_by_region.csv",    # allows users to save results as a CSV.
        mime="text/csv"
    )

'''Step 1: Prepare Your Streamlit Project 
            1. Ensure your main file is named: app.py (or streamlit_app.py). 
            2. Create a requirements.txt with all dependencies: requirements.txt --> streamlit pandas matplotlib requests
This tells Streamlit Cloud what packages to install.

Step 2: Push Code to GitHub 
Run the following commands in your project folder: 

    git init  # Initialize Git 
    git add . # Add all files 
    git commit -m "Initial commit - Streamlit app" # Commit changes 
    git remote add origin https://github.com/your-username/your-repo.git # Add remote (replace with your repo link) 
    git push -u origin main # Push to GitHub 

Your code is now stored in a GitHub repository. 

Step 3: Deploy on Streamlit Cloud 

    1. Go to  https://share.streamlit.io. 
    2. Sign in with your GitHub account. 
    3. Click New App. 
    4. Select: 
            a. Repository: your repo name. 
            b. Branch: usually main. 
            c. File path: app.py. 
            5. Click Deploy. 

Streamlit Cloud will: 
        • Install packages from requirements.txt. 
        • Run your app automatically.

Step 4: Access Your Public App 

        • After a few minutes, you will get a unique URL like: https://your-username-your-repo.streamlit.app 
        • Open the link to test your app. 
        • Try uploading files, using widgets, and verifying functionality.

        
Step 5: Make Updates - Whenever you change your app locally: 
        git add . 
        git commit -m "Update app features" 
        git push 
        Streamlit Cloud automatically redeploys the latest version.
'''




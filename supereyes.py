import streamlit as st
import pandas as pd
import plotly.express as px

# Load your Toyota dataset
data = pd.read_csv('df_car_Toyota.csv')  # Adjust with your dataset path

# CSS
css = """
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f2f2f2;  
    color: #333;  
    text-align: center;  
}

h1 {
    color: #E4002B;  /* Toyota red */
}

h2, h3 {
    color: #333;
}

.stButton button {
    background-color: #E4002B;  /* Toyota red */
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.stButton button:hover {
    background-color: #B3001B;  /* Darker red on hover */
}

.plotly-graph div {
    background-color: white;  /* White background for plots */
    border-radius: 10px;  /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    padding: 10px;  /* Padding for the plot area */
}

.markdown-text {
    margin: 20px 0;
}
</style>
"""

# Inject CSS
st.markdown(css, unsafe_allow_html=True)

st.image("toyota_logo_icon_169445.png")
# Title and Introduction
st.title("Looking for a used Toyota car?")
st.markdown("<div class='markdown-text'>I got you</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>I understand the struggle of looking for a new car, so I did the heavy lifting for you.</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>First of all, I wanted to show you the main top 10 cars from Toyota in the used car market. It could interest you in specific car</div>", unsafe_allow_html=True)

st.markdown("### Here are the main top 10 cars from Toyota")
# Count the occurrences of each car type
top_10_types = data['Type'].value_counts().head(10)
chart_data = pd.DataFrame({
    'Type': top_10_types.index,
    'Total': top_10_types.values
})
fig1 = px.bar(chart_data, x='Type', y='Total', title='Top 10 Toyota Car Types',
              range_y=[0, max(chart_data['Total']) + 5])
st.plotly_chart(fig1)

st.markdown("<div class='markdown-text'>However, if you have something in mind, maybe a specific car from Toyota?</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>Take a look</div>", unsafe_allow_html=True)

# User Input for Car Type
car_types = data['Type'].unique()
selected_car = st.selectbox('What Type of car are you interested in?', car_types)

# Filter based on the selected car type
filtered_data = data[data['Type'] == selected_car]

# Display price ranges for the selected car type
st.markdown("### Of course, you want it to be in your budget, so obviously I got your back here too. "
            "Check out the ranges of prices for a used Toyota car.")

# Creating bins for price ranges
price_bins = pd.cut(filtered_data['Price'], bins=10)  # Adjust bins as needed
price_range_counts = price_bins.value_counts().sort_index()

price_data = pd.DataFrame({
    'Price Range': price_range_counts.index.astype(str),
    'Count': price_range_counts.values
})

# Visualize price ranges with Plotly (line chart)
fig2 = px.line(price_data, x='Price Range', y='Count', title='Check out the Price Range for Your Selected Car',
                markers=True)  # Markers added for visibility
fig2.update_traces(line=dict(width=2, color='blue'))  # Adjust line width and color

# Update layout for better appearance
fig2.update_layout(yaxis_title='Count', xaxis_title='Price Range',
                   xaxis_tickangle=-45,  # Rotate x-axis labels for better visibility
                   transition_duration=500)  # Set the duration of the transition

st.plotly_chart(fig2)

# Display regions where the selected car type is available
st.markdown("### Once you've figured out if it's in your budget, are you wondering where to get it from?")

# Count the occurrences of each region
region_counts = filtered_data['Region'].value_counts()
region_data = pd.DataFrame({
    'Region': region_counts.index,
    'Count': region_counts.values
})

# Visualize regions with Plotly (pie chart)
fig3 = px.pie(region_data, names='Region', values='Count', title='Regions Where Your Car is Available In',
               hole=0.3)  # Use a donut chart style for a nice effect
fig3.update_traces(pull=[0.05] * len(region_data),  # Small separation for each slice
                   textinfo='percent+label',  # Show percentage and label
                   marker=dict(line=dict(color='#FFFFFF', width=2)))  # Add white border for contrast
st.plotly_chart(fig3)

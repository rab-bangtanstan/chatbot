# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    # URL of the dataset
    # url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/Store_sales_transactions.csv"
    data = pd.read_csv('storeSalesData.csv')
    return data

# Function to create pie chart
def create_pie_chart(data):
    # Grouping the data by 'Product_Category' and counting the occurrences
    product_sales = data['Product_Category'].value_counts()
    labels = product_sales.index.tolist()  # Product categories
    sizes = product_sales.values.tolist()  # Number of sales per category

    # Creating the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Sales Distribution by Product Category')
    return fig

# Main function to run the Streamlit app
def main():
    # Page layout
    st.set_page_config(page_title="Sales Analysis App", page_icon=":bar_chart:", layout="wide")

    # Title
    st.title("Sales Analysis App")

    # Load data
    data = load_data()

    # Display data
    st.write("## Sales Data")
    st.write(data.head())  # Display the first few rows of the dataset

    # Create pie chart
    st.write("## Sales Distribution by Product Category")
    fig = create_pie_chart(data)
    st.pyplot(fig)  # Display the pie chart in the Streamlit app

# Run the app
if __name__ == "__main__":
    main()

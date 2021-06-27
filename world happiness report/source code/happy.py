from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Francis\YDG\Learning Zone\LearnStreamlit\Datasets\world-happiness-report-2021.csv")
#print(data.head())

# dispaly widget
st.sidebar.title("World Happiness Index 2021:")

# display image 
st.image("https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg", caption="World Happiness Dataset")

# show dataset
st.write(data)

# create country filter
region_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", 
            "North America and ANZ","Middle East and North Africa", 
            "Latin America and Caribbean","Central and Eastern Europe",
            "Commonwealth of Independent States","Sub-Saharan Africa"]

select = st.sidebar.selectbox("Select Region:", region_list, key=1)

if select=="All":
    data = data
else:
    data = data[data['Regional indicator']==select]

score = st.sidebar.slider("Select minimum slider score", min_value=5, max_value=10, value=10)
# get input
data = data[data["Ladder score"]<=score]


# scatter plot
fig = px.scatter(data, x="Logged GDP per capita", y="Healthy life expectancy",
                    size = "Ladder score", color = "Regional indicator", 
                    hover_name="Country name", size_max=10)

st.write(fig)

# bar chart
st.write(px.bar(data, x='Country name', y='Ladder score'))

# correlation heatmap
corr = data.corr()

plt.figure(figsize=(12,8))
fig1 = plt.figure()

ax = sns.heatmap(corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)
ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);

st.pyplot(fig1)


# ---- Exploratory data analysis

st.sidebar.title("Data Exploration:")
st.markdown("Welcome to data exploration. Tick a box below to quickly explore the dataset.")
if st.sidebar.subheader("Explore"):
    if st.sidebar.checkbox("Descriptive Statistics"):
        st.subheader("A Quick look of the dataset:")
        st.write(data.describe())
    if st.sidebar.checkbox("Data columns"):
        st.subheader("Data columns:")
        cols = data.columns.to_list()
        st.write(cols)
    if st.sidebar.checkbox("Missing values"):
        st.subheader("Missing values:")
        st.write(data.isnull().sum())

fig2= sns.pairplot(data)
st.pyplot(fig2)
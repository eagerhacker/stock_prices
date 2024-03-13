import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df2 = sns.load_dataset('healthexp')
# print(df2)
# df2.Country.unique()

# sns.barplot(x=df2['Year'], y=df2['Spending_USD'])

country_data = []
health_expense = []

cols = st.columns(3)
with cols[0]:
  country = st.selectbox('Country', df2.Country.unique())
  country_data = df2[df2['Country'] == country]
#   health_expense = df2[df2['Country'] == country]
  st.expander('Country Data').table(country_data)
  

with cols[1]:
  fig1 = plt.figure(figsize=(8, 4))
  sns.lineplot(x=country_data['Year'], y=country_data['Life_Expectancy'], data=country_data)
  st.pyplot(fig1)

with cols[2]:
  fig2 = plt.figure(figsize=(8, 4))
#   plt.pie(data=)

fig, ax1 = plt.subplots(figsize=(10,5))

sns.barplot(x='Country', y='Spending_USD', data=df2, ax=ax1)
ax2 = ax1.twinx()
sns.lineplot(x='Country', y='Life_Expectancy', data=df2, ax=ax2)
# sns.barplot(x=country_data
#['Year'], y=country_data
#['Spending_USD'])

st.pyplot(fig)
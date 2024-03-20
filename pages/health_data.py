import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout='wide')
df2 = sns.load_dataset('healthexp')
# print(df2)
# df2.Country.unique()

# sns.barplot(x=df2['Year'], y=df2['Spending_USD'])

country_data = []
health_expense = []

cols = st.columns(2)
country = st.selectbox('Country', df2.Country.unique())
country_data = df2[df2['Country'] == country]
#   health_expense = df2[df2['Country'] == country]
with st.container(height=400):
  st.expander('Country Data', expanded=True).table(country_data)

with cols[0]:
  
  h =  df2.loc[df2.Country == country]

  f= plt.figure(figsize=(8, 4))
  ax = sns.barplot(data=h, y='Spending_USD', x='Year')

  ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=5)
  plt.tight_layout()
  st.pyplot(f)

with cols[1]:

  fig1, axis1 = plt.subplots(figsize=(8, 4))
  sns.lineplot(x=country_data['Year'], y=country_data['Life_Expectancy'], data=country_data, ax=axis1)
  st.pyplot(fig1)



with st.container():
  col = st.columns(2)

  with col[0]:
    st.title('Avg Health Expense - Life Expectancy 1970 - 2020')
    
    no_year = len(df2['Year'].unique())

    countries = df2.Country.unique()
    avg_expense = []
    life_avg = []

    for c in countries:
        avg_expense.append(df2.loc[df2['Country'] == c, 'Spending_USD'].sum() / len(df2.loc[df2['Country'] == c, 'Spending_USD']))
        life_avg.append(df2.loc[df2['Country'] == c, 'Life_Expectancy'].sum() / len(df2.loc[df2['Country'] == c, 'Life_Expectancy']))

    health_avg = pd.DataFrame(list(zip(countries, avg_expense, life_avg)),columns=['Country','Expense', 'Life_Expectancy' ])
    
    fig, ax1 = plt.subplots(figsize=(5,3))

    sns.barplot(x='Country', y='Expense', data=health_avg, ax=ax1)
    ax2 = ax1.twinx()
    sns.lineplot(x='Country', y='Life_Expectancy', data=health_avg, ax=ax2, color='r')
    # sns.barplot(x=country_data
    #['Year'], y=country_data
    #['Spending_USD'])

    st.pyplot(fig)

  with col[1]:
    st.title('Health Spending')
    countries = df2.Country.unique()
    expense = []

    for c in countries:
      expense.append(df2.loc[df2['Country'] == c, 'Spending_USD'].sum())
  
    fig2 = plt.figure(figsize=(5,3))
    
    data = {'Countries': countries, 'Expense': expense}
    pd.DataFrame(data)

    plt.pie(data['Expense'], labels=data['Countries'])
    st.pyplot(fig2)
    

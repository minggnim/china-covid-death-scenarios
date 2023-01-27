import pathlib
import pandas as pd
import plotly.io as pio
import streamlit as st
st.set_page_config(layout="wide")

PATH = pathlib.Path(__file__).resolve().parents[2]
data_store = PATH / 'data/store.h5'
graph_store = PATH / 'data/plotly_json'

uk_death_rate_weekly = pd.read_hdf(data_store, 'uk_death_rate_weekly')
china_age_group = pd.read_hdf(data_store, 'china_age_group')

estimate_total = pio.read_json(graph_store / 'estimate_total.json')
estimate_age_group = pio.read_json(graph_store / 'estimate_age_group.json')


st.header('China COVID Death Assumptions')
st.markdown('''
This analysis estimates death toll scenarios by assuming that policy change occurred between February 2021 and December 2022 in weekly intervals.
''')
st.markdown('''
For each assumed COVID-zero end date, the figure below shows the estimated total number of deaths till 2 December. 
Each estimate is based on the projection from [UK death rate in each age group during the same period](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/articles/coronaviruscovid19latestinsights/deaths#deaths-by-age).
''')
st.plotly_chart(estimate_total, use_container_width=True)
st.markdown('''
From the estimate, it shows that one year delay of policy change reduces the death toll by :red[over half a million], 
while 6 months delay reduces it by :red[nearly 200,000].
''')
st.markdown('''
The breakdown of death toll per age group over time is presented below. 
Age groups `65 to 74` and `75 to 84` suffer the highest death toll, though both age groups combined account for 13% overall population.
''')
st.plotly_chart(estimate_age_group, use_container_width=True)
st.markdown('''
**Note**

The estimates in this analysis did not factor in 
- The impact of early waves of COVID-19 deaths pre-February 2021 in the UK, which may increase the death estimates
- The difference in medical conditions in both countries
''')
st.markdown('**Reference Data**')
col1, col2 = st.columns([2,2])
col1.markdown('1. Population age group in China')
col1.dataframe(china_age_group)
col2.markdown('2. Weekly COVID death rate in UK')
col2.dataframe(uk_death_rate_weekly)
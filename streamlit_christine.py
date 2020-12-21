#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import plotly.figure_factory as ff

@st.cache
def load_hospitals():
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2

@st.cache
def load_inatpatient():
    df_inpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_2

@st.cache
def load_outpatient():
    df_outpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_2


st.title('Medicare Expenses Across NY Hospitals')

# Loading bar, but the main purpose is just for aesthestics to divide the dashboard into separate sections for this dashboard.
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)
  
  
# Load the data:     
df_hospital_2 = load_hospitals()
df_inpatient_2 = load_inatpatient()
df_outpatient_2 = load_outpatient()


#NY hospitals
hospitals_ny = df_hospital_2[df_hospital_2['state'] == 'NY']
inpatient_ny = df_inpatient_2[df_inpatient_2['provider_state'] == 'NY']
outpatient_ny = df_outpatient_2[df_outpatient_2['provider_state'] == 'NY']

#Stony Brook
hospital_stony_brook = df_hospital_2[df_hospital_2['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
inpatient_stony_brook = df_inpatient_2[df_inpatient_2['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )']
outpatient_stony_brook = df_outpatient_2[df_outpatient_2['provider_name'] == 'University Hospital ( Stony Brook )']

#Mt. Sinai
hospital_mount_sinai = df_hospital_2[df_hospital_2['hospital_name'] == 'MOUNT SINAI HOSPITAL']
inpatient_mount_sinai = df_inpatient_2[df_inpatient_2['provider_name'] == 'MOUNT SINAI HOSPITAL']
outpatient_mount_sinai = df_outpatient_2[df_outpatient_2['provider_name'] == 'Mount Sinai Hospital']

#New York Presbyterian
hospital_nyp = df_hospital_2[df_hospital_2['hospital_name'] == 'NEW YORK-PRESBYTERIAN HOSPITAL']
inpatient_nyp = df_inpatient_2[df_inpatient_2['provider_name'] == 'NEW YORK-PRESBYTERIAN HOSPITAL']
outpatient_nyp = df_outpatient_2[df_outpatient_2['provider_name'] == 'New York-Presbyterian Hospital']

#Bar Chart
st.subheader('**Hospital Types Within NY**')
bar1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

st.markdown('This chart shows the number of hospitals within NY that identify as acute care, psychiatric, critical access, acute care - department of defense, and childrens. The majority of hospitals identify as acute care with 144 hospitals, followed by psychiatric with 27 hospitals, critical access with 18 hospitals, acute care - department of defense with 1 hospital, and childrens with 1 hospital.')

#Pie Chart
st.subheader('**Types of Hospitals Within NY**')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)

st.markdown('This pie chart visually displays the same data presented in the previous bar chart. The largest percentage of NY hospitals are classified as acute care with 75.4%.')
          
#Map
st.subheader('**NY Hospital Locations**')

hospitals_ny_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 	
hospitals_ny_gps['lon'] = hospitals_ny_gps['lon'].str.strip('(')
hospitals_ny_gps = hospitals_ny_gps.dropna()
hospitals_ny_gps['lon'] = pd.to_numeric(hospitals_ny_gps['lon'])
hospitals_ny_gps['lat'] = pd.to_numeric(hospitals_ny_gps['lat'])

st.map(hospitals_ny_gps)

st.markdown('This is an interactive map that displays the locations for the NY hospital sites found within this dataset.')

#Timeliness of Care
bar2 = hospitals_ny['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig5 = px.bar(bar2, x='index', y='timeliness_of_care_national_comparison')
fig5.update_layout(
    title=("NY Hospitals - Timelieness of Care"),
    xaxis_title="Timelieness of Care",
    yaxis_title="Count",
    font=dict(
    )
)
st.plotly_chart(fig5)

st.markdown('Based on this bar graph, the majority of hospitals in the NY area fall below the national average for timeliness of care. There seems to be a large quantity of NY hospitals that are unable to provide quality care in a reasonable amount of time. This indicates the possibility that there are not enough healthcare professionals to serve the growing population of patients that need healthcare services.')

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

st.subheader('**Stony Brook University Hospital (SBUH)**')
st.markdown('These dataframes specifically display Stony Brook University Hospital data. The first dataframe is from the hospital dataset, followed by the inpatient dataset, and lastly with the outpatient dataset.')
st.dataframe(hospital_stony_brook)
st.dataframe(inpatient_stony_brook)
st.dataframe(outpatient_stony_brook)

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

st.subheader('**Mount Sinai Hospital**')
st.markdown('These dataframes specifically display Mount Sinai Hospital data. The first dataframe is from the hospital dataset, followed by the inpatient dataset, and lastly with the outpatient dataset.')
st.dataframe(hospital_mount_sinai)
st.dataframe(inpatient_mount_sinai)
st.dataframe(outpatient_mount_sinai)

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

st.subheader('**New York Presbyterian (NYP) Hospital**')
st.markdown('These dataframes specifically display New York Presbyterian Hospital data. The first dataframe is from the hospital dataset, followed by the inpatient dataset, and lastly with the outpatient dataset.')
st.dataframe(hospital_nyp)
st.dataframe(inpatient_nyp)
st.dataframe(outpatient_nyp)

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

st.subheader('**National Comparisons**')
st.markdown('Shown below are the collected national comparison values for Stony Brook University Hospital, Mount Sinai Hospital, and New York Presbyterian Hospital.')
hospital_combined = df_hospital_2[(df_hospital_2['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL') | (df_hospital_2['hospital_name'] == 'MOUNT SINAI HOSPITAL') | (df_hospital_2['hospital_name'] == 'NEW YORK-PRESBYTERIAN HOSPITAL')]
st.dataframe(hospital_combined)

st.markdown('**Mortality:** Stony Brook University Hospital, Mount Sinai Hospital, and New York Presbyterian Hospital are all above the national average.')
st.markdown('**Safety of Care:** Stony Brook University Hospital and Mount Sinai Hospital are above the national average, but  New York Presbyterian Hospital is below the national average.')
st.markdown('**Readmission:** Stony Brook University Hospital and New York Presbyterian Hospital are below the national average, but Mount Sinai Hospital is below the national average.')
st.markdown('**Patient Experience:** Stony Brook University Hospital and Mount Sinai Hospital are below the national average, but  New York Presbyterian Hospital is the same as the national average.')
st.markdown('**Effectiveness of Care:** Stony Brook University Hospital, Mount Sinai Hospital, and New York Presbyterian Hospital are all the same as the national average.')
st.markdown('**Timeliness of Care:** Stony Brook University Hospital, Mount Sinai Hospital, and New York Presbyterian Hospital are all below the national average.')
st.markdown('**Efficient Use of Medical Imaging:** Stony Brook University Hospital and Mount Sinai Hospital are the same as the national average, but  New York Presbyterian Hospital is below the national average.')

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

#Inpatient Data for NY
st.subheader('**NY Inpatient Costs**')

inpatient_ny = df_inpatient_2[df_inpatient_2['provider_state'] == 'NY']
total_inpatient_count = sum(inpatient_ny['total_discharges'])

st.markdown('Total Count of Inpatient Discharges:' )
st.markdown( str(total_inpatient_count) )

##Common D/C 

common_discharges = inpatient_ny.groupby('drg_definition')['total_discharges'].sum().reset_index()

top10 = common_discharges.head(10)
bottom10 = common_discharges.tail(10)

st.markdown('**Common DRGs**')
st.dataframe(common_discharges)
st.markdown('These are the common diagnosis-related groups (DRGs) among the NY inpatient facilities. The most common DRG is 871 - Septicemia or severe sepsis w/o mv 96+ hours w mcc with a total amount of 31964 discharges. The least common DRG is 035 - Carotid artery stent procedure w cc with 11 total discharges.')

#Costs by Condition and Hospital / Average Total Payments
costs_condition_hospital = inpatient_ny.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.markdown("**Costs by Condition and Hospital - Average Total Payments**")
st.dataframe(costs_condition_hospital)

st.markdown('This dataframe shows the average total payments based on the DRG and site for all NY inpatient locations.')

#Bar Charts of the costs 

costs = inpatient_ny.groupby('provider_name')['average_total_payments'].sum().reset_index()
costs['average_total_payments'] = costs['average_total_payments'].astype('int64')


costs_medicare = inpatient_ny.groupby('provider_name')['average_medicare_payments'].sum().reset_index()
costs_medicare['average_medicare_payments'] = costs_medicare['average_medicare_payments'].astype('int64')


costs_sum = costs.merge(costs_medicare, how='left', left_on='provider_name', right_on='provider_name')
costs_sum['delta'] = costs_sum['average_total_payments'] - costs_sum['average_medicare_payments']

st.markdown("**Average Total Payments VS Average Medicare Payments by Hospital**")
st.dataframe(costs_sum)
st.markdown('This dataframe displays the values for the average total payment and average Medicare payments for every inpatient NY hospital site.')


st.markdown('**Stony Brook University Hospital Inpatient DRGs**')
bar2 = inpatient_stony_brook['drg_definition'].value_counts().reset_index()
st.dataframe(bar2)

st.markdown('**Mount Sinai Hospital Inpatient DRGs**')
bar2 = inpatient_mount_sinai['drg_definition'].value_counts().reset_index()
st.dataframe(bar2)

st.markdown('**New York Presbyterian Hospital Inpatient DRGs**')
bar2 = inpatient_nyp['drg_definition'].value_counts().reset_index()
st.dataframe(bar2)

st.markdown('The above dataframes display the types of DRGs charged from Stony Brook University Hospital, Mount Sinai Hospital, and New York Presbyterian Hospital. New York Presbyterian Hospital has the most with 370 DRGs, followed by Mount Sinai with 278 DRGs, and Stony Brook University Hospital with 224 DRGs.')

inpatient_combined = df_inpatient_2[(df_inpatient_2['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )') | (df_inpatient_2['provider_name'] == 'MOUNT SINAI HOSPITAL') | (df_inpatient_2['provider_name'] == 'NEW YORK-PRESBYTERIAN HOSPITAL')]
outpatient_combined = df_outpatient_2[(df_outpatient_2['provider_name'] == 'University Hospital ( Stony Brook )') | (df_outpatient_2['provider_name'] == 'Mount Sinai Hospital') | (df_outpatient_2['provider_name'] == 'New York-Presbyterian Hospital')]


fig2 = px.box(inpatient_combined, x="provider_name", y="total_discharges", points="all")
fig2.update_layout(
    title="Total Number of Discharges for SBUH, Mt. Sinai, and NYP",
    xaxis_title="Provider Name",
    yaxis_title="Total Number of Discharges",
    font=dict(
    )
)
st.plotly_chart(fig2)

st.markdown('The above box plots shows the values for minimum, maximum, median, 25%, 50%, and 75% quartiles. New York Presbyterian Hospital has the largest outlier value at 892 followed by Stony Brook University Hospital at 628, and lastly Mount Sinai at 560.')


fig3 = px.histogram(inpatient_combined, x="average_medicare_payments", y="total_discharges", color="provider_name",
                   marginal="box",
                   hover_data=inpatient_combined.columns)
fig3.update_layout(
    title="Average Medicare Payment VS Total Number of Discharges for SBUH, Mt. Sinai, and NYP",
    xaxis_title="Average Medicare Payments",
    yaxis_title="Total Number of Discharges",
    legend_title="Provider Name",
    font=dict(
    )
)
st.plotly_chart(fig3)

st.markdown('The above histogram shows that Stony Brook University Hospital has the most amount of discharges across a majority of the ranges for the average amount of Medicare payments compared to Mount Sinai Hospital and New York Presbyterian Hospital.')

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.00025)
my_bar.progress(percent_complete + 1)

st.subheader('**NY Outpatient Costs**')

fig7 = px.bar(outpatient_combined, x='provider_name', y='average_total_payments')
fig7.update_layout(
    title=("NY Outpatient Locations - Average Total Costs"),
    xaxis_title="Provider Name",
    yaxis_title="Average Total Payments",
    font=dict(
    )
)
st.plotly_chart(fig7)

st.markdown('Stony Brook Univeristy Hospital has the least amount of average total payments on average compared to Mount Sinai Hospital and New York Presbyterian Hospital.')


fig8 = px.histogram(outpatient_combined, x="outpatient_services", y="average_total_payments", color="provider_name",
                   marginal="box",
                   hover_data=outpatient_combined.columns)
fig8.update_layout(
    title="Number of Outpatient Services VS Average Total Payments for SBUH, Mt. Sinai, and NYP",
    xaxis_title="Outpatient Services",
    yaxis_title="Average Total Payments",
    legend_title="Provider Name",
    font=dict(
    )
)
st.plotly_chart(fig8)

st.markdown('The histogram above emphasizes that Mount Sinai Hospital and New York Presbyterian Hospital contain one outlier value each. These values show that there is an influx of patients who visit Mount Sinai Hospital and New York Presbyterian Hospital for "Hospital Clinic Visits."')


            
            

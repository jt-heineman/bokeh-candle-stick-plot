#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data
import datetime as dt
from bokeh.plotting import figure, show, output_file
start_date=dt.datetime(2020,1,1)
end_date=dt.datetime(2020,9,1)
df=data.DataReader("spy","yahoo",start_date,end_date) #returns a dataframe

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close, df.Open)] #list comprehensions
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p=figure(x_axis_type="datetime",width=1000,height=300)
p.title.text="Example Candlestick Chart"
p.grid.grid_line_alpha=0.3 #level of transparecy of gridline

hours_12=12*60*60*1000 #miliseconds for width
p.segment(df.index, df.High, df.index, df.Low, color="black")#segment glif 4 parameter x, y, x lower, x higher
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], 
       hours_12, df.Height[df.Status == "Increase"],
      fill_color="green",line_color="black")
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], 
       hours_12, df.Height[df.Status == "Decrease"],
      fill_color="red",line_color="black")


df
output_file("Stockplot_test1.html")
show(p)

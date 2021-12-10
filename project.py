"""
Name:  Jakub Czachor
Email: jakub.czachor15@myhunter.cuny.edu
URL: JakubC.com
Project Title: Water Quality In NYC
Resources:
https://data.cityofnewyork.us/Environment/Watershed-Water-Quality-Data/y43c-5n92, https://data.cityofnewyork.us/Environment/Drinking-Water-Quality-Distribution-Monitoring-Dat/bkwf-xfky
https://waterdata.usgs.gov/ny/nwis/qw/
https://www1.nyc.gov/assets/nyw/downloads/pdf/nyw-2017-dep-water-report.pdf
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
https://seaborn.pydata.org/generated/seaborn.regplot.html
https://python-visualization.github.io/folium/quickstart.html


"""
import folium
import seaborn
import numpy as np
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from scipy import stats


center =[40.7678, -73.9645] #Center is at Hunter College
Map = folium.Map(location=center, zoom_start= 8)

wd1 = [42.08468448955769, -75.32343047356032] #location of start of West Delaware Tunnel
DA1 = [41.82797659215036, -74.47941633867714]#location of delaware aqueduct
DA2 = [40.912636638224825, -73.87045480537631] #End of Delaware Aqueduct
CA2 = [41.20041909849701, -73.59894446149191]#location of end of catskill aqueduct
so3b = [40.89774232312983, -73.88514412013986] #Location of 1S03B
eastharlem = [40.89774232312983, -73.88514412013986] #Location of site 33950
harlem = [40.877184007366075, -73.8974065382458] #Location of site 1SCL1

coord = []
coord.append(DA1)
coord.append(DA2)

folium.Marker(location=wd1,popup = "Location of West Delaware Tunnel").add_to(Map) #Places markers
folium.Marker(location= DA1, popup= "Start of Delaware Aqueduct").add_to(Map)
folium.Marker(location= DA2, popup= "End of Delaware Aqueduct").add_to(Map)
folium.Marker(location=CA2, popup= "Location of Catskill Aqueduct").add_to(Map)
folium.Marker(location=so3b, popup="Location of test site 1S03B").add_to(Map)
folium.Marker(location=eastharlem, popup= "Location of test site 33950").add_to(Map)
folium.Marker(location=harlem, popup= "Location of test site 1SCL1").add_to(Map)


folium.PolyLine(coord,color = "red", weight = 2.5,opacity=1).add_to(Map) #Draws a line to show the general path of the Delaware Aqueduct
Map.save("map.html") #Saves Map

df = pd.read_csv("water.csv") #opens csv file with information
df = df.replace(["<0.10"], "0.10") #makes calculations easier
df["Turbidity (NTU)"] = df["Turbidity (NTU)"].astype(float) #changes turbidity into a float value
df["Sample Date"] = pd.to_datetime(df["Sample Date"], format= "%m/%d/%Y") #changes Sample Date into datetime
df["DateOrdinal"] = df["Sample Date"].apply(lambda date: date.toordinal())
df = df.sort_values(by=["Sample Site"]) #Sorts by Sample Site
df = df[["Sample Site", "Turbidity (NTU)", "Sample Date", "DateOrdinal"]] #Gets the important information


##ANALYSIS OF 1S03B##

df3b = df[df["Sample Site"] == "1S03B"] #Limits sample sites to 1S03B
df3b = df3b.sort_values(by="Sample Date") #Sorts by date
df3bAvg = df3b["Turbidity (NTU)"].mean() #Finds mean
df3bMax = df3b["Turbidity (NTU)"].max() #Finds max


print("Average Turbidity of 1S03B:", df3bAvg) #Prints average
print("Max Turbidity of 1S03B: ", df3bMax) #Prints max

x = df3b["Turbidity (NTU)"]
y = df3b["Sample Date"]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df3b['DateOrdinal'],df3b['Turbidity (NTU)']) #calculate slope, intercept, rvalue, pvalue and standard error of Turbidity
print("Slope: ", slope, "Intercept: ", intercept, "R Coef: ", rvalue, "Standard Error: ", stderr)
gr = seaborn.regplot( #Creates plot
    data = df3b,
    x = "DateOrdinal",
    y = "Turbidity (NTU)",
    line_kws={"color": "red"},
    scatter_kws={"color": "green"}
)
gr.set_ylim(0, 2) #Sets max values of Y
gr.set_xlabel("Date") #Sets the X label
gr.set_ylabel("Turbidity (NTU)")
newLabels = [date.fromordinal(int(item)) for item in gr.get_xticks()] #Changes Date labels from ordinal to regular
gr.set_xticklabels(newLabels)
gr.set(title="Graph of Turbidity in 1S03B") #Sets title of graph
plt.show() #Shows plot
df3b.to_csv("1s03b.csv", index=0) #Saves CSV Data to separate file


##ANALYSIS OF 33950##

dfeastHarlem = df[df["Sample Site"] == "33950"]
dfeastHarlem = dfeastHarlem.sort_values(by="Sample Date")

dfeHAvg = dfeastHarlem["Turbidity (NTU)"].mean() #Finds avg value of turbidity
dfeHMax = dfeastHarlem["Turbidity (NTU)"].max() #Finds max value of turbidity


print("Average Turbidity of 33950:", dfeHAvg)
print("Max Turbidity of 33950: ", dfeHMax)

x = dfeastHarlem["Turbidity (NTU)"]
y = dfeastHarlem["Sample Date"]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dfeastHarlem['DateOrdinal'],dfeastHarlem['Turbidity (NTU)'])#calculate slope, intercept, rvalue, pvalue and standard error of Turbidity
print("Slope: ", slope, "Intercept: ", intercept, "R Coef: ", rvalue, "Standard Error: ", stderr)
gr = seaborn.regplot( #Creates plot of values
    data = dfeastHarlem,
    x = "DateOrdinal",
    y = "Turbidity (NTU)",
    line_kws={"color": "red"},
    scatter_kws={"color": "green"}
)
gr.set_ylim(0, 2) #Sets Y Max
gr.set_xlabel("Date") #Sets X Label
gr.set_ylabel("Turbidity (NTU)") #Sets Y Label
new_labels = [date.fromordinal(int(item)) for item in gr.get_xticks()] #Changes Date labels from ordinal to regular
gr.set_xticklabels(new_labels)
gr.set(title="Graph of Turbidity in 33950") #Sets title
plt.show() #Shows plot
dfeastHarlem.to_csv("33950.csv", index=0) #Saves value to separate csv


##ANALYSIS OF 1SCL1##

dfHarlem = df[df["Sample Site"] == "1SCL1"]  #Sorts by Sample Site 1SCL1
dfHarlem = dfHarlem.sort_values(by="Sample Date") #Sorts by Sample Date
dfHAvg = dfeastHarlem["Turbidity (NTU)"].mean() #Finds average value of Turbidity
dfHMax = dfeastHarlem["Turbidity (NTU)"].max() #Finds max value of Turbidity


print("Average Turbidity of 1SCL1:", dfHAvg)
print("Max Turbidity of 1SCL1: ", dfHMax)

x = dfHarlem["Turbidity (NTU)"]
y = dfHarlem["Sample Date"]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dfHarlem['DateOrdinal'],dfHarlem['Turbidity (NTU)'])#calculate slope, intercept, rvalue, pvalue and standard error of Turbidity
print("Slope: ", slope, "Intercept: ", intercept, "R Coef: ", rvalue, "Standard Error: ", stderr)
gr = seaborn.regplot( #Creates plot
    data = dfHarlem,
    x = "DateOrdinal",
    y = "Turbidity (NTU)",
    line_kws={"color": "red"},
    scatter_kws={"color": "green"}
)
gr.set_ylim(0, 2) #Sets Y Lim
gr.set_xlabel("Date") #Sets X Label
gr.set_ylabel("Turbidity (NTU)") #Sets Y Label
new_labels = [date.fromordinal(int(item)) for item in gr.get_xticks()] #Changes Date labels from ordinal to regular
gr.set_xticklabels(new_labels)
gr.set(title="Graph of Turbidity in 1SCL1") #Sets title
plt.show() #Shows plot
dfHarlem.to_csv("1SCL1.csv", index=0) #Saves values to a seperate CSV file



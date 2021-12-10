---
layout: page
---
<html>
<body>
<h1>Jakub Czachor</h1><br>
<h2>Project: Water Quality in NYC</h2><br>
  <h3>Abstract: </h3><br>
  My project will be looking at the water quality of NYC especially as the source of the water has changed recently as a result of the closure of the Catskill Aqueduct, <br> 
  and how this can be used to make informed decisions on if the water quality in NYC needs further treatment when such closures happen.
 <br>
  <img src="map.jpg" alt="Map Of Delaware Aqueduct" class="center">
  <h3>Methods:</h3><br>
  <p>In order to test if the closures of the aqueducts have affected water quality, I would analyze the water turbidity data at multiple sampling points in New York City.  
  This information is freely available online for everybody, with the links provided below. I chose to analyze the 1S03B, 33950, and 1SCL1 testing sites because of their close proximity to the end of the Delaware Aqueduct as well as their proximity to the city. I began by cleaning up the data, and replacing the values of <.10 in the data with .10 in order to make analysis easier. My hypothesis was that because of the recent closures, and increase in complaints from people regarding the quality of the water, that there would be a noticable increase in the level of turbidity in the water. In order to test this hypothesis, I would run linear regressions on the data and figure out the current trend by finding the slope of the data.</p>
  <img src="1s03b.jpg" alt="1S03B Test Site" class="center">
  <h3> Analysis: </h3><br>
<center>Average Turbidity of 1S03B: 0.783551282051282<br>
Max Turbidity of 1S03B:  1.55<br>
Slope:  -3.502062579920943e-05 Intercept:  26.588376830008453 R Coef:  -0.17617771500352084 Standard Error:  3.918121922477679e-06<br>
    <img src="33950.jpg" alt="33950 Test Site" class="center">
  Average Turbidity of 33950: 0.46952991452991455
Max Turbidity of 33950:  1.46
Slope:  -0.00010090655415646666 Intercept:  74.82335186471137 R Coef:  -0.22429875286444997 Standard Error:  2.8783226342871914e-05
    <img src="1SCL1.jpg" alt="1SCL1 Test Site" class="center"></center>
Average Turbidity of 1SCL1: 0.46952991452991455
Max Turbidity of 1SCL1:  1.46
Slope:  -5.8137282401677444e-05 Intercept:  43.28282748538266 R Coef:  -0.11325207032188532 Standard Error:  1.0847035290399334e-05</center>
  
  <h3> Visualization</h3><br>
  
  <h3> Sources: </h3>
https://data.cityofnewyork.us/Environment/Watershed-Water-Quality-Data/y43c-5n92 <br>
https://data.cityofnewyork.us/Environment/Drinking-Water-Quality-Distribution-Monitoring-Dat/bkwf-xfky <br>
https://waterdata.usgs.gov/ny/nwis/qw/ 
https://www1.nyc.gov/assets/nyw/downloads/pdf/nyw-2017-dep-water-report.pdf
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html<br>
  
</body>
</html>

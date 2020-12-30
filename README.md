# Analysis of Airbnb data for Washington, DC.

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

To install the package needed to run the code/notebooks create/or update a conda environment with the following steps:


```
$ conda env create -f environment.yml -y
```

```
$ conda activate <environment
$ conda isntall --file requirements.txt
```

## Project Motivation<a name="motivation"></a>

For this project, I was interestested in understanding which DC neighborhood would be best to invest in a Airbnb property:

1. Which DC Neighborhood has the highest average price per listing?
2. Which DC Neighborhood's Airbnb market is saturated?
3. Which DC Neighborhood has the highest rated listings?
4. Are there any other factors that I need to review before investing in a property?

## File Descriptions <a name="files"></a>

There are two notebooks that will walk you through my analysis of these questions, and all the data needed is in the `data/` folder.  

There is an additional haler `.py` file that will clean some of the data that is obtained from other sources.

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@josh_2774/how-do-you-become-a-developer-5ef1c1c68711).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

You can find the Licensing for the Airbnb data and other descriptive information at the "Inside Airbnb" link available [here](http://insideairbnb.com/get-the-data.html), and you can find the Licensing information for the DC Neighborhood data [here](https://opendata.dc.gov/datasets/neighborhood-clusters?geometry=-78.323%2C38.707%2C-75.706%2C39.081). Otherwise, feel free to use the code here as you would like! 

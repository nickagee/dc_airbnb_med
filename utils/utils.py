import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import contextily as ctx


def clean_bath_text(x):
    """
    Cleanes the bathrooms_text field from AirBnB datasource.
    This has only been tested for data obtained from Washington DC.  For a new city you may need to update the list.
    
    x = is the input of the bathroom_text field.
    
    """
    if isinstance(x, str):
        return(x.replace("shared", '').replace("private", "").replace("baths", "").replace("bath", "").replace("Half-", "").replace("Shared half-", "").replace("Private half-", ""))
    return(x)



def bar_chart(df, size=(16,14), color='coral'):
    """
    Creates a quick Bar Chart with Matplotlib!
    
    df: Dataframe you want to graph
    size: Size of the output chart. Accepts Tuple (ex. (12,12)). Default[(16,14)]
    color: Color name you want the bars to be. Accepts matplotlib colors https://matplotlib.org/tutorials/colors/colors.html Default['coral']
    """
    ax = df.plot(kind='bar', figsize=size, color=color, fontsize=13);
    ax.set_alpha(0.8)
    ax.set_title("Mean Price by Neiborhood", fontsize=18)
    ax.set_xlabel("Neighborhood", fontsize=12)
    ax.set_ylabel("Price($)", fontsize=12);
    
    return plt.show()


def cat_map(gdf, column, title, size=(20, 20), alpha=0.5):
    """
    Creates a quick Categorical Map with Contextily
    
    gdf: GeoPandas GeoDataFrame that you want to map.
    column: Column name that you want to group by in your map.
    title: Add a title to your map.
    size: Size of the output map. Accepts Tuple (ex. (12,12)). Default[(20,20)]
    alpha: Transparency 0.0 - 1.0. Default[0.5]
    """
    gdf_webmerc = gdf.to_crs(epsg=3857)
    ax = gdf_webmerc.plot(figsize=size, column=column, categorical="True", alpha=alpha)
    ax.set(title=title)
    return ctx.add_basemap(ax)
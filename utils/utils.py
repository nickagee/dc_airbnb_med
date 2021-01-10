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


def bar_chart(df, title, xlabel, ylabel, size=(16,14), color='coral', save=False, barlabel=False, barlabel_rotate=0):
    """
    Creates a quick Bar Chart with Matplotlib!
    
    df: Dataframe you want to graph
    tite: Set title for chart
    xlabel: Set X Axis label
    ylabel: Set Y Axis label
    size: Size of the output chart. Accepts Tuple (ex. (12,12)). Default[(16,14)]
    color: Color name you want the bars to be. Accepts matplotlib colors https://matplotlib.org/tutorials/colors/colors.html Default['coral']
    save: Boolean for saving chart as a png
    barlabel: Boolean to label bar with value
    barlable_rotate: Number for the angle you want your bar label to be set at
    """
    if save:
        name = title.replace(" ", "_")
        ax = df.plot(kind='bar', figsize=size, color=color, fontsize=13);
        ax.set_alpha(0.8)
        ax.set_title(title, fontsize=18)
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)
        
        if barlabel:
            for p in ax.patches:
                ax.annotate(str(round(p.get_height(), 3)), (p.get_x()+0.1, p.get_height()+2), fontsize=12, rotation=barlabel_rotate)
            
        fig = plt.gcf();
        plt.show();
        plt.draw();
        fig.savefig("bar_chart_"+name+".png", bbox_inches='tight')
        return 
    else:
        ax = df.plot(kind='bar', figsize=size, color=color, fontsize=13);
        ax.set_alpha(0.8)
        ax.set_title(title, fontsize=18)
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12);
        plt.show();
        return


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
    ax.axis('off')

    return ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)


def chor_map(gdf, column, title, size=(20, 20), alpha=0.5):
    """
    Creates a quick Choropleth Map with Contextily
    
    gdf: GeoPandas GeoDataFrame that you want to map.
    column: Column name that you want to group by in your map.
    title: Add a title to your map.
    size: Size of the output map. Accepts Tuple (ex. (12,12)). Default[(20,20)]
    alpha: Transparency 0.0 - 1.0. Default[0.5]
    """
    
    gdf_webmerc = gdf.to_crs(epsg=3857)
    ax = gdf_webmerc.plot(column=column, cmap = 'coolwarm', figsize=size, scheme='quantiles', k=4, alpha=alpha, edgecolor='white', linewidth=3, legend=True,legend_kwds=dict(loc='best', facecolor='white',framealpha=1));
    ax.set_title(label=title, fontdict={'fontsize':20})
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    ax.axis('off')
    for x, y, label in zip(gdf_webmerc.centroid.x, gdf_webmerc.centroid.y, gdf_webmerc[column]):
        ax.annotate(round(label, 2), xy=(x, y),horizontalalignment='center', fontsize=14, fontweight='bold')
        # show the subplot
        ax.figure
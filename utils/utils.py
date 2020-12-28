def clean_the_bathroom(x):
    """
    Cleanes the bathrooms_text field from AirBnB datasource
    
    """
    if isinstance(x, str):
        return(x.replace("shared", '').replace("private", "").replace("baths", "").replace("bath", "").replace("Half-", "").replace("Shared half-", "").replace("Private half-", ""))
    return(x)
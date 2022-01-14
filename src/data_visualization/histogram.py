def histogram(df, x, y):
    """Plot a histogram with the color scheme magma
    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the numerical variable to be plotted on the x-axis
    y : string
        An aggregation function to be plotted on the y-axis
    Returns
    -------
    altair.vegalite.v4.api.Chart
        Boxplot displaying distribution of categorical variables with/without faceting
    Examples
    --------
    >>> from data_visualization.data_visualization import histogram
    >>> plot(mtcars, "cars", "count()")
    """

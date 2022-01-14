def scatterplot(df, x, y):
    """Plot a scatterplot with the color scheme magma.
    Parameters
    ----------
    df : dataframe
        Dataframe containing the numerical features x and y
    x : string
        Column-name of the numerical variable to be plotted on the x-axis
    y : string
        Column-name of the numerical variable to be plotted on the y-axis
    Returns
    -------
    altair.vegalite.v4.api.Chart
        Scatterplot between the numerical variables x and y
    --------
    >>> from data_visualization.data_visualization import scatterplot
    >>> plot(mtcars, horsepower, cars)
    """
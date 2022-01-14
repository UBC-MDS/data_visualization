def histogram(df, x, y, facet=False):
    """Plot a histogram with the color scheme magma and an option to facet.
    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the numerical variable to be plotted on the x-axis
    y : string
        An aggregation function to be plotted on the y-axis
    facet : boolean
        Determines whether seprate graphs will be created for each category
    Returns
    -------
    altair.vegalite.v4.api.Chart
        Boxplot displaying distribution of categorical variables with/without faceting
    Examples
    --------
    >>> from data_visualization.data_visualization import boxplot
    >>> plot_words(mtcars, horsepower, cars, facet=True)
    """

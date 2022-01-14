def color_boxplot(df, x, y, facet=False):
    """Plot a boxplot with the color scheme red-yellow-green and an option to facet.

    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column-name of the numerical variable to view the distribution of
    y : list
        Column names of the categorical variables to assign boxes to
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

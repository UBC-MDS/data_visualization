# Correlation plot function

def corrplot(df):
    """
    Shows a correlation plot for all the numeric
    columns in a dataframe.

    Parameters
    ----------
    df : dataframe
        the dataframe to use for the plot

    Returns
    -------
    altair chart
        the correlation plot for the numeric
        columns in the dataframe

    Examples
    --------
    >>> corrplot(movies)
    """
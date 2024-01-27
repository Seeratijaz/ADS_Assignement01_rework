import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def lineplot(x, y, xlabel, ylabel, title, color, labels):
    """
    Function to Plot the Line Graph

    Parameters
    ----------
    x : list of values on x-axis
        Values on the X-axis.
    y : List of Values for y-axis
        Values for the Y-axis.
    xlabel : String
        Label Defining what's on the x-axis.
    ylabel : String
        Label Defining what's on the y-axis.
    title : String
        Title of the Graph.
    color : List
        List of Colors for the Graph.
    labels : list
        Labels on the of the lines.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(10, 5))
    for index in range(len(y)):
        plt.plot(x, y[index], label=labels[index], color=color[index])

    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
    return


def plot_pie_charts(data_list, labels_list, title, colors=None, entities=None):
    """
    Function to Plot Pie chart.

    Parameters
    ----------
    data_list : lists of Data
        List of Data values.
    labels_list : List of Labels
          List of label values.
    title : String
        Title of the Graph.
    colors : list of colors, optional
        DESCRIPTION. The default is None.
    entities : String, optional
        Name of Countries in our case. The default is None.

    Returns
    -------
    None.

    """
    # Set up the figure
    fig, axs = plt.subplots(
        1, len(data_list), figsize=(
            12, 6), subplot_kw=dict(
            aspect="equal"))

    # Default colors if not provided
    if colors is None:
        colors = plt.cm.Paired.colors

    # Iterate through each set of data and labels
    for i, (data, labels) in enumerate(zip(data_list, labels_list)):
        # Plotting the pie chart
        axs[i].pie(
            data,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors)

        # Equal aspect ratio ensures that pie is drawn as a circle
        axs[i].axis('equal')

        # Set the title (if entities are provided)
        if entities is not None:
            axs[i].set_title(entities[i])

    # Set a common title
    fig.suptitle(title)

    # Show the plot
    plt.show()


def plot_multiline_(
        years,
        labels,
        xlabel,
        ylabel,
        title,
        *cancer_data,
        colors=None):
    """
    Funtion to Plot a Bar chart.

    Parameters
    ----------
    years : list
        List of years for the x-axis in our case.
    labels : list
        list of label values.
    xlabel : String
        what to show as xlabel.
    ylabel : String
        what to show as ylabel.
    title : String
        title of bar chart.
    *cancer_data : lists of values
        Data for the y-axis.
    colors : list, optional
        to give custom colors to labels. The default is None.

    Returns
    -------
    None.

    """
    # Set up figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Number of cancer types
    num_cancers = len(cancer_data)

    # Bar width and opacity
    bar_width = 0.15
    opacity = 0.7

    # Default colors if not provided
    if colors is None:
        colors = ['b', 'g', 'r', 'c', 'm', 'y']

    # Plotting multiline bar chart
    for i in range(num_cancers):
        plt.bar(
            np.arange(
                len(years)) +
            i *
            bar_width,
            cancer_data[i],
            bar_width,
            alpha=opacity,
            color=colors[i],
            label=labels[i])

    # Customize the plot
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(np.arange(len(years)) +
               (num_cancers - 1) * bar_width / 2, years)
    plt.legend()


def get_refine_data(dataframe):
    """


    Parameters
    ----------
    dataframe : TYPE
        DESCRIPTION.

    Returns
    -------
    total_cancer_death_by_type : TYPE
        DESCRIPTION.

    """

    years = dataframe['Year']
    entity = dataframe['Entity']
    # Droping the Entity, Code, Year, Column
    total_cancer_death_by_type = dataframe.drop(
        ['Entity', 'Code', 'Year'], axis=1)
    cols = total_cancer_death_by_type.columns
    type_name = []
    # Renaming the Columns of Dataframe
    for names in cols:
        type_name.append(names.split('-')[1])
    total_cancer_death_by_type = total_cancer_death_by_type.rename(
        columns=dict(zip(total_cancer_death_by_type.columns, type_name)))
    cancer_types = [
        ' Tracheal, bronchus, and lung cancer ',
        ' Liver cancer ',
        ' Kidney cancer ',
        ' Breast cancer ',
        ' Prostate cancer ',
        ' Colon and rectum cancer ']
    # getting only the Required columns
    total_cancer_death_by_type = total_cancer_death_by_type[cancer_types]
    total_cancer_death_by_type['Year'] = years
    total_cancer_death_by_type['entity'] = entity
    return total_cancer_death_by_type


dataframe = pd.read_csv('total-cancer-deaths-by-type.csv')
total_cancer_death_by_type = get_refine_data(dataframe)
total_cancer_death_by_type.head()

total_cancer_death = total_cancer_death_by_type[
    total_cancer_death_by_type['entity'] == 'World']

xlabel = 'Years'
ylabel = 'Total Death By Cancer'
titel = 'Total Deaths Around the Glob By Cancer Type From 1990-2020'
lineplot(total_cancer_death['Year'],
         [total_cancer_death[' Colon and rectum cancer '],
          total_cancer_death[' Liver cancer '],
          total_cancer_death[' Kidney cancer '],
          total_cancer_death[' Prostate cancer ']],
         xlabel,
         ylabel,
         titel,
         ['red',
          'green',
          'blue',
          'black'],
         [' Colon and rectum cancer ',
          ' Liver cancer ',
          ' Kidney cancer ',
          ' Prostate cancer '])
total_cancer_death_years = total_cancer_death[total_cancer_death['Year'].isin(
    [1990, 1995, 2000, 2005, 2010, 2015, 2020])]
total_cancer_death_years
xlabel = 'Years'
ylabel = 'Total Death By Cancer'
title = 'Total Deaths Around the Glob By Cancer Type in Specific Years'
plot_multiline_(
    total_cancer_death_years['Year'],
    [
        'Colon and rectum cancer',
        'Liver cancer',
        'Kidney cancer',
        'Prostate cancer'],
    xlabel,
    ylabel,
    title,
    total_cancer_death_years[' Colon and rectum cancer '],
    total_cancer_death_years[' Liver cancer '],
    total_cancer_death_years[' Kidney cancer '],
    total_cancer_death_years[' Prostate cancer '])

total_country = total_cancer_death_by_type[(
    total_cancer_death_by_type['Year'] == 2019) & (
    total_cancer_death_by_type['entity'].isin(['Pakistan', 'United Kingdom']))]
entities = ['Pakistan', 'United Kingdom']
data_pk = total_country[total_country['entity'] == 'Pakistan']
data_uk = total_country[total_country['entity'] == 'United Kingdom']
labels_pakistan = total_country.columns[1:-2]
# Call the function with the provided data
plot_pie_charts([list(data_pk.iloc[0,1:-2]),
                 list(data_uk.iloc[0,1:-2])],
                [labels_pakistan,
                 labels_pakistan],
                'Distribution of Cancer'
                ' Cases in Pakistan and United Kingdom 2019',
                entities=entities)

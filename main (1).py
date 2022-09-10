import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot
df = pd.read_csv("charts.csv")

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

df.info()

is_number1 = df["peak-rank"] == 1
number1_no_duplicates = df[is_number1].groupby("song").first().sort_values("date", ascending = True)
number1_no_duplicates.sample(5)

def get_decade(year):
    year = str(year)
    decade = year[0:3] + "0's"
    return decade

number1_no_duplicates["decade"] = number1_no_duplicates["year"].apply(get_decade)
number1_no_duplicates.sample(5)

top_num = 5

graph_data = number1_no_duplicates[["artist", "decade"]].value_counts().head(top_num)
graph_data.sample(5)

# default plot aesthetics
default_layout = {
    # display title with bigger font
    "title": dict(
        font = {"size": 30}
    ),
    
    # change plot font
    "font" : dict(
        family = "arial",
        size = 16,
        color = "white"
    ),
    
    # plot colors and size
    "paper_bgcolor" : "#3d3d3d",
    "plot_bgcolor" : "rgba(0,0,0,0)",
    "height" : 700,
    "yaxis" : {"showgrid": False},
    
    # move the legend
    "legend" : dict(
        orientation = "v",
        x=.7,
        y=.93,
        traceorder="normal",
    )
}

# ordered list of unique decades in our graph data
decade_index = sorted(graph_data.index.get_level_values(1).unique())

# dict defining decades by color
decade_colors = {
    "1950's" : "#cd4b42",
    "1960's" : "#cd7e42",
    "1970's" : "#b13e55",
    "1980's" : "#42cd56",
    "1990's" : "#42b8cd",
    "2000's" : "#606faf",
    "2010's" : "#9677bb",
    "2020's" : "#b771ab"
}

# will become our final list of traces
data = []

for decade in decade_index:
    search_filter = graph_data.index.get_level_values(1) == decade
    subset = graph_data[search_filter]
    
    # create the bars for the decade
    trace = go.Bar(
        x = subset.index.get_level_values(0),
        y = subset,

        # annotate text above the bars
        text = subset,
        textposition = "outside",
        
        # change bar color based of custom dict decade_colors
        marker = {"color" : decade_colors[decade]},
        
        name = decade
    )
    # add trace to the data list
    data.append(trace)

fig = go.Figure(data = data, layout = default_layout)

# updates to the default layout
fig.update_layout(
    {
    "title": dict(
            text = f"Top {top_num} Artists by Number of #1 Billboard Songs"
        ),
    "xaxis": dict(
            categoryorder = 'array',
            categoryarray = graph_data.index.get_level_values(0)
        ),
    "legend": dict(
            orientation = "v",
            x=.7,
            y=.93,
            traceorder="normal"
        )
    }
)

# display the plot!
iplot(fig)

# filter out every week's number 1 song
all_number1 = df[df["rank"]==1]
all_number1.head()

def get_decade(year):
    year = str(year)
    decade = year[0:3] + "0's"
    return decade

all_number1["decade"] = all_number1["year"].apply(get_decade)
all_number1.head()

# after building the plot, I saw that a title of one of the songs was too long and made the chart ugly, so I crop it here
is_long_song = all_number1["song"]=="Somebody That I Used To Know"
all_number1.loc[is_long_song, "song"] = "Somebody That I Used To Know"

top_songs = all_number1[["song", "decade"]].value_counts()

top_songs.head()

# change this number to see more or fewer songs
num_songs = 15
graph_data = top_songs.head(num_songs)

decade_index = sorted(graph_data.index.get_level_values(1).unique())
data = []

for decade in decade_index:
    search_filter = graph_data.index.get_level_values(1) == decade
    subset = graph_data[search_filter]
    
    # create the bars for the decade
    trace = go.Bar(
        x = subset.index.get_level_values(0),
        y = subset,

        # annotate text above the bars
        text = subset,
        textposition = "outside",
        
        # change bar color based of custom dict decade_colors
        marker = {"color" : decade_colors[decade]},
        name = decade,
        
        # prevent the text annotations from being cropped by the top of the plot
        cliponaxis = False
    )
    # add trace to the data list
    data.append(trace)

fig = go.Figure(data = data, layout = default_layout)

# updates to the default layout
fig.update_layout(
    {
    "title": dict(
            text = f"Top {top_num} Songs by Total Weeks as Billboard #1"
        ),
    "xaxis": dict(
            categoryorder = 'array',
            categoryarray = graph_data.index.get_level_values(0)
        ),
    "legend": dict(
            orientation = "v",
            x=.9,
            y=1,
            traceorder="normal"
        )
    }
)

# display the plot!
iplot(fig)

import altair as alt
from vega_datasets import data
import io

source = data.cars()

brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin',
    color='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

chart = alt.hconcat(points, bars)
    
# Save html as a StringIO object in memory
cars_html = io.StringIO()
chart.save(cars_html, 'html')

# Return the html from StringIO object
altair_visualization  = cars_html.getvalue()

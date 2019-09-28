import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/MODIS_C6_Global_24h.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights, dates, times = [], [], [], [], []
    for row in reader:
        lat = row[0]
        lon = row[1]
        brightness = float(row[2]) / 25
        date = datetime.strptime(row[5], '%Y-%m-%d')
        time = datetime.strptime(row[6], '%H%M')

        lats.append(lat)
        lons.append(lon)
        brights.append(brightness)
        dates.append(date)
        times.append(time)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates + times,
    'marker': {
        'color': brights,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightness of fire'}
    }
    }]

my_layout = Layout(title="Fires from 9/27/2019 at 1800 to 9/28/2019 at 1800")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='globalfires.html')

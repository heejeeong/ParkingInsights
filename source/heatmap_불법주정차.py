import pandas as pd
import folium

from folium import plugins

#df = pd.read_excel('../data/불법주정차_high.xlsx')
df = pd.read_excel('../data/불법주정차_low.xlsx')

map_center = [df['위도'].mean(), df['경도'].mean()]  # 중앙 좌표 설정
mymap = folium.Map(location=map_center, zoom_start=10)

heat_data = [[point.위도, point.경도] for point in df[['위도', '경도']].itertuples()]
plugins.HeatMap(heat_data).add_to(mymap)

#mymap.save('../result/heatmap_불법주정차_high.html')
mymap.save('../result/heatmap_불법주정차_low.html')

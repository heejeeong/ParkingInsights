import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 첫 번째 데이터프레임: 불법주정차 빈도
df_illegal_parking = pd.read_excel('../data/불법주정차_high.xlsx')

# 두 번째 데이터프레임: 주차장 수
df_parking_lots = pd.read_excel('../data/filtered_parking_data_high.xlsx')

# Folium을 사용하여 지도 생성
map_center = [df_illegal_parking['위도'].mean(), df_illegal_parking['경도'].mean()]  # 중앙 좌표 설정
mymap = folium.Map(location=map_center, zoom_start=10)

# MarkerCluster 생성
marker_cluster_illegal_parking = MarkerCluster().add_to(mymap)
marker_cluster_parking_lots = MarkerCluster().add_to(mymap)

# 각 행에 대한 마커 및 정보 추가 - 불법주정차 빈도
map_info_illegal_parking = df_illegal_parking[['위도', '경도', '중복횟수']].dropna()
for lat, long, name in zip(map_info_illegal_parking["위도"], map_info_illegal_parking["경도"], map_info_illegal_parking['중복횟수']):
    folium.Marker([lat, long], popup=name, tooltip=name,icon=folium.Icon(color='pink')).add_to(marker_cluster_illegal_parking)

# 각 행에 대한 마커 및 정보 추가 - 주차장 수
map_info_parking_lots = df_parking_lots[['위도', '경도', '주차장명']].dropna()
for lat, long, count in zip(map_info_parking_lots["위도"], map_info_parking_lots["경도"], map_info_parking_lots['주차장명']):
    folium.Marker([lat, long], popup=count, tooltip=count, icon=folium.Icon(color='green')).add_to(marker_cluster_parking_lots)

# LayerControl을 통해 레이어 추가
folium.LayerControl(collapsed=False).add_to(mymap)

# 지도 저장
mymap.save('../result/map_with_layers.html')

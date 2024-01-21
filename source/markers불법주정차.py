import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 엑셀 파일에서 데이터 읽어오기
#df = pd.read_excel('../data/불법주정차_high.xlsx')
df = pd.read_excel('../data/불법주정차_low.xlsx')

# Folium을 사용하여 지도 생성
map_center = [df['위도'].mean(), df['경도'].mean()]  # 중앙 좌표 설정
mymap = folium.Map(location=map_center, zoom_start=10)

# MarkerCluster 생성
marker_cluster = MarkerCluster().add_to(mymap)

# 각 행에 대한 마커 및 정보 추가
map_info = df[['위도', '경도','중복횟수']].dropna()

for lat, long, name in zip(map_info["위도"], map_info["경도"], map_info['중복횟수']):
    folium.Marker([lat, long], popup=name, tooltip=name).add_to(marker_cluster)

# 지도 저장
#mymap.save('../result/map_with_markers_불법주정차_high.html')
mymap.save('../result/map_with_markers_불법주정차_low.html')

import folium
import pandas as pd

# 엑셀 파일에서 데이터 로드 (위도와 경도가 있는 열이 있다고 가정)
data = pd.read_excel("C:/Users/heeje/OneDrive/바탕 화면/project/불법주정차.xlsx")

# 지도 객체 생성
map_object = folium.Map(location=[data['위도'].mean(), data['경도'].mean()], zoom_start=10)

# 데이터 포인트를 지도에 추가
for index, row in data.iterrows():
    folium.Marker(location=[row['위도'], row['경도']], popup=row['단속일']).add_to(map_object)

# 지도를 HTML 파일로 저장
map_object.save('C:/Users/heeje/OneDrive/바탕 화면/project/map.html')
print("끝났습니다.")
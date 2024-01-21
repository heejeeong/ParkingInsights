import pandas as pd
from geopy.geocoders import Nominatim

excel_file_path = '../data/중복_불법주정차.xlsx'
df = pd.read_excel(excel_file_path)

geolocator = Nominatim(user_agent="my_geocoder")

def get_address(row):
    location = geolocator.reverse((row['위도'], row['경도']), language='ko')
    return location.address if location else None

df['주소'] = df.apply(get_address, axis=1)

output_excel_path = '../data/preprocessed_file.xlsx'
df.to_excel(output_excel_path, index=False)

print(f"주소가 추가된 새로운 엑셀 파일이 생성되었습니다: {output_excel_path}")
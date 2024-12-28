import requests
import xml.etree.ElementTree as ET
from pythonosc import udp_client

# Where to send osc
client = udp_client.SimpleUDPClient('127.0.0.1', 8000) # ip. port

# Variables
key = '777a716870617374363855535a6567'
tree_number = '64'
url = 'http://openAPI.seoul.go.kr:8088/' + key + '/xml/GeoInfoNurseTreeOldTreeWGS/1/5/' + tree_number
isAllValue = False # set it True to log all values in variables

# Get xml response
response = requests.get(url)
xml_response = response.content
    
# Parse xml
root = ET.fromstring(xml_response)

# Variables for each value
variables = {
    "OBJECTID": root.find('.//OBJECTID').text,
    "GU_NM": root.find('.//GU_NM').text, 
    "HNR_NAM": root.find('.//HNR_NAM').text,
    "MTC_AT": root.find('.//MTC_AT').text,
    "MASTERNO": root.find('.//MASTERNO').text,
    "SLAVENO": root.find('.//SLAVENO').text,
    "NEADRES_NM": root.find('.//NEADRES_NM').text,
    "LOCPLC_CN": root.find('.//LOCPLC_CN').text,
    "JMK_KOR": root.find('.//JMK_KOR').text,
    "WDPT_AR": root.find('.//WDPT_AR').text,
    "TRE_SOM_KOR": root.find('.//TRE_SOM_KOR').text,
    "BSU_CO": root.find('.//BSU_CO').text,
    "WRK_NAM": root.find('.//WRK_NAM').text,
    "SCNCENM_NM": root.find('.//SCNCENM_NM').text,
    "ATE": root.find('.//ATE').text,
    "THT_HG": root.find('.//THT_HG').text,
    "BHT_GRH": root.find('.//BHT_GRH').text,
    "WTRTB_BT": root.find('.//WTRTB_BT').text,
    "ERY_ETT": root.find('.//ERY_ETT').text,
    "ATT": root.find('.//ATT').text,
    "ATT_YMD": root.find('.//ATT_YMD').text,
    "WDPT_SE_CN": root.find('.//WDPT_SE_CN').text,
    "VAL_LVL": root.find('.//VAL_LVL').text,
    "PSS_MAN": root.find('.//PSS_MAN').text,
    "MGE_MAN": root.find('.//MGE_MAN').text,
    "SDE_KND_NM": root.find('.//SDE_KND_NM').text,
    "SDE_DME_ETT": root.find('.//SDE_DME_ETT').text,
    "SDE_MGE_STTN": root.find('.//SDE_MGE_STTN').text,
    "SDE_MGE_MET": root.find('.//SDE_MGE_MET').text,
    "VDE_KND_NM": root.find('.//VDE_KND_NM').text,
    "VDE_DME_ETT": root.find('.//VDE_DME_ETT').text,
    "VDE_MGE_STTN": root.find('.//VDE_MGE_STTN').text,
    "VDE_MGE_MET": root.find('.//VDE_MGE_MET').text,
    "ETC_DME_ETT": root.find('.//ETC_DME_ETT').text,
    "ETC_DME_MGE": root.find('.//ETC_DME_MGE').text,
    "ATT_WHY": root.find('.//ATT_WHY').text,
    "TRE_CRR": root.find('.//TRE_CRR').text,
    "HSY_TDN_CTT": root.find('.//HSY_TDN_CTT').text,
    "ETC": root.find('.//ETC').text,
    "TRE_IDN": root.find('.//TRE_IDN').text,
    "ITM_LVL": root.find('.//ITM_LVL').text,
    "CREAT_DE": root.find('.//CREAT_DE').text,
    "PO_FE_NM": root.find('.//PO_FE_NM').text,
    "LNG": root.find('.//LNG').text,
    "LAT": root.find('.//LAT').text
}

selected_data = [
    "OBJECTID", #고유번호
    "GU_NM", #구명
    "LOCPLC_CN", #소재지
    "JMK_KOR" #지목한글
    "WDPT_AR", #수목면적
    "TRE_SOM_KOR", #수종한굴
    "BSU_CO", #본수
    "WRK_NAM", #과명
    "SCNCENM_NM", #학명
    "ATE", #수령
    "THT_HG", #수고(높이)
    "BHT_GRH", #흉고둘레(줄기둘레)
    "WTRTB_BT", #수관너비(나무갓 너비)
    "ERY_ETT", #활력도
    "ATT", #지정품목
    "ATT_YMD", #지정년월일
    "WDPT_SE_CN", #수목구분내용
    "VAL_LVL", #가치등급
    "PSS_MAN", #소유자
    "MGE_MAN", #관리자
    "SDE_KND_NM", #병해종류명
    "SDE_MGE_MET", #병해관리방안
    "VDE_KND_NM", #충해종류명
    "VDE_DME_ETT", #충해피해도
    "ATT_WHY", #지정사유
    "TRE_CRR", #나무의 특징
    "HSY_TDN_CTT", #연혁 및 전설
    "TRE_IDN", #수목고유번호
    "ITM_LVL", #품계등급
    "LNG", #경도
    "LAT" #위도
]

# Print the variables
if isAllValue is True:
    for key, value in variables.items():
        # send osc
        client.send_message('/data', value)
    print('Osc sent with all data')
else:
    for key, value in variables.items():
        if key in selected_data:
            # send osc for selected data
            client.send_message(f'/{key}', value)
    print('Osc sent with selected data')

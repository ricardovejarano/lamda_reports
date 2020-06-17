import requests
import datetime

actual_year = datetime.datetime.now().strftime("%Y")
year_to_download = str(int(actual_year) - 1)

startDate_param_name = 'startDate'
endDate_param_name = 'endDate'

startDate_param_value = year_to_download + "-01-01 00:00:00.000 -05:00"
endDate_param_value = year_to_download + "-12-31 23:59:59.999 -05:00"

url_base = 'https://hidden-fortress-02723.herokuapp.com'
api = '/attachment-total-costs-report'

payload = ((startDate_param_name, startDate_param_value),
           (endDate_param_name, endDate_param_value))

response = requests.get(
    url_base + api, params=payload
)

json_response = response.json()
if json_response == True:
    print(1)
else:
    print(1)


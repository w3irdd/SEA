import os
from sea import dataparse, visualize
import pandas as pd

new_column_names = {
    "time": "Время",
    "event_src.host": "fortigate",
    "src.ip": "Атакующий",
    "object.type": "Сигнатура",
    "text": "Описание"
}

config = dataparse.parse_json_to_dict("../config/config.json")
mailing_is_enabled = config["mailing_is_enabled"]

args = dataparse.parse_arguments()
input_file = args.input_file
print(f"The input file is: {input_file}")

output_dir = '../data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file_pdf = os.path.join(output_dir, 'stats.pdf')
output_file_xlsx = os.path.join(output_dir, 'events.xlsx')

writer = pd.ExcelWriter(output_file_xlsx, engine='xlsxwriter')

ip_whitelist = dataparse.parse_ip_file("../config/filtered_addresses.txt") 

json_list = dataparse.csv_to_json_list(input_file, ip_whitelist)

df = dataparse.json_to_dataframe(json_list)
dataparse.dataframe_to_excel(df, writer, 'Все события', new_column_names)
dataparse.group_by_src_ip_to_excel(df, writer, 'Группировка по атакующим', new_column_names)
dataparse.group_by_unique_src_ip(df, writer, 'Уникальные атакующие адреса', new_column_names)
dataparse.group_by_unique_dst_combinations(df, writer, 'Уникальные ресурсы', new_column_names)
dataparse.create_summary_statistics(df, writer, 'Статистика')

writer._save()
print(f"Processing {input_file} and saving the output to {output_file_xlsx}")

visualize.visualize_data_to_pdf(json_list, output_file_pdf)
print(f"Processing {input_file} and saving the output to {output_file_pdf}")

print("\nDone!")
from docx2pdf import convert
import os

name_dir = 'MLCC_Certificates' # Replace the spaces with _

file_list=os.listdir(f'./{name_dir}')

if not os.path.exists(f'./{name_dir}_pdf'):
    os.makedirs(f'./{name_dir}_pdf')

for file in file_list:
    convert(f'./{name_dir}/{file}', f'./{name_dir}_pdf/{file.replace('.docx', '.pdf')}')

if len(os.listdir(f'./{name_dir}')) == len(os.listdir(f'./{name_dir}_pdf')):
    print('Job done correctly')

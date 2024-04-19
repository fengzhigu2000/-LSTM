import csv
input_filename = {
    './ssqdaletou2.txt':'./ssqdaletou2.csv',
    './ssqshuangseqiu.txt':'./ssqshuangseqiu.csv',
    }
normal_dict = dict(input_filename)
print(normal_dict)
for key,val in normal_dict.items():
    fieldnames = []
    if (key == './ssqshuangseqiu.txt') :
        fieldnames = [',','时间','期数','红1','红2','红3','红4','红5','红6','蓝'] 
    else:
        fieldnames = [',','时间','期数','红1','红2','红3','红4','红5','蓝1','蓝2'] 
    with open(key, 'r', encoding='utf-8') as input, open(val, 'w', newline='', encoding='utf-8-sig') as output:
         lines = input.readlines()
         csv_writer = csv.writer(output)

         # 写入输出文件的列名
         csv_writer.writerow(fieldnames)

         # 遍历输入文件的每行数据，处理后写入输出文件
         for idx, line in enumerate(lines, 0):
          data = line.strip().split(',')
          csv_writer.writerow([idx] + data)
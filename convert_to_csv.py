import csv
data = []

with open('cardio_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    print(csv_reader)
    for row in csv_reader:
        data.append(row)
    print(data[0])


with open('cardio.csv', mode='w') as target_csv:
    # fieldnames = data[0]
    writer = csv.writer(target_csv)
    # writer.writeheader()
    for i in range(len(data)) :
        writer.writerow(data[i])
import csv


with open ('goodreads-book.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    with open("/Users/roxana/Desktop/Automation/goodreads/Drive/topFiveRatedAuthors.csv", 'w') as new_file:
        for line in csv_reader:
            rate = line[1]
            rate = rate[19:-8]
            if str(rate) == '':
                pass
            else:
                rate = int(rate.replace(',', ''))

            if int(rate) > 178875:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(line)


# with open ('goodreads-book.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     next(csv_reader)
#
#
#     with open("TopFiveRatedAuthors.csv", 'w') as new_file:
#
#         for line in csv_reader:
#             rates = line[1]
#             rates = rates[0:5]
#             if rates == 'reall':
#                pass
#             elif float(rates)> float(4.32):
#                   t =line
#                   csv_writer = csv.writer(new_file)
#                   csv_writer.writerow(line)


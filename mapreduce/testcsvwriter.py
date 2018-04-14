from csv import writer

with open('testingcsvwrite.csv','w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name','AGE'])
    csv_writer.writerow(['shub',24])
    csv_writer.writerow(['Ani',22])
    csv_writer.writerow(['Abhi',24])

print("SUCCESSFULL RUN")

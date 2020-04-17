from django.shortcuts import render

import csv,io
from mysite import models
from django.apps import apps
from _collections import defaultdict
from mysite.models import Data


def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        csv_file = request.FILES["csv_file"]
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Data.objects.update_or_create(
                id=column[0],
                message=column[1],
                truth=column[2],
                cube=column[3],
                google=column[4],
                google_spam=column[5],
                google_not_spam=column[6],
                ibm=column[7],
                ibm_spam=column[8],
                ibm_not_spam=column[9],


            )
        context = {}
        return render(request,"index.html",{})

        # you may put validations here to check extension or file size

        wb = csv.load_workbook(csv_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'index.html', {"csv_file":excel_data})
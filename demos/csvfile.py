from metaflow import FlowSpec, Parameter, step, IncludeFile
from io import StringIO
import csv


class CSVFileFlow(FlowSpec):
    data = IncludeFile('csv', help='CSV file with data', is_text=True)
    delimiter = Parameter('delimiter', help='delimiter', default=',')

    @step
    def start(self):
        fileobj = StringIO(self.data)
        for i, row in enumerate(csv.reader(fileobj, delimiter=self.delimiter)):
            print(i, row)
        self.next(self.end)
        
    @step
    def end(self):
        print("done")

if __name__ == '__main__':
    CSVFileFlow()

#run with:python demos/csvfile.py run --csv demos/test.csv 
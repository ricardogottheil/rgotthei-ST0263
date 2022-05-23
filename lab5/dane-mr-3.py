
from mrjob.job import MRJob

class DaneMR3(MRJob):

    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')
        yield idemp, int(sececon)

    def reducer(self, employee, values):
        l = list(values)
        total = len(l)
        yield employee, total

if __name__ == '__main__':
    DaneMR3.run()

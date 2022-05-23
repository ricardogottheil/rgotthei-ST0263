
from mrjob.job import MRJob

class DaneMR2(MRJob):

    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')
        yield idemp, int(salary)

    def reducer(self, employee, values):
        l = list(values)
        avg = sum(l)/len(l)
        yield employee, avg

if __name__ == '__main__':
    DaneMR2.run()

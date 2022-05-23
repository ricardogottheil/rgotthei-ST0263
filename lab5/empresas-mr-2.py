from mrjob.job import MRJob

class EmpresasMR2(MRJob):
  def mapper(self, _, line):
    company,price,date = line.split(',')
    yield company, float(price)

  def reducer(self, company, data):
    d = list(data)
    result = False
    for i in range(len(d)):
      if d[i] < d[i-1]:
        result = True
      else:
        result = False
      break
    yield company, result

if __name__ == '__main__':
  EmpresasMR2.run()
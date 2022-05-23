from mrjob.job import MRJob

class MoviesMR2(MRJob):
  def mapper(self, _, line):
    user,movie,rating,genre,date = line.split(',')
    yield user, int(rating)

  def reducer(self, user, rating):
    d = list(rating)
    movies = len(d)
    avg = sum(d)/len(d)
    yield user, (movies, avg)

if __name__ == '__main__':
  MoviesMR2.run()
import numpy
from scipy import stats

class AlphaStatsPlugin:
    def input(self, filename):
       infile = open(filename, 'r')

       # Assumes category is under column "Description"
       # Values is under column "Value"

       self.values = dict()
       self.values["All"] = []

       line = infile.readline()
       contents = line.strip().split(',')
       print(contents)
       cat = contents.index("\"Description\"")
       val = contents.index("\"value\"")

       for line in infile:
          contents = line.strip().split(',')
          category = contents[cat]
          value = float(contents[val])
          self.values["All"].append(value)
          if (category not in self.values):
              self.values[category] = []
          self.values[category].append(value)

    def run(self):
       pass

    def output(self, filename):
       outfile = open(filename, 'w')
       
       for key in self.values:
           outfile.write(key+"\t"+str(numpy.mean(self.values[key]))+"\t"+str(stats.sem(self.values[key]))+"\n")

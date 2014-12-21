#!/usr/bin/env python
# Example script for recurrent network usage in PyBrain.
__author__ = "Martin Felder"
__version__ = '$Id$'

from pylab import plot, hold, show
from scipy import sin, rand, arange
from pybrain.datasets            import SequenceClassificationDataSet, SupervisedDataSet, SequentialDataSet
from pybrain.structure.modules   import LSTMLayer, SoftmaxLayer, SigmoidLayer
from pybrain.supervised          import RPropMinusTrainer, BackpropTrainer
from pybrain.tools.validation    import testOnSequenceData
from pybrain.tools.shortcuts     import buildNetwork
import datetime
import os, sys
import pickle
import itertools
import numpy as np

sys.path.append("/home/neal/git/finance/mine/")
os.environ["DJANGO_SETTINGS_MODULE"] = "mine.settings"

from myApp.models import Sector, Industry, Company
from datasets import generateNoisySines
year = 2014
day = 29
month = 9

inputs = 10
outputs = 10
hidden = 5

#{'date_field__range': (datetime.datetime.combine(date, datetime.time.min), datetime.datetime.combine(date, datetime.time.max))}
#sectors = Sector.objects.filter({'curr_date__range': (datetime.datetime.combine	(datetime.datetime(2014, 9, 29), datetime.time.min),
#	datetime.datetime.combine(datetime.datetime(year, month, day), datetime.time.max))})

#print datetime.datetime(2014, 9, 29)
sectors = Sector.objects.filter().values("day_price_change")
numSectors = 9
#print sectors['price_to_book']
data = []
for x in xrange(0, numSectors):
    secList = []
    for i in xrange(x, len(sectors), numSectors):
	   secList.append(sectors[i]['day_price_change'])
    data.append(secList)
#print data
#dataset = SequentialDataSet(inputs, outputs)

#(data1, data2) = np.array_split(data,2)
#print data2
#for x in itertools.izip(data):
#    dataset.newSequence()
#    dataset.addSample(x)
# create training and test data
#datatrn = data1 + data2
#trndata = generateNoisySines(50, 40)

#the data is now 2 d array - need to determine the dimensions of the data sets
trndata = SequenceClassificationDataSet(numSectors,1)
for i in xrange( 1, len(data[0]) ):
    trndata.newSequence()
    trndata.appendLinked(data[i - 1], (data[i] ))

tstdata = SequenceClassificationDataSet(numSectors,1)
for i in xrange( 1, len(data[0]) ):
    tstdata.newSequence()
    tstdata.appendLinked(data[i - 1], (data[i] ))

#trndata._convertToOneOfMany( bounds=[0.,1.] )
#tstdata = SequenceClassificationDataSet(1,1)
#for i in xrange(len(data2) -1):
#    tstdata.newSequence()
#    tstdata.addSample(data2[i], data2[i+1])
#tstdata._convertToOneOfMany( bounds=[0.,1.] )

# construct LSTM network - note the missing output bias
#rnn = buildNetwork( trndata.indim, 5, trndata.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)

rnn = buildNetwork(trndata.indim, hidden, trndata.outdim, hiddenclass=LSTMLayer, outclass=SigmoidLayer, recurrent=True)

#rnn.randomize()

#trainer = BackpropTrainer(rnn, dataset)

#for _ in range(100):
#    print trainer.train()
# define a training method
#trainer = RPropMinusTrainer( rnn, dataset=trndata, verbose=True )
# instead, you may also try
trainer = BackpropTrainer( rnn, dataset=trndata, verbose=True)

#carry out the training
for i in xrange(1000):
    #trainer.trainEpochs( 2)
    #trainer.trainOnDataset(trndata)
    #trnresult = 100. * (1.0-testOnSequenceData(rnn, trndata))
    #print trnresult
    #tstresult = 100. * (1.0-testOnSequenceData(rnn, tstdata))
    #print "train error: %5.2f%%" % trnresult, ",  test error: %5.2f%%" % tstresult
    trainer.train()
    #print "train error: %5.2f%%" % trnresult
# just for reference, plot the first 5 timeseries
trainer.testOnData(tstdata, verbose= True)
#plot(trndata['input'][0:50,:],'-o')
#old(True)
#plot(trndata['target'][0:50,:],'-o')
#show()

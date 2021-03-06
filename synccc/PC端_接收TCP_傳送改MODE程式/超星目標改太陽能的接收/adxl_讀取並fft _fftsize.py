#-*- coding: UTF-8 -*-
import numpy as np
import time
import os
import sys
import matplotlib
# solve the bug for myself 
# It maybe not necessary 
#matplotlib.use("Pdf")
import matplotlib.pyplot as plt

def average_fft ( x , fft_size ): #輸入矩陣，與一次要分析的大小
	    n = len ( x ) // fft_size * fft_size 
	    tmp = x [: n ] . reshape ( - 1 , fft_size ) #  把n切個乘很多小段
	    #tmp *= signal . hann ( fft_size , sym = 0 )  #乘上窗函數，把一個很多段的array乘上hann，代表每一段都乘上
	    xf = np . abs ( np . fft . rfft ( tmp ) / fft_size ) #傅立葉
	    avgf = np . average ( xf , axis = 0 ) #二维数组纵向求和，每一段的第幾個數求平均
	    return avgf#20 * np . log10 ( avgf )  #傳回大小
fft_size =512
while 1:
    print (os.listdir(os.getcwd()))
    name = input("whitch one ? ")
    #name = 'new_2017_07_12_05_20_08.npz'
    filepath =os.getcwd()+'/'+name
    if (os.path.isfile(filepath)):
        break
result = np.load(filepath)

#l = np.load('new_2017_07_11_07_45_53.npz')

total_data = result['data']

for i in range(3):
    data= total_data[i][:]
    p=average_fft(data,fft_size)
    samplerate = result['adxl_samplerate']
    rate =int(samplerate)
    print ('samplerate is '+str(samplerate))
    
    #fft
    f = np.linspace(0, rate/2, len(p))

    freqs  =  np . linspace ( 0 ,  rate / 2 ,  fft_size / 2 + 1 )
    #print(len(freqs) )
    #pic set
    n=data.shape[0]
    fig, (ax0, ax1) = plt.subplots(nrows=2 ,figsize=(16,8))
    ax0.set_title('Samplerate: {}   N: {}  '.format(rate,n), fontsize=10)
    ax0.plot(range(1000), data[:1000])
    ax0.set_ylabel('voltage(V)')
    #ax0.set_xlabel('tissme(n)')
    n=data.shape[0]
    print(n)
    
    #set the fft result to pic
    idx = np.argsort(freqs)
    idx2=idx[int((idx.shape[0]/2)+1):] #int (idx.shape[0]/2+800) ]
    ax1.set_xlabel("Frequence(Hz)")
    ax1.set_ylabel("Amplitude")
    ax1.set_title ( "axis 0x 1y 2z: %d"%(i) ) 
    ax1.plot(freqs[1:], p[1:]) #bar畫很慢
    #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    #save the pic
    filename=time.strftime("%Y%m%d_%H%M%S",time.localtime())
    dirPath=os.path.dirname(os.path.abspath(sys.argv[0]))
    filePath=os.path.join(dirPath,filename+str(i)+".jpg")
    plt.savefig(filePath)
    print("file: {}".format(filePath))
    #plt.show()
'''
#fft
fft_size =4096
p = average(data[:,3],fft_size)
print(p)
#p = np.abs(np.fft.fft(data[;100]))/n
#f = np.linspace(0, rate/2, len(p))
#freqs = np.fft.fftfreq(data.size, 1/rate)
#idx = np.argsort(freqs)
#idx2=idx[int(idx.shape[0]/2):] #int (idx.shape[0]/2+800) ]
freqs  =  np . linspace ( 0 ,  rate / 2 ,  fft_size / 2 + 1 )
#--------------------
plt.figure(figsize = ( 8 , 4 ))
#plt.subplot(311)
plt.plot(freqs, p)
plt.show()
'''
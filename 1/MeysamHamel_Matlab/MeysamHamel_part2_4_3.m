clear, clc, close all
[MainData,txt,raw] = xlsread('2010_Census_Populations_by_Zip_Code(1).csv');

TotalPopul=MainData(:,2);
MedianAge=MainData(:,3);

figure;plot(TotalPopul,MedianAge,'ok')
xlabel('Area Population')
ylabel('Median Age')

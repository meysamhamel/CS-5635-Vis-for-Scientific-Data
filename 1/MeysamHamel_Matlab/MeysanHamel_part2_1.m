clear, clc, close all
[MainData,txt,raw] = xlsread('1880-2017.csv');

%create vector for x
x=MainData(:,1);
%create vector for y
y=MainData(:,2);

%Generate BSr chart with label
bar(x, y, 'r'), xlabel('Year'), ylabel('Degrees F +/- From Average'), title('NOAA Land Ocean Temperature Anomalies Data')
xlim([1880, 2020])



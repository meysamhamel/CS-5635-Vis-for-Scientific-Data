clear, clc, close all
[MainData,txt,raw] = xlsread('Air_Quality.csv');

Data2005=MainData(1:6, 9);
Data2013=MainData(97:102, 9);

X = [Data2005'; Data2013'];

figure

parallelcoords(X,'Labels',{'Bronx','Brooklyn','Manhattan',...
    'Queens','Staten Island','New York City'},'Group',[2005,2013])

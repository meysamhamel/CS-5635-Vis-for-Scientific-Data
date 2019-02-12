clear, clc, close all
[MainData,txt,raw] = xlsread('US_births_2000-2014_SSA.csv');

x=MainData(:,5);
y=MainData(:,2);
%plot(x, y, 'g*')

%title('US Birth 2000 to 2014')
%xlabel('Birth') 
%ylabel('Year')
hist(x)

clear, clc, close all
[MainData,txt,raw] = xlsread('2010_Census_Populations_by_Zip_Code(1).csv');

TotalPopul=MainData(:,2);

figure;histogram(TotalPopul, 20)

xlim([0, max(TotalPopul)*1.01])

ylabel('count'); xlabel('Total Population Across Zipcodes')
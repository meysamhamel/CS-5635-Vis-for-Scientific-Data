clear, clc, close all
%Import  .csv file
[MainData,txt,raw] = xlsread('congress-terms.csv');

DorR_full={'Democrat','Republican'};
DorR_abbrev={'D','R'};
for DemOrRep=[1,2]
    countHouse=0; countSenate=0;
    for n=1:size(MainData,1)
        if strcmp(raw{n,10}, DorR_abbrev{DemOrRep})==1
            
            if strcmp(raw{n,2},'house')==1
                countHouse=countHouse+1;
            else
                countSenate=countSenate+1;
            end
        end
    end
    
    countIncum=0; countNotIncum=0;
    for n=1:size(MainData,1)
        if strcmp(raw{n,10}, DorR_abbrev{DemOrRep})==1
            
            if strcmp(raw{n,11},'Yes')==1
                countIncum=countIncum+1;
            else
                countNotIncum=countNotIncum+1;
            end
        end
    end
    
    PercHouse=countHouse/(countSenate+countHouse)*100;
    PercSenate=countSenate/(countSenate+countHouse)*100;
    PercIncum = countIncum/(countIncum+countNotIncum)*100;
    PercNotIncum = countNotIncum/(countIncum+countNotIncum)*100;
    
    countDemOrRep=0; SumAge=0;
    for n=1:size(MainData,1)
        if strcmp(raw{n,10}, DorR_abbrev{DemOrRep})==1
            SumAge=SumAge+MainData(n,13);
            countDemOrRep = countDemOrRep+ 1;
        end
    end
    AvgAge = SumAge/countDemOrRep;
    
    X(DemOrRep,:) = [AvgAge PercHouse PercSenate PercIncum PercNotIncum];
    
    
end


figure
glyphplot(X,'obslabels',['D';'R'])
figure
parallelcoords(X, 'Labels', {'Avg Age', '% House', '% Senate', '% Incumbinent',...
    '% Not incumbinent'}, 'Group', {'Democrats','Republicans'})

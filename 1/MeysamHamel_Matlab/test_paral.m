%load data
%components= {'Ba'	'Mn'	'Sr'	'Ti'	'Zr'	'Mg'	'V'	'Zn'};
components=  {'Mg'	'Sr'	'Mn'	'Ba'	'Ti'	'Zr'	'Zn'	'V'};
index=[6 3 2 1 4 5 8 7 9];

names=      {'L' 'HCM' 'BER'  'SK'  'PO'  'CH' 'UK'   'AA' 'SLO' 'ES' 'SA'};

ptypes=     {'.'  'o'   'x'   '+'   '*'   's'   'd'    'v' '^'    'p' 'h'};



data=[]
for i=1:size(names,2);
   %Data load and correlation 
   load(names{i});
   temp=eval(names{i}) ;
   temp=[temp ones(size(temp,1),1)*i];
   data=[data; temp];
end
%normal 
v0=[200 500 500 1000 50 8950 100 100];
data=data(:,index);
v0=v0(index(1:8));

%test=2*v0;
%test(1)=0;
%star(test,v0,1)

close all

lambda=2.5;
figure(1)
for i=1:11
   v=mean(data(find(data(:,end)==i),1:end-1));
   subplot(4,3,i)
   flagl=0;
   star(v,v0,i,lambda,flagl)
   title(names{i})
   axis([-2.5 2.5 -2.5 2.5])
   axis off
end   
   subplot(4,3,12)
   flagl=1;
   star(v0,v0,i,lambda,flagl)
   title('Standard')
   axis([-2.5 2.5 -2.5 2.5])
	%legend('Mg',	'Sr',	'Mn',	'Ba',	'Ti',	'Zr',	'Zn',	'V')
	colormap(gray)
    hold on
	%plot([1.5 2.5],[-2.5 -2.5])
   hold off
   axis off


colormap(gray)
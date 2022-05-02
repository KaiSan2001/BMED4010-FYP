%The file is used for plotting the bar chart of T7E1 result
%Author: Chan Kai San on 2021/11/20

clc;clear;close all;
%Data aqcuisition%
%Can use the readCSV function but here directly copy and paste%
T41_1=[44.77369022,44.10331576,49.60020771,37.80546884,12.68367462,29.08971557,27.9258056,31.84134624,32.05357327,42.23498196,35.6384616,21.31134974,18.66066952,34.62699309,22.95819656,14.16271647];
T41_2=[21.03208904,25.41292137,17.24018784,26.32957693,34.25911724,35.50190074,38.43217954,31.82988443,27.38478552,28.09821767,24.53234328,17.96273091,25.69213269,36.09051349,37.28103528,15.44490367];
T41_3=[47.51699714,47.18521375,45.21470914,44.80753234,42.01960655,37.93899105,40.68216704,39.48716223,48.2165417,49.64888461,45.27382899,23.96957013,33.09078197,39.18443084,37.36683694,20.07303812];
T42_1=[25.31432478,1.327470531,20.57329277,17.01195358,15.11072457,24.62192085,19.07942721,17.18414911,0.986869265,16.47893227,18.79645645,7.269492603,1.457361518,18.23366614,10.88723939,4.714020217];
T42_2=[2.741289053,2.17157771,29.44436065,21.18477877,32.45786738,39.4096429,36.81845478,20.88689065,0.778374742,32.19215024,28.99513815,23.45454674,5.439386332,4.166143929,6.571476872,11.43493303];

%X_categories%
%The four samples are different from the sgRNA length (in base-pair), 21 20 19 22%
X = categorical({'KKH-eSaCas9-19bp','KKH-eSaCas9-20bp','KKH-eSaCas9-21bp','KKH-eSaCas9-22bp','KKH-SaCas9-19bp','KKH-SaCas9-20bp','KKH-SaCas9-21bp','KKH-SaCas9-22bp','KKH-SAV2-19bp','KKH-SAV2-20bp','KKH-SAV2-21bp','KKH-SAV2-22bp','KKH-SAV1-19bp','KKH-SAV1-20bp','KKH-SAV1-21bp','KKH-SAV1-22bp'});
X = reordercats(X,{'KKH-eSaCas9-19bp','KKH-eSaCas9-20bp','KKH-eSaCas9-21bp','KKH-eSaCas9-22bp','KKH-SaCas9-19bp','KKH-SaCas9-20bp','KKH-SaCas9-21bp','KKH-SaCas9-22bp','KKH-SAV2-19bp','KKH-SAV2-20bp','KKH-SAV2-21bp','KKH-SAV2-22bp','KKH-SAV1-19bp','KKH-SAV1-20bp','KKH-SAV1-21bp','KKH-SAV1-22bp'});

%Y-components%
Y41_71=[T41_1(1:4);T41_2(1:4);T41_3(1:4)];
Y41_124=[T41_1(5:8);T41_2(5:8);T41_3(5:8)];
Y41_310=[T41_1(9:12);T41_2(9:12);T41_3(9:12)];
Y41_316=[T41_1(13:16);T41_2(13:16);T41_3(13:16)];
Y42_71=[T42_1(1:4);T42_2(1:4)];
Y42_124=[T42_1(5:8);T42_2(5:8)];
Y42_310=[T42_1(9:12);T42_2(9:12)];
Y42_316=[T42_1(13:16);T42_2(13:16)];

%Bar plotting%
figure
b1=bar(X(1:4),Y41_71);hold on
b2=bar(X(5:8),Y41_124);hold on
b3=bar(X(9:12),Y41_310);hold on
b4=bar(X(13:16),Y41_316);hold off
xlabel('Categories of the samples with different sgRNA length in base-pair');
ylabel('Quantification of T7E1 results');
title('Comparison of the cutting efficiency for VEGFA-8');

figure
b5=bar(X(1:4),Y42_71);hold on
b6=bar(X(5:8),Y42_124);hold on
b7=bar(X(9:12),Y42_310);hold on
b8=bar(X(13:16),Y42_316);hold off
xlabel('Categories of the samples with different sgRNA length in base-pair');
ylabel('Quantification of T7E1 results');
title('Comparison of the cutting efficiency for FANCF-13');

%Taking the average of quantification result to make the outcome has more universality%
Avg_41=(T41_1+T42_2+T41_3)./3;
Avg_42=(T42_1+T42_2)./2;

%Getting the standard deviation%
Pool_41_tri=[T41_1;T41_2;T41_3];
Pool_41_dup=[T41_1;T41_3];
Pool_42=[T42_1;T42_2];

%computation for 41B set%
sd41_tri=[];%Initialization of an empty array
sd41_dup=[];
sd42=[];
for i=1:16
    sd41_tri(end+1)=std(Pool_41_tri(1:3,i),1);
    sd41_dup(end+1)=std(Pool_41_dup(1:2,i),1);
    sd42(end+1)=std(Pool_42(1:2,i),1);
end

%Plotting%
figure
b9=bar(X(1:4),Avg_41(1:4),BarWidth=0.5);hold on
er13=errorbar(X(1:4),Avg_41(1:4),sd41_tri(1:4));er13.Color=[0 0 0];er13.LineStyle = 'none';
b14=bar(X(5:8),Avg_41(5:8),BarWidth=0.5);hold on
er14=errorbar(X(5:8),Avg_41(5:8),sd41_tri(5:8));er14.Color=[0 0 0];er14.LineStyle = 'none';
b15=bar(X(9:12),Avg_41(9:12),BarWidth=0.5);hold on
er15=errorbar(X(9:12),Avg_41(9:12),sd41_tri(9:12));er15.Color=[0 0 0];er15.LineStyle = 'none';
b16=bar(X(13:16),Avg_41(13:16),BarWidth=0.5);hold on
er16=errorbar(X(13:16),Avg_41(13:16),sd41_tri(13:16));er16.Color=[0 0 0];er16.LineStyle = 'none';
hold off
xlabel('Categories of the samples with different sgRNA length in base-pair');
ylabel('Quantification of T7E1 results');
title('Average of the cutting efficiency for VEGFA-8');

figure
b13=bar(X(1:4),Avg_42(1:4),BarWidth=0.5);hold on
er13=errorbar(X(1:4),Avg_42(1:4),sd42(1:4));er13.Color=[0 0 0];er13.LineStyle = 'none';
b14=bar(X(5:8),Avg_42(5:8),BarWidth=0.5);hold on
er14=errorbar(X(5:8),Avg_42(5:8),sd42(5:8));er14.Color=[0 0 0];er14.LineStyle = 'none';
b15=bar(X(9:12),Avg_42(9:12),BarWidth=0.5);hold on
er15=errorbar(X(9:12),Avg_42(9:12),sd42(9:12));er15.Color=[0 0 0];er15.LineStyle = 'none';
b16=bar(X(13:16),Avg_42(13:16),BarWidth=0.5);hold on
er16=errorbar(X(13:16),Avg_42(13:16),sd42(13:16));er16.Color=[0 0 0];er16.LineStyle = 'none';
hold off
xlabel('Categories of the samples with different sgRNA length in base-pair');
ylabel('Quantification of T7E1 results');
title('Average of the cutting efficiency for FANCF-13');


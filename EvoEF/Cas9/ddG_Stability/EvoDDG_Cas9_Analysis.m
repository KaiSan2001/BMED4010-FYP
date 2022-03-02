% Starting Date: 2022.01.25
% Ending Date: 2022.01.25
% Coder: Chan Kai San
% Email: u3556373@connect.hku.hk
% Description: This file is used to calculate the correlation between the
% DDG calculated from EvoEF and the fitness data calculated from EvMutation
% Reference: -Formatting:https://ww2.mathworks.cn/help/matlab/ref/sprintf.html
%            -File Reading:https://ww2.mathworks.cn/help/matlab/ref/xlsread.html
%            -Correlation:https://zhuanlan.zhihu.com/p/338322942

clc;clear all;close all;
%Data Preperation%
filename = 'EvoDDG_Cas9.xlsx';
Fitness_SaCas9 = xlsread(filename,'Filtered data','B2:B1297');
EvoDDG_SaCas9 = xlsread(filename,'Filtered data','E2:E1297');
Fitness_SpCas9 = xlsread(filename,'Filtered data','H2:H649');
EvoDDG_SpCas9 = xlsread(filename,'Filtered data','K2:K649');
[r,p]=corr(EvoDDG_SaCas9,Fitness_SaCas9,'type','Pearson');
[r1,p1]=corr(EvoDDG_SaCas9,Fitness_SaCas9,'type','Spearman');
[r2,p2]=corr(EvoDDG_SpCas9,Fitness_SpCas9,'type','Pearson');
[r3,p3]=corr(EvoDDG_SpCas9,Fitness_SpCas9,'type','Spearman');
%Plotting the fitness vs. DDG graph%
figure;
scatter(Fitness_SaCas9,EvoDDG_SaCas9);
xlabel("Fitness-SaCas9");ylabel("EvoDDG-SaCas9")
title('Fitness vs. DDG');
figure;
scatter(Fitness_SpCas9,EvoDDG_SpCas9);
xlabel("Fitness-SpCas9");ylabel("EvoDDG-SpCas9")
title('Fitness vs. DDG');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','SaCas9',r);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','SaCas9',r1);
fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','SpCas9',r2);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','SpCas9',r3);
fprintf('\n');

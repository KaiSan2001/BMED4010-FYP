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
filename = 'SingleMutate.xlsx';
Fitness = xlsread(filename,'Sheet1','B2:B76');
DDG = xlsread(filename,'Sheet1','E2:E76');
[r,p]=corr(DDG,Fitness,'type','Pearson');
[r1,p1]=corr(DDG,Fitness,'type','Spearman');
[r2,p2]=corr(Fitness,DDG,'type','Spearman');
%Plotting the fitness vs. DDG graph%
scatter(Fitness,DDG);
xlabel("Fitness");ylabel("DDG")
title('Fitness vs. DDG');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f',filename,r);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f',filename,r1);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f',filename,r2);fprintf('\n');
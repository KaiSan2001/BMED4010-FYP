% Starting Date: 2022.02.24
% Ending Date: 2022.02.24
% Coder: Chan Kai San
% Email: u3556373@connect.hku.hk
% Description: This file is used to calculate the correlation between the
% ddG_binding calculated from UniDesign and the fitness data from Experiments
% Reference: -Formatting:https://ww2.mathworks.cn/help/matlab/ref/sprintf.html
%            -File Reading:https://ww2.mathworks.cn/help/matlab/ref/xlsread.html
%            -Correlation:https://zhuanlan.zhihu.com/p/338322942

clc;clear all;close all;
%Data Preperation%
filename = 'SaCas9Fitness.csv';
Fitness_SaCas9 = xlsread(filename,'SaCas9Fitness','B2:B1297');
EvoDDG_SaCas9 = xlsread(filename,'SaCas9Fitness','E2:E1297');
[r,p]=corr(EvoDDG_SaCas9,Fitness_SaCas9,'type','Pearson');
[r1,p1]=corr(EvoDDG_SaCas9,Fitness_SaCas9,'type','Spearman');
%Plotting the fitness vs. DDG graph%
figure;
scatter(Fitness_SaCas9,EvoDDG_SaCas9);
xlabel("Fitness-SaCas9");ylabel("UniDesignddG-SaCas9")
title('Fitness vs. DDG');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','SaCas9',r);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','SaCas9',r1);
fprintf('\n');

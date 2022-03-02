% Starting Date: 2022.02.22
% Ending Date: 2022.02.22
% Coder: Chan Kai San
% Email: u3556373@connect.hku.hk
% Description: This file is used to calculate the correlation between the
% DDG calculated from EvoEF and the fitness data calculated from EvMutation
% Reference: -Formatting:https://ww2.mathworks.cn/help/matlab/ref/sprintf.html
%            -File Reading:https://ww2.mathworks.cn/help/matlab/ref/xlsread.html
%            -Correlation:https://zhuanlan.zhihu.com/p/338322942

clc;clear all;close all;
%Data Preperation%
filename = 'regionalSampling.csv';
Fitness2_SpCas9 = xlsread(filename,'regionalSampling','B2:B5');
EvoDDG2_SpCas9 = xlsread(filename,'regionalSampling','E2:E5');
Fitness3_SpCas9 = xlsread(filename,'regionalSampling','H2:H12');
EvoDDG3_SpCas9 = xlsread(filename,'regionalSampling','J2:J12');
[r2,p2]=corr(EvoDDG2_SpCas9,Fitness2_SpCas9,'type','Pearson');
[r3,p3]=corr(EvoDDG2_SpCas9,Fitness2_SpCas9,'type','Spearman');
[r4,p4]=corr(EvoDDG3_SpCas9,Fitness3_SpCas9,'type','Pearson');
[r5,p5]=corr(EvoDDG3_SpCas9,Fitness3_SpCas9,'type','Spearman');
%Plotting the fitness vs. DDG graph%
figure
scatter(Fitness2_SpCas9,EvoDDG2_SpCas9);
xlabel("Fitness SpCas9 double M");ylabel("EvoDDG SpCas9 double M")
title('Fitness vs. EvoDDG');

figure
scatter(Fitness3_SpCas9,EvoDDG3_SpCas9);
xlabel("Fitness SpCas9 triple M");ylabel("EvoDDG SpCas9 triple M")
title('Fitness vs. EvoDDG');

fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','SpCas9_doubleM',r2);fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','SpCas9_doubleM',r3);fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','SpCas9_tripleM',r4);fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','SpCas9_tripleM',r5);fprintf('\n');


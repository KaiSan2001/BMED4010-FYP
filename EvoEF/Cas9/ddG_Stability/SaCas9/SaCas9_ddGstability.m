% Starting Date: 2022.02.25
% Ending Date: 2022.02.25
% Coder: Chan Kai San
% Email: u3556373@connect.hku.hk
% Description: This file is used to calculate the correlation between the
% ddG_binding calculated from UniDesign and the fitness data from Experiments
% Reference: -Formatting:https://ww2.mathworks.cn/help/matlab/ref/sprintf.html
%            -File Reading:https://ww2.mathworks.cn/help/matlab/ref/xlsread.html
%            -Correlation:https://zhuanlan.zhihu.com/p/338322942

clc;clear all;close all;
%Data Preperation%
filename = 'ddG_Stability_5czz.xlsx';
Mutant = xlsread(filename,'ddG','A2:A53');
Fitness1_SaCas9 = xlsread(filename,'ddG','D2:D53');
Fitness2_SaCas9 = xlsread(filename,'ddG','E2:E53');
EvoDDG_SaCas9 = xlsread(filename,'ddG','B2:B53');
[r,p]=corr(EvoDDG_SaCas9,Fitness1_SaCas9,'type','Pearson');
[r1,p1]=corr(EvoDDG_SaCas9,Fitness1_SaCas9,'type','Spearman');
[r2,p2]=corr(EvoDDG_SaCas9,Fitness2_SaCas9,'type','Pearson');
[r3,p3]=corr(EvoDDG_SaCas9,Fitness2_SaCas9,'type','Spearman');
%Plotting the fitness vs. DDG graph%
figure;
scatter(EvoDDG_SaCas9,Fitness1_SaCas9);
xlabel("EvoEFddG-SaCas9");ylabel("KO value of ON1")
title('Fitness vs. EvoEFddG  ON1');
figure;
scatter(EvoDDG_SaCas9,Fitness2_SaCas9);
xlabel("EvoEFddG-SaCas9");ylabel("KO value of ON2")
title('Fitness vs. EvoEFDDG  ON2');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','ON1',r);fprintf('\n');fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','ON1',r1);fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','ON1',r2);fprintf('\n');fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','ON1',r3);fprintf('\n');
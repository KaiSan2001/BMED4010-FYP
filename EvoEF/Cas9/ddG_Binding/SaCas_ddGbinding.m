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
filename = 'ddG_binding_5czz.xlsx';
Fitness_On1 = xlsread(filename,'ddG','D2:D53');
EvoDDG_On1NOPAM = xlsread(filename,'ddG','B2:B53');
EvoDDG_On1PAM = xlsread(filename,'ddG','C2:C53');
Fitness_On2 = xlsread(filename,'ddG','I2:I53');
EvoDDG_On2NOPAM = xlsread(filename,'ddG','G2:G53');
EvoDDG_On2PAM = xlsread(filename,'ddG','H2:H53');
[r,p]=corr(EvoDDG_On1NOPAM,Fitness_On1,'type','Pearson');[r1,p1]=corr(EvoDDG_On1NOPAM,Fitness_On1,'type','Spearman');
[r2,p2]=corr(EvoDDG_On1PAM,Fitness_On1,'type','Pearson');[r3,p3]=corr(EvoDDG_On1PAM,Fitness_On1,'type','Spearman');
[r4,p4]=corr(EvoDDG_On2NOPAM,Fitness_On2,'type','Pearson');[r5,p5]=corr(EvoDDG_On2NOPAM,Fitness_On2,'type','Spearman');
[r6,p6]=corr(EvoDDG_On2PAM,Fitness_On2,'type','Pearson');[r7,p7]=corr(EvoDDG_On2PAM,Fitness_On2,'type','Spearman');

%Plotting the fitness vs. DDG graph%
figure;
scatter(EvoDDG_On1NOPAM,Fitness_On1);xlabel('ddG Binding of On1 without PAM');ylabel('KO value of ON1');title('scatter plot for ddG Binding of On1 without PAM vs KO value of ON1');
figure;
scatter(EvoDDG_On1PAM,Fitness_On1);xlabel('ddG Binding of On1 with PAM');ylabel('KO value of ON1');title('scatter plot for ddG Binding of On1 with PAM vs KO value of ON1');
figure;
scatter(EvoDDG_On2NOPAM,Fitness_On2);xlabel('ddG Binding of On2 without PAM');ylabel('KO value of ON2');title('scatter plot for ddG Binding of On2 without PAM vs KO value of ON2');
figure;
scatter(EvoDDG_On2PAM,Fitness_On2);xlabel('ddG Binding of On2 with PAM');ylabel('KO value of ON2');title('scatter plot for ddG Binding of On2 with PAM vs KO value of ON2');
%Output the result%
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','On1NOPAM',r);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','On1NOPAM',r1);
fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','On1PAM',r2);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','On1PAM',r3);
fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','On2NOPAM',r4);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','On2NOPAM',r5);
fprintf('\n');
fprintf('The Pearson Correlation Coefficient for %s is: %0.05f','On2PAM',r6);
fprintf('\n');
fprintf('The Spearman Correlation Coefficient for %s is: %0.05f','On2PAM',r7);
fprintf('\n');
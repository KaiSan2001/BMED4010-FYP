% Starting Date: 2022.01.25
% Ending Date: 2022.01.25
% Coder: Chan Kai San
% Email: u3556373@connect.hku.hk
% Description: This file is used to calculate the correlation between the
% DDG calculated from EvoEF and the fitness data calculated from EvMutation
% Reference: -Formatting:https://ww2.mathworks.cn/help/matlab/ref/sprintf.html
%            -File Reading:https://ww2.mathworks.cn/help/matlab/ref/xlsread.html
%            -Correlation:https://zhuanlan.zhihu.com/p/338322942

%Data Preperation%
for i= 1:5
    filename = sprintf('RandomData_%d.xlsx',i);
    Fitness = xlsread(filename,'Filtered data','B2:B1001');
    DDG = xlsread(filename,'Filtered data','E2:E1001');
    [r,p]=corr(DDG,Fitness,'type','Pearson');
    [r1,p1]=corr(DDG,Fitness,'type','Spearman');
    fprintf('The Pearson Correlation Coefficient for %s is: %0.05f',filename,r);
    fprintf('\n');
    fprintf('The Spearman Correlation Coefficient for %s is: %0.05f',filename,r1);
    fprintf('\n');fprintf('\n');
end


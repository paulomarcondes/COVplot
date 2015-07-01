function [vcount,m1,m2]=hitcountpolar(M,bin_azi,bin_x)
    
pi=%pi


//HitCount

aux1=0;
aux2=0;

nbin_azi=(360/bin_azi)+1
nbin_x=(max(M(:,1))/bin_x)+1

for i=1:nbin_azi
    for j=1:nbin_x
        
        lazi=(M(:,2)>aux1)&(M(:,2)<i*(bin_azi*pi/180));
        lx=(M(:,1)>aux2)&(M(:,1)<j*bin_x)
        
        count=sum(lazi&lx)
        vcount(i,j)=count
        
        
        aux2=dx*(j-1)
        m1(i)=aux1
        m2(j)=aux2
end

aux1=bin_azi*pi/180*i
end

endfunction

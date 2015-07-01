def hitcountpolar(M,bin_azi,bin_x):

#HitCount

#aux1=0;
#aux2=0;

nbin_azi = np.linspace(0,360,bin_azi)
nbin_x = np.linspace(0,max(M[0]),bin_x)

for az in nbin_azi:
    for x in nbin_x:
        lazi = (M[x,az] > aux1) && (M[x,az]<az*radian(bin_azi)
        lx = (M[x,az] > aux2 && (M[x,az] < j*bin_x)

        count=sum(lazi&lx)
        vcount(x,az)=count


        aux2=bin_x*
        m1(i)=aux1
        m2(j)=aux2

aux1=radian(bin_azi*i)

return(

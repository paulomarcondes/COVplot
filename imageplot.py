__author__ = 'cmp9'

if __name__ == "__main__":
	import sys
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.cm as cm

	z_step=15
	h_step=100
	h_max = 15000

	z_bin = np.linspace(0,360,(360/z_step)+1)
	h_bin = np.linspace(0,h_max,(h_max/h_step)+1)

	[Az,Os]=np.meshgrid(z_bin,h_bin)

	# Bins preenchidos com ruido branco
	X=np.random.rand(len(z_bin),len(h_bin))

	# Aleatorio para azimute e afastamento
	randz=np.random.randn(10000)
	randh=np.random.randn(10000)
	z=360*(abs(randz)/max(abs(randz)))
	h=15000*(abs(randh)/max(abs(randh)))

	#data =
	
	#xtick = np.linspace(0,h_max,16)
	#ytick = np.linspace(0,360,9)

	xtick = [0,2.5,5,7.5,10,12.5,15]
	ytick = [0,45,90,135,180,225,270,315,360]
	
	fig, ax = plt.subplots()
	im=ax.imshow(X, cmap=cm.RdYlGn, origin="lower", interpolation='nearest')
	plt.colorbar(im,orientation='horizontal')
	ax.set_title('Azimuthal Fold')
	#ax.set_xticks(xtick)
	#ax.set_yticks(ytick)
	#ax.set_xticklabels(xtick)
	#ax.set_yticklabels(ytick)
	ax.set_ylabel('Azimuth bins')
	ax.set_xlabel('Offset bins')
	

	# numrows, numcols = X.shape
	# def format_coord(x, y):
	#     col = int(x+0.5)
	#     row = int(y+0.5)
	#     if col>=0 and col<numcols and row>=0 and row<numrows:
	#         z = X[row,col]
	#         return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)
	#     else:
	#         return 'x=%1.4f, y=%1.4f'%(x, y)
	#
	# ax.format_coord = format_coord
	plt.show()
	sys.exit()
else:
	print("Problem found. Exiting.")
	sys.exit()

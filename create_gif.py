import imageio.v3 as iio

filenames = ['hippocorn1.png' , 'hippocorn2.png' , 'hippocorn3.png' , 'hippocorn4.png' ]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  
iio.imwrite('myfirstgif.gif', images, duration = 500, loop = 0)
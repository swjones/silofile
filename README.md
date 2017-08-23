# silofile

A small class to write silo format files using
[pyvisfile](https://mathema.tician.de/software/pyvisfile/).

See my [website](swjones.github.io/resources) for details of how to install
[pyvisfile](https://mathema.tician.de/software/pyvisfile/) and its
dependencies.

## Example usage:

~~~python
>>> from silofile import silofile as sf

create a 3d mesh:

>>> x = np.linspace(0.,1.,11); y = np.linspace(0.,1.,11); z = np.linspace(0.,1.,11)
>>> mesh = [ x, y, z ]

create some 3d data:

>>> xx,yy,zz = np.meshgrid(x,y,z)
>>> spam = np.cos(xx) + 2.*np.sin(xx-yy) + 4.*np.cos(yy-zz)**2
>>> jones = np.sqrt(np.abs(spam))

create the object:

>>> s = sf(mesh, ["spam","jones"], [spam,jones])

write the file:

>>> s.write("myfile.silo")
~~~

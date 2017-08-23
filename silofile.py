import pyvisfile.silo as silo
from warnings import warn

class silofile():
    def __init__(self, mesh, keys, values):
        """object containing data to be written to a silo file

        Parameters
        ----------
        mesh: list
            python list containing mesh coordinates as numpy arrays
        keys: list
            python list containing the names of the grid data
        values: list
            python list containing the grid data

        Examples
        --------
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
        """

        self.dim = len(mesh)     # dimensions of data set
        assert self.dim in [2,3] # make sure we have 2d or 3d data

        self.mesh = mesh
        self.keys = keys
        self.values = values

    def write(self,filename):
        """write silo file with name `filename`"""

        # open the silo file
        self.f = silo.SiloFile(filename, mode = silo.DB_CLOBBER)

        # write the mesh
        self.f.put_quadmesh("mesh", self.mesh)

        # write the data
        for item in zip(self.keys,self.values):
            self.f.put_quadvar1(item[0], "mesh", item[1], item[1].shape,
                    centering = silo.DB_NODECENT)

        # close file
        self.f.close()





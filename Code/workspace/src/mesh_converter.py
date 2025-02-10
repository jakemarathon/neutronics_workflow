from remesh import remesh_stl
import os
import subprocess
import meshio

GMSH2EXO_CMD = 'gmsh2exo'

#Input the name of the directory containing the STL files generated by CAD_to_OpenMC script
STL_DIR = 'dagmc_20250210_063843.307509'
#List the stl file names you wish to convert and the name you wish the resultant mesh to have
STL_FILENAMES = {

'volume_1_with_corrected_face_normals.stl':'firstwall.msh',
'volume_2_with_corrected_face_normals.stl':'structural1.msh',
'volume_3_with_corrected_face_normals.stl':'internalspace.msh',
'volume_4_with_corrected_face_normals.stl':'structural2.msh',
'volume_5_with_corrected_face_normals.stl':'blankettank.msh',
'volume_6_with_corrected_face_normals.stl':'blanketouter.msh',
}       

for stl_filename, mesh_filename in STL_FILENAMES.items():
    src=os.path.join(STL_DIR,stl_filename)
    dst=os.path.join(STL_DIR,mesh_filename)
    remesh_stl(src,dst)
    exo_name = '%s.exo' % mesh_filename [:-4]
    subprocess.run([GMSH2EXO_CMD,dst, exo_name])

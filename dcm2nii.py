import SimpleITK as sitk
import glob

paths= glob.glob('/data/jytang/CT2MR_sample/*/MRI')
for file_path in paths:
    print(file_path)
    id = file_path.split('/')[-2]
    modal = file_path.split('/')[-1]
    output = '/data/jytang/CT2MR_sample/'+ id + '/' + id + '_' + modal + '.nii.gz'
    print(output)
    
    series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(file_path)
    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path)

    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)

    image3D = series_reader.Execute()
    sitk.WriteImage(image3D, output)
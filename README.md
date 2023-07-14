# PyImageProcPipeLine
A Project to watch folders for new image files and automatically process them to the extents available.
Python version - 3.11+
Platform - tested on Windows 11


Prior art: 
- Prose - an astronomical set of building blocks for building image processing pipelines.
- https://guiwitz.github.io/PyImageCourse_beginner/README.html
- Siri, Siril, Gess 

#Function 
The purpose of this is to watch a folder on the image processing file server and update intelligently the output files depending on the availability of supporting files ( e.g. bias, darks, flats ) and the configuration settings for the types of image file found. 

#Features desired: 
Recursive inspection of file systems for new files
Programmable delay of action on new file found 
Programmable frequency of scanning folder tree contents vs lstening for change events 
Addressing the key use cases : 
<ul>
  <li>Addition of bias file - CRUD bias master files </li>
  <li>Addition of dark file - CRUD dark master files </li>
  <li>Addition of flat file for filtered and unfiltered images </li>
  <li>Creation/Modification/Update/Delete of folder, files</li>
  <li>Addition of image file  - perform automatic calibration modified by configuration file settings. Maintain originals while minimising working set retention.
    <ul>
      <li>Use variations on image calibration chains identified by common attributes - camera type, camera name, image binning ratio etc and specified in the settings files.</li>
      <li>Update existing master image files</li>
      <li>
    </ul>
  </li>
  <li>Logging of outcomes</li>
  <li>Alerting and flagging of issues - missing files, processing errors</li>
  <ul>
    <li>Option Email reports on success/fail/errors</li>
    <li>Log file record of operations</li>
    <li></li>
  </ul>
</ul>

# Structure 
The program will centre on a folder watchdog service and a related xml/Json configuration settings file 
  Create a settings file hierarchy of settings. 
  Create and register handlers for the events on a per attribute-type basis 
The watchdog will trigger on detecting an event - ie folder content change. 
the watchdog will 

# Assumptions 
We assume that each image folder is structured on a 

# config structure 
Header
{
foldertree: { 
name : string;
path : path to monitored folder root ;
[<attribute selector list>{ }] }

imageTypes : [
  {bias: { path, name, [attributes] }, 
  {darks: {path , name, [attributes] }, 
  {flats: { path, name, [attributes] }, 
]
imageOperators : [
  { addition; division, subtraction, average, median, 

};

# Library Dependencies
prose - 
numpy - numerical processing library 
pandas - ?
matplotlib.pyplot - plotting library 
skimage - 
scipy - Scientific processing library, contains Image.io tools. 
watchdog  - folder watchdog library 
pyyaml - https://pypi.org/project/watchdog/
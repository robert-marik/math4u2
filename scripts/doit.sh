python3 build_python.py
cp -r _site site
rm -r ../../../site 
mv site ../../../
cp -r _latex/0* ../../../site/
#cp -r _latex/cesium ../../../site/sandbox/
#cp -r _latex/lov ../../../site/sandbox/
#cp -r _latex/ostrovy ../../../site/sandbox/
#cp -r _latex/troficke_funkce ../../../site/sandbox/
#cp -r _latex/tomograf_EBSI ../../../site/sandbox/
#cp -r _latex/resistograph ../../../site/sandbox/
#cp -r _latex/spoje ../../../site/sandbox/


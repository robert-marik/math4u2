# Converts Markdown to PDF using xelatex

if [ $# -eq 0 ]; then
    echo "No parameter provided. Exiting."
    exit 1
fi

# copy data to bild directory
mkdir -p build
rm ./build/*
cp $1/* build/
cp math4u_template.html build/
cd build

# convert to html
for file in cs_article.md
do
  echo $file
  base="${file%.*}"  
  #pandoc -s "$file" --template=./math4u_template.html -H ../math4u_header.css --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js  -o "${base}.html"
  #pandoc -s "$file" -t html --template math4u_template.html --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js  -o "${base}.html"
  pandoc -t html "$file" -s --template math4u_template.html --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js > "${base}.html"
done



# Converts Markdown to PDF using xelatex

if [ $# -eq 0 ]; then
    echo "No parameter provided. Exiting."
    exit 1
fi

# copy data to build directory
mkdir -p build
rm ./build/*
cp $1/* build/
cd build

# convert to LaTeX
for file in *.md
do
  echo $file
  base="${file%.*}"  
  pandoc -s "$file" -H ../math4u_header.tex -o "${base}.tex"
  sed -i 's/\.svg/\.pdf/' "${base}.tex"
done

for file in *.svg
do
    echo $file
    base="${file%.*}"  
    rsvg-convert -f pdf -o ${base}.pdf $file
done

ls

# compile using xelatex
for file in *article.tex
do
    echo $file
    vlna $file
    xelatex --shell-escape $file
    xelatex --shell-escape $file
done


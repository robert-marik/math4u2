#!/bin/bash

if [ $# -eq 0 ]; then
    >&2 echo "Enter filename as the first argument."
    exit 1
fi

name=$1


for lang in CS ES PL SK
do
   lang_lovercase=$(echo "$lang" | tr '[:upper:]' '[:lower:]')
   target=$(echo "$1" | sed "s/\/en_/\/${lang_lovercase}_/")
   content="The translation of $1 to $lang should be here."
   echo $lang_lovercase
   echo $target
   echo $content > ../$target
   git add ../$target    
   gh issue create --title "Missing $lang translation: $name" --body "Translate [$1](https://github.com/robert-marik/math4u/blob/main/$1) to $lang and save in  [$target](https://github.com/robert-marik/math4u/blob/main/$target) file." --label "Needs $lang"
done

echo "-------------------------"
echo "Commit your changes and push to server to upload an initial version of files."
echo "git commit -m \"Files for translation uploaded\" -a"
echo "git push"

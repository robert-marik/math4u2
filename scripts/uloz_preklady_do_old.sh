for dir in ../000*; do
    for lang in sk pl es; do
        file="$dir/${lang}_article.md"
        if [ -f "$file" ]; then
            cp -v "$file" "${dir}/${lang}_article_old.md"
        fi
    done
done


for dir in ../000*; do
    for lang in sk pl es; do
        file="$dir/${lang}_article_old.md"
        if [ -f "$file" ]; then
            echo "Čistím: $file"
            sed -i '/^# workflow/d' "$file"
        fi
    done
done
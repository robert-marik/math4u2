for file in ../00*/*_article.md; do
    # Přeskoč soubor, pokud už obsahuje "# workflow: in progress"
    if grep -q '^# workflow: in progress' "$file"; then
        echo "Přeskakuji (už obsahuje workflow): $file"
        continue
    fi

    echo "Upravuji: $file"
    # Vlož tři řádky za první výskyt "---"
    awk '
        BEGIN { done=0 }
        /^---$/ && !done {
            print $0
            print "# workflow: in progress"
            print "# workflow: translating"
            print "# workflow: finished"
            done=1
            next
        }
        { print $0 }
    ' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
done

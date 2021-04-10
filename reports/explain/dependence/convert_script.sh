for p in *.pdf
do 
   pdftoppm "$p" "$p" -png
done

rm *.pdf
mmv \*pdf-1.png \#1png



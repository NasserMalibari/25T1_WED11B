mlalias 'cs2041.wed11-brass' | sed -E -n '/^\s*Addresses/,/^\s*Owners/p' |
head -n -1 | 
tail -n +2| 
cut -d'@' -f1 |
sed -E 's/^\s*//'
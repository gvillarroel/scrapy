scrapy runspider economicos.py -o data.json
grep -ie "201[8]-\(01\|02\)" data.json | grep -ie "macul" | grep -ie "\(casa\|propiedad\|inmueble\|departamento\|[\$\ 0-9\.]\{4,\}\)"

grep -ie "201[8]-\(01\|02\)" data.json | grep -ie "macul" | grep -ie "\(casa\|propiedad\|inmueble\|departamento\|[\$\ 0-9\.]\{4,\}\)"
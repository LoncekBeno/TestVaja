odgovor = {
"temperatura": 24 ,
"vlaznost": 60 ,
"veter": 8 ,
"lokacija": "Ljubljana"
}

print(odgovor["temperatura"])

print(odgovor["vlaznost"])

print(f"V mestu Ljubljana je {odgovor["temperatura"]} stopinj.")



student = {
"ime": "Marko",
"priimek": "Horvat",
"naslov": {
"ulica": "Slovenska cesta 12",
"mesto": "Maribor",
"posta": 2000
    }
}

print(student["naslov"]["ulica"])

print(student["priimek"])

print(f"{student['ime']} {student['priimek']}, {student["naslov"]["ulica"]}")

razred = {
"oznaka": "4.a",
"dijaki": ["Ana", "Bojan", "Cvetka", "David"] ,
"ocene": [5 , 4 , 5 , 3]
}

print(f"{razred["dijaki"][0]}")

print(f"{razred["ocene"][2]}")

print(f"{razred["dijaki"]}")
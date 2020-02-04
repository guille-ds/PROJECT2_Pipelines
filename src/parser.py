from argparse import ArgumentParser

def parser():
    parser = ArgumentParser(description="Nos imprime los parámetros")

    parser.add_argument("country") # flag para indicar el pais
    parser.add_argument("year", type=int, nargs="+") # flag para indicar el año
    parser.add_argument("tracktime", type=int, nargs="+") # flag para indicar el tiempo de trackeo
        
    args = parser.parse_args()
    
    country = args.country
    year = args.year
    sec = args.tracktime

    print(args)
    return country, year, sec


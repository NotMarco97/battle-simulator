if __name__ == "__main__":
    hpA = 100
    attackA = 10
    nameA = "Waldo"
    nameB = "Bob"
    hpB = 110
    attackB = 8
    
    while hpA > 0 and hpB > 0:
        hpB = hpB - attackA
        if hpB <= 0:
            print(f"{nameB} has been defeated!")
            break
        hpA = hpA - attackB
        if hpA <= 0:
            print(f"{nameA} has been defeated!")
            break
        
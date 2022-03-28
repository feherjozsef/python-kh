from tetelek.nevezetes_tetelek import sum_numbers       # így hivatkozhatunk másik mappában lévő file-ra

print(sum_numbers([]))
print(f"Az import vagy mi neve: {__name__}")
print(sum_numbers.__module__)   # Megmutatja mely module-ban van az fv
print(sum_numbers.__doc__)  # Ha van dokumentációs megjegyzés az fv-hezz, akkor kiírja a prog
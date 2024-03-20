#!/usr/bin/env python3

table = 0

while table <= 10:
    number = 0
    
    table_line = f"Table de {table}:"
    
    while number <= 10:
        table_line += f" {table * number}"
        number += 1

    print(table_line)
    table += 1

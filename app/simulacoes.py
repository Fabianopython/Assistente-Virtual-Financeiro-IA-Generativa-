def juros_compostos(valor, taxa, meses):
    taxa_decimal = taxa / 100
    montante = valor * (1 + taxa_decimal) ** meses
    return round(montante, 2)


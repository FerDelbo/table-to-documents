from src.table_representation import TableRepresentation

t = TableRepresentation('./results.csv')
l = t.get_all_representations()

saida = list(l.values())
print(saida[1])

from rdkit import Chem
from rdkit.Chem import Descriptors

# Exemplo de uma molécula de Aspirina (C9H8O4)
mol = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')  # SMILES da Aspirina

# Verifica se a molécula foi carregada corretamente
if mol:
    print("Molécula carregada com sucesso!")
else:
    print("Erro ao carregar a molécula!")

# Calculando propriedades
peso_molecular = Descriptors.MolWt(mol)  # Peso molecular
num_atoms = mol.GetNumAtoms()  # Número de átomos
num_bonds = mol.GetNumBonds()  # Número de ligações


class Formula:
    def __init__(self, mol):
        self.mol = mol
        self.formula = self.calculate_formula()

    def calculate_formula(self):
        """Calcula a fórmula empírica da molécula."""
        formula = Chem.rdMolDescriptors.CalcMolFormula(self.mol)
        return formula

# Exemplo de uma molécula de Aspirina (C9H8O4)
mol = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')  # SMILES da Aspirina


if mol:
    print("Molécula carregada com sucesso!")
else:
    print("Erro ao carregar a molécula!")


formula_obj = Formula(mol)
print(f"A fórmula empírica da molécula é: {formula_obj.formula}")

# Calculando outras propriedades
peso_molecular = Descriptors.MolWt(mol)  # Peso molecular
num_atoms = mol.GetNumAtoms()  # Número de átomos
num_bonds = mol.GetNumBonds()  # Número de ligações


print(f"Peso molecular: {peso_molecular:.2f} g/mol")
print(f"Número de átomos: {num_atoms}")
print(f"Número de ligações: {num_bonds}")


from rdkit.Chem import Draw
img = Draw.MolToImage(mol)
img.show()  # Exibe a imagem da molécula






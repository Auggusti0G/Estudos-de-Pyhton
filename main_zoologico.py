from classes_zoologico import Animal, Mamifero, Ave

def main():
    # --- Superclasse ---
    print("=== TESTANDO SUPERCLASSE ANIMAL ===")
    a1 = Animal("Animal Genérico", 5)
    print(a1.get_nome(), "-", a1.get_idade())
    a1.emitir_som()
    a1.envelhecer()
    a1.set_idade(-3)  # Teste de validação

    # --- Subclasse Mamifero ---
    print("\n=== TESTANDO SUBCLASSE MAMIFERO ===")
    m1 = Mamifero("Leão", 8, "Felino", "Savana")
    m2 = Mamifero("Macaco", 3, "Primata", "Floresta", False)

    m1.amamentar()
    print(m2.get_especie(), "-", m2.get_habitat())
    m2.emitir_som()
    m1.set_possui_pelos("sim")  # Teste de validação

    # --- Subclasse Ave ---
    print("\n=== TESTANDO SUBCLASSE AVE ===")
    a2 = Ave("Papagaio", 2, "Psitacídeo", "Verde")
    a3 = Ave("Pinguim", 5, "Spheniscidae", "Preto e branco", False)

    a2.cantar()
    a3.emitir_som()
    a2.set_cor_das_penas("")  # Teste de validação
    a3.envelhecer()


if __name__ == "__main__":
    main()

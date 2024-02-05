# Sistema de Gerenciamento de Inventário para E-commerce

Este projeto consiste em um sistema de gerenciamento de inventário desenvolvido em Python e SQLite3 para um e-commerce. O objetivo é oferecer funcionalidades básicas de gerenciamento de estoque, como adicionar produtos, consultar a quantidade disponível, remover produtos do estoque e listar os produtos disponíveis.

## Funcionalidades

- **Adicionar Produto**: Permite adicionar novos produtos ao inventário juntamente com a quantidade inicial.
- **Consultar Produto**: Permite verificar a quantidade disponível de um determinado produto no estoque.
- **Remover Produto**: Permite remover uma certa quantidade de um produto do estoque, atualizando a quantidade disponível.
- **Listar Produtos**: Fornece uma lista de todos os produtos atualmente disponíveis no estoque.

## Como Usar

Para utilizar o sistema, basta instanciar a classe `Management` e realizar as operações desejadas, como exemplificado no código abaixo:

```python
# Exemplo de uso do sistema
from inventory_management import Management

# Criar uma instância do sistema
System = Management("inventory.db")

# Adicionar produtos
System.add_product("T-Shirt", 20)
System.add_product("Pants", 30)
System.add_product("Shoes", 15)

# Consultar a quantidade de um produto
shirt_stock = System.consult_product("T-Shirt")
print(f"Amount of T-Shirts in Stock: {shirt_stock}")

# Remover uma quantidade de produto do estoque
System.remove_product("Pants", 20)

# Listar produtos disponíveis
products_stock = System.list_products()
print(f"Products in Stock: {products_stock}")

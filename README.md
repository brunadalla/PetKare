# Pet Kare

O objetivo desse projeto era desenvolver uma API que gerencia cadastro de pets e suas características.

### 1. **Criação de um Pet**

### `api/pets`

### Exemplo de Request:
```
POST api/pets
Host: 
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:
```json
{
  "name": "Seraphim",
  "age": 1,
  "weight": 20,
  "sex": "Male",
  "group": {"scientific_name": "canis familiaris"},
  "traits": [{"name": "clever"}, {"name": "friendly"}]
}
```

### Exemplo de Response:
```
201 Created
```

```json
{
  "id": 1,
  "name": "Seraphim",
  "age": 1,
  "weight": 20.0,
  "sex": "Male",
  "group": {
    "id": 1,
    "scientific_name": "canis familiaris",
    "created_at": "2022-11-27T17:55:22.819371Z"
  },
  "traits": [
    {
      "id": 1,
      "name": "clever",
      "created_at": "2022-11-27T17:55:30.819371Z"
    },
    {
      "id": 2,
      "name": "friendly",
      "created_at": "2022-11-27T17:55:31.819371Z"
    }
  ]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 400 Bad Request | Fields required |

---

### 1.2. **Listando Pets**

### `api/pets`

### Exemplo de Request:
```
GET api/pets
Host: 
Authorization: Bearer Token
Content-type: application/json
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
[
  {
    "id": 1,
    "name": "Seraphim",
    "age": 1,
    "weight": 20.0,
    "sex": "Male",
    "group": {
      "id": 1,
      "scientific_name": "canis familiaris",
      "created_at": "2022-11-27T17:55:22.819371Z"
    },
    "traits": [
      {
        "id": 1,
        "name": "clever",
        "created_at": "2022-11-27T17:55:30.819371Z"
      },
      {
        "id": 2,
        "name": "friendly",
        "created_at": "2022-11-27T17:55:31.819371Z"
      },
    ]
  }
  ...
]
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized | Invalid token |

---

### 1.3. **Listar Pet por ID**

### `api/pets/:pet_id`

### Exemplo de Request:
```
GET api/pets/9cda28c9-e540-4b2c-bf0c-c90006d37893
Host: 
Authorization: Bearer Token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| pet_id     | string      | Identificador único do pet (Pet) |

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
  "id": 1,
  "name": "Seraphim",
  "age": 1,
  "weight": 20.0,
  "sex": "Male",
  "traits_count": 2,
  "group": {
    "id": 1,
    "scientific_name": "canis familiaris",
    "created_at": "2022-11-27T17:55:22.819371Z"
  },
  "traits": [
    {
      "id": 1,
      "name": "clever",
      "created_at": "2022-11-27T17:55:30.819371Z"
    },
    {
      "id": 2,
      "name": "friendly",
      "created_at": "2022-11-27T17:55:31.819371Z"
    },
  ]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized | Invalid token |
| 404 Not Found    | Pet not found |

---

### 1.4. **Atualizar Usuário por ID**

### `api/pets/:pet_id`

### Exemplo de Request:
```
PATCH api/pets/9cda28c9-e540-4b2c-bf0c-c90006d37893
Host: 
Authorization: Bearer Token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| pet_id     | string      | Identificador único do pet (Pet) |

### Corpo da Requisição:
```json
{
  "age": 3
  "traits": [{"name": "hunter"}]
}
```

### Exemplo de Response:
```
200 OK
```
```json
{
  "id": 1,
  "name": "Seraphim",
  "age": 3,
  "weight": 20.0,
  "sex": "Female",
  "group": {
    "id": 1,
    "scientific_name": "canis familiaris",
    "created_at": "2022-11-27T17:55:22.819371Z"
  }
  "traits": [
    {
      "id": 4,
      "name": "hunter",
      "created_at": "2022-11-28T13:23:31.819371Z"
    }
  ]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized | Invalid token |
| 404 Not Found    | Pet not found |

---

### 1.5. **Deletar Pet por ID**

### `api/pets/:pet_id`

### Exemplo de Request:
```
DELETE api/pets/9cda28c9-e540-4b2c-bf0c-c90006d37893
Host: 
Authorization: Bearer Token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| pet_id      | string      | Identificador único do pet (Pet)      |

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
204 No Content
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized | Invalid token |
| 404 Not Found    | Pet not found |

---

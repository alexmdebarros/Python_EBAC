#lista simples
filmes = [
    'Um Sonho de Liberdade',
    'O Poderoso Chefão',
    'Batman: O Cavaleiro das Trevas',
    'O Poderoso Chefão II',
    '12 Homens e uma Sentença',
    'A Lista de Schindler',
    'O Senhor dos Anéis: O Retorno do Rei',
    'Pulp Fiction - Tempo de Violência',
    'O Senhor dos Anéis: A Sociedade do Anel',
    'Três Homens em Conflito'
    ]

print(filmes)

#usando pop e insert para modificar ordem da lista
filmes.pop(1)
print(filmes)
filmes.insert(0, 'O Poderoso Chefão')
print(filmes)

#simulando duplicidade na lista e convertendo para set pra não repetir
filmes = [
    'Um Sonho de Liberdade',    
    'O Poderoso Chefão',
    'Batman: O Cavaleiro das Trevas',    
    'O Poderoso Chefão II',
    '12 Homens e uma Sentença',
    'A Lista de Schindler',
    'O Senhor dos Anéis: O Retorno do Rei',    
    'Pulp Fiction - Tempo de Violência',
    'O Senhor dos Anéis: A Sociedade do Anel',
    'Três Homens em Conflito'
]

print(filmes)

filmes.append('Um Sonho de Liberdade')
filmes.append('Três Homens em Conflito')
filmes.append('A Lista de Schindler')

print(filmes)
print(type(filmes))

filmes_set = list(set(filmes))

print(filmes_set)

#criando dicionário
filmes = {
    
    'Top 1': {
        'nome':'Um Sonho de Liberdade',
        'ano' : '1994',
        'sinopse': 'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'
    },

    'Top 2': {
        'nome': 'O Poderoso Chefão',
        'ano': '1972',
        'sinopse': 'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.'
    },

    'Top 3': {
        'nome': 'Batman: O Cavaleiro das Trevas',
        'ano': '2008',
        'sinopse': 'Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça.'
    },
      
    'Top 4': {
        'nome': 'O Poderoso Chefão II',
        'ano': '1974',
        'sinopse': 'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.'
    },

    'Top 5': {
        'nome': '12 Homens e uma Sentença',
        'ano': '1957',
        'sinopse': 'O julgamento de um assassinato em Nova Iorque é frustrado por um único membro, cujo ceticismo força o júri a considerar cuidadosamente as evidências antes de dar o veredito.'
    },

    'Top 6': {
        'nome': 'A Lista de Schindler',
        'ano': '1993',
        'sinopse': 'Na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler começa a ser preocupar com seus trabalhadores judeus depois de testemunhar sua perseguição pelos nazistas.'
    },

    'Top 7': {
        'nome': 'O Senhor dos Anéis: O Retorno do Rei',
        'ano': '2003',
        'sinopse': 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.'
    },

    'Top 8': {
        'nome': 'Pulp Fiction - Tempo de Violência',
        'ano': '1994',
        'sinopse': 'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.'
    },

    'Top 9': {
        'nome': 'O Senhor dos Anéis: A Sociedade do Anel',
        'ano': '2001',
        'sinopse': 'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas.'
    },

    'Top 10': {
        'nome': 'Três Homens em Conflito',
        'ano': '1966',
        'sinopse': 'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.'
    }
}


print(filmes)
print(type(filmes))

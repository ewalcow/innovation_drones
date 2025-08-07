import pandas as pd

# Estrutura de Dados Normalizada
data = {
    'Objetivo do Site Survey': ['Ambiente Virtual (SIM / NÃO)', 'Versão / Detalhamento', 'Obs'],
    'Finalidade do uso dos drones': ['monitoramento ambiental', 'coleta de dados geoespaciais', 'inspeção de infraestrutura'],
    'Dados coletados durante o levantamento': ['Localização geográfica', 'Área do projeto', 'Tipo de terreno', 'Propriedade do terreno', 'Clima'],
    'Mapeamento da Área': ['Mapa topográfico', 'Mapas de uso do solo', 'Imagens de satélite ou fotografias aéreas', 'Identificação de zonas de risco'],
    'Definir Limitações de Voo': ['Altitude máxima permitida', 'Corredores aéreos e zonas de exclusão', 'Perigos potenciais'],
    'Infraestrutura de Apoio': ['Área de decolagem e aterrissagem', 'Ponto de carregamento ou reposição de baterias', 'Comunicação', 'Equipamentos de segurança'],
    'Permissões e Autorizações': ['Autorização de voo', 'Permissões de acesso ao local', 'Notificação a terceiros'],
    'Análise das Condições Ambientais': ['Ventos', 'Temperatura', 'Precipitação', 'Níveis de radiação solar ou UV'],
    'Planejamento de Rota e Mission Planning': ['Rotas otimizadas', 'Altitude de voo recomendada', 'Frequências e canais de comunicação'],
    'Segurança e Considerações Legais': ['Plano de segurança', 'Responsabilidade civil e seguros'],
    'Relatório Final': ['Descrição do local e do projeto', 'Mapas, imagens e gráficos que ilustram o terreno e os obstáculos', 'Dados meteorológicos e ambientais', 
                        'Permissões necessárias e status das autorizações', 'Plano de voo e de segurança', 'Riscos identificados e estratégias de mitigação']
}

# Criar DataFrame
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Exibir DataFrame
print(df)

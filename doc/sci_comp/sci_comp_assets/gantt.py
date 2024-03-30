import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

tasks = [
    dict(Task="A1", Start='2024-01-02', Finish='2024-01-16', Resource = "A1", Description='Entrevistas com Clientes'),
    dict(Task="A2", Start='2024-01-16', Finish='2024-01-26', Resource = "A2", Description='Levantamento de Requisitos Funcionais'),
    dict(Task="A3", Start='2024-01-26', Finish='2024-02-05', Resource = "A3", Description='Requisitos Não Funcionais'),
    dict(Task="A4", Start='2024-02-05', Finish='2024-02-15', Resource = "A4", Description='Análise de Caso de Uso'),
    dict(Task="A5", Start='2024-02-15', Finish='2024-02-25', Resource = "A5", Description='Definição de Histórias de Usuário'),
    dict(Task="A6", Start='2024-02-25', Finish='2024-03-02', Resource = "A6", Description='Priorização de Requisitos'),
    dict(Task="A7", Start='2024-03-02', Finish='2024-03-16', Resource = "A7", Description='Documentação de Requisitos'),
    dict(Task="B1", Start='2024-03-17', Finish='2024-04-07', Resource = "B1", Description='Definição da Arquitetura do Sistema'),
    dict(Task="B2", Start='2024-04-08', Finish='2024-04-29', Resource = "B2", Description='Design UI/UX'),
    dict(Task="B3", Start='2024-04-30', Finish='2024-05-21', Resource = "B3", Description='Especificação dos Componentes do Sistema'),
    dict(Task="B4", Start='2024-05-22', Finish='2024-06-12', Resource = "B4", Description='Design de Banco de Dados'),
    dict(Task="B5", Start='2024-06-13', Finish='2024-06-27', Resource = "B5", Description='Definição de Padrões de Codificação'),
    dict(Task="B6", Start='2024-06-28', Finish='2024-07-12', Resource = "B6", Description='Desenho de Diagramas UML'),
    dict(Task="B7", Start='2024-07-13', Finish='2024-07-20', Resource = "B7", Description='Revisão de Design'),
    dict(Task="C1", Start='2024-07-21', Finish='2024-08-20', Resource = "C1", Description='Desenvolvimento do Código Fonte'),
    dict(Task="C2", Start='2024-08-21', Finish='2024-10-05', Resource = "C2", Description='Programação das Funcionalidades Principais'),
    dict(Task="C3", Start='2024-10-06', Finish='2024-11-05', Resource = "C3", Description='Desenvolvimento de Testes Unitários'),
    dict(Task="C4", Start='2024-11-06', Finish='2024-12-06', Resource = "C4", Description='Integração de Componentes'),
    dict(Task="C5", Start='2024-12-07', Finish='2025-01-06', Resource = "C5", Description='Refatoração do Código'),
    dict(Task="C6", Start='2024-07-21', Finish='2025-01-20', Resource = "C6", Description='Controle de Versão'),
    dict(Task="C7", Start='2025-01-07', Finish='2025-01-21', Resource = "C7", Description='Revisão do Código'),
    dict(Task="D1", Start='2025-01-22', Finish='2025-02-05', Resource = "D1", Description='Planejamento de Testes'),
    dict(Task="D2", Start='2025-02-06', Finish='2025-02-27', Resource = "D2", Description='Execução de Testes Unitários'),
    dict(Task="D3", Start='2025-02-28', Finish='2025-03-21', Resource = "D3", Description='Testes de Integração'),
    dict(Task="D4", Start='2025-03-22', Finish='2025-04-12', Resource = "D4", Description='Testes de Sistema'),
    dict(Task="D5", Start='2025-04-13', Finish='2025-04-27', Resource = "D5", Description='Testes de Aceitação do Usuário'),
    dict(Task="D6", Start='2025-04-28', Finish='2025-05-12', Resource = "D6", Description='Relatório de Bugs e Problemas'),
    dict(Task="D7", Start='2025-05-13', Finish='2025-05-27', Resource = "D7", Description='Reteste e Validação'),
    dict(Task="E1", Start='2025-05-28', Finish='2025-06-11', Resource = "E1", Description='Preparação do Ambiente de Produção'),
    dict(Task="E2", Start='2025-06-12', Finish='2025-06-26', Resource = "E2", Description='Migração de Dados'),
    dict(Task="E3", Start='2025-06-27', Finish='2025-07-04', Resource = "E3", Description='Lançamento Inicial'),
    dict(Task="E4", Start='2025-07-05', Finish='2025-08-04', Resource = "E4", Description='Monitoramento de Desempenho'),
    dict(Task="E5", Start='2025-08-05', Finish='2025-08-19', Resource = "E5", Description='Treinamento de Usuários Finais'),
    dict(Task="E6", Start='2025-08-20', Finish='2025-09-20', Resource = "E6", Description='Suporte Pós-Lançamento'),
    dict(Task="E7", Start='2025-09-21', Finish='2025-10-05', Resource = "E7", Description='Documentação de Implantação')]

colors = {'A': 'rgb(220, 0, 0)', 'B': 'rgb(212, 175, 55)', 'C': 'rgb(173, 216, 230)', 'D': 'rgb(221, 128, 166)', 'E': 'rgb(0, 56, 168)',
          'A1': 'rgb(220, 0, 0)', 'A2': 'rgb(220, 0, 0)', 'A3': 'rgb(220, 0, 0)', 'A4': 'rgb(220, 0, 0)', 'A5': 'rgb(220, 0, 0)', 'A6': 'rgb(220, 0, 0)', 'A7': 'rgb(220, 0, 0)',
          'B1': 'rgb(212, 175, 55)', 'B2': 'rgb(212, 175, 55)', 'B3': 'rgb(212, 175, 55)', 'B4': 'rgb(212, 175, 55)', 'B5': 'rgb(212, 175, 55)', 'B6': 'rgb(212, 175, 55)', 'B7': 'rgb(212, 175, 55)',
          'C1': 'rgb(173, 216, 230)', 'C2': 'rgb(173, 216, 230)', 'C3': 'rgb(173, 216, 230)', 'C4': 'rgb(173, 216, 230)', 'C5': 'rgb(173, 216, 230)', 'C6': 'rgb(173, 216, 230)', 'C7': 'rgb(173, 216, 230)',
          'D1': 'rgb(221, 128, 166)', 'D2': 'rgb(221, 128, 166)', 'D3': 'rgb(221, 128, 166)', 'D4': 'rgb(221, 128, 166)', 'D5': 'rgb(221, 128, 166)', 'D6': 'rgb(221, 128, 166)', 'D7': 'rgb(221, 128, 166)',
          'E1': 'rgb(0, 56, 168)', 'E2': 'rgb(0, 56, 168)', 'E3': 'rgb(0, 56, 168)', 'E4': 'rgb(0, 56, 168)', 'E5': 'rgb(0, 56, 168)', 'E6': 'rgb(0, 56, 168)', 'E7': 'rgb(0, 56, 168)'}




fig = go.Figure()

fig = ff.create_gantt(tasks, index_col='Resource', title='Desenvolvimento MVP - App Inteferência',
                      colors=colors, show_colorbar=True, group_tasks=True, height=800, width=1200,
                      bar_width=0.4, showgrid_y=True)

for task in tasks:
  fig.add_trace(go.Bar(
    x=[task['Start'], task['Finish']],
    y=[task['Task']],
    name=task['Task'],
    hovertext=task['Description']  
  ))



milestones = [task['Finish'] for task in tasks if task['Task'] in ["A7","B7","C7","D7","E7"]]
fig.add_trace(go.Scatter(
  x=milestones,
  y=["A7","B7","C7","D7","E7"],
  mode='markers',
  marker=dict(
    symbol='triangle-down',
    size=10,
    color='light pink'
  ),
  name='Milestones'
))



for milestone in milestones:
  fig.add_shape(
    type="line",
    xref="x",
    yref="paper",
    x0=milestone, y0=0, x1=milestone, y1=1,
    line=dict(
      color="grey",
      width=1,
      dash="dot"
    )
  )
  
fig.update_layout(
  plot_bgcolor = 'rgba(0,0,0,0)',
  paper_bgcolor = 'rgba(0,0,0,0)',
  font=dict(
    family="Monaco, monospace",
    size=12,
    color="black"
  )
)

fig.show()
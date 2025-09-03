# populate_db.py
# Execute este arquivo no shell do Django: python manage.py shell
# Em seguida, copie e cole este código

from App.models import User, Status, Task

def populate_database():
    """
    Popula o banco de dados com dados iniciais para testar o dashboard
    """
    
    # Criar status padrão
    print("Criando status padrão...")
    status_pendente, created = Status.objects.get_or_create(name="Pendente")
    if created:
        print("- Status 'Pendente' criado")
    
    status_andamento, created = Status.objects.get_or_create(name="Em Andamento") 
    if created:
        print("- Status 'Em Andamento' criado")
    
    status_concluida, created = Status.objects.get_or_create(name="Concluída")
    if created:
        print("- Status 'Concluída' criado")
    
    # Criar usuários de exemplo
    print("\nCriando usuários de exemplo...")
    user1, created = User.objects.get_or_create(
        username="joao",
        defaults={'password': '123456'}
    )
    if created:
        print("- Usuário 'joao' criado")
    
    user2, created = User.objects.get_or_create(
        username="maria",
        defaults={'password': '123456'}
    )
    if created:
        print("- Usuário 'maria' criado")
    
    user3, created = User.objects.get_or_create(
        username="admin",
        defaults={'password': 'admin123'}
    )
    if created:
        print("- Usuário 'admin' criado")
    
    # Criar tarefas de exemplo
    print("\nCriando tarefas de exemplo...")
    
    tarefas_exemplo = [
        {
            'title': 'Implementar sistema de login',
            'description': 'Desenvolver funcionalidade de autenticação de usuários com validação de senha e controle de sessão.',
            'user': user1,
            'status': status_concluida
        },
        {
            'title': 'Criar dashboard administrativo',
            'description': 'Desenvolver interface para visualizar todas as tarefas do sistema com estatísticas e filtros.',
            'user': user1,
            'status': status_andamento
        },
        {
            'title': 'Implementar responsividade',
            'description': 'Adaptar todas as telas para funcionar corretamente em dispositivos móveis.',
            'user': user2,
            'status': status_pendente
        },
        {
            'title': 'Otimizar performance do banco',
            'description': 'Revisar queries e adicionar índices para melhorar performance das consultas.',
            'user': user2,
            'status': status_pendente
        },
        {
            'title': 'Documentar API',
            'description': 'Criar documentação completa das funcionalidades e endpoints do sistema.',
            'user': user3,
            'status': status_andamento
        },
        {
            'title': 'Implementar testes unitários',
            'description': 'Desenvolver suite de testes para garantir qualidade do código.',
            'user': user3,
            'status': status_pendente
        },
        {
            'title': 'Configurar deploy em produção',
            'description': 'Configurar servidor de produção e automatizar processo de deploy.',
            'user': user1,
            'status': status_concluida
        },
        {
            'title': 'Implementar notificações por email',
            'description': 'Adicionar sistema de notificações automáticas quando tarefas são atribuídas ou atualizadas.',
            'user': user2,
            'status': status_andamento
        }
    ]
    
    for tarefa_data in tarefas_exemplo:
        tarefa, created = Task.objects.get_or_create(
            title=tarefa_data['title'],
            defaults={
                'description': tarefa_data['description'],
                'user': tarefa_data['user'],
                'status': tarefa_data['status']
            }
        )
        if created:
            print(f"- Tarefa '{tarefa_data['title']}' criada para {tarefa_data['user'].username}")
    
    print(f"\n✅ Banco de dados populado com sucesso!")
    print(f"📊 Total de usuários: {User.objects.count()}")
    print(f"📋 Total de tarefas: {Task.objects.count()}")
    print(f"📈 Total de status: {Status.objects.count()}")
    
    print("\n🔑 Usuários criados:")
    print("- joao / 123456")
    print("- maria / 123456") 
    print("- admin / admin123")

# Executar a função
if __name__ == "__main__":
    populate_database()